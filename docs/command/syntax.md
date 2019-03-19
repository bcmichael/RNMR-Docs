# Command Syntax
The general form of an RNMR command line is:

    (Repeat-count) command (Qualifiers) argument_1 (,) argument_2 (,)...

For example, the command line below executes the command ABC with qualifier D and parameters 1, 2, and 3 five times:

    5 ABC /D 1 2 3

Qualifiers always start with a / and should precede the commands arguments.

While commas need not be included to delimit the arguments of a command, they may be used to specify a null
argument as in the example below:

    ALLCPY 90, ,4096

When RNMR reads a user's command, any integer preceding a valid instruction is understood as a repeat count. For
example, the command line:

    2 EM 0.05

instructs RNMR to exponentially multiply an FID by 0.05 twice.
Repeat counts are interpreted as summarized below:

Repeat Count | Action
------------ | ------
1 and above  | Execute command N times
0            | Illegal
-1           | Execute command an indefinite number of times until stopped by Q or Ctrl-Z
-2 and below | illegal

# Archives
RNMR data is saved in archives and a number of RNMR commands take archives as arguments. Up to 4 archives may be open in
an instance of RNMR at any one time. Each archive has an associated archive number (1-4). These archive numbers are what
are passed as arguments to commands rather than the archive name.

<a name="archive_access"></a>
At the time that an archive is opened (by `OPNARV`) the level of access RNMR has to that archive is set. RNMR will
always have read access to an open archive, but not necessarily write access. A given archive may be open in multiple
instances of RNMR but only one may have write access to it. This enforced by lock files which are created when RNMR
opens an archive with write access and deleted when the archive is closed. If RNMR closes unexpectedly (as in a program
crash or power loss) these lock files may not be properly deleted. When RNMR is reopened it will not be able to open the
archives for which lock files are still present. This can be circumvented by manually deleting the lock files in the
users archive folder or by using `OPNARV /FORCE`. Be careful to only take these actions if you are sure that the archive
is not in fact open in an instance of RNMR to avoid data corruption.

# Records
Archives consist of individual numbered records that hold data. An archive may have up to 200 records. When a command
accepts a record as an argument the record number should be used. Records in archive 1 can simply be specified by their
record number within the archive. Records in archives other than 1 can be selected in two ways. Records in archive 2 are
mapped to record numbers 201-400, archive 3 401-600, and archive 4 601-800. Any numbers in these ranges specify a record
in the corresponding archive. The other method is to prepend the record number with the archive number and a colon. For
example 2:12 refers to record number 12 in archive 2.

<a name="record_type"></a>
There are three types of record: scratch records, archive records, and blocked records. Many commands that deal with
records can only accept one of these types of records. The first four records in an archive are scratch records. They
are meant as a temporary place to keep data while working with it. The other record numbers (5-200) may hold either
archive records or blocked records. An archive record stores a single one dimensional data set. A blocked record is a
multi dimensional set of blocks that can each store a one dimensional data set.

# Blocked Records
Blocked records store multi dimensional data sets as a collection of blocks that each hold a one dimensional data set.
Blocked records must be allocated (by commands such as `ALLB` and `ALLCPY`) before data can be stored in them. A blocked
record may have up to four dimensions. The size of each dimension is set at the time that the blocked record is
allocated. Space within the archive file is also reserved when a blocked record is allocated. Space is reserved in
blocks of 512 bytes each. Therefore the allocated space may exceed the actual amount of data.

<a name="ndimx"></a>
The layout of the blocked record in the archive file depends upon the parameter NDIMX which determines the dimensions in
which RNMR will be able to access the data in the blocked record. If NDIMX is 1 (the typical default) RNMR will only be
able to access the data along the first dimension. The data will be stored in sequential order as one dimensional
blocks. If NDIMX is 2 RNMR will be able to access data along the first two dimensions and will store the data in square
blocks. The trend continues for larger values of NDIMX. The value of NDIMX cannot be changed after the record is
allocated. Commands which must access data from a blocked along a particular dimension will fail if the value of NDIMX
for that record is not large enough.

<a name="slice"></a>
When RNMR commands need to access some number of dimensions in a blocked record they access the first directions of the
record. These directions are not necessarily the first dimensions of the record. The mapping of directions to dimensions
is set by `DIRB`. This mapping is set separately for each possible dimensionality. When RNMR commands access some number
of directions they will access a n-dimensional slice of the record. They will generally take an argument to indicate
which slice. If the record has the same number of dimensions as are being accessed this slice must be 1. Otherwise the
slice parameter is interpreted as a linear index along the other directions.

<a name="nseg"></a>
Blocked records may have multiple segments. These segments are typically used to store the different channels of the
hypercomplex acquisition used for multi-dimensional spectra. When loading data from or saving data to a blocked record
a particular segment can be selected by appending a period and the segment number to the record number.

# Buffers
Data in RNMR is kept in buffers. There are two types of buffers in RNMR: acquisition and processing. The acquisition
buffer is only available in RNMRA and holds the same values as the averager. Data will initially be in the acquisition
buffer when it is collected and it can then be transferred to a processing buffer for further manipulation and analysis.
There are currently four processing buffers available in RNMR. Processing buffer 1 is the visible processing buffer and
its contents may be displayed on the screen. Many commands operate only on the visible processing buffer. Others will
accept processing buffers as arguments. Processing buffers are specified by their indexes (1-4).

Processing buffers can be divided into multiple blocks using `DBSZ`. Multiple blocks of data can be read into these
processing buffer blocks from a blocked record. Most commands that process data will operate on all of these blocks
independently with a single RNMR command. This approach to data processing can increase efficiency by reducing the
overhead of interpreting RNMR commands.

There are a series of commands that perform mathematical operations on the data in two processing buffers. These will
typically have a source and destination buffer as their arguments. The operation is performed on the data from the two
buffers and the result is stored in the destination buffer. For these operations it is required that the two records
have the same active size and domain. They are not required to be partitioned into the same number of blocks. RNMR uses
the following formula to match source and destination blocks.

    SRC_BLCK = MOD(DTS_BLCK-1, NBLK_SRC)+1

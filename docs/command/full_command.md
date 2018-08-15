
# A
---
## ABORT
Abort acquisition

Category: Acquisition

Format: `ABORT`

Prerequisites: RNMRA only

Description:
Aborts acquisition. If acquisition is not currently active, an error message will result. `ABORT` is equivalent to
`QUIT`.  Acquisition will be aborted abruptly i.e. RNMR will not wait for next shot to be completed.
## ADDV
Add buffers

Category: Data Manipulation

Format: `ADDV` src dst

Defaults: 2 1

Description:
`ADDV` adds the source buffer SRC to the destination buffer DST changing the destination buffer:

        DST = DST + SRC

The arguments "SRC" and "DST" specify the numbers of the buffers to be added. Each buffer number may be either 1 or 2;
buffer 1 is the visible processing buffer.  If either argument is omitted, RNMR will prompt for a buffer number. The
default source is buffer 2 while the default destination is buffer 1.  While `ADDV` operates only on processing buffers,
the user need not be viewing the processing buffers to perform the addition.  For two buffers to be added, they must
have the same domain (time or frequency) and the same active size (though not necessarily the same allocated size).  If
the destination buffer is partitioned into two or more blocks, each block is separately added with the corresponding
block of the source buffer.  The number of blocks in the source buffer need not be the same as that in the destination
buffer.  RNMR uses the formula below to match source blocks with destination blocks:

        IBLK_SRC = MOD(IBLK_DST-1,NBLK_SRC) + 1, IBLK_DST=1,...,NBLK_DST

If the processing buffer is currently visible and "DST" is 1, `ADDV` always updates the display upon completion.
## AI
Scale to absolute intensity

Category: Display Control

Format: `AI` sfa

Defaults: current

Description:
`AI` scales data in the visible processing buffer (buffer 1) to make the scale factor equal to a specified absolute
scale factor. This absolute scale factor, "sfa", is a floating point number greater than 0. If sfa is equal to the
buffer scale factor, `AI` does nothing.  If sfa is not equal to the buffer scale factor, the buffer data is scaled by
sfa/(buffer_sf) and the current scale factor, buffer scale factor, and display are updated. If the sfa parameter is
omitted, `AI` will scale to the current absolute scale factor.
## AK
Set absolute scale factor

Category: Display Control

Format: `AK` sfa

Defaults: current

Description:
`AK` sets the current absolute scale factor. This scale factor is  a global parameter. If the absolute scale factor
"sfa" is omitted, `AK` will prompt for the scale factor. The default value for this parameter is the current global
scale factor. The argument "sfa" is a floating point number greater than or equal to 0. If the value of sfa is 0, i.e.
`AK 0`, then the global scale factor will be set equal to the scale factor of the visible processing buffer (buffer 1).
## ALLB
Allocate a blocked record

Category: Blocked Records

Format: `ALLB` rec# ndim isize(1)...isize(ndim) ndimx nsega

Defaults: 0 2 64 ... 64 1

Description:
`ALLB` allocates a blocked record for 2D to 4D records. By allocating multidimensional records in advance, the user is
assured that there will be adequate disk space to hold all the data to be acquired.  Blocked records must be allocated
using `ALLB`, `ALLCPY`, or `CPY` before data may be written into them. The parameter "rec#" is the record number to be
allocated. If 0 is entered for this parameter or if the parameter is omitted form the command line, then RNMR will
allocate the next available record and print out the record number as an informational message once the allocation is
complete. When "rec#" is missing or 0, an error message (FNDTA ) NO AVAILABLE TITLE RECORD indicates that there are no
more empty title records available to be allocated. If this message is encountered, the user should either delete one or
more existing records in the current archive or create a new, empty  archive ($ CRTARC) before retrying the allocation.
If "rec#" is specified and is not 0, the specified record must be empty (i.e. not previously allocated). Only records 5
through 200 may be allocated with `ALLB`; scratch records (numbers 1-4) may not be allocated. The parameter NDIM
specifies the number of dimensions. NDIM may be chosen from 1 to 4. If NDIM is not specified on the command line, RNMR
will prompt for it with a default value of 2.

The parameters ISIZE(1), ISIZE(2), ISIZE(3), and ISIZE(4) give the number of points in dimensions 1 through 4,
respectively.  For a particular choice of NDIM, RNMR expects the user to supply NDIM arguments describing the size of
each dimension, starting with dimension 1.  If insufficiently many sizes are specified for the requested number of
dimensions, RNMR will prompt for the missing sizes; the default size for each dimension is 64 points.  The minimum size
that may be specified for any dimension is 1.

NDIMX is the number of dimensions that will be simultaneously accessible. NDIMX is an integer between 1 and NDIM,
inclusive.  This parameter controls the manner in which the blocks of the allocated record are physically stored on
disk.  If NDIMX is 1, data is written in sequential order, as appropriate for a one-dimensional read operation.
However, if NDIMX is 2, data is written in 64 X 64 point blocks to facilitate simultaneous retrieval in two dimensions.
Similarly, NDIMX values of 3 and 4 direct RNMR to store data in a manner optimized for 3 and 4 dimensional retrieval.
If NDIMX is not specified on the command line, RNMR will prompt for its value; the default value of this parameter is
always 1, regardless of NDIM.  Note that once a record has been allocated, it is impossible to reset  its NDIMX value.

When NDIMX is greater than 1, data is stored physically in units of a specific size, which depends only on the value of
NDIMX.  Since the user may allocate only an integer number of these units, RNMR will sometimes create a blocked record
with more blocks than the number requested by the user.  For example, a request to allocate a blocked record with 5
blocks of 4096 points each and NDIMX 1 gives `SIZEB` 2 of 5, i.e. RNMR returns exactly the number of blocks requested.
However, if the same request is made with NDIMX 2, 8 blocks will be allocated since 8 X 4096 corresponds to the smallest
number of storage units greater than equal to the number required.

NSEGA is the number of aquisition segments. If NSEGA is not specified RNMR will not prompt for a value and it will
default to 1.

If the physical size of the data file \*DATA.DAT must be increased to allocate the requested record, RNMR will write a
message to the screen reporting the new, extended size in blocks (512 bytes = 1 block).  Note that the total allocated
space occupied by an RNMR archive (including any deleted blocks that have not been squeezed) is limited to 524288 disk
blocks (268.4 MB or 33554432 complex data points).

If the allocation is successful and no record number (or record  number "0") was specified, RNMR will return the record
number for the allocated blocked record.  After a successful allocation, the current record pointer will be updated.
Thus, `PTRA` may be used to check which record was just allocated.

See command `PARB` for establishing the parameters (e.g. time step in each dimension) of a blocked record allocated with
`ALLB`.
## ALLCPY
Allocate a copy of a blocked record

Category: Blocked Records

Format: `ALLCPY` inrec outrec isize(1) ... isize(4) ndimx nsega

Defaults: current 0 insize(1)...insize(4) 1

Description:
`ALLCPY` allocates a copy of an existing blocked record. Parameters of the existing record are copied to the new record,
but the data is not copied. To copy both parameters and data, use the command `CPY`. In allocating a copy of a given
record, `ALLCPY` may be given new sizes and NDIMX in place of those used in the original record.

INREC is the number of the record which `ALLCPY` is to copy. If this parameter is not supplied, RNMR will prompt for it
with the current record number (as displayed by `PTRA`) as the default. INREC is an integer between 5 and 200; scratch
records (numbers 1 to 4) cannot be copied with `ALLCPY`. The record specified by INREC must be a blocked record.

OUTREC is the record number that will contain the copy of INREC. If OUTREC is omitted or is 0 then RNMR will allocate
the next available record as a copy of record INREC. In this case, the destination record number will be printed as an
informational message once the allocation is complete. When OUTREC is missing or 0, an error message (FOUNDTA ) NO
AVAILABLE TITLE RECORD indicates that there are no more empty title records available to be allocated. If this message
is encountered, the user should either delete one or more existing records in the current archive or create a new, empty
archive ($ CRTARC) before retrying the allocation. If OUTREC is specified and is not 0, it must have a value between 5
and 200; the scratch records (1-4) cannot be allocated. Furthermore, OUTREC must be empty before it may be allocated.

ISIZE(1) through ISIZE(4) are the sizes (in points) of the allocated copy in dimensions 1 through 4. These sizes are
optional parameters; if one or more sizes are omitted, RNMR will use the sizes of the input record INREC to allocate the
copy OUTREC. However, if the user wishes to make one or more sizes different in OUTREC from their corresponding sizes
in INREC, RNMR expects to find NDIM size arguments following OUTREC, where NDIM is the number of dimensions. Each of
these arguments must be an integer greater than or equal to one.

NDIMX is the number of simultaneously accessible dimensions for the allocated copy OUTREC.  See the description of the
command `ALLB` for more information.  If this parameter is not specified, only one dimension of the resulting record may
be accessed at a time, i.e. NDIMX always defaults to 1, regardless of its value in the source record INREC. Once record
OUTREC has been allocated, it is impossible to reset its NDIMX value.  If NDIMX is specified, it must be an integer
between 1 and NDIM inclusive, where NDIM is the number of dimensions.

NSEGA is the number of aquisition segments. If NSEGA is not specified RNMR will not prompt for a value and it will
default to 1.

If the physical size of the data file \*DATA.DAT must be increased to allocate the requested record, RNMR will write a
message to the screen reporting the new, extended size in blocks (512 bytes = 1 block).

If the allocation is successful and no record
number (or record number "0") was specified, RNMR will return the record number for the allocated blocked record in an
informational message.  After a successful allocation, the current record pointer will be updated.  Thus, `PTRA` may be
used to check which record was just allocated.
## AMD
Set acquisition modes

Category: Acquisition

Format: `AMD` spec1 spec2 ... spec8

Qualifiers: /ACQ /BLK /MOD=MODMD

Qualifier Defaults: /ACQ /MOD=4

Defaults: none none ... none

Prerequisites: Acquisition stopped (HALT) RNMRA only

Description:
`AMD` sets the receiver phase cycling. /MOD defines the number of different phase values to be used. These phase values
will be equally spaced so the default value of 4 yields 90° phase steps while for example 6 would yield 60° steps. Each
element or mode of the `AMD` sequence is a number from 1 to the value specified by /MOD. With the default qualifier /ACQ
these modes indicate a sequence of phase shifts to apply to an acquired FID on sequential shots.

The default value is /MOD=4, which yields phase values of (0°, 90°, 180°, 270°) corresponding to the numbers 1 through 4.
The maximum number of acquisition modes in a sequence is 64. If the number of modes entered is less than 64, the
specified modes will be replicated to a 64 mode sequence. For example, if the user specifies:

        AMD 1111 3333

the eight modes specified are replicated by RNMR to give a full 64 step phase cycle:

     11113333 11113333 11113333 11113333
     11113333 11113333 11113333 11113333

While all sequences are replicated to 64 modes internally, only a number of steps equal to the active phase cycle length
(set by `NAMD`) are actually used. The sequence of modes may be broken up across multiple command line arguments as
shown in the example above. This can help improve readability.

If `AMD` is called with no parameters RNMR will not prompt for modes. Instead it will print the current receiver phase
cycle out to the active phase cycle length with 16 modes per line.

The /BLK qualifier is used to setup additional receiver phase shifts for different blocks of acquisition. The number of
blocks can be set using `NAMD /BLK`. This capability is typically used to set up phase differences used for the
different steps in hypercomplex acquisition of multi-dimensional spectra.
## APNFIL
Append text to file

Category: File IO

Format: `APNFIL` fspec

Qualifiers: /END=<end\> /TTY

Qualifier Defaults: /END=''

Defaults: 'temp.dat'

Description:
`APNFIL` appends lines of text to a file fspec. /END sets a string which marks the end of what is to be appended.
`APNFIL` behaves slightly differently if called at the command line or in a macro. At the command line if no file is
specified RNMR will prompt for a file with temp.dat as a default. If the file exists and RNMR succeeds in opening it,
RNMR will then prompt for a line to append to the file with a default of <end\>. Otherwise an error will be thrown. RNMR
will continue to prompt for lines until a line is entered which matches <end\>. By default <end\> is an empty string and
`APNFIL` will end if an empty line is provided.

When called from a macro `APNFIL` will not prompt for a file name. The lines to be appended should be provided on the
lines following `APNFIL` in the macro and should start with ;;. The first line will be interpreted as a file name if
none is provided as an argument. `APNFIL` will stop appending lines when it either reaches a line that matches <end\> or
runs out of lines. /TTY will make RNMR prompt for the lines to enter much like the behavior at the command line even
when `APNFIL` is called from a macro. RNMR will still expect the file name to passed in the same way as when /TTY is not
used. An example of use in a macro is given here:

    APNFIL TEMP.TXT
    ;;Append this
    ;;Also append this

Text written by `APNFIL` will be all caps regardless of the capitalization provided in RNMR.
## APNLST
Append values to list

Category: List Handling

Format: `APNLST` nam

Qualifiers: /END=<end\> /TTY

Qualifier Defaults: /END=''

Defaults: temp

Description:
`APNLST` appends lines list specified by nam. /END sets a string which marks the end of what is to be appended. If no list is specified RNMR will prompt for a list name with a default of temp. The list must already exist or an error will be thrown. A list can be created using `CRTLST` if needed.
`APNLST` behaves slightly differently if called at the command line or in a macro. At the command line
RNMR will prompt for a line to append to the list with a default of <end\>. Otherwise an error will be thrown. RNMR
will continue to prompt for lines until a line is entered which matches <end\>. By default <end\> is an empty string and
`APNLST` will end if an empty line is provided.

When called from a macro `APNLST` will not prompt for a line to append unless the /TTY qualifier is used. Instead the lines to be appended should be provided on the
lines following `APNLST` in the macro and should start with ;;. `APNLST` will stop appending lines when it either reaches a line that matches <end\> or
runs out of lines. /TTY will make RNMR prompt for the lines to enter much like the behavior at the command line even
when `APNLST` is called from a macro.
used. An example of use in a macro is given here:

    APNLST TEMP
    ;;Append this
    ;;Also append this

Text appended by `APNLST` will be all caps regardless of the capitalization provided in RNMR.
## APNMAC
Append text to macro

Category: Macro

Format: `APNMAC` nam

Qualifiers: /END=<end\> /TTY

Qualifier Defaults: /END=''

Defaults: temp

Description:
`APNMAC` appends lines of text to a macro nam. /END sets a string which marks the end of what is to be appended.
`APNMAC` behaves slightly differently if called at the command line or in a macro. At the command line if no macro is
specified RNMR will prompt for a macro with temp as a default. If the macro exists, RNMR will then prompt for a line to
append to the macro with a default of <end\>. Otherwise an error will be thrown. RNMR will continue to prompt for lines
until a line is entered which matches <end\>. By default <end\> is an empty string and `APNMAC` will end if an empty
line is provided.

When called from a macro `APNMAC` will not prompt for a macro name. The lines to be appended should be provided on the
lines following `APNMAC` in the macro and should start with ;;. The first line will be interpreted as a macro name if
none is provided as an argument. `APNMAC` will stop appending lines when it either reaches a line that matches <end\> or
runs out of lines. /TTY will make RNMR prompt for the lines to enter much like the behavior at the command line even
when `APNMAC` is called from a macro. RNMR will still expect the macro name to passed in the same way as when /TTY is not
used. An example of use in a macro is given here:

    APNMAC TEMP.TXT
    ;;Append this
    ;;Also append this

Text written by `APNMAC` will be all caps regardless of the capitalization provided in RNMR.
## ARV
Return archive information

Category: Data Storage

Format: `ARV` iarv

Qualifiers: /ACCESS /NAME

Qualifier Defaults: /NAME

Defaults: 1

Description:
The argument iarv is an archive number, which can be 1 through 4. The default /NAME qualifier causes `ARV` to print the
name of the specified archive as an informational message. The /ACCESS qualifier causes `ARV` to print an integer
indicating the level of access to the archive. The integer codes are generated by using the least significant bit to
indicate whether there is read access to the archive and the next least significant bit to indicate write access.
Numbers for which no archive is open will have neither and there will never be write access without read access. This
yields the following possible codes.

Access Code | Meaning
----------- | -------
0 | No open archive
1 | Read access
3 | Read and write access

## ASIG
Acknowledge signal

Category: Acquisition

Format: `ASIG` nam

Defaults: temp

Prerequisites: RNMRA only

Description:
Signals are events that occur asynchronously to the macro execution. They are only present in RNMRA. Signals are
primarily used for multi dimensional acquisition. `ASIG` acknowledges a signal and resets it. The following signals are
available:

Signal | Meaning
------ | -------
GAV    | Indicates a slice is ready to be read from the averager and written to a blocked record
SAV    | Indicates a slice is ready to be read from a blocked record and written to the averager for further averaging
SGO    | Indicates that acquisition has begun for the slice

A particular signal can also be tested for using `TST SIG`.
## ASKYN
Ask yes or no

Category: Macro

Format: `ASKYN` default labelt labelf

Defaults: NO none none

Prerequisites: Macro only (MAC)

Description:
`ASKYN` falls into the same category as the old if commands. It prompts the user for a YES/NO response and jumps to
labelt if YES or labelf if NO.

The old if commands have been replaced. Instead use `TST` to conditionally execute commands or `GOTST` to make
conditional jumps.
## AUTOZ
Set automatic Z shim parameters

Category: Shim

Format: `AUTOZ` step time

Defaults: current

Prerequisites: RNMRA only. Spectrometer must have lock and shim setup to run via RNMR.

Description:
`AUTOZ` sets up automatic Z shimming in RNMRA. In order for this to function RNMR must have access to both the lock and
shim controls. The step must be between 0 and 1, while time must be between 4 and 100.
# B
---
## BC
Baseline correct FID

Category: Data Manipulation

Format: `BC`

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`BC` performs a baseline correction to a complex FID by subtracting the average of the last 1/8th of the data points
from the entire FID. `BC` does not require the user to be viewing the processing block (`VIEW PRO`), but baseline
correction is only performed on the processing block. To calculate the constant complex offset to be subtracted from
the entire FID, `BC` examines the final 1/8th of the FID data points with a minimum of 1 point if there are less than 8
points. The average of these points (a complex number) is subtracted from each (complex) point of the entire
FID, yielding a baseline corrected FID. A separate baseline correction is performed on each block of the processing
buffer. If the processing buffer is currently visible, `BC` always updates the display upon completion.
## BF
Baseline fix spectrum

Category: Data Manipulation

Format: `BF`

Prerequisites: Frequency domain data in processing buffer (FREQ)

Description:
`BF` performs a linear baseline fix by subtracting a straight line from the data between the current display limits.
`BF` does not require the user to be viewing the processing block (`VIEW PRO`), but baseline fixing is only performed
on the processing block.

`BF` uses the average of the leftmost and rightmost 5 points between the current display limits to determine the line to
subtract. If there are fewer than 5 points between the current display limits `BF` subtracts the average over all the
points instead of calculating a line. `BF` only subtracts from the points between the current display limits, leaving
everything outside of those limits untouched. If the processing buffer is currently visible, `BF` always updates the
display upon completion.
## BINCP
Perform binary pulse phase correction

Category: Data Manipulation

Format: `BINCP` fnyq fmax

Defaults: first (fnyq-orgn)/2+orgn

Prerequisites: Frequency data in processing buffer (FREQ)

Description:
`BINCP` performs the phase portion of a binary pulse correction. When used with the `BINCP` solvent suppression pulse
sequence, this command corrects the phase of the off-resonant component of the magnetization, which is preserved while
the on-resonance solvent peak is cancelled out. `BINCP` does not require the user to be viewing the processing block
(`VIEW PRO`), but phase correction is only performed on the processing block. The parameters fnyq and fmax are the
nyquist frequency of the processing buffer and the max frequency to be used for the correction. Both parameters are
specified in terms of current frequency units including the frequency offset of the origin of the buffer (orgn). The
default value of fnyq will be correspond to the frequency of the first point in the buffer. The default of fmax is
(fnyq-orgn)/2+orgn. Internally `BINCP` subtracts the origin from the values before using them. In order to make the
calculations more understandable all references to these parameters going forward will refer to the corrected values
with the origin subtracted out. The corrected fnyq must be greater than 0. The absolute value of the corrected fmax
divided by the corrected fnyq must be between 0.1 and 2.0.

To calculate the phase portion of the finite pulse correction, `BINCP` first calculates a constant phase and a phase
increment:

 	PHI = 270.0*DFRST/FMAX - 90.0
 	DPHI = 270.0*DSTEP/FMAX

where DSTEP is -1 times the frequency per point and DFRST is the frequency of the first point in the spectrum.

Each point I ranging from 1 to the size of the buffer is multiplied by a complex phase shift calculated as follows:

    EXP(i*(PHI + (I-1)* DPHI))

The data in each block of the processing buffer is phase corrected independently.

If the data point closest to zero frequency (without offset) is not the last point in the spectrum, then all points
in each block from zero to minimum (most negative) frequency are negated.

If the processing buffer is currently visible, `BINCP` always updates the display upon completion.
## BRKDO
Break out of a macro `DO` loop

Category: Macro

Format: `BRKDO`

Prerequisites: Macro only and must be in a `DO` loop

Description:
`BRKDO` can be used to break out of a macro `DO` loop. The loop will terminate immediately without executing any more
commands within the loop regardless of how many more iterations it was supposed to do. Execution will continue on the
line after the `ENDDO` at the end of the loop. `BRKDO` must appear between `DO` and `ENDDO`
## BRUK
Convert BRUKER FID to complex FID

Category: Foreign

Format: `BRUK`

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`BRUK` converts a BRUKER format (real) FID into a complex FID. `BRUK` does not require the user to be viewing the
processing block (`VIEW PRO`), but data conversion is only performed on the processing block. Upon conversion from
BRUKER to complex format, the size of the FID (number of points) is adjusted to the smallest power of 2 greater than or
equal to the original size. `BRUK` will convert the data only if this adjusted size is at least 4 points and not
greater than the allocated buffer size (ISIZEA); otherwise an error message will be
displayed.

If the adjusted FID size is within limits, the data is zero filled from the current size to the adjusted size.  Thus, a
100 point FID is zero filled to 256 points.  If the processing buffer is divided into two or more blocks, each block is
zero filled separately.

The actual conversion from BRUKER (real) to complex data follows the  algorithm below:

1.	The entire zero-filled BRUKER FID is conjugated.
2.	Starting with the second point, every other point in the FID is negated.

3.	A real Fourier transform is performed on the FID, yielding a complex vector with half the adjusted size of the source
FID.

4.	The resulting vector is inverse Fourier transformed.

5.	Starting with the second point, every other point in the FID is negated.

If the processing buffer is divided into two or more blocks, each block is transformed separately. If the processing
buffer is currently visible, `BRUK` always updates the display upon completion.
## BUF
View real or imaginary buffer

Category: Display Control

Format: `BUF` nam

Defaults: current

Description:
`BUF` selects whether the real or imaginary part of the current buffer should be displayed. The current buffer (PRO,
ACQ, or LCK) is selected using the command `VIEW`. For the parameter nam, the user may enter either REAL or IMAG
to display the real or imaginary part of the buffer, respectively. If this parameter is omitted from the command line,
RNMR will prompt for a response with the current buffer display type as the default. If the user accepts the default
buffer display mode, `BUF` does nothing. Otherwise, the display is updated if it is currently visible.
## BUFA
View real or imaginary acquisition buffer

Category: Display Control

Format: `BUF` nam

Defaults: current

Prerequisites: RNMRA only

Description:
`BUFA` selects whether the real or imaginary part of the acquisition buffer should be displayed. For the parameter nam,
the user may enter either REAL or IMAG to display the real or imaginary part of the buffer, respectively. If this
parameter is omitted from the command line, RNMR will prompt for a response with the current buffer display type as the
default. If the user accepts the default buffer display mode, `BUFA` does nothing. Otherwise, the display is updated if
it is currently visible.
# C
---
## CALC
Perform floating point arithmetic and logical calculations

Category: Calculator

Format: `CALC` arg1 ... arg10

Qualifiers: /NDEC

Qualifier Defaults: /NDEC=-1

Defaults: none

Description:
`CALC` performs desk calculator operations in reverse Polish notation. Arguments are pushed onto the calculator stack
and operations are performed on them, yielding results which may either be printed to the screen (PRT) or popped into
local (>>) or global (>) arguments or symbols (>>>). `CALC` can perform basic arithmetic operations (+, -, \*, /) using
infix notation when pushing values onto the stack. Infix operations are performed left to right with no regard for order
of operations, but parentheses can be used to alter this order. The result of this infix math is pushed onto the stack
like any other argument. All calculations are performed internally using single precision floating point arithmetic. The
results are presented as integers (NDEC -1) unless modified by the NDEC qualifier or the NDEC operator, as described
below. For example the following command:

    CALC /NDEC=2 1/3 PRT

will print the following as an informational message:

    VAL    =0.33

The /NDEC qualifier must be an integer from -1 to 6.

`CALC` operates on each argument on the command line from left to right. Remember that each argument can contain no more
than 16 characters. The calculator stack used by `CALC` has a depth of 10. If an attempt is made to push more than 10
arguments onto the stack, the error message "(CALC0 ) STACK OVERFLOW" will be displayed. When `CALC` encounters a unary
arithmetic operator such as ABS (absolute value), it expects that there exists at least one value on the stack on which
to operate. To put this another way, TOS (Top Of Stack) must exist. If the stack is empty, the error message "(CALC0)
STACK UNDERFLOW" will be displayed. Similarly, there must be at least two values on the stack in order to perform a
binary arithmetic operation; a lack of sufficiently many arguments will give an underflow error. When a binary operation
is executed, the result replaces both (TOS) and (TOS-1), reducing the number of values on the stack by one. When a
constant is pushed onto the stack, the number of values on the stack increases by one. When a unary operation is
executed, the number of values on the stack does not change. `CALC` also has access to a 16 element register, which
values can be stored in.

The arguments which may be used with the `CALC` command are as follows:

Constants:

Argument | Description | Equation
-------- | ----------- | --------
E        | Pushes the constant e onto the top of the stack. | (TOS)=e
PI       | Pushes the constant pi onto the stack.           | (TOS)=pi

Unary Arithmetic Operators:

Argument | Description | Equation
-------- | ----------- | --------
ABS      | Replaces the top of stack with its absolute value | (TOS)=ABS(TOS)
ACOS     | Replaces the top of stack with its inverse cosine. The result is in units of radians. | (TOS)=ACOS(TOS)
ACOSD    | Replaces the top of stack with its inverse cosine. The result is in units of degrees. | (TOS)=ACOSD(TOS)
ASIN     | Replaces the top of stack with its inverse sine. The result is in units of radians. | (TOS)=ASIN(TOS)
ASIND    | Replaces the top of stack with its inverse sine. The result is in units of degrees. | (TOS)=ASIND(TOS)
ATAN     | Replaces the top of stack with its inverse tangent. The result is in units of radians. | (TOS)=ATAN(TOS)
ATAND    | Replaces the top of stack with its inverse tangent. The result is in units of degrees. | (TOS)=ATAND(TOS)
COS      | Replaces the top of stack with its cosine. The operand is assumed to be in units of radians. | (TOS)=COS(TOS)
COSD     | Replaces the top of stack with its cosine. The operand is assumed to be in units of degrees. | (TOS)=COSD(TOS)
COSH     | Replaces the top of stack with its hyperbolic cosine. | (TOS)=COSH(TOS)
EXP      | Replaces the top of stack with e^(TOS). The operand must be no greater than 30.0. | (TOS)=EXP(TOS)
INT      | Replaces the top of stack with the largest integer whose absolute value does not exceed the absolute value of (TOS) and has the same sign as (TOS). | (TOS)=AINT(TOS)
LOG      | Replaces the top of stack with its natural (base e) logarithm.  The operand must be greater than 0.0. | (TOS)=LOG(TOS)
LOG10    | Replaces the top of stack with its common (base 10) logarithm. The operand must be greater than 0.0. | (TOS)=ALOG10(TOS)
NEG      | Replaces the top of stack with its negative. | (TOS)=-(TOS).
NINT     | Replaces the top of stack with the integer nearest to (TOS). | (TOS)=ANINT(TOS).
SIN      | Replaces the top of stack with its sine. The operand is assumed to be in units of radians. | (TOS)=SIN(TOS)
SIND     | Replaces the top of stack with its sine. The operand is assumed to be in units of degrees. | (TOS)=SIND(TOS)
SIN      | Replaces the top of stack with its hyperbolic sine. | (TOS)=SINH(TOS)
SQRT     | Replaces the top of stack with its square root. The operand must be greater than or equal to 0.0. | (TOS)=SQRT(TOS)
TAN      | Replaces the top of stack with its tangent. The operand is assumed to be in units of radians. | (TOS)=TAN(TOS)
TAND     | Replaces the top of stack with its tangent. The operand is assumed to be in units of degrees. | (TOS)=TAND(TOS)
TAN      | Replaces the top of stack with its hyperbolic tangent. | (TOS)=TANH(TOS)

Binary Arithmetic Operators:

Argument | Description | Equation
-------- | ----------- | --------
ADD      | Replaces (TOS) and (TOS-1) with their sum. | (TOS)=(TOS-1)+(TOS)
ATAN2    | Replaces (TOS-1) and (TOS) with the inverse tangent of their ratio. The result is in units of radians. | (TOS)=ATAN((TOS-1)/(TOS))
ATAN2D   | Replaces (TOS-1) and (TOS) with the inverse tangent of their ratio. The result is in units of degrees. | (TOS)=ATAND((TOS-1)/(TOS))
DIV      | Replaces (TOS-1) and (TOS) with their quotient. Division by zero is not allowed. | (TOS)=(TOS-1)/(TOS)
MAX      | Replaces (TOS-1) and (TOS) with the greater of the two values. | (TOS)=AMAX1((TOS-1),(TOS))
MIN      | Replaces (TOS-1) and (TOS) with the lesser of the two values. | (TOS)=AMIN1((TOS-1),(TOS))
MOD      | Replaces (TOS-1) and (TOS) with the remainder of: (TOS1)/(TOS). Division by zero is not allowed. | (TOS)=AMOD((TOS-1),(TOS))
MUL      | Replaces (TOS-1) and (TOS) with their product. | (TOS)=(TOS-1)\*(TOS)
SUB      | Replaces (TOS-1) and (TOS) with their difference. | (TOS)=(TOS-1)-(TOS)

Unary Logical Operators:

Argument | Description | Equation
-------- | ----------- | --------
NOT      | Replaces (TOS) with the bitwise not of its integer representation. | (TOS)=NOT INT(TOS)

Binary Logical Operators:

Argument | Description | Equation
-------- | ----------- | --------
AND      | Replaces (TOS-1) and (TOS) with the bitwise and of their integer representations. | (TOS)=INT(TOS-1) AND INT(TOS)
OR       | Replaces (TOS-1) and (TOS) with the bitwise or of their integer representations. | (TOS)=INT(TOS-1) OR INT(TOS)

Binary Relational Operators:

Argument | Description | Equation
-------- | ----------- | --------
EQ       | Replaces (TOS-1) and (TOS) with 1.0 if they are equal or with 0.0 if they are not equal. | (TOS)=(TOS-1)==(TOS)
GE       | Replaces (TOS-1) and (TOS) with 1.0 if (TOS-1) is greater than or equal to (TOS) or with 0.0 otherwise. | (TOS)=(TOS-1)>=(TOS)
GT       | Replaces (TOS-1) and (TOS) with 1.0 if (TOS-1) is greater than (TOS) or with 0.0 otherwise. | (TOS)=(TOS-1)>(TOS)
LE       | Replaces (TOS-1) and (TOS) with 1.0 if (TOS-1) is less than or equal to (TOS) or with 0.0 otherwise. | (TOS)=(TOS-1)<=(TOS)
LT       | Replaces (TOS-1) and (TOS) with 1.0 if (TOS-1) is less than (TOS) or with 0.0 otherwise. | (TOS)=(TOS-1)<(TOS)
NE       | Replaces (TOS-1) and (TOS) with 1.0 if they are not equal or with 0.0 if they are equal. | (TOS)=(TOS-1)!=(TOS)

Register Operators:

Argument | Description
-------- | -----------
LOAD     | Replace TOS with the value in the register position specified by TOS
STORE    | Store TOS-1 in the register position specified by TOS. STORE reduces the number of values on the stack by 2.

Special Operators:

Argument | Description
-------- | -----------
DUP      | Duplicates the top of stack, increasing the number of values on  the stack by 1. If the stack is empty, DUP will result in a (CALC0 ) STACK UNDERFLOW error message. Conversely, if the stack is full when `CALC` encounters the DUP operator, a (CALC0) STACK OVERFLOW error message will be displayed.
NDEC     | sets the number of decimal places for displaying or popping results from the calculator stack. The top of stack defines the maximum number of decimal places that will be displayed. On completion, NDEC pops the top of stack, decreasing the stack size be one. In order to use NDEC, the stack must not be empty. "-1 NDEC" directs `CALC` to display and pop results as integers i.e. with no decimal point, while "0 NDEC" yields results with a final decimal point but no digits to the right of the decimal point. Higher values of NDEC request additional digits to the right of the decimal point, but these may be dropped if the value is too large.
PRT      | Displays the top of stack as an informational message. The value of the top of stack is displayed with the current number of decimal places as set by a previous NDEC operator on the same `CALC` command line. If no NDEC operator preceded the PRT command, then the top of stack will be displayed as an integer (NDEC -1). On completion, PRT pops the top of stack, decreasing the stack size be one. In order to use PRT, the stack must not be empty.
SWAP     | Swap the positions on the stack of the values at (TOS) and (TOS-1)
\>       | Pops the top of stack into a global argument. The name of the global argument which will receive the value is given by the remaining characters in the `CALC` parameter beginning with "\>". The name of the global argument may not be blank, cannot be longer than sixteen characters, and must use only the characters A-Z, 0-9, $, or \_. Because \> pops the top of stack, the stack size is decreased by one after \> is processed. In order to use \>, the stack must not be empty.
\>\>     | Pops the top of stack into a local argument. The name of the local argument which will receive the value is given by the remaining characters in the `CALC` parameter beginning with "\>\>". The name of the local argument may not be blank, cannot be longer than sixteen characters, and must use only the characters A-Z, 0-9, $, or \_. Because \>\> pops the top of stack, the stack size is decreased by one after \>\> is processed. In order to use \>\>, the stack must not be empty.
\>\>\>   | Pops the top of stack into a symbol. The name of the symbol which will receive the value is given by the remaining characters in the `CALC` parameter beginning with "\>\>\>". The name of the symbol may not be blank, cannot be longer than sixteen characters, and must use only the characters A-Z, 0-9, $, or \_. Because \>\>\> pops the top of stack, the stack size is decreased by one after \>\>\> is processed. In order to use \>\>\>, the stack must not be empty.

Any argument on the `CALC` command line other than those listed above is treated as a default push onto the calculator
stack. Values may be pushed onto the stack only if the stack is not full, i.e. there are fewer than 10 values on the
stack before the push operation. A default push operation increases the stack depth by one. Because all `CALC`
manipulations are performed using real arithmetic, only integers or real numbers may be pushed onto the stack;
alphabetic and special characters may not be entered. Values to be pushed onto the stack may be written in exponential
notation if desired. A value to be pushed onto the stack must be no more than sixteen characters long. Values popped
from the stack into local or global arguments should not be more than sixteen characters. If a longer value is popped
into an argument the argument will be filled with \*s. Be careful not to set NDEC to too large a value in order to avoid
this situation. An example of a default push is shown in the command below:

    CALC 1 2 MAX PRT

Here, the arguments "1" and "2" are not operations known to RNMR, so they are interpreted as values to be pushed onto
the calculator stack. Once all operations specified on the `CALC` command line have been executed, RNMR checks that the
calculator stack is empty. If it is not empty, an error message will be displayed.
## CALCI
Perform integer arithmetic, logical, and bitwise calculations

Category: Calculator

Format: `CALCI` arg1 ... arg10

Defaults: none

Description:
`CALCI` performs desk calculator operations in reverse Polish notation. Arguments are pushed onto the calculator stack
and operations are performed on them, yielding results which may either be printed to the screen (PRT) or popped into
local (>>) or global (>) arguments or symbols (>>>). `CALCI` can perform basic arithmetic operations (+, -, \*, /) using
infix notation when pushing values onto the stack. Infix operations are performed left to right with no regard for order
of operations, but parentheses can be used to alter this order. The result of this infix math is pushed onto the stack
like any other argument. All calculations are performed internally using 32 bit integer arithmetic. As a result values
to be pushed onto the stack should be between -2,147,483,647 and 2,147,483,647. `CALCI` does allow for integer overflow
so be cautious if performing calculations with large numbers near these bounds. For example the following command:

    CALCI 2*3 PRT

will print the following as an informational message:

    VAL    =6

`CALCI` operates on each argument on the command line from left to right. The calculator stack used by `CALCI` has a
depth of 10. If an attempt is made to push more than 10 arguments onto the stack, the error message "(CALCI0 ) STACK
OVERFLOW" will be displayed. When `CALCI` encounters a unary arithmetic operator such as ABS (absolute value), it
expects that there exists at least one value on the stack on which to operate. To put this another way, TOS (Top Of
Stack) must exist. If the stack is empty, the error message "(CALC0) STACK UNDERFLOW" will be displayed. Similarly,
there must be at least two values on the stack in order to perform a binary arithmetic operation; a lack of sufficiently
many arguments will give an underflow error. When a binary operation is executed, the result replaces both (TOS) and
(TOS-1), reducing the number of values on the stack by one. When a constant is pushed onto the stack, the number of
values on the stack increases by one. When a unary operation is executed, the number of values on the stack does not
change.

The arguments which may be used with the `CALCI` command are as follows:

Unary Arithmetic Operators:

Argument | Description | Equation
-------- | ----------- | --------
ABS      | Replaces the top of stack with its absolute value | (TOS)=ABS(TOS)
EXP2     | Replaces the top of stack with 2 raised to the power given by the top of the stack. The operand must be no greater than 30. | (TOS)=2^(TOS)
LOG2     |  Replaces the top of stack with its base 2 logarithm. The operand must be greater than 0. | (TOS)=LOG2(TOS)
NEG      | Replaces the top of stack with its negative. | (TOS)=-(TOS).

Binary Arithmetic Operators:

Argument | Description | Equation
-------- | ----------- | --------
ADD      | Replaces (TOS) and (TOS-1) with their sum. | (TOS)=(TOS-1)+(TOS)
DIV      | Replaces (TOS-1) and (TOS) with their quotient using integer division. Division by zero is not allowed. | (TOS)=(TOS-1)/(TOS)
MAX      | Replaces (TOS-1) and (TOS) with the greater of the two values. | (TOS)=AMAX1((TOS-1),(TOS))
MIN      | Replaces (TOS-1) and (TOS) with the lesser of the two values. | (TOS)=AMIN1((TOS-1),(TOS))
MOD      | Replaces (TOS-1) and (TOS) with the remainder of: (TOS1)/(TOS). Division by zero is not allowed. | (TOS)=AMOD((TOS-1),(TOS))
MUL      | Replaces (TOS-1) and (TOS) with their product. | (TOS)=(TOS-1)\*(TOS)
SUB      | Replaces (TOS-1) and (TOS) with their difference. | (TOS)=(TOS-1)-(TOS)

Unary Logical Operators:

Argument | Description | Equation
-------- | ----------- | --------
NOT      | Replaces (TOS) with its bitwise not. | (TOS)=NOT (TOS)

Binary Logical Operators:

Argument | Description | Equation
-------- | ----------- | --------
AND      | Replaces (TOS-1) and (TOS) with their bitwise and. | (TOS)=(TOS-1) AND (TOS)
OR       | Replaces (TOS-1) and (TOS) with their bitwise or. | (TOS)=(TOS-1) OR (TOS)

Binary Relational Operators:

Argument | Description | Equation
-------- | ----------- | --------
EQ       | Replaces (TOS-1) and (TOS) with 1 if they are equal or with 0 if they are not equal. | (TOS)=(TOS-1)==(TOS)
GE       | Replaces (TOS-1) and (TOS) with 1 if (TOS-1) is greater than or equal to (TOS) or with 0 otherwise. | (TOS)=(TOS-1)>=(TOS)
GT       | Replaces (TOS-1) and (TOS) with 1 if (TOS-1) is greater than (TOS) or with 0 otherwise. | (TOS)=(TOS-1)>(TOS)
LE       | Replaces (TOS-1) and (TOS) with 1 if (TOS-1) is less than or equal to (TOS) or with 0 otherwise. | (TOS)=(TOS-1)<=(TOS)
LT       | Replaces (TOS-1) and (TOS) with 1 if (TOS-1) is less than (TOS) or with 0 otherwise. | (TOS)=(TOS-1)<(TOS)
NE       | Replaces (TOS-1) and (TOS) with 1 if they are not equal or with 0 if they are equal. | (TOS)=(TOS-1)!=(TOS)

Register Operators:

Argument | Description
-------- | -----------
LOAD     | Replace TOS with the value in the register position specified by TOS
STORE    | Store TOS-1 in the register position specified by TOS. STORE reduces the number of values on the stack by 2.

Bit Manipulation Operators:

Argument | Description
-------- | -----------
EXTRACT  | Extract (TOS) bits starting at bit (TOS-1) from (TOS-2). The extracted bits will be the least significant bits of the new (TOS) with all other bits being 0. EXTRACT reduces the number of values on the stack by 2.
INSERT   | Insert (TOS) bits starting at bit (TOS-1) from (TOS-2) into (TOS-3) and put the result in (TOS). The rest of the bits will be untouched. INSERT reduces the number of values on the stack by 3.
SHFT     | Replace (TOS) and (TOS-1) with (TOS-1) bit shifted by (TOS) bits. Positive (TOS) indicates a left shift while negative (TOS) indicates a right shift.

Special Operators:

Argument | Description
-------- | -----------
DUP      | Duplicates the top of stack, increasing the number of values on  the stack by 1. If the stack is empty, DUP will result in a (CALC0 ) STACK UNDERFLOW error message. Conversely, if the stack is full when `CALCI` encounters the DUP operator, a (CALC0) STACK OVERFLOW error message will be displayed.
PRT      | Displays the top of stack as an informational message. The value of the top of stack is displayed with the current number of decimal places as set by a previous NDEC operator on the same `CALCI` command line. If no NDEC operator preceded the PRT command, then the top of stack will be displayed as an integer (NDEC -1). On completion, PRT pops the top of stack, decreasing the stack size be one. In order to use PRT, the stack must not be empty.
SWAP     | Swap the positions on the stack of the values at (TOS) and (TOS-1)
\>\>     | Pops the top of stack into a local argument. The name of the local argument which will receive the value is given by the remaining characters in the `CALCI` parameter beginning with "\>\>". The name of the local argument may not be blank, cannot be longer than sixteen characters, and must use only the characters A-Z, 0-9, $, or \_. Because \>\> pops the top of stack, the stack size is decreased by one after \>\> is processed. In order to use \>\>, the stack must not be empty.
\>       | Pops the top of stack into a global argument. The name of the global argument which will receive the value is given by the remaining characters in the `CALCI` parameter beginning with "\>". The name of the global argument may not be blank, cannot be longer than sixteen characters, and must use only the characters A-Z, 0-9, $, or \_. Because \> pops the top of stack, the stack size is decreased by one after \> is processed. In order to use \>, the stack must not be empty.
\>\>\>   | Pops the top of stack into a symbol. The name of the symbol which will receive the value is given by the remaining characters in the `CALCI` parameter beginning with "\>\>\>". The name of the symbol may not be blank, cannot be longer than sixteen characters, and must use only the characters A-Z, 0-9, $, or \_. Because \>\>\> pops the top of stack, the stack size is decreased by one after \>\>\> is processed. In order to use \>\>\>, the stack must not be empty.

Any argument on the `CALCI` command line other than those listed above is treated as a default push onto the calculator
stack. Values may be pushed onto the stack only if the stack is not full, i.e. there are fewer than 10 values on the
stack before the push operation. A default push operation increases the stack depth by one. Because all `CALCI`
manipulations are performed using integer arithmetic, only integers may be pushed onto the stack; decimals as well as
alphabetic and special characters may not be entered. An example of a default push is shown in the command below:

    CALCI 1 2 MAX PRT

Here, the arguments "1" and "2" are not operations known to RNMR, so they are interpreted as values to be pushed onto
the calculator stack. Once all operations specified on the `CALCI` command line have been executed, RNMR checks that the
calculator stack is empty. If it is not empty, an error message will be displayed.
## CALIB
Determine data buffer amplitudes and phases

Category: Acquisition

Format: `CALIB` fcalib

Qualifiers: /REAL /IMAG

Qualifier Defaults: /REAL

Defaults: current

Prerequisites: Time domain data in processing buffer (TIME)

Description:
This command is used with the `CALIB` pulse program to calibrate spectrometer phases. It is to be used only by the
support staff. `CALIB` does not require the user to be viewing the processing block (`VIEW PRO`), but all manipulations
are performed on the processing block. The argument "fcalib" is a real number interpreted in the current frequency unit
of the processing buffer (PPM or absolute units). If "fcalib" is omitted from the command line, RNMR will prompt for a
frequency, with the current calibration frequency as the default. After conversion to Hz, the calibration frequency
must be nonzero.
## CASE
Process `CASE` clause of `SEL` block

Category: Macro

Format: `CASE` val

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`CASE` executes the block of commands that falls between it and either the next `CASE` command or `ENDSEL` if the value used in the `SEL` block matches val. If val is omitted then `CASE` will act as if it matches for any value. `CASE` must be between a `SEL` and a matching `ENDSEL`.
## CAT
List catalog of records

Category: Data Storage

Format: `CAT` first-rec last-rec

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: 5 200

Description:
`CAT` displays a catalog of archive records from first-rec to last-rec. `CAT` takes two parameters, which are the first
and last record numbers to be displayed. If these are omitted, the listing will begin with record 5 and end at record
200; RNMR will not prompt for "first-rec" and "last-rec".

Any value corresponding to a record in an open archive may be provided for first-rec. Records in archives other than 1
can be specified by either pre-pending the archive number and a ":" or specifying numbers larger than 200. For example
record # in archive can be specified either as 2:# or by adding 200 to #. Similarly, last-rec may be any integer from
the record number within an archive specified in first-rec to 200, inclusive. If only one argument is specified, `CAT`
will list information about only that single record. For each nonempty record, `CAT` returns the record  number, owner,
record length, record position within the archive, date, and title. Note that `CAT` reports record length and position
in units of blocks, which are 512 bytes long each.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## CATARV
List catalog of archives

Category: Data Storage

Format: `CATARV` first_archive last_archive

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: 1 4

Description:
Displays a list of archives from first-archive to last-archive which must be integers between 1 and 4. If only one
argument is specified, `CATARV` will list information about only that single archive. `CATARV` shows the archive number
and if the archive is open it also shows flags indicating the presence of read access and write access, as well as the
name of the archive.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## CATGBL
List catalog of global variables

Category: Arguments

Format : `CATGBL` first last

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATGBL` displays a catalog of the currently defined global arguments by name from first to last in alphabetical order.
If first is omitted from the command line, then the catalog will begin with the first entry in the global argument
table. RNMR will not prompt for first. Similarly, if last is not specified, `CATGBL` will list all global arguments. If
only one argument is specified, `CATGBL` will list information about only that single argument. Each global argument is
listed by name along with its current value.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## CATLCL
List catalog of local variables

Category: Arguments

Format: `CATLCL` first last

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATLCL` displays a catalog of the currently defined local arguments by name from first to last in alphabetical order.
If first is omitted from the command line, then the catalog will begin with the first entry in the local argument table.
RNMR will not prompt for first. Similarly, if last is not specified, `CATLCL` will list all local arguments. If only one
argument is specified, `CATLCL` will list information about only that single argument. Each local argument is listed by
name along with its current value.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## CATMAC
List catalog of macros

Category: Macros

Format: `CATMAC` first last

Defaults: none ZZZZZZZZ

Description:
`CATMAC` displays a catalog of the currently defined macros by name from "first" to "last" in alphabetical order.  Each
macro must have a unique name up to 8 characters long.  There may be as many as 100 defined macros at any time in an
RNMR session, including entries from both the user library (MACRO.DAT) and the system library (MACRO.SYS).  If "first"
is omitted from the command line, then the catalog will begin with the first entry in the macro table. RNMR will not
prompt for "first".  Similarly, if "last" is not specified, RNMR will list local arguments up to and including ZZZZZZZZ;
the user will not be prompted for "last".  Both "first" and "last" must be character strings beginning with A-Z,
containing only characters A-Z, 0-9, $, or \_, and no more than 8 characters long. While "first" may be blank, "last"
must be nonblank.  Each defined macro name is listed along with its entry number.  Positive entry numbers are assigned
to user macros (stored in MACRO.DAT) while negative entry numbers are assigned to system macros (stored in MACRO.SYS).
Recall that user macros are modifiable while system macros are not.  Pressing <RETURN\> or <SPACE\> lists the next macro
name while pressing "Q" or <CTRL-Z\> quits `CATMAC` and returns the console prompt.
## CATNUC
List catalog of nuclei

Category: Nuclei

Format: `CATNUC` first last

Defaults: none ZZZZZZZZ

Description:
`CATNUC` displays a catalog of the currently defined nuclei by name from "first" to "last" in alphabetical order.  If
"first" is omitted from the command line, then the catalog will begin with the first entry in the nucleus table. RNMR
will not prompt for "first".  Similarly, if "last" is not specified, RNMR will list nuclei up to and including
ZZZZZZZZ; the user will not be  prompted for "last".  Each defined nucleus is listed by name along with its current
frequency (PPM to Hz conversion factor) in MHz and its reference frequency in the current frequency unit (as set by
`UNIT /FREQ`).  The nucleus frequency is always reported to three decimal places, while the number of decimal places in
the reference frequency depends on the choice of frequency unit (as set by the `NDEC` command).  Pressing <RETURN\> or
<SPACE\> lists the next defined nucleus while pressing "Q" or <CTRL-Z\> quits `CATNUC` and returns the console prompt.
## CD
Perform convolution difference apodization

Category: Data Manipulation

Format: `CD` narrow wide wfract

Defaults: 0.0 0.0 0.0


Prerequisites: Time domain data in processing buffer (TIME)

Description:
`CD` performs a convolution difference apodization on an FID.  The apodization function applied to the FID is given by:

         	apodization = EM(narrow) - wfract*EM(wide)

Note that `CD` yields the same result as separately exponentially line broadening the original FID using `EM`, scaling
the wide result using `SC` and subtracting the two resulting FID's.  This apodization is useful for separating out
spectral components with greatly different line widths and for masking the effects of probe ring-down.  `CD` does not
require the user to be viewing the processing block (`VIEW PRO`), but apodization is only performed on the processing
block.  The narrow line broadening "narrow" and the wide line broadening "wide" are a real numbers expressed in the
current default frequency units (as displayed and set by `UNIT /FREQ /DFLT`).  If either of these parameters are not
specified, RNMR will prompt for its value with 0.0 as the default.  Each linewidth entered must be between -1000 Hz and
1000 Hz, inclusive.  The parameter "wfract" specifies the fraction of the wide component (with linewidth "wide") in the
apodization. This fraction is a real number between 0.0 and 1.0, inclusive.  If "wfract" is not specified, then RNMR
will prompt for its value with 0.000 as the default.

The apodization vector is calculated for each data point according to the formula:

    VEC(N) = EXP(-PI*L1*T(N)) - WFRACT*EXP(-PI*L2*T(N))         N=1,...,SIZE

where L1 and L2 are the narrow and wide line widths, respectively, and  T(N) is the time value of data point N in the
FID.  Each block of the processing buffer is separately multiplied by the apodization vector VEC(N), yielding an
apodized complex FID.  If the processing buffer is currently visible, `CD` always updates the display upon completion.
## CHN
Select channel Category:

Format:

Defaults:
## CLSARV
Close archive 	 `CHN`

Category: Data Storage

Format: `CLSARV` archive

Defaults: 1

Description:
Closes the specified archive.
## CLSB
Close blocked record

Category:

Format: `CLSB`

Defaults:
## CLSDSP
Close display

Category:

Format: `CLSDSP`

Defaults:
## CLSPLT
Close plotter stream and print

Category: Printing

Format: `CLSPLT`

Description:
`CLSPLT` writes out the current plot buffer and submits the resulting file for printing or plotting, terminating the
plot sequence that began with `OPNPLT`.  All plots between `OPNPLT` and `CLSPLT` will appear on one sheet of paper.
`CLSPLT` is legal only if the plot file is currently open.  If the plotter or printer selected by `PLDEV` is not
currently idle, `CLSPLT` sends the appropriate control sequences to put it in idle mode.  Next, the current plot buffer,
containing the code for each spectrum or FID to be plotted, is written out to a temporary plot file, PL.TMP, in the
user's directory.  This plot file is then submitted to the appropriate queue for printing or plotting.  Upon successful
generation of the plot, the plot file is deleted.
## CLSRD
Close file opened for read

Category: File IO

Format: `CLSRD`

Description:
`CLSRD` closes a file opened by `OPNRD` for reading with `RDWRT`.  If `CLSRD` is entered when no file is open for read,
RNMR will display an error message.
## CLSWRT
Close file which has been opened for writing

Category: File IO

Format: `CLSWRT`

Description:
`CLSWRT` closes a file opened by `OPNWRT` for writing with the `WRT` command.  All output from `WRT` commands issued
between `OPNWRT` and `CLSWRT` will appear in one file.  If `CLSWRT` is entered when no file is open for write, RNMR will
display an error message.
## CMUL
Multiply buffer by complex constant

Category: Data Manipulation

Format: `CMUL` valr valphi buf

Defaults: 1.0 0.0 1

Description:
`CMUL` multiplies the contents of a buffer by a complex constant, updating the buffer.  This constant is specified in
polar form:

REAL(CONST) = VALR\*COS(VALPHI\*PI/2)

IMAG(CONST) = VALR\*SIN(VALPHI\*PI/2)

The first parameter, "valr" is a real number which is the magnitude of the complex constant.  If this parameter is
omitted, the magnitude will be 1.0; RNMR will not prompt for "valr".  The second parameter, "valphi" is a real number
which is the polar angle phi of the complex constant in degrees.  If this parameter is omitted, this angle will be 0.0;
RNMR will not prompt for "valphi".  The last parameter, "buf" selects which processing buffer should be multiplied and
updated; the visible buffer is buffer 1.  The buffer number may be either 1 or 2.  If "buf" is omitted, buffer 1 will be
processed; RNMR will not prompt for "buf".  `CMUL` multiplies each block of the selected processing buffer by the
specified constant:

        BUFFER = BUFFER*CONST

If the processing buffer is currently visible and "buf" is 1, `CMUL` always updates the display upon completion.
## CMULV
Complex multiply two buffers

Category: Data Manipulation

Format: `CMULV` src dst

Defaults: 2 1

Description:
`CMULV` complex multiplies the destination buffer DST by the source buffer SRC changing the destination buffer:

        DST = DST * SRC

The arguments "SRC" and "DST" specify the numbers of the buffers to be multiplied.  Each buffer number may be either 1
or 2; buffer 1 is the visible processing buffer.  If either argument is omitted, RNMR will prompt for a buffer number.
The default source is buffer 2 while the default destination is buffer 1.  While `CMULV` operates only on processing
buffers, the user need not be viewing the processing buffers to perform the multiplication.  For two buffers to be
multiplied, they must have the same domain  (time or frequency) and the same active size (though not necessarily the
same allocated size).  If the destination buffer is partitioned into two or more blocks, each block is separately
multiplied by the corresponding block of the source buffer.  The number of blocks in the source buffer need not be the
same as that in the destination buffer.  RNMR uses the formula below to match source blocks with destination blocks:

        IBLK_SRC = MOD(IBLK_DST-1,NBLK_SRC) + 1,                    IBLK_DST=1,...,NBLK_DST

If the processing buffer is currently visible and "dst" is 1, `CMULV` always updates the display upon completion.
## CND
Set condition flag

Category: Misc.

Format: `CND` cnd# state

Defaults: 1 current

Description:
`CND` sets the state of the specified condition flag to ON or OFF.  The first parameter, "cnd#" specifies which of the
64 available condition flags is to be set. Accordingly, "cnd#" may be any integer from 1 to 64 inclusive.  If this
parameter is omitted, RNMR will prompt for a flag number with 1 as the default.  The second parameter, "state" specifies
the logical state to  which the condition flag should be set. The acceptable choices of this parameter are ON and OFF.
 If "state" is omitted, RNMR will prompt for the state of the `CND` flag with the current state as the default.  That
is, by default no changes are made to the condition flag.
## CNVFL
Convolution filter

Category:

Format: `CNVFL`

Defaults:

Description:
Convolution filter for time domain data processing (post-acquisition digital solvent suppression)
## COLOR
Set data display colors

Category: Display Control

Format: `COLOR` [qual] red green blue

Qualifiers: /REAL /IMAG /CURSOR

Qualifier defaults:         /REAL

Defaults: current_color_values

Description:
Sets the color for the display. Use /REAL and /IMAG to set the color of the real and imaginary data respectively. Use
/CURSOR to set the color of all cursors.

The red/green/blue values may each range from 0 to 100.  That is, to specify pure red, use  100  0   0.

Defaults are:

Option | Default Color
------ | -------------
/REAL  | 0 100 0 (Green)
/IMAG  | 100 0 0 (Red)
/CURSOR | 100 100 100 (White)

## CONJG
Complex conjugate data

Category: Data Manipulation

Format: `CONJG`

Description:
`CONJG` complex conjugates processing buffer 1:

         	BUF = CONJG(BUF)

The user need not be viewing the processing buffer in order to use `CONJG`.  If the buffer is partitioned into two or
more blocks, `CONJG` separately conjugates each block.  If the processing buffer is currently visible, `CONJG` always
updates the display upon completion.
## CONLIM
Set contour plot height limits

Category: `ZO2DC`

Format: `CONLIM` min max

Defaults: current current

Description:
`CONLIM` sets intensity limits for contour plotting.  Contours will only be drawn for intensities between these limits.
If either "min" or "max" is omitted from the command line, RNMR will prompt for the contour limit with its current value
as the default.  Contour levels are real numbers and are displayed to a maximum of three decimal places.  If the user
accepts the defaults for both "min" and "max", no changes are made to the current contour limits.  If both "min" and
"max" are 0.0 (`CONLIM` 0 0), then RNMR sets "max" to 1.0; "min" remains 0.0.  Thus, `CONLIM 0 0` resets the contour
limits to their system default values.  If "min" and "max" are not both zero, "max" must be strictly greater than "min".
 When a contour plot is generated, the maximum contour level will be "max" while the minimum contour level will approach
but not equal "min".
## CONMD
Set contour plotting mode

Category: `ZO2DC`

Format: `CONMD` mode

Defaults: current

Description:
`CONMD` sets the contour plotting mode.  The argument "mode" may be entered as ABS, NEG, or POS.  If "mode" is omitted,
RNMR will prompt for a contour plotting mode with the current mode as the default.  If the user accepts this default, no
changes are made.
## CPXV
Complex merge two buffers

Category: Data Manipulation

Format: `CPXV` src dst

Defaults: 2 1

Description:
`CPXV` combines the real parts of two buffers to form the real and imaginary parts of the destination buffer:

         	DST = COMPLEX(REAL(DST),REAL(SRC))

 or      REAL(DST) = REAL(DST)

 IMAG(DST) = REAL(SRC)

The arguments "SRC" and "DST" specify the numbers of the buffers to be processed. Each buffer number may be either 1 or
2; buffer 1 is the visible processing buffer.  If either argument is omitted, RNMR will prompt for a buffer number. The
default source is buffer 2 while the default destination is buffer 1.  While `CPXV` operates only on processing buffers,
the user need not be viewing the processing buffer to perform the operation.  For two buffers to be merged with `CPXV`,
they must have the same domain (time or frequency) and the same active size (though not necessarily the same allocated
size).  If the destination buffer is partitioned into two or more blocks, each block is separately merged with the
corresponding block of the source buffer.  The number of blocks in the source buffer need not be the same as that in the
destination buffer.  RNMR uses the formula below to match source blocks with destination blocks:

         	IBLK_SRC = MOD(IBLK_DST-1,NBLK_SRC) + 1,  IBLK_DST=1,...,NBLK_DST

If the processing buffer is currently visible and "dst" is 1, `CPXV` always updates the display upon completion.
## CPY
Copy record

Category: Data Storage

Format: `CPY` src dst

Defaults: current_read_record next_available_record

Description:
`CPY` copies the archive record "src" into record "dst".  Unlike `ALLCPY`, `CPY` copies both title parameters and data
from source to destination.  The first parameter, "src" is the number of the record to be copied. If no source record
number is specified, RNMR will prompt for "src" with the current read record (as displayed and set by `PTRA`) as the
default.  The allowable values of "src" are integers between 5 and 200, inclusive.  Consequently, scratch records may
not be copied by `CPY`.  The source record specified must not be empty.  The second parameter, "dst" is the number of
the destination record, i.e. the record which will contain a copy of "src".  If "dst" is not specified, then RNMR will
attempt to put the copy of "src" into the next available record; RNMR does not prompt for a destination record number.
If "dst" is zero, then RNMR will use the next available record for "dst". Otherwise, this parameter must be an integer
between 5 and 200; `CPY` does not copy records into scratch records (numbers 1-4).  When `CPY` is asked to use the next
available record for "dst", a search is made for an empty record starting with the current read record .  The search
proceeds toward record 200 and starts over at record 5 if no empty records are found ahead of the current record.  If no
empty records can be located, then an error message is displayed.  In this case, the user must either delete an existing
record (`DL`) or start a new archive.  If "dst" is specified and is not zero, then RNMR checks that the  requested
destination record is empty.  If it is not empty, an error message will be printed and neither the existing data nor
parameters of "dst" will be overwritten.  If the data file (\*DATA.DAT) is extended to hold the copy of "src", then RNMR
will display a message reporting the new data file size in blocks (512 bytes per block).  Once the copy operation has
been completed, `CPY` updates the current read record pointer to "dst".  Afterwards, `PTRA` will display the number of
the record which received the copy of "src".  If "dst" was zero or omitted, `CPY` displays the destination record number
as an informational message.
## CRS
Set cursor positions

Category: Display Control

Format: `CRS` cursor1_pos cursor2_pos

Defaults: current current

Description:
`CRS` takes two parameters, "crs1" and "crs2", which are cursor 1 and 2 positions, respectively.  These positions are
expressed in the current unit for the visible buffer (ACQ, PRO, or LCK) with the current maximum number of decimal
places for that unit.  The current unit is set and displayed by the `UNIT` command and the maximum number of decimal
places is set and displayed by `NDEC`.  If "crs1" or "crs2" is missing from the command line, RNMR will display the
current value for the missing position and prompt for a new value.  For each display limit, the user should enter a
value expressed in  the current time or frequency unit or "\*" to select the leftmost position.  If the user requests a
position to the left of the leftmost point in the data buffer, the cursor will be positioned at the leftmost data point.
 Similarly, if the position specified is beyond the rightmost data point, the cursor will be position at the rightmost
data point.  If the user specifies a position that is within the range of the data buffer but which does not correspond
to a specific data point, RNMR will set that position to the time or frequency of the closest data point to the right of
the value specified.
## CRTARV
Create archive

Category: Data Storage

Format: `CRTARV` archive name

Defaults: 1 TEMP

Description:
Creates and opens a new archive with read/write access.
## CVTMD
Set modes for blocked record index conversion

Category: Blocked Records

Format: `CVTMD` sizmd blkmd

Defaults: current current

Description:
`CVTMD` sets modes for blocked record index conversion.  The first parameter, "sizmd" is the record size conversion
mode.  If "sizmd" is omitted, RNMR will prompt for a mode with the current size conversion mode as the default.  The
legal choices for "sizmd" are SIZEA, SIZE, and CVTSZ.  The second parameter, "blkmd" is the record blocking
conversion mode.  If "blkmd" is omitted, RNMR will prompt for a mode with the current mode as the default.  The legal
values for "blkmd" are 0, 1, 2, 3, or 4.

## CVTSZ
Set sizes for blocked record index conversion

Category: Blocked Records

Format: `CVTSZ` ndim size(1) size(2) size(3) size(4)

Defaults: 2 current current current current

Description:
`CVTSZ` sets the sizes for a blocked record index conversion.  The first parameter, "ndim" is the number of dimensions
for the conversion. If "ndim" is not specified, RNMR will prompt for its value with a default value of 2.  The allowed
values of "ndim" are 1, 2, 3, or 4.  The remaining parameters are the sizes in each of the "ndim" dimensions. RNMR
expects to find "ndim" integers greater than or equal to 1 following "ndim".  These sizes are to be entered in order of
dimension, starting with dimension 1. If one or more of these is omitted, RNMR will prompt for its value with the
current conversion size in the appropriate dimension as the default.
# D
---
## D
Set pulse programmer delay

Category: Acquisition

Format: `D` dly msec

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD); RNMR only

Description:
`D` sets the length of a pulse program delay time in milliseconds.  Pulse program delays are specified in the PP source
code by DLY statements and assigned default values by DEF statements.  Upon loading a pulse program with the RNMR
command `EX`, these delays are initialized with any default values that were declared in the source code.  To modify or
check the current value of a delay, the RNMR command `D` may be entered whenever a pulse program is loaded; the
acquisition need not be stopped to use this command.  The first parameter of the `D` command, "dly", specifies which delay
is to be modified.  If "dly" is omitted, RNMR will prompt for its value with a default of 1.  The legal values for "dly"
are integers from 1 to 16.  While the pulse programmer supports 32 delays, only the first
16 can be set from RNMR; delays 17 through 32 may be used internally in a pulse program but are not accessible to RNMR.
The second parameter, "msec" specifies the length of the selected delay in milliseconds. If this parameter is omitted,
RNMR will prompt for the delay length with its current value as the default.  While delays may be entered with any
desired number of decimal places, restrictions on the speed of the pulse programmer limit the precision of delay values
to 0.01 msec, i.e. only the first two decimal places in "msec" are significant.  When a delay value is entered, RNMR
rounds the user's value down to the nearest multiple of 0.01 msec, thereby truncating any additional decimal places
specified by the user.  The resulting rounded value must lie between 0.0 msec and 1.0E+05 msec, inclusive.  Note that a
delay value of 0.0 msec directs the pulse programmer to simply skip the specified delay during the execution of the
pulse program.  If the user accepts the current delay value by pressing <RETURN\> at the "MSEC" prompt, RNMR does not
change the delay value.  After changing a delay with the `D` command during acquisition, several seconds will usually
elapse before the pulse programmer responds to the change.  However, if the delay value is modified before acquisition
is started, the first shot should reflect the modified delay setting.
## DADJ
Interactively adjust pulse programmer delay

Category: Acquisition

Format: `DADJ` dly

Defaults: 1

Prerequisites: Pulse program loaded (LOAD); (`VIEW ACQ`); RNMR only

Description:
`DADJ` interactively adjusts the value of a pulse programmer delay.  With acquisition is in progress, `DADJ` prompts the
user for a new delay value, updates the delay, and then prompts for the next value.  Thus, `DADJ` is equivalent to
multiple uses of the command `D`.  `DADJ` is particularly useful for dynamically optimizing the value of a delay by
examining the FID for each shot.  `DADJ` accepts one parameter, "dly", which specifies the number of the delay to be
adjusted.  If "dly" is omitted, RNMR will prompt for its value with a default of 1.  The legal values for "dly" are
integers from 1 to 16.  While the pulse programmer supports 32 delays, only the first 16 can be set from RNMR; delays 17
through 32 may be used internally in a pulse program but are not accessible to RNMR.  Once the delay to be adjusted has
been selected, `DADJ` enters a loop in which the user is prompted for values for that delay repeatedly.
In each iteration, the current value of the delay is displayed and the user is asked to enter a new value.  Each time
RNMR prompts for a delay value, RNMR rounds the user's  response down to the nearest multiple of 0.01 msec, thereby
truncating any digits specified beyond the second decimal place.  The resulting rounded value must lie between 0.0 msec
and 1.0E+05 msec, inclusive.  Note that a delay value of 0.0 msec directs the pulse programmer to simply skip the
specified delay during the execution of the pulse program.  If the user enters a delay value that is outside the legal
range  specified above, `DADJ` prints an error message but continues to prompt for new delay values.  All other errors
abort the `DADJ` loop and return the console prompt.  After each modification to delay "dly" during acquisition, several
seconds will usually elapse before the pulse programmer responds to the change.  After all desired delay adjustments are
complete, pressing <RETURN\> exits the `DADJ` loop and returns the console prompt.
## DBSZ
Set data buffer size and partitioning

Category: Misc.

Format: `DBSZ` ipro isize nblk

Defaults: 1 current current

Description:
`DBSZ` sets the allocated size and partitioning of a processing data buffer.  Each processing buffer may be partitioned
into multiple blocks of equal size such that the total number of data points in all  blocks does not exceed 8192.  By
partitioning the data buffer into two or more segments, multiple data sets may be similarly processed using a single
RNMR command.  This "vector processing" capability allows multidimensional processing to be performed many blocks at a
time at a considerable savings in computation time due to the reduction in the number of commands that must be
interpreted by RNMR.

The first parameter, "ipro" selects which data buffer is to be resized.  If this parameter is omitted, RNMR will prompt
for its value with a default of 1.  The allowable values of "ipro" are 1 and 2, thus `DBSZ` can resize only the two
processing buffers; to resize the acquisition buffer, use `DBSZA`.  Note that buffer 1 is the visible processing buffer.

The second parameter, "isize" sets the allocated size for each block of buffer "ipro".  If this parameter is omitted,
RNMR will prompt for its value with the current allocated size as the default.  The user may enter any integer from 0 to
8192 (inclusive) for "isize"; a size value of 0 is interpreted as 8192, the maximum permissible data buffer size.

The last parameter, "nblk" sets the number of blocks into which data buffer "ipro" is to be divided.  If this parameter
is omitted, RNMR will prompt for the number of blocks with the current "nblk" as the default.  The user may enter any
positive integer including zero for "nblk".  A value of zero for this parameter requests that NBLK be set to 8192/ISIZE,
which gives the maximum possible number of data blocks for a given choice of "isize". If both "isize" and "nblk" are set
to zero (`DBSZ * 0 0`), then the appropriate data buffer is partitioned into one block of allocated size 8192.  If no
modifications were made to "isize" or "nblk", `DBSZ` does nothing.  Otherwise, RNMR verifies that ISIZE X NBLK does not
exceed the maximum data buffer size of 8192.  Once either the size or number of blocks of the selected data buffer has
been modified, the active size of the buffer is set to its allocated size and the active number of blocks is set to 1.
Later on, the active size may be decreased below the allocated size and the number of blocks may be increased.  After
the size and partitioning have been modified, the data buffer is filled with zeroes.  If the selected processing buffer
"ibuf" is currently visible, `DBSZ` updates the display.
## DBSZA
Set acquisition buffer size and partitioning

Category: Acquisition

Format: `DBSZA` isize nblk

Defaults: current current

Prerequisites: RNMR only

Description:
`DBSZA` sets the allocated size and partitioning of the acquisition data buffer.  The buffer may be partitioned into
multiple blocks of equal size such that the total number of data points in all blocks does not exceed 8192. By
partitioning the data buffer into two or more segments, multiple FID's may be acquired with different parameters without
quitting and restarting acquisition between each parameter update.  This procedure assures that FID's with like
parameters are added together separately so that the averaged data  for each parameter value can be independently
retrieved after quitting the acquisition.

When there are multiple blocks in the acquisition buffer, successive shots fill up successive blocks until all blocks
have been stored, at which time the storage sequence repeats itself, adding successive shots to successive blocks.  To
use acquisition buffer partitioning properly, the user must ensure that successive shots are taken with the appropriate
parameters and that the parameter sequence repeats every "nblk" shots.

An example of the use of acquisition buffer partitioning is the collection of stepped-gradient spectra using the
waveform generator.  In such an experiment, the gradient strength is stepped automatically with each shot according to a
preset cycle (see WFGREF).  If the acquisition buffer contains one block per gradient value, a whole gradient series may
be taken with signal averaging without quitting and restarting acquisition multiple times.

The first parameter, "isize" sets the allocated size for each block of the acquisition buffer.  If this parameter is
omitted, RNMR will prompt for its value with the current allocated size as the default.  The user may enter any integer
from 0 to 8192 (inclusive) for "isize"; a size value of 0 is interpreted as 8192, the maximum permissible data buffer
size.
The second parameter, "nblk" sets the number of blocks into which the acquisition buffer is to be divided.  If this
parameter is omitted, RNMR will prompt for the number of blocks with the current "nblk" as the default.  The user may
enter any positive integer including zero for "nblk".  A value of zero for this parameter requests that NBLK be set to
8192/ISIZE, which gives the maximum possible number of data blocks for a given choice of "isize".  If both "isize" and
"nblk" are set to zero (`DBSZA 0 0`), then the  acquisition buffer is partitioned into one block of allocated size 8192.
 If no modifications were made to "isize" or "nblk", `DBSZA` does nothing. Otherwise, RNMR verifies that ISIZE X NBLK
does not exceed the maximum data buffer size of 8192.  Once either the size or number of blocks of the acquisition
buffer has been modified, the active size of the buffer is set to its allocated size and the active number of blocks is
set to 1.  Later on, the active size may be decreased below the allocated size and the number of blocks may be
increased.
## DCDB
Decode block limits

Category:

Format: `DCDB`

Defaults:
## DCDBP
Decode block limits in points

Category:

Format: `DCDBP`

Defaults:
## DCL
Execute a `DCL` command in background Category:  	Pipe OS

Format: `DCL`

Description:
`DCL` spawns a subprocess to execute a single `DCL` command.  This command is useful for performing background tasks
such as printing and submitting files which do not require a separate terminal session.  `DCL` also allows a macro to
compose and execute `DCL` commands transparently.  If the `DCL` command is used at console level, RNMR will prompt the
user for the command line to be executed.  This may be any valid `DCL` command up to 80 characters long.  If the user
presses <RETURN\> when prompted for a `DCL` command, no subprocess is created and the console prompt is returned.  If
`DCL` is used from within a macro, RNMR expects the `DCL` command to be delimited by two semicolons (;;) on the line
following `DCL`.  The entire line after ;; constitutes the `DCL` command string, as illustrated below:

    DCL
    ;;PRINT/NOHEADER XYZ.WRT

If the double semicolon delimiter ;; is not found on the line after `DCL`, or if there are no characters on the line
following ;;, `DCL` does nothing and the macro execution continues.  The `DCL` command line may contain local and global
argument substitutions, e.g.

    DCL
    ;;@MYCOMMAND &ABC %XYZ
The local and global arguments specified will be evaluated and filled in before the command line is passed to `DCL`.
The subprocess created by `DCL` is unable to either read from or write to the terminal; both SYS$INPUT and
SYS$OUTPUT are defined to be NLA0: (the null device).  Consequently, any attempt by the spawned process to read from the
terminal will result in an immediate end of file during read condition, and any data directed to the terminal will be
lost.  While the subprocess is executing the specified `DCL` command, no new RNMR commands may be entered.  During
execution, <CTRL-Z\> may not be used to cancel the subprocess, but any acquisition in progress continues without
interruption.  If the subprocess exits on error, RNMR will display an error message indicating the `DCL` error condition
returned.  If `DCL` was called from within a macro, the current macro error handler (as set by `ONERR`) is executed.
## DEC
Enable or disable decoupling

Category: Acquisition

Format: `DEC` state

Defaults: current

Prerequisites: Acquisition stopped (HALT); RNMR only

Description:
`DEC` sets the decouple flag FLAG_DEC on or off.  In all system pulse programs, FLAG_DEC must be on for decoupling to be
active.  Thus, for these programs, `DEC OFF` deactivates all decoupling.  To turn on decoupling, however, it may be
necessary to turn on additional decouple flags - see `DECFLG` for more details.  `DEC` takes one parameter, "state"
which may be either ON or OFF.  If "state" is omitted, RNMR will prompt for a decouple state with the current
decoupler state as the default.  If the user accepts the current decoupler state, no changes are made.
## DECFLG
Enable or disable segments of decoupling during a pulse sequence

Category: Acquisition

Format: `DECFLG` flag state

Defaults: 1 current

Prerequisites: Acquisition stopped (HALT); RNMR only

Description:
`DECFLG` sets a decouple segment flag on or off.  In system pulse programs, the decouple flags FLAG_DEC1 through
FLAG_DEC4 turn on and off segments of decoupling, while the main decouple flag FLAG_DEC disables all decoupling when it
is OFF.  That is, in order to have decoupling on during a segment of a pulse program, one must have FLAG_DEC ON and
the appropriate segment flag (if any) ON.  To turn FLAG_DEC on or off, use the command `DEC`.  To determine which
segment flags are used in a given pulse program, examine the PP book entry for that pulse program.

The first parameter of the `DECFLG` command, "flag" selects which decouple flag is to be set.  If this parameter is
omitted, then RNMR will prompt for its value with a default of 1, i.e. FLAG_DEC1 will be set by default.  The legal
values of "flag" are the integers 1, 2, 3, and 4.  A particular choice of "flag" directs `DECFLG` to set FLAG_DEC"flag".

The second parameter, "state" specifies whether the selected decouple flag should be turned on or off.  If "state" is
omitted, RNMR will prompt for a decouple state with the current state of "flag" as the default.  If the user accepts the
default state by pressing <RETURN\> at the STATE prompt, no changes are made.  The allowable values of "state" are ON
and OFF.
## DF
Differentiate data

Category: Data Manipulation

Format: `DF`

Prerequisites: Frequency domain data in processing buffer (FREQ)

Description:
`DF` differentiates data in the visible processing buffer (buffer 1).  While the user is not required to view the
processing buffer in order to use `DF`, `DF` acts only on that buffer.  Differentiation of a spectrum is often useful in
resolving subtle features on broad lines since inflection points on the source spectrum become peaks in its derivative.
If the processing buffer is partitioned into two or more blocks, `DF` differentiates each block independently.  If the
active size of each block in the processing buffer is 0 or 1, `DF` does nothing.

Differentiation replaces data points in each block of the processing buffer as shown below:

         	I(1) = Io(1)
         	I(2) = Io(3) - Io(2)
         	I(3) = (Io(4) - Io(2))/2
         	I(4) = (Io(5) - Io(3))/2
                .
                .                 .
         	I(ISIZE-1) = (Io(ISIZE) - Io(ISIZE-2))/2
         	I(ISIZE) = Io(ISIZE) - Io(ISIZE-1)

where Io(i) is the original value of the ith data point and I(i) is its updated value.  If the processing buffer is
currently visible, `DF` always updates the display.
## DFLT
Prompt for local variable with default

Category: Macro

Format: `DFLT` lclnam lclval prompt

Defaults: TEMP none none

Prerequisites: Macro only (MAC)

Description:
`DFLT` prompts the user for the value of a local argument if that argument has not already been defined.  The first
parameter, "lclnam" specifies the name of the local argument to be defined.  If this parameter is omitted, RNMR will
prompt for a local argument name.  The default action is to define a local argument named TEMP.  Legal argument names
are nonblank strings no more than eight characters long.  These names must be composed from the letters A through Z, the
numbers 0 through 9, and special characters $ and \_.  Argument names must not contain internal spaces.  If the argument
"lclnam" already exists, then `DFLT` does nothing.  The user will not be prompted for a new value, and macro execution
will continue with the next line.

The third parameter, "prompt" specifies a prompt string to use when RNMR prompts for the value of "lclnam".  If "prompt"
is not blank and "lclnam" is not defined, RNMR will prompt for the value of "lclnam" with "lclval" as the default.  If
"lclval" is omitted, then the default value of "lclnam" is blank.  If the user presses <RETURN\> at the prompt, "lclnam"
is defined with value "lclval".  Otherwise, "lclnam" is defined with the value that the user enters.  If "prompt" is
blank, "lclnam" is defined with value "lclval" and no prompt is made.

For example, if local argument ABC is undefined, the command

    DFLT ABC,123,VALUE

generates the prompt:

    VALUE = 123 _

If the user presses <RETURN\> at this prompt, ABC is defined with value "123". Otherwise, ABC is defined with the value
entered by the user.  Conversely, the command

    DFLT ABC,123
 defines the local argument ABC with the value 123 and no prompt is made.
## DG
Start acquisition with delay shots

Category: Acquisition

Format: `DG` ndly na

Defaults: current current

Prerequisites: Acquisition must be stopped (LOAD and HALT); RNMR only.

Description:
`DG` starts acquisition after `NDLY` dummy shots.  By starting the averaging of FID's after one or more dummy shots, the
initial magnetization is allowed to come to an equilibrium value before data is acquired.  When the pulse cycle
repetition is significantly faster than the longest relaxation time in the sample, the first several shots will show a
fluctuation due to saturation.  With sufficiently many dummy shots, the initial FID intensity comes to some equilibrium
value, so succeeding shots will start with a stable initial magnetization.

The first parameter of the `DG` command, "ndly" is the number of dummy shots to take before beginning signal averaging.
If this parameter is omitted, the current number of dummy shots (as displayed and set by `NDLY`) will be taken. RNMR
does not prompt for "ndly".  The legal values of "ndly" are the positive integers including zero.

The second parameter, "na" specifies the number of shots that will be taken with signal averaging.  Once "na" shots have
been taken, acquisition will stop automatically.  Before "na" shots have been taken, the user may stop acquisition
manually using the `QUIT` command.  If "na" is omitted from the command line, the current number of averaged shots (as
displayed and set by `NA`) will be taken.  RNMR does not prompt for "na".  The legal values of "na" are -1 and positive
integers excluding zero.  If "na" is -1, there will be no automatic limit to the number of shots taken, i.e. acquisition
will continue until halted by `QUIT` or `WAIT`.

`DG` always zeroes the acquisition buffer (averager) and shot counter.  If the acquisition buffer is currently visible,
then `DG` updates the display.  The acquisition parameters `NA` and `NDLY` are updated with the values specified for
"na" and "ndly" on the command line, if any.  The new settings override any values specified previously with the `NA`
and `NDLY` commands.

The number of averaged shots that will be taken is always `NA` if `DG` is executed at console level.  However, if `DG`
is called from a macro, either `NWAIT` or `NA` shots will be taken, whichever is smaller.  If `NWAIT` is 0, then `NA`
will determine the number of shots taken from a macro, and similarly, `NWAIT` shots will be taken if `NA` is -1 and
`NWAIT` is nonzero.

Once acquisition is started, each shot will increment the shot indicator in the upper right hand corner of the display.
If the acquisition block is visible, the current sum of FID's will be updated on the screen every two seconds or once
per shot, whichever is slower.  Note that the shot indicator counts off dummy shots with negative integers starting with
-1 and decreasing, while averaged shots are counted off with positive integers starting with 1.
## DIRB
Set blocked record access sequence

Category: Blocked Records

Format: `DIRB` ndim seq

Defaults: 2 current

Description:
`DIRB` sets the order in which the dimensions of a blocked record are accessed.  Dimensions of a multidimensional record
are always viewed with direction 1 as the "display" dimension and higher directions as the "blocked" dimensions.  `DIRB`
assigns dimensions to directions, controlling both the orientation in which the data set is viewed in `ZO2D`, `ZO2DC`,
and `PLOTC` and the order in which the data points are accessed for processing.  For example, it is possible to view a
two dimensional data set either along the acquisition dimension (dimension 1) or along the blocked dimension (dimension
2).  Since direction 1 is always the "display" direction, the first view is specified by `DIRB 2 12` and the second view
by `DIRB 2 21`.

The first parameter for `DIRB`, "ndim", is the number of dimensions to be sequenced. Each number of dimensions from one
to four is assigned a modifiable direction sequence. The "ndim" parameter selects which sequence is to be modified. If
"ndim" is omitted, RNMR will prompt for the number of dimensions with a default of 2. The legal values of "ndim" are 1,
2, 3, and 4.

The second parameter, "seq" assigns each dimension a direction.  If this parameter is omitted, RNMR will prompt for a
direction sequence with the current sequence for "ndim" dimensions as the default.  This sequence is a string of "ndim"
integers from 1 to "ndim" with no repeats.  For example, if "ndim" is 2, the legal direction sequences are 12 and 21,
while for an "ndim" value of 3, "seq" may be 123, 132, 213, 231, 312, or 321.  If "seq" fails to assign each dimension a
direction, then RNMR completes the sequence with the missing dimensions in ascending order.  Thus, if "ndim" is 4 and
the user enters the direction sequence 32, RNMR fills in the missing two fields to make the sequence 3214.  If the user
accepts the current direction sequence for "ndim" dimensions, no changes are made.
## DL
Delete records

Category: Data Storage

Format: `DL` first last

Defaults: 5 first

Description:
`DL` deletes all archive records by record number from "first" to "last".  Deleting records marks the appropriate title
records and blocks of the data file (\*DATA.DAT) as available for reuse.  Neither the size of the title file nor the
data file is reduced by `DL`; in order to compress the data file by eliminating deallocated blocks, use `SQZ` (an RNMR
command) or SQZARC (at the `DCL` prompt).

Since both "first" and "last" are record numbers, each must be an integer from 1 to 200, inclusive.  Further, "last"
must be greater than or equal to "first".  If "first" and "last" are equal, only one record is deleted.  If "first" is
omitted, RNMR will prompt for the number of the first record to be deleted with a default of 5.  However, if "last" is
omitted, RNMR will not prompt for its value and only one record, "first", will be deleted.

For example, the command:

    DL 5 20

directs RNMR to mark all records from 5 to 20 for deletion, while the commands

    DL 10 10

and

    DL 10

simply delete record 10.

Any records between "first" and "last" which are already empty are skipped by `DL`.  In order to delete a record, one of
the following must be true:

1.	The user owns the record to be deleted      (`USER`=OWNER).
2.	The current user is \*SYSTEM\*.
3.	The record to be deleted has no owner.  This means that the record has been allocated but never used.

Type `CAT` to check who owns a given record.  To check who is the current user, use the command `USER`.
## DLTARV
Delete archive

Category: Data Storage

Format: `DLTARV` archive

Defaults: 1

Description:
Deletes the specified archive.
## DO
Begin macro `DO` loop Category:  	Macro

Format: `DO` [qual] beg end argnam
	Qualifiers: 	/GBL    /LCL    /IDN
Qualifier defaults:           /LCL    (if "argnam" is nonblank)             none    (if "argnam" is blank)
Parameter defaults:                    1       beg     none

Prerequisites: Macro only (MAC)

Description:
`DO` begins a `DO` loop in a macro.  All macro commands between `DO` and `ENDDO` will be repeated according to the
user's specifications for "beg" and "end".  Optionally, `DO` may create and increment a local or global variable to
store the current iteration count and this count may also be displayed on the screen as an `IDN` field.  `DO` loops may
be nested up to a depth of 16.  Jumps out of `DO` loops are permitted, but a jump into a `DO` loop is not allowed except
as part of an extended range, as described below.

Any qualifiers to be used with `DO` must be specified before the parameters "beg", "end", and "argnam".  Remember to
leave a space between the command name "`DO`" and the qualifier, e.g. `DO /LCL` not `DO/LCL`.  Any combination of the
three qualifiers is permitted.

If /LCL is specified, RNMR will define a local argument named "argnam" to contain the current iteration count, i.e.
the number of times the instructions between `DO` and `ENDDO` have been executed plus one.

If /GBL is specified, RNMR will define a global argument named "argnam" to contain the current iteration count.  Note
that /LCL and /GBL are not mutually exclusive.

If /IDN is specified, the current iteration count will be displayed in the second `IDN` field at the top right hand
corner of the screen.

The first parameter, "beg" is the value assigned to "argnam" in the first pass through the `DO`/`ENDDO` loop.  Together
with "end", "beg" determines how many cycles will be executed even if no qualifiers are  specified and no arguments are
defined.  If "beg" is omitted, the counter will begin at 1; RNMR does not prompt for "beg".  The legal values for "beg"
are greater than or equal to one.

The second parameter, "end" is the value assigned to "argnam"  during the last `DO`/`ENDDO` cycle.  Together with "beg",
"end" determines how many cycles will be done.  If "end" is omitted, "end" is set equal to "beg", i.e. one cycle will be
done with "argnam" defined with value "beg".  The legal values for "end" are -1 and all integers greater than or equal
to "beg". If "end" is -1, all commands between `DO` and `ENDDO` will be performed repeatedly an unlimited number of
times; the user must break the cycle manually somewhere inside the loop via a command such as `GOTO`, `ONERR`, or
`MEXIT` or by pressing <CTRL-Z\>.

The last parameter, "argnam" specifies the name of a local or global argument to contain the current loop count.  If
"argnam" is omitted, any /LCL and/or /GBL qualifiers will be ignored and no local or global arguments will be created.
The argument name specified must be nonblank and must be composed from the characters A-Z, 0-9, $ and \_.  Argument
names may not contain internal blanks.  If "argnam" is present and valid but neither /LCL nor /GBL were specified, RNMR
defines a local argument "argnam" to contain the loop count.  That is, /LCL is the default qualifier when "argnam" is
nonblank.

Whether any arguments or `IDN` fields are defined or not by `DO`, the number of `DO` cycles will be:

End Values | Cycles
---------- | ------
end != -1  | end - beg + 1
end == -1  | unlimited

If one or more arguments or `IDN` fields are incremented by `DO`, each cycle will increment the appropriate counter by
one.  Note that any modifications to "argnam" by commands between `DO` and `ENDDO` will not affect the number of
repetitions.  In addition, the total number of cycles is not affected by any changes made to "beg" and "end" within the
`DO`/`ENDDO` loop.

`DO`/`ENDDO` loops in RNMR may have extended range.  That is, it is legal to jump out of a `DO`/`ENDDO` loop then jump
back in again after executing one or more statements.  The range of the `DO`/`ENDDO` loop is thus extended to include
all the statements after the jump out and before the jump back in.  Unlike FORTRAN, RNMR permits the statements in the
extended range to change the values of "beg" and/or "end" without effect on the number of cycles that will be executed.
This is possible because the `DO` command is only processed once.  Jumps into a `DO` loop are not allowed when that `DO`
command has not yet been processed, though the error will not be detected until the matching `ENDDO` statement is
executed.
## DPS
Digital peak suppression

Category:

Format: `DPS`

Defaults:
## DPS2D
Digital peak suppression for 2D

Category:

Format: `DPS2D`

Defaults:
## DW
Set dwell time for data sampling during acquisition

Category: Acquisition

Format: `DW` usec

Defaults: current

Prerequisites: Acquisition stopped (HALT); RNMR only

Description:
`DW` sets the dwell time for analog-to-digital conversion, in microseconds.  The dwell time is defined to be the time
per point used in digitizing the FID.  This time is related to the sweep width after Fourier transformation by
SW=1.0E+06/DW.  The `DW` command takes one parameter, "usec" which is the dwell time in microseconds.  If this
parameter is omitted, RNMR will prompt for a dwell time with the current `DW` as the default.  Note that although pulse
lengths are specified only to one decimal place in microseconds, dwell times are considered precise to 0.01 usec.  If
the user accepts the current dwell time (by pressing <RETURN\> at the `DW` prompt), no changes are made.  Otherwise, the
user must enter the new dwell time as a floating point number strictly greater than zero.  The dwell time "usec"
requested by the user may be adjusted by RNMR to meet certain analog-to-digital converter (ADC) restrictions.  If RNMR
is forced to adjust the dwell time from the value requested by the user, an informational message is displayed reporting
the adjusted dwell time.

On spectrometers with audio filters under computer control via S-bus, changing the dwell time resets the filter cutoff
frequencies.  The filter setting is identical for the real and imaginary channels.  Since the filter frequencies are
digitally programmed, only discrete cutoff values (in increments of 200.0 Hz up to 50000.0 Hz) are allowed.
Accordingly, RNMR sets the filters to the closest available values given the new dwell time and the current filter
factor (as displayed and set by `FLF`).  If the filter factor is 0.0, then the filters are disabled entirely.
Otherwise, they are set to the nearest cutoff setting at least as wide as FLF X (SW/2.0).  If the calculated filter
bandwidth exceeds 50000.0 Hz, then the filters are disabled entirely.  Whenever the dwell time is changed, the shot
counter and averager are zeroed.  Finally, if the acquisition buffer is currently visible, `DW` always updates the
display.

# E
---
## ECDB
Encode block limits

Category:

Format: `ECDB`

Defaults:
## ECDBP
Encode block limits in points

Category:

Format: `ECDBP`

Defaults:
## ELSTST
Separate the code blocks after a `TST` check

Category: Macro

Format: `ELSTST`

Prerequisites: Macro only (MAC)

Description:
`ELSTST` separates the two blocks of commands to be executed based upon the results of a conditional test using `TST`.
For usage details see the description of `TST`.
## EM
Exponential multiply FID

Category: Data Manipulation

Format: `EM` lb

Defaults: current

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`EM` performs exponential multiplication apodization.  In this  apodization, the FID is multiplied by a decaying real
exponential function.  This results in a broadening of spectral lines after Fourier transformation which masks noise at
the expense of resolution.  When a perfect, non-decaying complex sine wave is exponentially multiplied and Fourier
transformed, the result is a perfect Lorentzian line-shape.  While the user need not be currently viewing the processing
 buffer in order to use `EM`, `EM` operates only on processing buffer 1.

`EM` takes one argument, "lb" which is the line broadening factor expressed in the current default frequency units (Hz,
kHz, or MHz), as set and displayed by `UNIT /FREQ` or by `UNIT /FREQ /DFLT` if `UNIT /FREQ` is PPM.  The legal values
of "lb" are real numbers between -1000 Hz and 1000 Hz, inclusive.  If "lb" is omitted, RNMR will not prompt for a value
but rather will perform the apodization with the current line broadening factor, as set and displayed by the command
`LB`. If a legal value of "lb" is specified, the current line broadening factor will be updated before exponential
multiplication of the data.  `EM` multiplies each block of processing buffer 1 by the real function:

    F(I) = EXP(-PI*(I-1) * LB/SW)

where I is the index of the data point (I=1,2,...), `LB` is the line broadening factor, and `SW` is the buffer sweep
width.  If the processing buffer is currently visible, `EM` always updates the display.
## ENDDO
End a macro `DO` loop

Category: Macro

Format: `ENDDO`

Prerequisites: Macro only (MAC)

Description:
`ENDDO` marks the end of a macro `DO` loop.  All commands between `DO` and `ENDDO` are executed repeatedly according to
the parameters of the `DO` command.  Between `DO` and `ENDDO`, a control statement may cause execution to jump out of
the loop.  However, jumps into the loop are not legal and result in an error message when `ENDDO` is executed:

    (ENDDO0) NO MATCHING DO

Each time `ENDDO` is executed, RNMR checks whether the current `DO` loop is finished.  The `DO` loop is terminated if
the "end" parameter in the `DO` statement was not -1 and the current loop count is greater than or equal to "end" (see
description of the "end" parameter under `DO`).  If "end" was specified as -1 in the `DO` command, then repetition of
the commands between `DO` and `ENDDO` will continue indefinitely; only a jump out of the loop or <CTRL-Z\> will
terminate the loop.

If execution of the current `DO`/`ENDDO` cycle is finished, `ENDDO`  decreases the `DO` stack depth by one, thus
increasing the number of nested `DO` loops that may be added by one.  The maximum depth of `DO`/`ENDDO` nesting that may
exist at any time is 16 levels.

If execution of the `DO`/`ENDDO` loop is not complete, `ENDDO` causes macro execution to jump to the next line after the
matching `DO` statement and the current loop count is incremented by 1.  If `DO` specified that a screen identification
field should be incremented (`DO` /`IDN`), then that field is updated to show the new loop count.  Similarly, any local
and/or global arguments created by `DO` are incremented by one.  For more details on the use of `DO`/`ENDDO` loops in
macros, see the description of the `DO` command.
## ENDTST
End a macro `TST` block

Category: Macro

Format: `ENDTST`

Prerequisites: Macro only (MAC)

Description:
`ENDTST` marks the end of a `TST` block used for conditional execution of commands. For usage details see the
description of `TST`.
## EX
Load a pulse program experiment

Category: Acquisition

Format: `EX` ppnam

Defaults: current

Prerequisites: Acquisition stopped (HALT), RNMR only

Description:
`EX` loads a pulse program into the pulse programmer.  To load a pulse program, the user must specify the name of that
program as the parameter "ppnam".  If "ppnam" is omitted, RNMR will prompt for the name of the pulse program to be
loaded with the currently loaded PP (if any) as the default.  If the user presses <RETURN\> at the `EX` prompt, no
changes are made.  If a new pulse program is specified, RNMR searches for the object code (\*.PPO) according to the
following search path:

 	(first) 	 	(current directory)
 	 	 	RNMR_SPECIFIC:[RNMR.PP]  	 	 	RNMR_GROUP:[RNMR.PP]
 	(last) 	 	RNMR_COMMON:[RNMR.PP]

When loading a pulse program, `EX` first checks that the version of the pulse program object code for "ppnam" is up to
date.  If not, the error message:

        (SUPP ) PROGRAM IS INCORRECT VERSION

will be displayed. If this occurs, the user should recompile before attempting to load it again with `EX`.  Once `EX`
has read the pulse program header, the title of the program (as specified in the PP source code using by the `TITLE`
statement) is displayed as an informational message.  This title is usually a brief description of the function of the
pulse program.

`EX` loads the pulse programmer with the current values of `SIZE`, `DW`, `RD`, HETR, `DEC`, and `DECFLG 1` through
`DECFLG 4`.  Note that the pulse programmer performs the recycle delay in discrete 0.1 second steps, so the actual
recycle time executed may be slightly different than that requested due to rounding to the nearest multiple of 0.1 sec.
See documentation under `RD` for more details.  When a pulse program is loaded into the pulse programmer, all the
default values for pulse lengths, loop counts, etc. specified within the program become active and will be executed
unless changed from RNMR.
## EXP
Export data to foreign format

Category: Foreign

Format: `EXP` format

Defaults: NMR1

Description:
`EXP` exports the contents of processing buffer 1 to a disk file in a foreign (non-RNMR) format.  This exportation
allows one-dimensional data to be transferred from RNMR to another processing program or from one RNMR archive to
another via `IMP`.

`EXP` takes one parameter, "format" which specifies the foreign destination format.  If "format" is omitted, RNMR will
prompt for a  foreign format with NMR1 as the default.  The currently supported foreign formats are:

Format | Description
------ | -----------
FELIX  | FELIX, complex data
FTNMR  | FTNMR, complex data
FTNMRR | FTNMR, real data
NMR1   | NMR1/NMR2, standard blocks
NMR1A  | NMR1/NMR2, alternate blocks 	(NMR1 and NMR1A formats are identical for 1D data.)
VARIAN | Complex data
BRUKER | Real data

Supported formats for page layout programs (these do not include acquisition parameters):

Format | Description
------ | -----------
ASCII  | Generic ASCII
SPYG   | IEEE floating point for Spyglass

Note that while the user need not be viewing the processing buffer to use `EXP`, `EXP` exports only the contents of
processing buffer 1.  If the `EXP` command is used at console level, RNMR will prompt the user for the name of the file
to contain the exported data.  The user may enter any valid VMS file name up to 64 characters long.  If the user presses
<RETURN\> at this prompt, no data is exported and no file is created.  If `EXP` is used from within a macro, RNMR
expects the foreign format file name to be delimited by two semicolons (;;) on the line following the `EXP` command.
The entire line after ;; constitutes the file name, as illustrated below:

         	EXP FTNMR
         	;;MYFILE.DAT

If the double semicolon delimiter ;; is not found on the line after `EXP`, RNMR will prompt for a file name as when
`EXP` is used from console level.  Conversely, if ;; is present but there is no text on the line after ;;, then `EXP`
does nothing and the macro execution continues.  The text following ;; may be any valid VMS file name up to 64
characters long. This text may contain local and global argument substitutions, e.g.

 	        EXP FTNMR
         	;;MYFILE_&1
The local and global arguments specified will be evaluated and filled in before the export file is created.

If no VMS file type was specified in the export file name, RNMR uses

Format | File Type
------ | -----------
FELIX  | .FELIX
FTNMR  | .FTNMR
NMR1 or NMR1A | .NMR1
ASCII  | .ASCII
SPYG   | .SPYG

Unlike `OPNWRT`, `EXP` will create a new version of the output file if there already exists a file in the current
directory with the name entered by the user.  Note that if processing buffer 1 is divided into two or more blocks, `EXP`
writes out data from the first block only.
## EXP2D
Export 2D data to foreign format

Category: Foreign

Format: `EXP2D` format rec blk2d

Defaults: NMR1 current 1

Description:
`EXP2D` exports a two-dimensional slice of a blocked archive record to a file in a foreign (non-RNMR) format. This
exportation allows two-dimensional data to be transferred from RNMR to another processing program or from one RNMR
archive to another via `IMP2D`.

The first parameter, "format" specifies the foreign destination format.  If "format" is omitted, RNMR will prompt for a
foreign format with NMR1 as the default.  The currently supported foreign formats are:

Format | Description
------ | -----------
FELIX  | FELIX, complex data
FTNMR  | FTNMR, complex data
NMR1   | NMR1/NMR2, standard blocks
NMR1A  | NMR1/NMR2, alternate blocks

Supported formats for page layout programs (these do not include acquisition parameters):

Format | Description
------ | -----------
SPYG   | IEEE floating point for Spyglass

The second parameter, "rec" specifies the number of a blocked archive record containing the data to be exported.  If
this parameter is omitted, RNMR will prompt for a source record number with the current read record (as displayed and
set by `PTRA`) as the default.  The acceptable values of "rec" are integers from 5 to 200; the scratch records (1-4) are
always one-dimensional. RNMR checks that "rec" is in fact a nonempty blocked record.  If "rec" is not a blocked  record,
RNMR will display the error message:

        (CHKTYP) RECORD WRONG TYPE

The last parameter, "blk2d" specifies which 2D slice of a 3D or 4D source record should be written out in the foreign
format. If the source record has only two dimensions, "blk2d" must be 1.  If "blk2d" is omitted, then the first 2D slice
of the source record will be exported.  That is, the default value of "blk2d" is 1.  RNMR does not prompt for "blk2d".
The legal values of "blk2d" are the integers 0,1,2,... up to the number of 2D slices in the source record. If "blk2d" is
zero, then RNMR will export the next 2D slice.  The command `PTRB` displays the current read block for a given record;
"blk2d" equal to zero directs `EXP2D` to export the block after the current read block.  Note that the current mapping
of dimensions to directions (as displayed and set by `DIRB`) will affect the selection of which one-dimensional blocks
of record "rec" comprise the 2D slice "blk2d" and will thus be exported.  When `EXP2D` is used to export 2D slices of a
four-dimensional record of size A X B X C X D, "blk2d" values from 1 to C select slices from the first cube, C+1 to 2C
select slices from the second cube, etc.  In this way, selection of 2D slices from a 4D data set can be accomplished
with one parameter, "blk2d".

If the `EXP2D` command is used at console level, RNMR will prompt the user for the name of the file to contain the
exported data.  The user may enter any valid VMS file name up to 64 characters long.  If the user presses <RETURN\> at
this prompt, no data is exported and no file is created.

If `EXP2D` is used from within a macro, RNMR expects the foreign format file name to be delimited by two semicolons (;;)
on the line following the `EXP2D` command.  The entire line after ;; constitutes the file name, as illustrated below:

        EXP2D FTNMR 25 34
        ;;MYFILE.DAT

If the double semicolon delimiter ;; is not found on the line after `EXP2D`, RNMR will prompt for a file name as when
`EXP2D` is used from console level.  Conversely, if ;; is present but there is no text on the line after ;;, `EXP2D`
does nothing and the macro execution continues.  The text following ;; may be any valid VMS file name up to 64
characters long.  This text may contain local and global argument substitutions, e.g.

        EXP2D FTNMR 25 34
        ;;MYFILE_&1

The local and global arguments specified will be evaluated and filled in before the export file is created.

If no VMS file type was specified in the export file name, RNMR uses:
Format | File Type
------ | -----------
FELIX  | .FELIX
FTNMR  | .FTNMR
NMR1 or NMR1A | .NMR1
ASCII  | .ASCII
SPYG   | .SPYG

Unlike `OPNWRT`, `EXP2D` will create a new version of the output file if there already exists a file in the current
directory with the name entered by the user.

Upon completion, the current read block of record "rec", as set and displayed by `PTRB`, is set to "blk2d" if "blk2d" is
nonzero.  If "blk2d" is zero, then the current read block is incremented by 1.  In addition, the current read record, as
set and displayed by `PTRA`, is set to "rec" by `EXP2D`.

Using the automatic block advance feature of `EXP2D` ("blk2d" equals 0), a 3D data set may conveniently be exported to a
sequence of 2D foreign format files, as shown in the example below:

    ! EXPORT 3D RECORD #29 TO SEQUENCE OF 2D NMR1 FILES
    DIRB 3 123       ! SET DIRECTION FOR BLOCKED ACCESS
    SET IMSG OFF 1 1 ! GET SIZE OF DIMENSION 3
    SIZEB 29 3
    SET IMSG ON
    PTRB 29 0 >        ! SET READ POINTER TO FIRST BLOCK
    DO /LCL 1,%1,BLK2D ! EXP EACH 2D SLICE TO NMR1 FILE
    EXP2D NMR1 29 0
    ;;3DDATA_SLICE&BLK2D
    ENDDO

This macro exports the first 2D slice of record 29 to 3DDATA_SLICE1.NMR1, the second slice to 3DDATA_SLICE2.NMR1, etc.
## EXP3D
Export 3D data to foreign file format

Category: Foreign

Format: `EXP3D` format rec blk3d

Defaults: NMR1 current 1

Description:
Currently supported formats: SPYG
# F
---
## F
Set synthesizer offset frequency

Category: Freq. Control

Format: `F` syn freq

Defaults: current current

Prerequisites: For RNMR: Acquisition stopped (HALT)
 	 	 	For RNMRP:  	no restrictions

Description:
`F` sets the frequency offset of a spectrometer synthesizer.  When `F` is used in RNMR on a spectrometer with S-bus
interfaced synthesizers, `F` resets the actual output frequency as well as the scale offset for processing.  On all
spectrometers without implemented synthesizer control and in RNMRP, the `F` command only affects the frequency scale
offset.

The first parameter, "syn" selects which synthesizer is to be adjusted.  If "syn" is omitted, RNMR will prompt for a
synthesizer number with the number of the current observe channel synthesizer as the default.  Since RNMR currently
supports up to four synthesizers, legal values of "syn" are integers from 1 to 4.  The synthesizer selected must have an
assigned nucleus.  To assign a nucleus to a synthesizer, use the command `NUC`.

The second argument, "freq" specifies the frequency offset to which the selected synthesizer will be set.  If this
argument is omitted, RNMR will prompt for a frequency with the current synthesizer offset as the default.  When RNMR
prompts with the current offset, this offset is expressed in the current frequency units for synthesizer "syn" (Hz, kHz,
MHz, or PPM) and includes any contribution from the reference frequency of the assigned nucleus.  Consequently, whenever
the reference frequency for the assigned  nucleus is changed by `NUCD`, the offset displayed by `F` will be changed to
reflect the new reference frequency.

The number of decimal places reported for the offset frequency is displayed and set by `NDEC` for the current frequency
unit. If the user accepts the current frequency by pressing <RETURN\> at the FREQ prompt, no changes are made.  The
frequency offset set by `F` is considered to be precise to 0.1 Hz, regardless of the choice of frequency units or number
of decimal places (`NDEC`).

The actual frequency output by the spectrometer is a function of the reference frequency and PPM to Hz conversion factor
of the synthesized nucleus as well as the offset selected by the `F` command:

    Factual(Hz) = 1.0E+06*FPPM(MHz) + FREQ(Hz) + FREF(Hz)

where FPPM is the PPM to Hz conversion factor and FREF is the reference frequency of the nucleus assigned to the
selected synthesizer and FREQ is the frequency entered with the `F` command.  Thus, if `NUC 1` is H1 with
`NUCD H1 359.600 250.0`, and `UNIT /FREQ` is Hz, entering `F 1 1000.0` gives an actual channel 1 frequency of
359.6012500 MHz.  The PPM to Hz conversion factor thus provides the base frequency, which is offset by small amounts
using the `F` command.

Changes to the spectrometer frequency for a given nucleus should be made by adjusting `F` rather than by redefining the
nucleus with `NUCD`.  Changes to FREF modify the synthesizer offset displayed by `F` but never change the synthesizer
setting itself.  FREF is simply used to redefine the zero point in frequency to a convenient value.  Changes to FPPM via
`NUCD` will result in modification of the spectrometer frequency, but only after `F`, `FSYN`, or `NUC` is entered since
`NUCD` does not update the synthesizer hardware.  After modifying the current synthesizer nucleus values with `NUCD`,
use `NUC` to call up the new nucleus definition and reset the synthesizer.  For example, if H1 is the nucleus assigned
to synthesizer 1, one may change the FPPM value for H1 with `NUCD H1` and then reset the synthesizer hardware by
entering `NUC 1 H1`.  If the frequency table for the selected synthesizer has been modified with the `FSYN` command,
only those table entries with value "\*" are affected by the `F` command.  All other entries yield frequencies which are
determined by FPPM and `FSYN`.  For more information on defining frequency table entries and their use in pulse
programs, see `FSYN`.

In RNMRP, `F` modifies the offset of processing buffer 1.  The user need not be viewing this buffer to use the `F` command.
The actual offset will be set to FREQ(Hz) + FREF(Hz), where FREF is the reference frequency for the nucleus assigned to
synthesizer "syn".  If the processing buffer is currently visible, `F` will update the display whenever the offset is
modified to show the new frequency scale.  All other aspects of the `F` command are identical in RNMR and RNMRP.  Thus,
the `F` command in RNMRP serves to make corrections to the frequency scales stored with experimental spectra.
## FLF
Set filter factor

Category: Acquisition

Format: `FLF` factor

Defaults: current

Prerequisites: Acquisition stopped (HALT) RNMR only

Description:
On spectrometers with S-bus interfaced acquisition filters, `FLF` sets the filter bandwidth factor.  This factor is used
to compute the cutoff frequencies for both the real and imaginary channel filters.  `FLF` takes one parameter, "factor"
which specifies the filter cutoff scaling factor.  If this parameter is omitted, RNMR will prompt for a factor with the
current filter factor as the default.  The allowable values for "factor" are real numbers from 0.0 to 5.0, inclusive.
If the user accepts the current filter factor by pressing <RETURN\> at the FACTOR prompt, no changes are made to the
filter settings.  Since the filter frequencies are digitally programmed, only discrete cutoff values (in increments of
200.0 Hz up to 50000.0 Hz) are allowed.  Accordingly, RNMR sets the filter cutoffs to the closest available value given
the current dwell time (as displayed and set by `DW`) and the filter factor (as displayed and set by `FLF`).  If the
filter factor is 0.0, then the filters are disabled entirely.  Otherwise, they are set to the nearest cutoff setting at
least as wide as FLF X (SW/2.0). If the calculated filter bandwidth exceeds 50000.0 Hz, then the filters are
disabled entirely.  Note that larger values of "factor" give wider filter cutoffs.  The filter factor is saved to
archive records by the commands `SA`, `SB`, and `SS` and is reported for those records by `LP`, even if S-bus filter
control is not implemented in the spectrometer running RNMR.
## FMX
Frequency modulation

Category:

Format: `FMX`

Defaults:

Description:
## FMXEX
Load frequency modulation program

Category:

Format: `FMXEX`

Defaults:
## FSYN
Define synthesizer frequency table

Category: Acquisition

Format: `FSYN` syn ifreq freq

Defaults: current 1 current

Prerequisites: Acquisition stopped (HALT) RNMR only

Description:
`FSYN` defines a frequency in a synthesizer frequency table.  Each synthesizer has a frequency table which specifies a
sequence of offsets which may be used during the course of a pulse program.  By modifying the entries in the frequency
tables, `FSYN` permits the user to specify which offset each synthesizer will use at different phases of the pulse
program.

The first parameter, "syn" selects which synthesizer will be affected.  If "syn" is omitted, RNMR will prompt for a
synthesizer number with the number of the current observe channel synthesizer as the default.  Since RNMR currently
supports up to four synthesizers, legal values of "syn" are integers from 1 to 4.  The synthesizer selected must have an
assigned nucleus.  To assign a nucleus to a synthesizer, use the command `NUC`.

The second parameter, "ifreq" is the entry number to be defined for synthesizer "syn".  For each synthesizer, there are
16 available frequency table entries.  At the present time the first table entry (ifreq=1) sets the frequency during the
presaturation period while all other entries are unused.  If "ifreq" is not specified, RNMR will prompt for an entry
number with 1 as the default, i.e. the default action is to modify the first table entry for the selected nucleus.  The
legal values of "ifreq" are integers from 1 to 16, inclusive.

The last argument, "freq" specifies the frequency offset to which the selected table entry will be set.  If this
argument is omitted, RNMR will prompt for a frequency with the current synthesizer table entry as the default.  If the
specified synthesizer table entry is undefined and "freq" is omitted, RNMR displays the current offset as
'\*\*\*\*\*\*\*\*'.  When RNMR prompts with the current offset, this offset is expressed in the current frequency units
for synthesizer "syn" (Hz, kHz, MHz, or PPM) and includes any contribution from the reference frequency of the assigned
nucleus.  Consequently, whenever the reference frequency for the assigned nucleus is changed by `NUCD`, the offset
displayed by `FSYN` will be changed to reflect the new reference frequency.  The number of decimal places reported for
the offset frequency is displayed and set by `NDEC` for the current frequency unit.  If the user accepts the current
frequency by pressing <RETURN\> at the FREQ prompt, no changes are made.  The frequency offset set by `FSYN` is
considered to be precise to 0.1 Hz, regardless of the choice of frequency units or number of  decimal places (`NDEC`).
If the user enters "\*" for "freq", RNMR will mark the specified table entry as undefined. This implies that the
frequency for that entry will be calculated by:

    Factual(Hz) = 1.0E+06*FPPM(MHz) + FREQ(Hz) + FREF(Hz)

where FPPM and FREF are frequencies defined for each nucleus by `NUCD`  and FREQ is the frequency entered with the F
command.  That is, a table entry of \* directs RNMR to follow the F command when calculating the corresponding
frequency.  If a table entry has a value other than \*, the corresponding frequency is calculated by:

    Factual(Hz) = 1.0E+06*FPPM(MHz) + `FSYN`(Hz) + FREF(Hz)

where `FSYN` is the value for "freq" entered into the table with the `FSYN` command.  Note that FREF defines the zero
point for frequency offsets but changes to FREF (via `NUCD`, `REF`, or `FSYS`) do not change the physical synthesizer
setting.  Changes to FPPM (via `NUCD` or `FSYS`) do change the synthesizer setting but only after the synthesizer
hardware is updated by `FSYN`, `F`, or `NUC`.

Once a synthesizer table entry is modified by `FSYN`, RNMR updates the corresponding entry of the synthesizer controller
hardware immediately.  Thus, the synthesizer is ready to execute the new frequency table immediately after it is
modified by `FSYN`.  At present, RNMR only examines the first two `FSYN` entries for each synthesizer, so a given pulse
program may only use these two frequencies.  Execution of each shot always begins with the first frequency in the table.
 Table frequencies are selected from within a pulse program by performing a pulse on GATE_SYN1 (to select the first
table frequency) or GATE_SYN2.
## FSYS
Set spectrometer system frequency

Category: Freq. Control

Format: `FSYS` fsys

Defaults: current

Description:
`FSYS` sets the spectrometer system frequency in MHz.  The system  frequency is defined to be the spectrometer frequency
for protons.  Thus, the system frequency depends only on the strength of the magnetic field for the spectrometer running
RNMR; "fsys" has one and only one value for each spectrometer.  All nucleus table entries are referenced to the system
frequency so that when "fsys" is updated, the PPM to Hz conversion factors and reference frequencies of all known nuclei
are modified appropriately.

`FSYS` takes one parameter, "fsys" which is the proton frequency in MHz.  This frequency is considered precise to 0.001
MHz and is reported by RNMR to three decimal places accordingly.  If "fsys" is omitted from the command line, RNMR will
prompt for a system frequency with the current frequency as the default.  If the user presses <RETURN\> at the `FSYS`
prompt or enters a value for "fsys" identical to the current value, no changes to the system frequency or nucleus table
are made.  Any real number may be entered for "fsys".

When "fsys" is modified, RNMR stores the new system frequency and updates the nucleus table.  Both the reference
frequency and PPM to Hz conversion factor of each nucleus are updated unless the conversion factor for that nucleus is
1.0, in which case no change is made to that nucleus entry.  While `FSYS` changes the frequency values of each nucleus,
the synthesizers are not updated with these new frequencies until the user issues a `NUC`, `F`, or `FSYN` command for each
synthesizer.
## FT
Fourier transform FID

Category: Data Manipulation

Format: `FT` size fctr1

Defaults: current 1.0

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`FT` performs a fast Fourier transform on time domain data in  processing buffer 1.  If the number of active points in
each block of the processing buffer is not a power of 2, zero filling is performed to increase the size to the next
power of 2.

The first parameter of `FT` is "size", which is the desired number of points after Fourier transformation.  If this
parameter is omitted, the size after transformation will be the smallest power of 2 greater than or equal to the FID
size. Thus, if the FID has 200 points, its Fourier transform will have 256 points.  When the size of the FID is not a
power of 2, RNMR zero fills the FID to the next power of 2 before Fourier transformation.  If "size" is omitted, RNMR
will not prompt for a size.  If "size" is specified, the value entered must be a power of 2 greater than or equal to the
FID size and between 4 and SIZEA inclusive, where SIZEA is the allocated size of each block in processing buffer 1.

The second parameter, "fctr1", specifies the correction factor to be applied to the first point of the FID.  The first
point is multiplied by 0.5\*fctr1 before Fourier transformation to correct the constant offset of the resulting
spectrum.  A value of 1.0 for "fctr1" should be appropriate for most applications.  If "fctr1" is omitted, a value of 1
will be used; RNMR does not prompt for "fctr1".  The legal values of "fctr1" are real numbers strictly greater than 0.0.

Before transformation, RNMR checks whether the frequency scale  should be reversed.  Since time domain data is presented
with minimum time on the left while frequency data is presented with maximum frequency on the left (by long standing NMR
convention), the default action of `FT` is to reverse the order of the data after transformation.  This is done by
conjugating the FID before the Fourier transform is calculated.  If the observe synthesizer has not been defined, the
FID is always conjugated.  Otherwise, the FID will be conjugated if the observe channel is generated from the lower
sideband (LSB) of the sum of the synthesizer and intermediate (IF)  frequencies.  After conjugation (if required), the
FID is zero filled to the  appropriate size if necessary.  Then the first point of the FID is scaled as specified by
"fctr1" and a fast Fourier transform is performed, replacing the FID with frequency domain data in processing buffer 1.
Use of `FT` resets the constant and linear phase values of the processing buffer (phi0 and phi1) to zero.  The frequency
data in each block of the processing buffer is scaled by a constant factor so that the complex magnitude of the largest
point in the first block is 1.0.  The largest point is the point whose intensity has the largest complex magnitude.  If
the largest magnitude in block 1 is 0.0, no rescaling of the data is performed.  After any rescaling is complete, the
buffer scale factor is multiplied by the new size and the rescaling factor:

    SFT = SFT*SIZE/VMAX

where VMAX is the maximum magnitude in block 1 if this magnitude is nonzero or 1.0 otherwise.

If the processing buffer is currently visible, `FT` always updates the display to show the transformed data.  If
processing buffer 1 is partitioned into two or more blocks, `FT` acts separately on each block.  Thus, multiple FID's
may be transformed to yield multiple spectra with a invocation of the `FT` command.  `FT` may only be used to transform
time domain data into the frequency domain.  To perform the reverse transformation, use `IFT`.

# G
---
## GA
Get archive record data

Category: Data Storage

Format: `GA` rec buf

Defaults: current 1

Description:
`GA` reads data from an archive record to a processing buffer.  The parameters and data of the buffer are replaced with
corresponding values read from the disk record.  Most RNMR commands require that data stored in an archive file be read
into a buffer before further processing may be performed.

The first parameter, "rec" is the number of the record to be  retrieved.  The allowable values for "rec" are integers
between 5 and 200, inclusive.  The scratch records (1-4) must be read with `GS` instead of `GA`.  Blocked records
(created by `ALLB`, `ALLCPY`, or `CPY` with a blocked source) must be read with `GB`.  RNMR checks that the specified
record is not empty and is not a blocked record.  If the user attempts to read a blocked record using `GA`, RNMR will
display the error message:

        (CHKTYP) RECORD WRONG TYPE

If "rec" is omitted, RNMR will prompt for a record number with the current read record (as displayed and set by `PTRA`)
as the default.  Unlike most other RNMR commands, pressing <RETURN\> at the REC prompt to accept the current read record
does cause RNMR to refresh the buffer.

The second parameter, "buf" specifies which processing buffer should receive the data and parameters from record
"rec". If "buf" is omitted, the archive record will be read into processing buffer 1.  RNMR does not prompt for "buf".
Legal values of "buf" are 1 and 2 since there are two processing buffers available.  Note that buffer 1 is the visible
processing buffer while buffer 2 is invisible.

In order to read record "rec" into buffer "buf", the allocated size of the buffer must be greater than or equal to the
size of the archive record.  To check and, if necessary, modify the allocated buffer size, use the command `DBSZ` "buf".

If the last record read into buffer `BUF` is different from REC, then the following buffer parameters are replaced with
the new values as described below:

Parameter | Description | Set Value
--------- | ----------- | ---------
TTLFLG    | Title flag  | FALSE to indicate that the buffer title should be verified
RECNO     | Record number | "rec"
NDIM      | Number of dims. | value in archive record
TITLE     | Buffer title | inherited from archive record
OWNER     | Record owner | "       "
DATE      | Date created | "       "
IDN       | Ident. Fields | "       "

`GA` always sets the buffer IDIMX parameter to 1; IDIMX specifies which dimension of a multidimensional source record is
currently stored in the buffer.  When a new record is read into a processing buffer by `GA`, RNMR checks the nucleus
assigned to each synthesizer in the disk archive.  For each synthesizer with an assigned nucleus, RNMR defines (or
redefines) the table entry for that nucleus with its reference frequency and PPM to Hz conversion factor as stored in
the disk archive.  For each synthesizer, the buffer frequency table is initialized with all values marked as undefined
(\*) and the buffer inherits the nucleus, offset, and phase sense (SR flag) assigned to  that synthesizer.  Other
hardware acquisition parameters (e.g. `PWR`, `GAIN`, `DW`, etc.) are inherited by the buffer without change so that the
user may list the parameters for a given archive record by entering `GA` then `LP`.  Note that the title entries for
each archive record store the values of only the first eight pulses, delays, and loops, so the values of P 9 through P
16, etc. will not be transferred to the buffer's parameter table and will not be printed out by `LP`.  Despite this, the
values of all 32 PP flags are stored on disk and are transferred by `GA`.

Whether record "rec" has already been read into buffer "buf" or not, RNMR sets the observe (direction 1) synthesizer
number of the buffer equal to the corresponding value for the record.  When a new record is read into the buffer, the
software acquisition parameters (e.g. `NAMD`, `NA`, `NWAIT`, etc.) are transferred from the source record to the buffer
parameter table.  `GA` always updates the buffer to reflect the archive record's first direction size, domain, time or
frequency scale, and dimension, and phase and scale factors.  After the data is read from the archive record to the
processing buffer, the active size of the buffer becomes the size of the record. `GA` updates the current read record
pointer (as displayed and set by `PTRA`) to "rec" and updates the display if processing buffer "buf" is currently
visible.
## GAIN
Set receiver gain

Category: Acquisition

Format: `GAIN` dB

Defaults: current

Prerequisites: RNMR only

Description:
`GAIN` sets the observe channel receiver relative gain.  This command sets the gain only if S-bus receiver gain control
has been implemented on the spectrometer running RNMR.  Whether gain control has been implemented or not, the gain value
is written to the archive title records and may be displayed by `LP` once the record has been read into a buffer.
`GAIN` takes one parameter, "db" which is the relative receiver gain in decibels.  If this parameter is omitted, RNMR
will prompt for the receiver gain with the current gain as the default.  The receiver gain is a real number between 0.0
and 100.0 dB, inclusive.  It is considered precise to 0.1 dB.  If the user accepts the current gain value by pressing
<RETURN\> at the `GAIN` prompt, no changes are made.  Since the receiver gain control is digital, only discrete gain
settings are allowed.  The currently supported gain values (in dB) are:
 	60, 50, 40, 30

CHECK THIS
When the user enters a new gain value, RNMR uses the largest allowed value less than or equal to the user's value
provided that the user's value is greater than or equal to 44.0 dB.  If the user enters a gain less than 44.0 dB, then
RNMR sets a receiver gain of 40.0 dB.  When RNMR sets a gain value different from that requested by the user, RNMR
displays an informational message showing the actual gain value set.
CHECK THIS
## GAINL
Set lock receiver gain

Category: Lock

Format: `GAINL` dB

Defaults: current

Prerequisites: `GAINL` requires implementation of RNMR lock control. (RNMR only.)

Description:
`GAINL` sets the lock channel receiver relative gain.  This command sets the gain only if RNMR lock channel control has
been implemented on the spectrometer running RNMR.  Unlike `GAIN`, the current value of `GAINL` is not stored in the
title records and is not available from `LP`.

`GAINL` takes one parameter, "db" which is the relative lock  receiver gain in decibels.  If this parameter is omitted,
RNMR will prompt for the receiver gain with the current gain as the default.  The receiver gain is a real number between
0.0 and 100.0 dB, inclusive.  It is considered precise to 1.0 dB. If the user accepts the current gain value by pressing
<RETURN\> at the `GAIN` prompt, no changes are made.  Since the receiver gain control is digital, only discrete gain
settings are allowed.  The currently supported gain values (in dB) are:

Fix this gain is wrong
           100.0  94.0  88.0  82.0
            76.0  70.0  64.0  58.0

When the user enters a new gain value, RNMR uses the largest allowed value less than or equal to the user's value
provided that the user's value is greater than or equal to 64.0 dB.  If the user enters a gain less than 64.0 dB, then
RNMR sets a receiver gain of 58.0 dB.  When RNMR sets a gain value different from that requested by the user, RNMR
displays an informational message showing the actual gain value set.
## GAV
Get data from averager

Category: Acquisition

Format: `GAV` iblk ipro nblk

Defaults: 1 1 1

Prerequisites: pulse program must currently be loaded and acquisition must be stopped. (RNMR only.)

Description:
`GAV` transfers data and parameters from the averager to a processing buffer.  `GAV` must be used in order to process
data acquired by the spectrometer hardware.  The averager memory may be logically partitioned into two or more blocks so
that multiple FID's with different experimental parameters can be acquired at once, without the need to start and stop
acquisition many times.  Once acquisition is stopped, `GAV` transfers one or more of these blocks to the processing
buffer according to the user's choice of "iblk" and "nblk".  Since the total capacity of the averager memory is 64K
complex points while that of the processing buffer is only 8K; RNMR allows each to independently partitioned, permitting
transfer of the averager memory to a processing buffer in 8K or smaller segments through multiple calls to `GAV`.  The
number of averager blocks is displayed and set by the RNMR command `NABLK`, while the number of buffer segments is set
by `DBSZA` (for the acquisition buffer) and `DBSZ` (for the processing buffers).

`GAV` initially transfers averager data and the first 16 pulse programmer parameters (pulse, delay, loop, and flag
values) from the averager hardware to RNMR's averager data buffer.  Next, certain averager buffer parameters are
initialized, as described below.  Finally, the data and all parameters from the acquisition buffer are copied to the
specified processing buffer.  Because `GAV` transfers all the acquisition buffer parameters to a processing buffer after
spectrometer data has been acquired, setting an acquisition parameter before collecting data ensures that it will be
inherited by the processing buffer upon completion of the experiment.  For example, one may ensure that data to be
collected will be saved to disk with a given title by using `TITLEA` to set the acquisition buffer title before starting
an experiment.  Once this is done, `GAV` will transfer this title to the processing buffer, so no `TITLE` command need
be issued before saving the experiment to disk.  This is equivalent to entering the title using the `TITLE` command
after `GAV` and before saving to disk.  Acquisition buffer commands which may be used to set up an experiment in this
way include `IDNA`, `OFFA`, `REFA`, and `TITLEA`.

The first parameter, "iblk" specifies the first averager block to be transferred to a processing buffer, while "nblk"
specifies the number of blocks to be transferred.  If "iblk" is omitted from the command line, the transfer of averager
blocks to the processing buffer will start with the first averager block. RNMR does not prompt for "iblk".  Legal values
for "iblk" are integers greater than or equal to one.

The second parameter, "ipro" specifies which processing buffer is to receive the averager parameters and data. If this
parameter is omitted, the averager will be transferred to processing buffer 1 (the visible processing buffer).  RNMR
will not prompt for "ipro".  Since there are two processing buffers, the legal values for "ipro" are 1 and 2.  If "nblk"
is omitted from the command line, only averager block "iblk" will be transferred to the processing buffer. RNMR does not
prompt for "nblk".  Acceptable values for "nblk" are integers from 1 to the number of blocks in the acquisition buffer,
inclusive.  The latter number is displayed and set by the command `DBSZA`.

Before transferring data, RNMR checks that the size of each averager block (as displayed and set by `DBSZA`) does not
exceed the size of each block in the averager data buffer (as displayed and set by `SIZE`).  If "iblk" and "nblk" are
chosen so that the averager blocks requested exceed the number of blocks declared by `NABLK`, RNMR will abort the
transfer and display an error message:

    (XAVDB ) BLOCK OUT OF BOUNDS

For example, if the averager is partitioned into 4 blocks (`NABLK 4`), the command:

    GAV 2 1 4

will give an error since the transfer begins at block 2 and there is no averager block 5.  Note that even in this
situation RNMR transfers as many averager memory blocks to the acquisition buffer as possible, updating the acquisition
buffer parameters.  However, data and parameters will not be transferred from the acquisition to the processing buffer
if this error is detected.

Each time `GAV` is used, the destination buffer parameters are initialized with constant and linear phase factors (phi0
and phi1) equal to 0.0 and with buffer scale factor 1.0.  In addition, the following parameters are initialized for the
first direction:

Parameter | Description | Set Value
--------- | ----------- | ---------
DIM       | 1st direction dimension | 1 (i.e. DIR 1 = 1)
DOMAIN    | 1st direction domain | TIME
SIZE      | 1st direction size | Averager size per block
FIRST     | 1st direction min. time | 0.0
STEP      | 1st direction step size | `DW` (msec)

The initialization of these parameters is done only once per invocation of `GAV`, regardless of how many averager blocks
are transferred.

When `GAV` transfers the averager data to the destination buffer, the data are scaled by 1/(IA\*ADCMAX) where IA is the
number of signal averaged shots actually taken and ADCMAX is the largest intensity that the spectrometer's analog to
digital converter (ADC) can represent.  If a given ADC yields N-bit signed integer data, then ADCMAX = 2.0\*\*(N-1).  If
no signal averaged shots were taken, the data are scaled by 1/ADCMAX instead.  The table below lists current values of
ADCMAX for each spectrometer:

Spectrometer | ADC bits | ADCMAX
------------ | -------- | ------
A | 12 | 2048
B | 12 | 2048
C | 16 | 32768
D | 12 | 2048
E | 16 | 32768
F | 8  | 128
G | 16 | 32768

Once the data has been scaled, it is converted from complex integer to complex floating point representation.  After
`GAV` has successfully transferred all the specified averager blocks, the active number of blocks in the processing
buffer becomes the number of blocks transferred by `GAV`.  Each time `GAV` is used, the TTLFLG parameter of the
destination buffer is set to FALSE.  This flag is TRUE is the buffer has a confirmed title; if FALSE, RNMR will prompt
the user for a title before the buffer is plotted with `PLOT` or `STK` or listed with `LP`, `LPK`, or `LPA`.  If the
processing buffer "ipro" is currently visible, `GAV` updates the display to show the data transferred from the averager.
## GB
Get blocked record data

Category: Data Storage

Format: `GB` rec blk buf nblk

Defaults: current next 1 1

Description:
`GB` reads data from a blocked record to a processing buffer.  The parameters and data of the buffer are replaced with
corresponding values read from the disk record.  Most RNMR commands require that data stored in a blocked record be read
into a buffer before further processing may be performed.  Since processing buffers are onedimensional, the user must
specify which one-dimensional slice(s) of the blocked record is to be read into the buffer.  In RNMR, this specification
is accomplished with one parameter, the block number.  As the block number is incremented from 1, 1D slices along the
first direction are selected for increasing depth in the second direction and minimum height in directions 3 and 4.
Next, 1D slices are read from the next lowest plane in direction 3 with minimum height in direction 4.  When all slices
have been read for minimum height in direction 4, retrieval continues with the next lowest cube.  In this way, every
slice along direction 1 is read out with depth in direction 2 varying fastest and height in direction 4 varying most
slowly.  Thus, if the block number is incremented to a adequately large number, all data points in the record will have
been selected.  Note that the assignment of data points to block numbers is dependent on the direction-to-dimension
mapping set and displayed for each number of dimensions by `DIRB`.  As a result, neither the number of blocks in a
record nor the mapping of data points to block numbers is constant.

The first parameter, "rec" is the number of the record to be  retrieved.  The allowable values for "rec" are integers
between 5 and 200, inclusive.  The scratch records (1-4) must be read with `GS` instead of `GB`.  Archive records
(created by `SA` or `CPY` with an archive record source) must be read with `GA`.  RNMR checks that the specified record
is not empty and is a blocked record.  If the user attempts to read a nonblocked record using `GB`, RNMR will display
the error message:

    (CHKTYP) RECORD WRONG TYPE

If "rec" is omitted, RNMR will prompt for a record number with the current read record (as displayed and set by `PTRA`)
as the default.

The second parameter, "blk" is used to select the first block of  record "rec" to be transferred.  If this parameter is
omitted, RNMR will not prompt for a block number.  Instead, "blk" will default to zero.  When "blk" is set to zero,
either explicitly or by default, the first record block transferred will be determined by the current `PTRB` setting.
The `PTRB` command displays and sets a pointer which marks the current read and write blocks of a given blocked record.
When "blk" is 0, RNMR begins the transfer with the first block after the current read block (`PTRB`+1).  Legal values
for "blk" are integers greater than or equal to zero.

The third parameter, "buf" specifies which processing buffer should receive the data and parameters from record "rec".
If "buf" is omitted, the specified blocks of the source record will be read into  processing buffer 1.  RNMR does not
prompt for "buf".  Legal values of "buf" are 1 and 2 since there are two processing buffers available.  Note that buffer
1 is the visible processing buffer while buffer 2 is invisible.

The final parameter, "nblk" specifies the number of blocks to read from record "rec" into buffer "buf".  Since the
processing buffer may be partitioned into two or more segments using the command `DBSZ`, one may read more than one
block from "rec" into "buf" with a single invocation of `GB`.  This feature is particularly useful when performing
operations uniformly on a multidimensional data set.  For example, one may perform a 1K Fourier transform on a blocked
record eight blocks at a time by partitioning the processing buffer into eight segments (e.g. `DBSZ` 1 1024 8) and
reading in data eight blocks at a time (e.g. `GB` 29 0 1 8) for transformation.  In this manner, the number of commands
to be executed by the processing macro is reduced by a factor of eight, greatly decreasing the required computation
time.  If "nblk" is omitted, `GB` will transfer only one block, "blk", from "rec" to "buf". RNMR does not prompt for the
"nblk" parameter.  Legal values of "nblk" are integers greater than or equal to one.  Before each block is transferred
from "rec" to "buf", RNMR checks that the requested block number is not greater than the number of blocks in the
specified record.  Failure to satisfy this condition results in the error message:

    (CVTBBX) BLOCK OUT OF BOUNDS

The number of points actually used in direction 1 of record "rec" must be at least 1 to use `GB`.  Thus, an attempt to
read from an allocated but unused record gives the error message:

    (RARCX ) DIMENSION EMPTY

In addition, RNMR checks that each block requested corresponds to data points which were actually used in record "rec",
i.e. that the requested block was not only allocated by actually recorded.  If this is not the case, then RNMR displays
the error message:

    (RARCX ) BLOCK OUT OF BOUNDS

Since blocks are transferred one at a time, RNMR reads in as many blocks as possible from those requested by the user.
If at any point one of the three error conditions described above occurs, the transfer stops.  In this case, all the
blocks that transferred successfully may be processed as usual, but the screen display is not updated.  Thus, if the
number of blocks in record "rec" is not known, one may use `GB` to get successive blocks until a BLOCK OUT OF BOUNDS
error is encountered.

In order to read one-dimensional slices from a blocked record, RNMR requires that the record has NDIMX sufficiently
large that direction 1 is accessible.  NDIMX is the number of dimensions that may be simultaneously accessed in a
blocked record and is a permanent attribute of the record set at allocation time.  Regardless of NDIMX, it is always
possible to access a block of data along the first dimension of any given record, but accessing one-dimensional slices
along the higher dimensions requires higher values of NDIMX.  In conclusion, in order to read slices along dimension N,
one must have allocated the source record with NDIMX at least N.  When NDIMX is too small to allow the requested
retrieval, RNMR displays the error message:

    (RARCX ) DIMENSION INACCESSIBLE

If this error occurs, the user should make sure that direction 1 is assigned the desired dimension by using the `DIRB`
command.  If the current `DIRB` setting is correct, then it will be necessary to allocate a copy of the source record
with higher NDIMX using `ALLCPY` and to then copy the data from the source record to the new record using `GB` with an
allowed `DIRB` setting.

The number of points actually used in direction 1 must not exceed the allocated size of each partition in processing
buffer "buf". This restriction is enforced because RNMR will attempt to transfer each requested block of the record
"rec" to a block of the processing buffer.  When there are too many points in each block to perform the transfer, RNMR
gives an error message:

    (CKTBPB) SIZE TOO LARGE

 To check and set the allocated size of the processing buffer, use the command `DBSZ` "buf".

If the last record read into buffer "buf" is different from "rec", then the following buffer parameters are replaced
with the new values as described below:

Parameter | Description | Set Value
--------- | ----------- | ---------
TTLFLG    | Title flag  | FALSE to indicate that the buffer title should be verified
RECNO     | Record number | "rec"
NDIM      | Number of dims. | value in archive record
TITLE     | Buffer title | inherited from archive record
OWNER     | Record owner | "       "
DATE      | Date created | "       "
IDN       | Ident. Fields | "       "

`GB` always sets the buffer IDIMX parameter to the direction 1 dimension; IDIMX specifies which dimension of a
multidimensional source record is currently stored in the buffer. Thus, `GB` marks the buffer as containing data from
direction 1 of "rec".

When a new record is read into a processing buffer by `GB`, RNMR checks the nucleus assigned to each synthesizer in the
disk archive.  For each synthesizer with an assigned nucleus, RNMR defines (or redefines) the table entry for that
nucleus with its reference frequency and PPM to Hz conversion factor as stored in the disk archive.  Note that if the
archive contains one or more nucleus entries which are already in the current RNMR nucleus table or if the nucleus table
is full, RNMR will redefine `NUC UNKN` with the nucleus parameters stored with the disk archive.  For each synthesizer,
the buffer frequency table is initialized with all values marked as undefined (\*) and the buffer inherits the nucleus,
offset, and phase sense (SR flag) assigned to that synthesizer. Other hardware acquisition parameters (e.g. `PWR`,
`GAIN`, `DW`, etc.) are inherited by the buffer without change so that the user may list the parameters for a given
blocked record by entering `GB` then `LP`.  Note that the title entries for each record store the values of only the
first eight pulses, delays, and loops, so the values of P 9 through P 16, etc. will not be transferred to the buffer's
parameter table and will not be printed out by `LP`.  However, the values of all 32 PP flags are stored on disk and are
transferred by `GB`.
The parameters stored with a given blocked record are set when the first block is stored using `SB` and are not updated
or augmented as additional blocks are written to disk.  Thus, when `LP` lists the parameters of a blocked record, the
parameters reported may not be correct for blocks other than the first stored block.

Whether record "rec" has already been read into buffer "buf" or not, RNMR sets the observe (direction 1) synthesizer
number of the buffer equal to the corresponding value for the record.  When a new record is read into the buffer, the
software acquisition parameters (e.g. `NAMD`, `NA`, `NWAIT`, etc.) are transferred from the source record to the buffer
parameter table.  `GB` always updates the buffer to reflect the archive record's first direction size, domain, time or
frequency scale, and dimension, and phase and scale factors.  After the data is read from the archive record to the
processing buffer, the active size of the buffer becomes the size of the record.  As each block is successfully
transferred from record REC to buffer `BUF`, RNMR sets the block read pointer to the number of the block just read. This
pointer indicates the "current" block of a given record and may be set as desired manually with the command `PTRB`.
Upon successful completion, `GB` updates the current read record pointer (as displayed and set by `PTRA`) to "rec" and
updates the display if processing buffer "buf" is currently visible.
## GBLARG
Set value of global argument

Category: Arguments

Format: `GBLARG` nam val prompt

Defaults: TEMP current VALUE

Description:
`GBLARG` defines (or redefines) a global argument.  Global arguments are variables available to all RNMR command levels,
including the console ("\>") level.  At any time there may be at most 64 defined global arguments.  Both the name and
the value of each argument are 8-byte character strings.

The first parameter, "nam", is the name of the global argument to be defined or redefined.  The name of a global
argument may not be blank and must use only the characters A-Z, 0-9, $, or \_.  If no argument name is specified, RNMR
will prompt for the name of the global argument with "TEMP" as the default.

The third parameter, "prompt", specifies a string to be used if  RNMR prompts for the global argument value "val". This
string may consist of up to 8 characters excluding blanks and commas.  If "prompt" is omitted, RNMR will use the prompt
"VALUE  ="; RNMR does not ask for a prompt string if one was not specified on the `GBLARG` command line.  If a prompt is
specified, it will be inserted into an eight character string in which the last two characters are always " =".  Thus,
if "prompt" is "ABC", RNMR will use the prompt "ABC    =" when asking for the global argument value.  If "val" is
specified on the `GBLARG` command line, "prompt" will be ignored.

The second parameter, "val" is the value to which RNMR will set the specified global argument.  If "val" is nonblank,
RNMR will define or redefine the global argument without prompting the user.  If "val" is blank, RNMR will prompt the
user for a value.  The prompt string requested by the "prompt" parameter (if any) will be used.  The default for this
prompt will be the current value of the global argument if the argument is already defined, or "        " if the global
argument "nam" does not yet exist.  Thus, to make `GBLARG` prompt the user for the global argument value, one may use a
`GBLARG` command  of the form:

    GBLARG XYZ,,XYZ_VAL

This command will cause RNMR to prompt the user for the value of global argument XYZ. If the user presses <RETURN\> at
this prompt, global argument XYZ will not be defined or redefined and the `GBLARG` command will have changed nothing.
If a global argument with name "nam" does not exist prior to the execution of the `GBLARG` command, RNMR will create a
new global argument with the specified non-blank value. Otherwise, the value of the existing global argument "nam" will
be updated.
## GBLDL
Delete global argument

Category: Arguments

Format: `GBLDL` nam

Defaults: TEMP

Description:
`GBLDL` deletes the specified global argument from the global argument table.  Once a global argument has been deleted,
attempts to retrieve its value via the "%" operator will yield an error message, while `GBLARG` will create a new global
argument with the same name.

`GBLDL` takes one parameter, "nam", which is the name of the argument to be deleted.  If no name is specified,
RNMR will prompt for a global argument name with "TEMP" as the default.  Pressing <RETURN\> at this prompt results in
deleting the global argument TEMP if it exists.  If the specified global argument exists, it will be deleted. Otherwise,
`GBLDL` will simply do nothing and no error message will be displayed.
## GENCS
Generate complex sine wave

Category: Data Manipulation

Format: `GENCS` freq. phase `SW`

Defaults: 1.0 0.0 current

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`GENCS` generates a complex sine wave of specified frequency and phase.  This sine wave has unit amplitude and replaces
any data currently in the visible processing buffer (buffer 1).  Using `GENCS` to create a complex sine and applying
`SC`, `EM`, and `GM` to scale and broaden the data, one may produce a simulated FID with any desired frequency, phase,
amplitude, and Gaussian and Lorentzian line widths.  These simulated FID's may be added together to give a waveform
corresponding to a multiline spectrum.  Such a simulation is generated by the system macro CONV, which reads
frequencies, amplitudes, and line widths from a text file and uses `GENCS` and other commands to calculate the FID.

The first parameter of `GENCS` is "freq", which specifies the frequency of the complex sine wave to be generated.
This frequency should be expressed in the current frequency unit, as set and displayed by the command `UNIT /FREQ`.
Currently, the available units are Hz, kHz, MHz, and PPM.  If "freq." is omitted, RNMR will prompt for a frequency with
a default of 1 in the current frequency units with the current number of decimal places (as displayed and set by
`NDEC`).

The second parameter, "phase", specifies the phase of the complex sine wave in degrees.  If this parameter is omitted,
RNMR will generate a complex sine with zero phase; RNMR does not prompt for "phase".  The value of "phase" may be any
real number.

The third parameter is the sweep width for the complex sine wave.  This sweep width determines the time per point for
the data to be generated and is expressed in the current frequency units.  If "`SW`" is omitted, RNMR will generate a
complex sine wave with the current buffer sweep width.  Legal values for "`SW`" are real numbers strictly greater than
zero.  If a valid value of "`SW`" is entered, RNMR resets the sweep width of the visible processing buffer to "`SW`".

When `GENCS` is executed, the first point of the buffer is always identified with zero time, regardless of its original
time value.  Each partition of the visible processing buffer receives an identical complex sine wave whose points are
given by:

    I(k) = EXP(i(phase + (k-1)dphi))  k= 1,...,SIZE

where "dphi" is 360\*freq/sw.  If the frequency scale of the buffer is reversed, "phase" and "dphi" will be negated
before computing the complex sine.  This will occur when the buffer synthesizer is 0 or when the spectrum reverse flag
(`SRFLG`) for the buffer synthesizer is false.

After the complex sine has been generated, RNMR initializes the following parameters for processing buffer 1:

Parameter | Description | Set Value
--------- | ----------- | ---------
TTLFLG    | Title flag  | FALSE to indicate that the buffer title should be verified
RECNO     | Record number for `GA`,`GS`,`GB` | 0
BLKNO     | Block number for `GB` | All 0
TITLE     | Buffer title | Null
OWNER     | Owner for `SA`,`SB`,`SS`  | Current `USER`
DATE      | Date for `SA`,`SB`,`SS` | Current date
IDN       | Identification fields | All null
PHI0      | Constant phase factor | 0.0
PHI1      | Linear phase factor | 0.0
SFT       | Buffer scale factor | 1.0

If the processing buffer is currently visible, `GENCS` always updates the display upon completion.
## GM
Gaussian multiply FID

Category: Data Manipulation

Format: `GM` lb

Defaults: current

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`GM` performs a Gaussian multiplication apodization.  In this  apodization, the FID is multiplied by a decaying real
Gaussian function.  This results in a broadening of spectral lines after Fourier transformation which masks noise at the
expense of resolution.  When Gaussian multiplication is applied to a perfect, non-decaying complex sine wave and a
Fourier transform is performed, the result will be a perfect Gaussian line shape.  While the user need not be currently
viewing the processing buffer in order to use `GM`, `GM` operates only on processing buffer 1.

`GM` takes one argument, "lb" which is the line broadening factor expressed in the current default frequency units (Hz,
kHz, or MHz), as set and displayed by `UNIT /FREQ` or by `UNIT /FREQ /DFLT` if `UNIT /FREQ` is PPM.  The legal values
of "lb" are real numbers between -1000 Hz and 1000 Hz, inclusive.  If "lb" is omitted, RNMR will not prompt for a value
but rather will perform the apodization with the current line broadening factor, as set and displayed by the command
`LB`.  If a legal value of "lb" is specified, the current line broadening factor will be updated before Gaussian
multiplication of the data.  `GM` multiplies each block of processing buffer 1 by the real function:

    F(I) = EXP-(0.5*PI*(I-1)* LB/SW)^2)

where I is the index of the data point (I=1,2,...), `LB` is the line broadening factor, and `SW` is buffer sweep width.
If the processing buffer is currently visible, `GM` always updates the display.
## GMV
Calculate geometric mean

Category: Data Manipulation

Format: `GMV` src dst

Defaults: 2 1

Description:
`GMV` computes the geometric mean of a complex source buffer "src" and a complex destination buffer DST and places the
result in the destination buffer:

    DST = SIGN(DST) * SQRT(ABS(DST*SRC))

The geometric means of the real and imaginary parts of the data are computed separately.  The arguments "src" and "dst"
specify the numbers of the buffers to be processed.  Each buffer number may be either 1 or 2; buffer 1 is the visible
processing buffer.  If either argument is omitted, RNMR will prompt for a buffer number.  The default source is buffer 2
while the default destination is buffer 1.  While `GMV` operates only on processing buffers, the user need not be
viewing the processing buffers to perform the computation.  For two buffers to be processed with `GMV`, they must have
the same domain (time or frequency) and the same active size (though not necessarily the same allocated size).  If the
destination buffer is partitioned into two or more blocks, each block is separately multiplied with the corresponding
block of the source buffer.  The number of blocks in the source buffer need not be the same as that in the destination
buffer.  RNMR uses the formula below to match source blocks with destination blocks:

    IBLK_SRC = MOD(IBLK_DST-1,NBLK_SRC) + 1, IBLK_DST=1,...,NBLK_DST

If the processing buffer is currently visible and "dst" is 1, `GMV` always updates the display upon completion.
## GO
Start or resume acquisition

Category: Acquisition

Format: `GO` NA

Defaults: current

Prerequisites: (LOAD) by `EX`; the acquisition must be stopped; RNMR only.

Description:
`GO` instructs RNMR to continue acquisition after acquisition has been stopped by `QUIT`.  Continuing shots will be
added to the current averager memory and the shot counter will be incremented upward from its current value.

`GO` takes one parameter, "na", which is the total number of shots to be taken.  Shots already taken before `GO` count
towards this limit.  If "`NA`" is omitted, the current shot limit as set and displayed by `NA` will determine how many
additional shots will be taken; RNMR does not prompt for "na".  Legal values for "`NA`" are -1 and integers greater than
or equal to 1. If "na" is -1, RNMR will continue acquisition with no limit to the number of shots taken; acquisition
will continue until stopped by `QUIT` or `WAIT`.  Before resuming acquisition, RNMR checks that the number of shots
already taken is less than the requested shot limit specified by the `NA` command or the "`NA`" parameter of `GO`.
Unless `NA` or "na" is -1, acquisition will not be started if this condition is not satisfied.  If "`NA`" is specified
and is greater than the current number of shots completed, RNMR will replace the current shot limit with "na".  When
acquisition is continued with `GO`, no delay shots are taken even if `NDLY` is greater than zero.  To continue
acquisition with one or more delay shots, use the command `NG`.  Unless no shots have been taken yet, `GO` will continue
acquisition until `NA` shots have been completed, regardless of whether `GO` is executed from console ("\>") level or
from a macro; this is unlike the behavior of `DG`.

If `GO` is used to start acquisition before any shots have been completed, data will be acquired until `NA` averaged
shots are complete if `GO` is executed from console level.  If `GO` is called from a macro in this situation,
acquisition will continue until `NWAIT` or `NA` shots have been taken, whichever is smaller.  If `NWAIT` is 0, then `NA`
will determine the number of shots taken from a macro, and similarly, `NWAIT` shots will be taken if `NA` is -1 and
`NWAIT` is nonzero.  In summary, if no shots have been taken, `GO` acts like `ZG` except that neither the averager nor
the acquisition title parameters nor the display is initialized by `GO`.  `GO` resets the following averager parameters
to their current settings in RNMR:

Parameter | Description
--------- | -----------
`NABLK`   | Number of averager blocks (logical avg. memory partitions)
`NAMD`    | Length of phase cycle
`NDLY`    | Number of dummy shots to take on `DG` or `NG`
`NDSP`    | Number of shots to take for each display update

Before acquisition is resumed, `GO` also resets the frequency table pointer for each synthesizer so that frequencies
will be generated starting with the first table entry.  Once acquisition is restarted, each shot will increment the shot
 indicator in the upper right hand corner of the display.  If the acquisition block is visible, the current sum of FID's
will be updated on the screen every two seconds or once per shot, whichever is slower.
## GOTO
Go to statement label in macro

Category: Macro

Format: `GOTO` label

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`GOTO` performs an unconditional jump within a macro.

The parameter "label" is the name of the macro label to which execution should jump.  If "label" is not specified,
execution will continue at the next line of the current macro.  Remember to specify "label" as a character string of the
form ".XXXXXXX" where "." is required syntax and X may be any ASCII character.

When a jump to "label" is requested, RNMR first searches ahead from the current macro line to the end of the macro for
the specified statement label.  If that label is not found, the search begins again at the first line of the macro.

The parameter "label" may contain a positive line offset, as in the command:

    GOTO .XYZ+1

In this example, macro execution jumps to the first line after the label ".XYZ".  Note that line offsets may not be so
large as to go beyond the end of the macro; the search for lines offset from .XYZ does not wrap around to the beginning
of the macro.  Also note that the label name and line offset together must be no more than eight characters in length.
## GOTST
Perform a conditional jump within a macro based on a test

Category: Macro

Format: `GOTST` [qual] name args... label1 label2

Qualifiers: /TRUE /FALSE

Qualifier defaults: /TRUE

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`GOTST` jumps to a label within a macro based upon the results of a conditional test. The available qualifiers and
arguments for `GOTST` tests are the same as those detailed in the description of `TST`. While `TST` executes different
blocks of commands based upon the test result, `GOTST` jumps to macro labels. Tests which would cause `TST` to execute
the commands between `TST` and `ELSTST` cause `GOTST` to jump to label1. Tests which would cause `TST` to execute the
commands between `ELSTST` and `ENDTST` cause `GOTST` to jump to label2.

`GOTST` is the most direct replacement for the behavior of the old if commands such as `IFEQ`. `GOTST` should only be
used when there is a need to jump to labels in different parts of a macro. `TST` should be used for conditional
execution of blocks of commands.
## GS
Get data from scratch record

Category: Data Storage

Format: `GS` rec buf

Defaults: 1 1

Description:
`GS` reads data from a scratch record to a processing buffer.  The scratch records are records 1 through 4 and may be
deleted but may not be allocated with `ALLB` or `ALLCPY`.  Unlike archive records (numbers 5 to 200), scratch records
may be freely overwritten; new data and parameters may be written to a scratch record without deleting it first, even if
the record is not owned by the current user.  `GS` replaces the parameters and data of the buffer with corresponding
values read from the disk record.  Most RNMR commands require that data stored in a disk file be read into a buffer
before further processing may be performed.

The first parameter, "rec" is the number of the record to be  retrieved.  The allowable values for "rec" are integers
between 1 and 4, inclusive.  The archive records (5-200) must be read with `GA` or `GB` instead of `GS`. RNMR checks
that the specified record is not empty and is a scratch record.  If the user attempts to read an archive record using
`GS`, RNMR will display the error message:

    (CHKTYP) RECORD WRONG TYPE

If "rec" is omitted, RNMR will read data from scratch record 1; RNMR does not prompt for "rec".

The second parameter, "buf" specifies which processing buffer should receive the data and parameters from record
"rec".  If "buf" is omitted, the scratch record will be read into processing buffer 1.  RNMR does not prompt for "buf".
Legal values of "buf" are 1 and 2 since there are two processing buffers available.  Note that buffer 1 is the visible
processing buffer while buffer 2 is invisible.  In order to read record "rec" into buffer "buf", the allocated size of
the buffer must be greater than or equal to the size of the scratch record.  To check and, if necessary, modify the
allocated buffer size, use the command `DBSZ` "buf".  If the last record read into buffer "buf" is different from "rec",
then the following buffer parameters are replaced with new values as described below:

Parameter | Description | Set Value
--------- | ----------- | ---------
TTLFLG    | Title flag  | FALSE to indicate that the buffer title should be verified
RECNO     | Record number | "rec"
NDIM      | Number of dims. | value in scratch record
TITLE     | Buffer title | inherited from scratch record
OWNER     | Record owner | "       "
DATE      | Date created | "       "
IDN       | Ident. Fields | "       "

`GS` always sets the buffer IDIMX parameter to 1; IDIMX specifies which dimension of a multidimensional source record is
currently stored in the buffer.  When a new record is read into a processing buffer by `GS`, RNMR checks the nucleus
assigned to each synthesizer in the disk record.  For each synthesizer with an assigned nucleus, RNMR defines (or
redefines) the table entry for that nucleus with its reference frequency and PPM to Hz conversion factor as stored in
the disk record.  Note that if the record contains one or more nucleus entries which are already in the current RNMR
nucleus table or if the nucleus table is full, RNMR will redefine `NUC UNKN` with the nucleus parameters stored with the
disk archive.  For each synthesizer, the buffer frequency table is initialized with all values marked as undefined (\*)
and the buffer inherits the nucleus, offset, and phase sense (SR flag) assigned to that synthesizer.  Other hardware
acquisition parameters (e.g. `PWR`, `GAIN`, `DW`, etc.) are inherited by the buffer without change so that the user may
list the parameters for a given scratch record by entering `GS` then `LP`.  Note that the title entries for each scratch
record store the values of only the first eight pulses, delays, and loops, so the values of P 9  through P 16, etc. will
not be transferred to the buffer's parameter table and will not be printed out by `LP`.  Despite this, the values of all
32 PP flags are stored on disk and are transferred by `GS`.

Whether record "rec" has already been read into buffer "buf" or not, RNMR sets the observe (direction 1) synthesizer
number of the buffer equal to the corresponding value for the record.  When a new record is read into the buffer, the
software acquisition parameters (e.g. `NAMD`, `NA`, `NWAIT`, etc.) are transferred from the source record to the buffer
parameter table.  `GS` always updates the buffer to reflect the scratch record's first direction size, domain, time or
frequency scale, and dimension, and phase and scale factors.  After the data is read from the scratch record to the
processing buffer, the active size of the buffer becomes the size of the record. `GS` updates the display if processing
buffer "buf" is currently visible.  Unlike `GA`, `GS` does not update the record read pointer, which is set and
displayed by the command `PTRA`.
## GSA
Get averager scratch record data

Category: Acquisition

Format: `GSA` rec buf

Defaults: 1 1

Prerequisites: RNMR only

Description:
`GSA` reads data from an averager scratch record to a processing buffer.  The averager scratch records are stored in the
files TITLEA.DAT and DATAA.DAT in the directory [`USER`] for each spectrometer.  `GSA` replaces the parameters and
data of the buffer with corresponding values read from the disk record.  Most RNMR commands require that data stored in
a disk file be read into a buffer before further processing may be performed.

The first parameter, "rec" is the number of the averager scratch record to be retrieved.  The allowable values for "rec"
are integers between 1 and the number of averager scratch records, which is a dynamic quantity.  If "rec" is omitted,
RNMR will read data from averager scratch record 1; RNMR does not prompt for "rec".

The second parameter, "buf" specifies which processing buffer should receive the data and parameters from record
"rec". If "buf" is omitted, the scratch record will be read into processing buffer 1.  RNMR does not prompt for "buf".
Legal values of "buf" are 1 and 2 since there are two processing buffers available.  Note that buffer 1 is the visible
processing buffer while buffer 2 is invisible.  In addition to transferring data from DATAA.DAT to the processing
buffer, `GSA` initializes the following buffer parameters:

Parameter | Description | Set Value
--------- | ----------- | ---------
TTLFLG    | Title flag  | FALSE to indicate that the buffer title should be verified
RECNO     | Record number | 0
BLKNO     | block number | All 0

When `GSA` completes successfully, the display is updated if "buf" is 1.

# H
---
## HELP
Get online help

Format: `HELP` lib key1 ... key9

Defaults: none none ... none

Description:
`HELP` obtains information from the RNMR on-line help library. Information is currently available on both RNMR commands
(`HELP RNMR`) and writing pulse programs (`HELP PPROG`).

The first parameter, "lib", specifies which RNMR help module is to be accessed.  Currently, the two modules available
are RNMR (for help on data acquisition and processing) and PPROG (for help on pulse programming).  If "lib" is omitted,
the system will ask for a help module once the help window is displayed.  There is no default value for "lib".  The
parameters "key1" through "key9" provide keywords to specify the desired help library topic.  Each successive keyword
selects a topic from a lower level of the `HELP` tree.  RNMR processes all keywords from left to right up to the first
blank keyword; keywords after a blank value are ignored.  The entire `HELP` specification, including "lib" and all
nonblank keywords must be no more than 80 characters long, including a single space between each token.  The `HELP`
keywords are optional and have no default values.

When the `HELP` command is executed, RNMR pushes its graphics window into the background so the text terminal window is
visible.  While the user views the contents of the RNMR help library, CTRL-Y interrupts are disabled.  This ensures that
any acquisition or processing running in the background will not be accidentally stopped.  After parsing by RNMR, the
`HELP` command is run in a spawned subprocess by VAX/VMS; RNMR continues to execute any scheduled activities in the main
process.  Once the `HELP` session is complete, RNMR resets the CTRL-Y state to its original value; i.e. if CTRL-Y
interrupts were allowed before `HELP`, they will be re-enabled.  The RNMR graphics window is then popped to the
foreground, hiding the text window.

The RNMR command help library is structured so that one may obtain help on a command XYZ by entering `HELP RNMR XYZ`.
Retrieving other information about RNMR or PPROG requires navigating through the `HELP` tree interactively or specifying
additional keywords "key2" through "key9".  For assistance in navigating through a VMS `HELP` library, enter (at the
`DCL` prompt "$") `HELP HELP`.
## HILB
Perform Hilbert transform on spectrum

Category: Data Manipulation

Format: `HILB`

Prerequisites: Frequency domain data in processing buffer 1 (FREQ)

Description:
`HILB` performs a Hilbert transform on a spectrum.  As a consequence of Fourier transformation, the real and imaginary
parts of a complex spectrum are Hilbert transform pairs.  Thus, it should be possible to discard the imaginary channel
and then recreate it by performing a Hilbert transform on the real part of the data.  Typically, this is done after a
spectrum has received linear phase correction, cubic spline baseline correction, or any other manipulation that results
in the real and imaginary channels no longer being Hilbert transform pairs.  Without correction by `HILB`, the inverse
Fourier transform of this data would be incorrect, as evidenced by divergence of the data at long times.  `HILB`
replaces the imaginary part of the buffer data with the Hilbert transform of the real part, and leaves the real part of
the buffer unchanged.
Before performing the transform, RNMR checks the active size of the visible processing buffer (buffer 1).  If this size
is not a power of 2, the buffer size is adjusted to the smallest power of 2 greater than the current size.  After any
size adjustments, the buffer size must be at least 4 points and no greater than the allocated buffer size.  To check the
allocated buffer size, use the command `DBSZ 1`.  If the adjusted buffer size is greater than the allocated size, the
original size is restored before RNMR exits the `HILB` command.  If the original buffer size was not a power of 2, RNMR
will zero fill the data up to the new size.  Each partition of the processing buffer is separately zero filled; to check
or set the partitioning of buffer 1, use the command `DBSZ 1`.  After zero filling (if required), RNMR performs a
Hilbert transform on each block of buffer 1.  The following algorithm is used:

1.	The imaginary part of the data is initially computed by interpolating points from the real part:

        IMAG(I) = (REAL(I) + REAL(I+1))/2                   I=1,...,SIZE-1
        IMAG(SIZE) = (REAL(SIZE) + REAL(1))/2               I=SIZE`

2.	A real FFT is performed on the real part and the imaginary part of the data separately.

3.	Both the real and imaginary parts of the first point are multiplied by 0.5 in preparation for inverse Fourier
transformation (see "fctr1" under the command "`IFT`"):

        REAL(1)=0.5*REAL(1)
        IMAG(1)=0.5*IMAG(1)

4.	A complex inverse FFT is performed on the real and imaginary parts of the data simultaneously.

5.	The resulting frequency-domain data is conjugated:

        IMAG(I)=-IMAG(I)     I=1,...,`SIZE`

After the transformation is complete, RNMR sets the buffer active size to its original value, even if that size was not
a power of 2.  If the processing buffer is currently visible (`VIEW PRO`), then RNMR updates the screen display
following `HILB`.
## HILBZ
Perform Hilbert transform on zero-filled spectrum

Category:

Format: `HILBZ`

Defaults:
## HTR
Enable or disable probe heater

Category: Heater

Format: `HTR` state

Defaults: current

Prerequisites: RNMR only.

Description:
`HTR` sets the heater enable flag on or off.  This flag enables or disables computer control of the probe temperature.
When the `HTR` command is issued, RNMR checks the current status of the probe heater.  If the heater is in ERROR status,
RNMR reports the error and resets the heater status.  `HTR` takes one parameter, "state", which is ON if heater control
is enabled and OFF otherwise.  If "state" is omitted, RNMR will prompt for the heater enable state with the current
state as the default.  The legal values of "state" are ON and OFF only.  If the user presses <RETURN\> when prompted
for a heater state, no changes are made.  Otherwise, the new heater state is written to the spectrometer hardware
immediately.
## HTRSTS
Return probe heater status

Category: Heater

Format: `HTRSTS`

Prerequisites: RNMR only.

Description:
`HTRSTS` returns the current probe heater status in an informational message.  `HTRSTS` directs RNMR to inquire the
heater status directly from the spectrometer hardware.  If the status returned by the temperature controller indicates
an error, RNMR will reset the heater status without printing an error message.  The heater status value read from the
hardware is displayed via an informational message as a two-character hexadecimal string.

# I
---
## IBOX
Set volume parameters for nD volume integration

Category:

Format: `IBOX`

Defaults:
## IDN
Set buffer identification fields

Category: Data Storage

Format: `IDN` idn val prompt

Defaults: 1 current VAL

Description:
`IDN` sets the value of an identifier field for the visible processing buffer.  These values are saved in the title
record when the data is saved and may be used to store any desired ancillary information about an experiment, such as
pH, temperature, or sample spinning speed.  Currently, there are four identifiers available.  `IDN` modifies only the
visible processing buffer (buffer 1), however the user need not be viewing this buffer to use `IDN`.

The first parameter, "idn", selects which identifier field is to be modified. The legal values for "idn" are the
integers
1,2,3, and 4. If "idn" is not specified, RNMR will prompt for an identifier number with a default value of 1.

The third parameter, "prompt", specifies a prompt string to use for inquiring the value of the specified `IDN` field.
This parameter is used only if "val" is omitted from the `IDN` command line. The purpose of the "prompt" parameter is to
facilitate interactive input of `IDN` values from a macro, as in the command:

    IDN 1 7.0    ! set default value for idn 1
    IDN 1,,PH    ! prompt user for new IDN 1 value

which prompts for the value of `IDN` number 1 as shown below:

    PH     = 7.0

If "prompt" is omitted, RNMR will use the prompt string "VAL    ="; RNMR does not ask the user for "prompt" if it is
not specified on the command line.  Values for "prompt" should be strings of 1 to 6 characters; RNMR will always use "
=" as the last two characters of an `IDN` prompt string.

The second parameter, "val", specifies a new value for the `IDN` field selected by "idn".  If no value is specified,
RNMR will ask the user for a value using the prompt selected by the "prompt" parameter and the current value of the
`IDN` field as the default.  Thus, entering "`IDN` 1" in RNMR will display the current value of the first identifier
field and ask the user for a new value.  If the user presses <RETURN\> at this prompt, no changes are made.  Otherwise,
RNMR sets the specified `IDN` field to the value entered.  If the "val" parameter is specified on the `IDN` command
line, RNMR will update the value of the identifier field and no prompt will be made.

Each `IDN` field stores a maximum of 8 characters and is written to the appropriate title record when the visible
processing buffer is saved to disk using the `SA`, `SB`, and `SS` commands.  Thus, the identifier fields may be used to
note user-defined conditions for each record.  When RNMR starts up, each identifier field is blank.  Processing buffer
identifier fields may be displayed and modified only by the `IDN` command.
## IDNA
Set acquisition buffer identification fields

Category: Acquisition

Format: `IDNA` idn val prompt

Defaults: 1 current VAL

Prerequisites: RNMR only.

Description:
`IDNA` sets the value of an identifier field for the acquisition buffer.  Following the get averager (`GAV`) command,
these values are saved in the title record when the data is saved and may be used to store any desired ancillary
information about an experiment, such as pH, temperature, or MAS spinning speed.  Currently, there are four identifiers
available.  `IDNA` modifies only the acquisition buffer, however the user need not be viewing this buffer to use `IDNA`.
 When the user transfers averager data and parameters to a processing buffer with `GAV`, the `IDNA` fields are saved to
the corresponding `IDN` fields of that processing buffer.  Thus, the user may set up identifier field values (to be
saved to disk after acquisition) before beginning an experiment.

The first parameter, "idn", selects which identifier field is to be modified.  The legal values for "idn" are the
integers 1,2,3, and 4. If "idn" is not specified, RNMR will prompt for an identifier number with a default value of 1.

The third parameter, "prompt", specifies a prompt string to use for inquiring the value of the specified `IDNA` field.
This parameter is used only if "val" is omitted from the `IDNA` command line.  The purpose of the "prompt" parameter is
to facilitate interactive input of `IDNA` values from a macro, as in the command:

    IDNA 1 7.0   	! set default value for idn 1
    IDNA 1,,PH   	! prompt user for new IDNA 1 value

which prompts for the value of `IDNA` number 1 as shown below:

    PH     = 7.0

If "prompt" is omitted, RNMR will use the prompt string "VAL    ="; RNMR does not ask the user for "prompt" if it is
not specified on the command line.  Values for "prompt" should be strings of 1 to 6 characters; RNMR will always use "
=" as the last two characters of an `IDNA` prompt string.

The second parameter, "val", specifies a new value for the `IDNA` field selected by "idn".  If no value is specified,
RNMR will ask the user for a value using the prompt selected by the "prompt" parameter and the current value of the
`IDNA` field as the default.  Thus, entering "`IDNA` 1" in RNMR will display the current value of the first identifier
field and ask the user for a new value.  If the user presses <RETURN\> at this prompt, no changes are made.  Otherwise,
RNMR sets the specified `IDNA` field to the value entered. If the "val" parameter is specified on the `IDNA` command
line, RNMR will update the value of the identifier field and no prompt will be made.  Each `IDNA` field stores a maximum
of 8 characters and is a parameter of the acquisition buffer.  When RNMR starts up, each identifier field is blank.
Acquisition buffer identifier fields may be displayed and modified only by the `IDNA` command.
## IFCND
Branch on condition flag

Category: Macro

Format: `IFCND` icnd labelt labelf

Defaults: 1 none none

Prerequisites: Macro only (MAC)

Description:
`IFCND` is one of the old if commands. It jumps to labelt if the specified condition flag is ON and to labelf if it is
OFF. As with all of the old if commands, if the label to jump to is not specified execution continues to the next line.

The old if commands have been replaced. Instead use `TST` to conditionally execute commands or `GOTST` to make
conditional jumps.
## IFEQ
Branch on equal

Category: Macro

Format: `IFEQ` arg1 arg2 labelt labelf

Defaults: none none none none

Prerequisites: Macro only (MAC)

Description:
`IFEQ` is one of the old if commands. It jumps to labelt if arg1 and arg2 are the same string and to labelf if they are
not. As with all of the old if commands, if the label to jump to is not specified execution continues to the next line.

The old if commands have been replaced. Instead use `TST` to conditionally execute commands or `GOTST` to make
conditional jumps.
## IFGBL
Check for global argument and branch

Category: Macro

Format: `IFGBL` gblnam labelt labelf

Defaults: TEMP none none

Prerequisites: Macro only (MAC)

Description:
`IFGBL` is one of the old if commands. It jumps to labelt if the specified global argument exists and to labelf if it
does not. As with all of the old if commands, if the label to jump to is not specified execution continues to the next
line.

The old if commands have been replaced. Instead use `TST` to conditionally execute commands or `GOTST` to make
conditional jumps.
## IFLCL
Check for local argument and branch

Category: Macro

Format: `IFLCL` lclnam labelt labelf

Defaults: TEMP none none

Prerequisites: Macro only (MAC)

Description:
`IFLCL` is one of the old if commands. It jumps to labelt if the specified local argument exists and to labelf if it
does not. As with all of the old if commands, if the label to jump to is not specified execution continues to the next
line.

The old if commands have been replaced. Instead use `TST` to conditionally execute commands or `GOTST` to make
conditional jumps.
## IFMAC
Check for macro and branch

Category: Macro

Format: `IFMAC` macnam labelt labelf

Defaults: TEMP none none

Prerequisites: Macro only (MAC)

Description:
`IFMAC` is one of the old if commands. It jumps to labelt if the specified macro exists and to labelf if it does not. As
with all of the old if commands, if the label to jump to is not specified execution continues to the next line.

The old if commands have been replaced. Instead use `TST` to conditionally execute commands or `GOTST` to make
conditional jumps.
## IFREC
Check for record and branch

Category: Macro

Format: `IFREC` rec. labelt labelf

Defaults: current none none

Prerequisites: Macro only (MAC)

Description:
`IFREC` is one of the old if commands. It jumps to labelt if the specified record exists and to labelf if it does not.
As with all of the old if commands, if the label to jump to is not specified execution continues to the next line.

The old if commands have been replaced. Instead use `TST` to conditionally execute commands or `GOTST` to make
conditional jumps.
## IFT
Inverse Fourier transform spectrum

Category: Data manipulation

Format: `IFT` size fctr1

Defaults: current 1.0

Prerequisites: Frequency domain data in visible processing buffer (FREQ)

Description:
`IFT` performs a fast Fourier transform on frequency domain data in processing buffer 1. If the number of active points
in each block of the processing buffer is not a power of 2, zero filling is performed to increase the size to the next
power of 2.

The first parameter of `IFT` is "size", which is the desired number of points after Fourier transformation.  If this
parameter is omitted, the size after transformation will be the smallest power of 2 greater than or equal to the current
size.  Thus, if the spectrum has 200 points, its Fourier transform will have 256 points.  The processing buffer must
have an allocated size at least as large as this adjusted size or an error message will be returned.  When the size of
the spectrum is not a power of 2, RNMR zero fills the  spectrum to the next power of 2 before Fourier transformation.
If "size" is omitted, RNMR will not prompt for a size and the current size must be at least 3.  If "size" is specified,
the value entered must be a power of 2 greater than or equal to the current size and between 4 and SIZEA inclusive,
where SIZEA is the allocated size of each block in processing buffer 1.  If "size" is explicitly specified, RNMR will
attempt to use the indicated size without adjustment.

The second parameter, "fctr1", specifies the correction factor to be applied to the first point of the data.  The first
point is multiplied by 0.5\*fctr1 before Fourier transformation to correct the constant offset of the resulting FID.  A
value of 1.0 for "fctr1" should be appropriate for most applications.  If "fctr1" is omitted, a value of 1 will be used;
RNMR does not prompt for "fctr1".  The legal values of "fctr1" are real numbers strictly greater than 0.0.

Before inverse Fourier transformation is performed, RNMR zero fills the spectrum if the FID size will be greater than
the current size.  This zero filling is done to each block of the processing buffer separately.  Next, each block of the
processing buffer receives an inverse fast Fourier transform.  The first point of each resulting FID is multiplied by
the real constant 2.0/fctr1, where "fctr1" is an `IFT` command parameter described above.  After transformation, RNMR
checks whether the time domain data should be conjugated.  Since time domain data is presented with minimum time on the
left while frequency data is presented with maximum frequency on the left (by long standing NMR convention), the default
action of `IFT` is to conjugate the data after transformation.  This ensures that performing an `IFT` followed by an
`FT` will give the same frequency data order.  If the observe synthesizer has not been defined, the data is always
conjugated.  Otherwise, the resulting FID will be conjugated if the observe channel is generated from the lower sideband
(LSB) of the sum of the synthesizer and intermediate (IF) frequencies.  If conjugation is required, it is done
separately to each block of the processing buffer.

Use of `IFT` resets the constant and linear phase values of the  processing buffer (phi0 and phi1) to zero.  The time
domain data in each block of the processing buffer is scaled by a constant factor so that the complex magnitude of the
largest point in the first block is 1.0.  The largest point is the point whose intensity has the largest complex
magnitude. If the largest magnitude in block 1 is 0.0, no rescaling of the data is performed.  After any rescaling is
complete, the buffer scale factor is divided by the new size and the rescaling factor:

    SFT = SFT/(VMAX*SIZE)

where VMAX is the maximum magnitude in block 1 if this magnitude is nonzero or 1.0 otherwise.  If the processing buffer
is currently visible, `IFT` always updates the display to show the transformed data.  If processing buffer 1 is
partitioned into two or more blocks, `IFT` acts separately on each block.  Thus, multiple spectra may be transformed to
yield multiple FID's with one invocation of the `IFT` command.  This "vector processing" feature saves processing time
by decreasing the number of `IFT` commands that RNMR's command interpreter must handle.  `IFT` may only be used to
transform frequency domain data into the  time domain.  To perform the forward transformation, use `FT`.
## IMP
Import data from foreign format

Category: Foreign

Format: `IMP` format

Defaults: NMR1

Description:
`IMP` imports the contents of a disk file in a foreign (non-RNMR) format to processing buffer 1.  This importation
allows one-dimensional data to be transferred to RNMR from another processing program or from one RNMR archive to
another via `EXP`.  Since the foreign data is only read into memory by `IMP`, the user must use `SA`, `SB`, or `SS` to
store the imported data permanently.

`IMP` takes one parameter, "format" which specifies the foreign source format.  If "format" is omitted, RNMR will prompt
for a  foreign format with NMR1 as the default.  The currently supported foreign formats are:

Format | Description
------ | -----------
FELIX  | FELIX, complex data
FTNMR  | FTNMR, complex data
FTNMRR | FTNMR, real data
NMR1   | NMR1/NMR2, standard blocks
NMR1A  | NMR1/NMR2, alternate blocks

For the importation of one-dimensional data, NMR1 and NMR1A formats are identical.  Note that while the user need not be
viewing the processing buffer to use `IMP`, `IMP` imports data only to processing buffer 1.  If the `IMP` command is
used at console level, RNMR will prompt the user for the name of the file which contains the data to be imported.  The
user may enter any valid VMS file name up to 64 characters long.  If the user presses <RETURN\> at this prompt, no data
is imported to the processing buffer.  If `IMP` is used from within a macro, RNMR expects the foreign format file name
to be delimited by two semicolons (;;) on the line following the `IMP` command.  The entire line after ;; constitutes
the file name, as illustrated below:

    IMP FTNMR
    ;;MYFILE.DAT

If the double semicolon delimiter ;; is not found on the line after `IMP`, RNMR will prompt for a file name as when
`IMP` is used from console level.  Conversely, if ;; is present but there is no text on the line after ;;, `IMP` does
nothing and the macro execution continues.  The text following ;; may be any valid VMS file name up to 64 characters
long.  This text may contain local and global argument substitutions, e.g.

    IMP FTNMR
    ;;MYFILE_&1

The local and global arguments specified will be evaluated and filled in before the import file is read in.  If no VMS
file type was specified in the import file name, RNMR uses:

Format | File Type
------ | -----------
FELIX  | .FELIX
FTNMR  | .FTNMR
NMR1 or NMR1A | .NMR1

RNMR will attempt to read the most recent version of the foreign format file in the current default directory (e.g.
USERA:[JONES]) unless an explicit version number and/or directory were specified by the user.  The foreign format file
is opened for read-only access.
FTNMR Importation
RNMR supports importation of FTNMR files with or without header records.  If RNMR finds a header record in an FTNMR file
being imported, the encoded header parameters will be used to establish the processing buffer size, domain, etc. and
RNMR will display the message "USING SUPPLIED FILE HEADER".  If no header is found in the FTNMR file, RNMR will set the
processing buffer parameters to default values, as described below.  In this case, the message "USING DEFAULT FILE
HEADER" will be displayed.  If the specified FTNMR file has a header record, the buffer size will be set to the size
value encoded in the file header.  Otherwise, the buffer size will be set to the number of data points (real or complex)
in the first file record.  This size must be at least 2 and no greater than 8192, which is the largest data buffer size
currently supported by RNMR.  The buffer domain (TIME or FREQ) and sweep width are obtained from the values encoded in
the FTNMR file header, if this header exists.  If there is no header, the buffer domain and sweep width are left
unchanged from their current values.  `IMP` FTNMR sets the buffer title to the name of the FTNMR file read in.  RNMR
marks this title as unconfirmed, so when the user saves the buffer to disk with `SA` or `SB` (but not `SS`), RNMR will
ask for a title, with the FTNMR file name as the default.  When FTNMR data is read into the processing buffer, the
buffer owner and date fields are set to the current user and date.

`IMP` FTNMR sets the processing buffer parameters to default values since none of these values are available from the
FTNMR file header:

Parameter | Description | IMP FTNMR default
--------- | ----------- | -----------------
RECNO     | Archive record number | 0
BLKNO     | Archive block number | 0 each
IDN       | Identifier field | '       ' each
SYN       | Buffer synthesizer | 1
PWR       | Transmitter power | 0.0 each
GAIN      | Receiver gain | 0.0
FLF       | Receiver filter factor | 1.0
PPNAM     | Pulse program name | '       '
PLS       | Pulse length | 0.0 each
DLY       | Delay length | 0.0 each
LOOP      | Loop value | 0 each
FLAG      | PP flag state (`PPFLG`) | .FALSE. each
FLDEC     | Decouple flag (`DEC`) | .FALSE.
FLHETR    | Heteronuclear decouple | .FALSE.
FLDECX    | Decouple flag (`DECFLG`) | .FALSE. each
RD        | Recycle delay | 0.0
NAMD      | Number of acq modes | 1
AMD       | Acquisition mode list | 0
PPMD      | PP mode list | 0 each
NA        | Total number of scans | 1
IA        | Number of scans taken | 1
NWAIT     | Number of scans to `WAIT` | 0
NDLY      | Number of dummy scans | 0
NDSP      | #scans/screen update | 0
DIM       | Buffer dimension | 1
IPHI0     | Constant phase value | 0
IPHI1     | Linear phase value | 0
SFT       | Buffer scale factor | 1.0

Note that RNMR ignores any PPM to Hz conversion parameters and constant and linear phase values encoded in the FTNMR
file header in favor of the default values listed above.  If the FTNMR file has a parameter header record, RNMR reads
the next record in the file to obtain the buffer data. RNMR checks that the FTNMR record length in the second record
matches the size value encoded in the header. If they do not agree, an error message:

    (RDAT_FTNMR  ) ILLEGAL RECORD SIZE

will be displayed along with the second record's length.

If the imported FTNMR file has no header, RNMR reads only the first record of the file to obtain the buffer data.  RNMR
can read FTNMR data in either complex (FTNMR) or real-only (FTNMRR) format.  When data is read from an FTNMRR file, the
imaginary part of the processing buffer is set to zero.  If the processing buffer is currently visible on the screen,
RNMR will update the display once the `IMP` operation is complete.
NMR1 Importation
RNMR supports importation of NMR1 files in either standard (NMR1) or alternate-block (NMR1A) formats.  For purposes of
importing one-dimensional data, NMR1 and NMR1A files are handled identically.  Consequently, in the description below,
"NMR1" will refer to both the NMR1 and NMR1A formats.

When importing NMR1 data, RNMR sets the processing buffer size to the size value encoded in the NMR1 file header. This
size is required to be at least 64 and no greater than 8192.  RNMR obtains the sweep width in the first dimension from
the NMR1 header parameter fdSweepWidth.  The title field in the NMR1 header becomes the buffer title and RNMR marks the
buffer title as unconfirmed.  Thus, when the user saves the buffer to disk with `SA` or `SB` (but not `SS`), RNMR will
ask for a title, with the NMR1 title field as the default. Any control characters in the NMR1 title field (characters
less than "`SP`") are replaced by blanks in composing the buffer title.  When NMR1 data is read into the processing
buffer, the buffer owner and date fields are set to the current user and date.  If the spectrometer frequency field in
the NMR1 header (fdSpecFreq) is not zero, RNMR defines the nucleus OBS with the NMR and reference frequencies encoded in
the header.  If OBS is already defined or if there is no more room in the nucleus table, the nucleus UNKN is redefined
with these frequencies.  RNMR sets the buffer observe synthesizer nucleus parameter to OBS or UNKN accordingly.  If the
NMR1 spectrometer frequency field is zero, RNMR does not update any nuclei, and the buffer observe nucleus is set to '
'.  The frequency value (SYNVAL) for synthesizer 1 is set to 0.0 and all synthesizer table entries for that synthesizer
(SYNFRQ) are marked as unused.  Similarly, if the decoupler frequency field in the NMR1 header (fdDecouplerFreq) is not
zero, RNMR defines the nucleus DEC with the NMR and reference frequencies encoded in the header.  If DEC is already
defined or if there is no more room in the nucleus table, the nucleus UNKN is redefined with these frequencies.  RNMR
sets the buffer decouple synthesizer nucleus parameter to DEC or UNKN accordingly.  If the NMR1 decoupler frequency
field is zero, RNMR does not update any nuclei, and the buffer decouple nucleus is set to ' '.  The frequency value
(SYNVAL) for synthesizer 2 is set to 0.0 and all synthesizer table entries for that synthesizer (SYNFRQ) are marked as
unused.  For synthesizers 3 and 4, RNMR sets the synthesizer nucleus buffer parameter to ' ' and the synthesizer value
buffer parameter to 0.0.  The synthesizer table entries for these synthesizers are initialized with all fields marked as
unused.  The pulse program name for the processing buffer is obtained from the NMR1 header experiment name parameter,
fdexnamel.  Both the total number of scans (`NA`) and the actual number of scans taken (IA) are set to the value of
fdnscan, the number of scans parameter in the NMR1 file header.

`IMP` NMR1 always sets the processing buffer DIM parameter to 1 to indicate that the buffer will contain NMR1 data from
the first (acquisition) dimension. The size and domain (time or frequency) of the buffer are set to their corresponding
values in the NMR1 header (fdsize and fdFtFlag).  `IMP` NMR1 sets certain processing buffer parameters to default values
since their values are not available from the NMR1 file header:

Parameter | Description | IMP FTNMR default
--------- | ----------- | -----------------
RECNO     | Archive record number | 0
BLKNO     | Archive block number | 0 each
IDN       | Identifier field | '       ' each
SYN       | Buffer synthesizer | 1
PWR       | Transmitter power | 0.0 each
GAIN      | Receiver gain | 0.0
FLF       | Receiver filter factor | 1.0
PPNAM     | Pulse program name | '       '
PLS       | Pulse length | 0.0 each
DLY       | Delay length | 0.0 each
LOOP      | Loop value | 0 each
FLAG      | PP flag state (`PPFLG`) | .FALSE. each
FLDEC     | Decouple flag (`DEC`) | .FALSE.
FLHETR    | Heteronuclear decouple | .FALSE.
FLDECX    | Decouple flag (`DECFLG`) | .FALSE. each
RD        | Recycle delay | 0.0
NAMD      | Number of acq modes | 1
AMD       | Acquisition mode list | 0
PPMD      | PP mode list | 0 each
NA        | Total number of scans | 1
IA        | Number of scans taken | 1
NWAIT     | Number of scans to `WAIT` | 0
NDLY      | Number of dummy scans | 0
NDSP      | #scans/screen update | 0
DIM       | Buffer dimension | 1
IPHI0     | Constant phase value | 0
IPHI1     | Linear phase value | 0
SFT       | Buffer scale factor | 1.0

When RNMR imports data from an NMR1 format file, the data is multiplied by a factor C as defined below:

C | Condition
- | ---------
SF | `NA` is less than or equal to 0 and time domain
SF/SIZE | `NA` is less than or equal to 0 and freq. domain
SF/(2048\*NA) | `NA` is greater than 0 and time domain
SF/(2048\*NA\*SIZE) | `NA` is greater than 0 and frequency domain

 where SF is the NMR1 scale factor:

 SF = 2.0^(-IPWR), IPWR = fdAbsScale

If the number of spectra in the source file, fdSpecNum, is greater than 1, `IMP` NMR1 will refuse to read the data, and
an error message:

    (IMP_NMR1 ) FILE NOT 1D

will be displayed. If this occurs, use `IMP2D` NMR1 to import the NMR1 data into an RNMR archive record.  If the
processing buffer is currently visible on the screen, RNMR will update the display once the `IMP` operation is complete.
## IMP2D
Import 2D data from foreign format


Category: Foreign

Format: `IMP2D` format rec blk

Defaults: NMR1 next 1


Description:
`IMP2D` imports a two-dimensional data set from a foreign (non-RNMR) format file to a pre-allocated blocked archive
record.  This importation allows two-dimensional data to be transferred from a foreign processing program to RNMR or
from one RNMR archive to another via `EXP2D`.  The first parameter, "format" specifies the foreign source format. If
"format" is omitted, RNMR will prompt for a foreign format with NMR1 as the default.  The currently supported foreign
formats are:

Format | Description
------ | -----------
FELIX  | FELIX, complex data
FTNMR  | FTNMR, complex data
FTNMRR | FTNMR, real data
NMR1   | NMR1/NMR2, standard blocks
NMR1A  | NMR1/NMR2, alternate blocks


The second parameter, "rec" specifies the number of a blocked archive record to receive the imported data.  If this
parameter is omitted, RNMR will prompt for a destination record number with the current archive record (as displayed and
set by `PTRA`) as the default.  The acceptable values of "rec" are integers from 5 to 200; the scratch records (1-4) are
always one-dimensional. RNMR checks that "rec" is in fact a nonempty blocked record.  If "rec" is not a blocked record,
RNMR will display the error message:

    (CHKTYP) RECORD WRONG TYPE

The last parameter, "blk2d" specifies which 2D slice of a 3D or 4D destination record "rec" should receive the foreign
format data. If the record "rec" has only two dimensions, "blk2d" must be 1.  If "blk2d" is omitted, then the data will
be written to the first 2D slice of record "rec".  That is, the default value of "blk2d" is 1.  RNMR does not prompt for
"blk2d".  The legal values of "blk2d" are the integers 0,1,2,... up to the number of 2D slices allocated for the
destination record.  If "blk2d" is zero, then RNMR will write the imported data to the next 2D slice in the destination
record.  The command `PTRB` "rec" displays the current write block for a given record; "blk2d" equal to zero directs
`IMP2D` to write to the block after the current write block.  Note that the current mapping of dimensions to directions
(as displayed and set by `DIRB`) will affect the selection of which one-dimensional blocks of record "rec" comprise the
2D slice "blk2d" and will thus receive the foreign data.  When `IMP2D` is used to import 2D slices to a four-dimensional
record of size A X B X C X D, "blk2d" values from 1 to C select slices from the first cube, C+1 to 2C select slices from
the second cube, etc.  In this way, selection of 2D slices from a 4D data set can be accomplished with one parameter,
"blk2d".  In order for record "rec" to receive data from `IMP2D`, the record must have been allocated with at least two
dimensions.  If the record has only one dimension allocated, RNMR will display the error message:

    (CVTBB ) TOO FEW DIMENSIONS

If the `IMP2D` command is used at console level, RNMR will prompt the user for the name of the file which contains the
data to be imported.  The user may enter any valid VMS file name up to 64 characters long.  If the user presses
<RETURN\> at this prompt, no data is imported to the processing buffer.  If `IMP2D` is used from within a macro, RNMR
expects the foreign format file name to be delimited by two semicolons (;;) on the line following the `IMP` command.
The entire line after ;; constitutes the file name, as illustrated below:

    IMP2D FTNMR 25
    ;;MYFILE.DAT

If the double semicolon delimiter ;; is not found on the line after `IMP2D`, RNMR will prompt for a file name as when
`IMP2D` is used from console level.  Conversely, if ;; is present but there is no text on the line after ;;, `IMP2D`
does nothing and the macro execution continues.  The text following ;; may be any valid VMS file name up to 64
characters long.  This text may contain local and global argument substitutions, e.g.

    IMP2D FTNMR 25
    ;;MYFILE_&1

The local and global arguments specified will be evaluated and filled in before the import file is read in.  If no VMS
file type was specified in the import file name, RNMR uses:

Format | File Type
------ | -----------
FELIX  | .FELIX
FTNMR  | .FTNMR
NMR1 or NMR1A | .NMR1

RNMR will attempt to read the most recent version of the foreign format file in the current default directory (e.g.
USERA:[JONES]) unless an explicit version number and/or directory were specified by the user.  The foreign format file
is opened for read-only access.
NMR1 Importation
RNMR supports importation of NMR1 files in either standard (NMR1) or alternate-block (NMR1A) formats.
Except as noted, "NMR1" will refer to both NMR1 and NMR1A formats in the discussion below.  When importing NMR1 data
(standard blocks), RNMR requires that the first-dimension size of the foreign data set (as encoded by the NMR1 header
parameter fdsize) be at least 64 and no greater than 8192.  For the NMR1A format, RNMR requires fdsize to be at least
128 and no more than 16384.  Failure to satisfy these constraints will result in an error message:

    (RPRM_NMR1) SIZE OUT OF BOUNDS

RNMR determines the number of 1D slices in the NMR1 data set by examining the header parameter fdSpecNum.  This
parameter must be greater than 1 to use `IMP2D` NMR1.  If fdSpecNum is less than or equal to one, RNMR will display the
error message:

    (IMP2D_NMR1  ) FILE NOT 2D

If fdSpecNum is greater than 1, RNMR assumes that the NMR1 data set is two-dimensional.  If "format" is NMR1, RNMR
expects that fdSpecNum is the number of 1D slices in the NMR1 format file.  Conversely, if "format" is
NMR1A, there should be 2\*fdSpecNum slices, with alternate slices belonging to the real and imaginary parts of the
2D data set.  RNMR obtains the sweep width in the first dimension from the NMR1 header parameter fdSweepWidth.  The
title field in the NMR1 header becomes the record title and RNMR marks the record title as unconfirmed.  Thus, when
`IMP2D` transfers the first 1D block of data to record "rec", RNMR will ask for a title, with the NMR1 title field as
the default.  Any control characters in the NMR1 title field (characters less than "`SP`") are replaced by blanks in
composing the buffer title.  When NMR1 data is read into the processing buffer, the buffer owner and date fields are set
to the current user and date.  If the spectrometer frequency field in the NMR1 header (fdSpecFreq) is not zero, RNMR
defines the nucleus OBS with the NMR and reference frequencies encoded in the header.  If OBS is already defined or if
there is no more room in the nucleus table, the nucleus UNKN is redefined with these frequencies.  RNMR sets the record
observe synthesizer nucleus parameter to OBS or UNKN accordingly.  If the NMR1 spectrometer frequency field is zero,
RNMR does not update any nuclei, and the buffer observe nucleus is set to ' '.  The record's frequency value (SYNVAL)
for synthesizer 1 is set to 0.0 and all synthesizer table entries for that synthesizer (SYNFRQ) stored for record "rec"
are marked as unused. Similarly, if the decoupler frequency field in the NMR1 header (fdDecouplerFreq) is not zero, RNMR
defines the nucleus DEC with the NMR and reference frequencies encoded in the header.  If DEC is already defined or
if there is no more room in the nucleus table, the nucleus UNKN is redefined with these frequencies.  RNMR sets the
record decouple synthesizer nucleus parameter to DEC or UNKN accordingly.  If the NMR1 decoupler frequency field is
zero, RNMR does not update any nuclei, and the record's decouple nucleus is set to ' '.  The record's frequency value
(SYNVAL) for synthesizer 2 is set to 0.0 and all synthesizer table entries for that synthesizer (SYNFRQ) stored for
record "rec" are marked as unused.  For synthesizers 3 and 4, RNMR sets the synthesizer nucleus title parameter to ' '
and the synthesizer value title parameter to 0.0.  The synthesizer table entries for these synthesizers are initialized
with all fields marked as unused. The pulse program name for the destination record is obtained from the NMR1 header
experiment name parameter, fdexnamel.  Both the total number of scans (`NA`) and the actual number of scans taken (IA)
are set to the value of fdnscan, the number of scans parameter in the NMR1 file header.

`IMP2D` NMR1 always sets the record DIM parameter to 1 to indicate that the record will contain NMR1 data from the first
(acquisition) dimension.  The first dimension size and domain (time or frequency) of the record are set to their
corresponding values in the NMR1 header (fdsize and fdFtFlag).  `IMP2D` NMR1 sets certain processing buffer parameters
to default values since their values are not available from the NMR1 file header:

Parameter | Description | IMP FTNMR default
--------- | ----------- | -----------------
IDN       | Identifier field | '       ' each
SYN       | Buffer synthesizer | 1
PWR       | Transmitter power | 0.0 each
GAIN      | Receiver gain | 0.0
FLF       | Receiver filter factor | 1.0
PPNAM     | Pulse program name | '       '
PLS       | Pulse length | 0.0 each
DLY       | Delay length | 0.0 each
LOOP      | Loop value | 0 each
FLAG      | PP flag state (`PPFLG`) | .FALSE. each
FLDEC     | Decouple flag (`DEC`) | .FALSE.
FLHETR    | Heteronuclear decouple | .FALSE.
FLDECX    | Decouple flag (`DECFLG`) | .FALSE. each
RD        | Recycle delay | 0.0
NAMD      | Number of acq modes | 1
AMD       | Acquisition mode list | 0
PPMD      | PP mode list | 0 each
NA        | Total number of scans | 1
NWAIT     | Number of scans to `WAIT` | 0
NDLY      | Number of dummy scans | 0
NDSP      | #scans/screen update | 0
DIM       | Buffer dimension | 1
IPHI0     | Constant phase value | 0
IPHI1     | Linear phase value | 0
SFT       | Buffer scale factor | 1.0

When RNMR imports data from an NMR1 format file, the data is multiplied by a factor C as defined below:

C | Condition
- | ---------
SF | `NA` is less than or equal to 0 and time domain
SF/SIZE | `NA` is less than or equal to 0 and freq. domain
SF/(2048\*NA) | `NA` is greater than 0 and time domain
SF/(2048\*NA\*SIZE) | `NA` is greater than 0 and frequency domain

where SF is the NMR1 scale factor:

    SF = 2.0^(-IPWR), IPWR = fdAbsScale

RNMR reads each 1D slice from the NMR1 format file and writes it (after scaling the data by the factor C above) to a
block in record "rec".
## IMP3D
Import 3D data from foreign file format


Category: Foreign

Format: `IMP3D` format rec blk

Defaults: NMR1 next 1


Description:
## INTG
Compute integral of spectrum

Category: Data Manipulation

Format: `INTG`

Prerequisites: Frequency domain data in processing buffer (FREQ)

Description:
`INTG` calculates and displays the indefinite integral (antiderivative) of the data in the visible processing buffer
(buffer 1) within the current display limits, as displayed and set by `LIM`.  By integrating a spectrum, one may measure
the total intensity of each peak.  For calculating the integrated intensity of individual peaks, one may compute the
definite integral within specified frequency limits using the command `INTRG`.  `INTG` acts only on the first processing
buffer.  The user need not be currently viewing this buffer (`VIEW PRO`) to use `INTG`.  Only the portion of the data
lying between the current display limits will be integrated by `INTG`.  If the left display limit is currently "\*",
`INTG` will begin the integration at the leftmost point in the data buffer.  Similarly, if the right display limit is
"\*", `INTG` will integrate up to the last point in the buffer.  To prepare the data for integration, `INTG` performs a
baseline fix apodization.  This step eliminates any constant offset after integration.  If the processing buffer is
divided into two or more blocks, a separate baseline fix is performed for each block.  The baseline is corrected before
integration by subtracting a straight line from the data between the left and right display limits.  The following
algorithm is used to obtain the equation of the line to subtract from the spectrum:

1.	Starting at the current left display limit, take the complex  average of the first five points toward the right
(including the point at the display limit).  If there are fewer than five points to the right in the spectrum (including
any points beyond the right display limit), average over all the points from the left display limit to the last point in
the spectrum instead.

2.	Starting at the current right display limit, take the complex average of the first five points toward the left
(including the point at the display limit).  If there are fewer than five points to the left in the spectrum (including
any points beyond the left display limit), average over all points from the right display limit to the first point in
the spectrum instead.

3.	Calculate complex polynomial coefficients P1 and P2:

        P1 = (Ravg - Lavg)/(Rlim - Llim)
        P2 = Lavg - P1*Llim
where Lavg and Ravg are the averages of the first few and last few points on either side of the display, as described in
(1) and (2), respectively, and Rlim and Llim are the point numbers corresponding to the right and left display limits.

4.	Calculate the value of a complex polynomial function Z at each point in the current display:

        Z(I) = (P1 X I) + P2
where I is the data point number (I=1 is the first point in the spectrum, regardless of display limits).  Note that this
polynomial describes a straight line in both its real and imaginary parts.

5.	For each point of the spectrum in the current display, subtract the value of the corresponding point of Z(I), the
baseline correction polynomial.  This corrects both the real and imaginary parts of each data point within the display
limits, but does not affect any points outside those limits.

After baseline fixing, each block of the processing buffer is separately integrated.  This integration consists of
replacing each data point within the region to be integrated by the sum of all points from the left display limit to
that data point, including the endpoints:

        DATA(LLIM) 	= DATA(LLIM)
        DATA(LLIM+1) = DATA(LLIM)+DATA(LLIM+1)
        DATA(LLIM+2) = DATA(LLIM)+DATA(LLIM+1)+DATA(LLIM+2)

After integration, the data is normalized so that the largest point in the first block (between the current display
limits) has a real absolute value intensity of 1.  If the largest real absolute value intensity is zero, the data is not
rescaled.  If the data is rescaled, RNMR updates the buffer scale factor, as displayed by `SC`:

    SFT = SFT*SF

where SF is the factor by which the data was multiplied to normalize the first block of the processing buffer.  If the
processing buffer is currently visible, RNMR updates the display after executing `INTG`.
## INTRG
Integrate region of spectrum

Category: Data Analysis

Format: `INTRG` llim rlim

Defaults: current_display_limits

Description:
`INTRG` calculates the definite integral of the real part of the data in the visible processing buffer (buffer 1) within
specified time or frequency limits.  To calculate and display the indefinite integral of a  spectrum within the current
display limits, use the command `INTG`.  `INTRG` acts only on the first processing buffer.  The user need not be
currently viewing this buffer (`VIEW PRO`) to use `INTRG`.  The parameters of the `INTRG` command are "llim" and "rlim",
the left and right integration limits, respectively.  If either or both of these limits are omitted from the command
line, RNMR will prompt for the missing limit(s).  The left and right integration limits default to the current left and
right display limits, which RNMR will report to the user in the current time or frequency unit, as set and displayed by
the `UNIT` command, with the current maximum number of decimal places, as set and displayed by `NDEC` for that unit.
For each display limit, the user should enter a value expressed in the current time or frequency unit or "\*" to select
the leftmost left limit or the rightmost right limit.  If the user requests an integration limit to the left of the
leftmost point in the data buffer, the integration will begin at the leftmost data point.  Similarly, if the right
integration limit specified is beyond the rightmost  data point, the integration will proceed to the rightmost data
point.  If the user specifies an integration limit that is within the range of the data buffer but which does not
correspond to a specific data point, RNMR will set that limit to the time or frequency of the closest data point to the
right of the value specified.  `INTRG` calculates the definite integral between the adjusted left and right limits in
the first block of the visible processing buffer.  This integral is defined as the sum of the real parts of each data
point between "llim" and "rlim", inclusive.  The integral is reported as an informational message with a maximum of two
decimal places.  If the integral cannot be reported as a floating point number in an eight character field, it is
reported in scientific notation.
## IXVAL
Convert from unit value to point index

Category: Data Analysis

Format: `IXVAL` xval
Default : 	        current_cursor_position Description:
`IXVAL` returns the point number (index value) of the specified time or frequency point.  This command may be used with
`XVAL`, which returns the time or frequency value given a point number, to locate and examine data points in a buffer
one by one within a specific time or frequency range.  `IXVAL` returns a point number using the time or frequency scale
of the visible processing buffer (buffer 1).  `IXVAL` takes one parameter, "xval", which is the time or frequency value
to be converted to a point number.  This value should be specified in the current time or frequency unit for processing
buffer 1.  If "xval" is not specified on the command line, RNMR will prompt for a time or frequency value with the
current cursor 1 position in buffer 1 as the default.  The cursor position is reported in the current time or frequency
unit (`UNIT`) with the current maximum number of decimal places for that unit (`NDEC`).  If the current cursor position
is "\*", then the default for "xval" is the time or frequency of the leftmost data point.  If the requested value of
"xval" is to the left of the leftmost data point, `IXVAL` will return the number 1.  Similarly, if "xval" is to the
right of the rightmost data point or if "xval" is "\*", `IXVAL` will return the number of data points in buffer 1.  If
the user specifies an "xval" value that is within the range of  the data buffer but which does not correspond to a
specific data point, RNMR will return the point number of the first data point to the right of the time or frequency
specified.  The point number corresponding to the adjusted time or frequency  value "xval" is reported to the user as an
informational message.  Note that "xval" need not lie within the current display limits, as set and displayed by the
`LIM` command.

# L
---
## LB
Set line broadening factor

Category: Data Manipulation

Format: `LB` lb

Defaults: current_lb_factor

Description:
`LB` displays and sets the line broadening factor for exponential and Gaussian multiplication apodizations (`EM` and
`GM`).  This factor can either be set with the `LB` command or by entering the line broadening factor as a parameter
with the `EM` or `GM` commands.  Thus, `EM 1`, `GM 1`, and `LB 1` all set the line broadening factor to 1.0 for
all subsequent apodizations.

`LB` has one parameter, "lb", which is the line broadening factor, expressed in the current default frequency unit.
This unit is set by the command "`UNIT /FREQ /DFLT`" and can be any frequency unit except PPM.  If "lb" is not
specified on the command line, RNMR will display the current line broadening factor and prompt for a value.  If the user
presses <RETURN\> at this prompt, the line broadening factor will not be updated.  The current line broadening factor is
expressed in the current default frequency unit with the current number of decimal places for that unit (`NDEC`).  The
line broadening parameter "lb" should be expressed in the current default frequency unit and may be either positive or
negative.  RNMR requires that the line broadening factor be no greater than 1000 Hz and no less than -1000 Hz,
regardless of the user's choice of default frequency unit.  An attempt to enter a line broadening factor outside this
range will result in an error message:

    (LB0    ) ARGUMENT ERROR

Once the line broadening factor has been updated, the new factor will be used for all future line broadening operations.
## LCK
Enable or disable lock feedback loop

Category: Lock

Format: `LCK` state

Defaults: current_lock_state

Prerequisites: `LCK` requires implementation of RNMR lock control. It is available in RNMR only.

Description:
`LCK` enables or disables the magnetic field-frequency lock on spectrometers with software lock control enabled.  `LCK`
takes one parameter, "state", which may be specified as  either ON or OFF to enable or disable the lock, respectively.
 If "state" is omitted from the command line, RNMR will display the current lock enable status and prompt for "state".
If the user presses <RETURN\> at this prompt, RNMR exits `LCK` without updating the hardware lock state.
## LCLARG
Set local argument value

Category: Arguments

Format: `LCLARG` nam val prompt

Defaults: TEMP current VALUE

Description:
`LCLARG` defines (or redefines) a local argument. Local arguments are  variables available only within the current
command level.  At any time there may be at most 128 defined local arguments at all levels.  Both the name and the value
of each local argument are 8-byte character strings.

The first parameter, "nam", is the name of the local argument to be defined or redefined.  The name of a local argument
may not be blank and must use only the characters A-Z, 0-9, $, or \_.  If no argument name is specified, RNMR will
prompt for the name of the local argument with "TEMP" as the default.

The third parameter, "prompt", specifies a string to be used if  RNMR prompts for the local argument value "val".  This
string may consist of up to 8 characters excluding blanks and commas.  If "prompt" is omitted, RNMR will use the prompt
"VALUE  ="; RNMR does not ask for a prompt string if one was not specified on the `LCLARG` command line.  If a prompt is
specified, it will be inserted into an eight character string in which the last two characters are always  " =".  Thus,
if "prompt" is "ABC", RNMR will use the prompt "ABC    =" when asking for the local argument value.  If "val" is
specified on the `LCLARG` command line, "prompt" will be ignored.

The second parameter, "val" is the value to which RNMR will set the specified local argument.  If "val" is nonblank,
RNMR will define or redefine the local argument without prompting the user.  If "val" is blank, RNMR will prompt the
user for a value.  The prompt string requested by the "prompt" parameter (if any) will be used.  The default for this
prompt will be the current value of the local argument if the argument is already defined, or "        " if the local
argument "nam" does not yet exist.  Thus, to make `LCLARG` prompt the user for the local argument value, one may use a
`LCLARG` command  of the form:

    LCLARG XYZ,,XYZ_VAL

This command will cause RNMR to prompt the user for the value of local argument XYZ.  If the user presses <RETURN\> at
this prompt, local argument XYZ will not be defined or redefined and the `LCLARG` command will have changed nothing.  If
a local argument with name "nam" does not exist prior to the execution of the `LCLARG` command, RNMR will create a new
local argument with the specified non-blank value.  Otherwise, the value of the existing local argument "nam" will be
updated.
## LCLDL
Delete local argument

Category: Arguments

Format: `LCLDL` lclnam

Defaults: TEMP

Description:
`LCLDL` deletes the specified local argument from the local argument table. Once a local argument has been deleted,
attempts to retrieve its value via the "&" operator  will yield an error message, while `LCLARG` will create a new local
argument with the same name.  `LCLDL` takes one parameter, "nam", which is the name of the argument to be deleted.  If
no name is specified, RNMR will prompt for a local argument name with "TEMP" as the default.  Pressing <RETURN\> at this
prompt results in deleting the local argument TEMP if it exists.  If the specified local argument exists, it will be
deleted.  Otherwise, `LCLDL` will simply do nothing and no error message will be displayed.
## LI
Increment pulse programmer loop value

Category: Acquisition

Format: `LI` loop incr.

Defaults: 1 1

Prerequisites: Pulse program loaded (LOAD), RNMR Only

Description:
`LI` increments a pulse program loop by a specified positive or negative integer value.  This function is particularly
useful in acquisition macros for multidimensional experiments or relaxation studies, where successive spectra are taken
with regularly incremented timings.  The pulse programs used in these experiments are written so that the timings to be
incremented consist of a pulse or delay within a loop.  The pulse or delay is then set to the desired time per point and
is left constant while the surrounding loop is incremented with `LI`.

Pulse program loops are specified in the PP source code by LOOP statements and assigned default values by DEF
statements.  Upon loading a pulse program with the RNMR command `EX`, these loops are initialized with any default
values that were declared in the source code.  To modify or check the current value of a loop, the RNMR commands `LI`
and `LS` may be entered whenever a pulse program is loaded; the acquisition need not be stopped to use these commands.

The first parameter of `LI` is "loop", the number of the loop to be incremented.  If "loop" is not specified on the
command line, RNMR will prompt for a loop number.  If the user presses <RETURN\> at this prompt, RNMR will increment
loop 1.  The legal values for "loop" are integers between 1 and 16, inclusive.  While the pulse programmer supports 32
loops, only the first 16 can be set from RNMR; loops 17 through 32 may be used internally in a pulse program but are not
accessible to RNMR.

The second parameter, "incr.", is the number by which the specified loop is to be incremented. If "incr." is not
specified on the command line, the loop will be incremented by 1; RNMR will not prompt for "incr." if it is omitted.
Legal values for "incr." are positive or negative integers between -32767 and 32767, inclusive.  Note that RNMR will
update the pulse programmer hardware even if "incr." is zero.

Once "loop" and "incr." have been entered, RNMR looks up the current value of the loop and tests that the incremented
value is between zero and 32767, inclusive. If the incremented value would fall outside this range, the loop is not
updated, and RNMR prints the error message:

    (PPLI0 ) VALUE OUT OF BOUNDS

followed by the rejected incremented loop value. If the incremented value falls within the legal range, RNMR updates the
loop in the pulse programmer parameter buffer and prints an informational message such as:

    CURRENT LOOP VALUE = 64

After incrementing a loop with the `LI` command during acquisition, several seconds will usually elapse before the pulse
programmer responds to the change.  However, if the loop value is modified before acquisition is started, the first shot
should reflect the incremented loop setting.  If the incremented loop value is zero, the pulse programmer will simply
skip all instructions within that loop as soon as the hardware is updated.
## LIM
Set display limits

Category: Display Control

Format: `LIM` llim rlim

Defaults: current_display_limits

Description:
`LIM` sets the display limits for the currently visible buffer, as selected by the `VIEW` command.  `LIM` takes two
parameters, "llim" and "rlim", which are the left and right display limits, respectively.  These limits are expressed in
the current unit for the visible buffer (ACQ, PRO, or LCK) with the current maximum number of decimal places for that
unit.  The current unit is set and displayed by the `UNIT` command and the maximum number of decimal places is set and
displayed by `NDEC`.  If "llim" or "rlim" is missing from the command line, RNMR will display the current value for the
missing limit and prompt for a new value.  If the user omits both "llim" and "rlim" on the command line and presses
<RETURN\> when prompted for each limit, RNMR will not update the display; in all other cases, the display will be
updated to reflect the new limits.

For each display limit, the user should enter a value expressed in  the current time or frequency unit or "\*" to select
the leftmost left limit or the rightmost right limit.  If the user requests a display limit to the left of the leftmost
point in the data buffer, the display will begin at the leftmost data point.  Similarly, if the right display limit
specified is beyond the rightmost data point, the display will extend to the rightmost data point.  If the user
specifies an display limit that is within the range of the data buffer but which does not correspond to a specific data
point, RNMR will set that limit to the time or frequency of the closest data point to the right of the value specified.
Note that the command `LIM * *` directs RNMR to set the display limits so that all points in the data buffer are
visible.  Unless display updating has been set off with the `SET DSP` command, RNMR will update the display to show the
data between "llim" and "rlim", whether the user is currently viewing the acquisition or the processing buffer.
## LIMB
Set blocked record display limits

Category: Display Control

Format: `LIMB` rec direc llim rlim

Defaults: current 1 current current

Description:
`LIMB` sets display limits for blocked record
## LP
List buffer parameters

Category: Data Storage

Format: `LP` buf

Defaults: 1

Description:
`LP` prints a summary of processing buffer parameter values on the current printer, as selected with the command
`LPDEV`.  When processing spectrometer data offline, many experimental parameters can only be determined from the `LP`
summary since RNMRP lacks commands to display and set pulse lengths, loop values, and other acquisition parameters.  The
exact format of the `LP` summary varies from spectrometer to spectrometer due to differences in implementation of
RNMR-controlled hardware.  `LP` takes one parameter, "buf", which is the number of the processing buffer whose
parameters will be listed.  This parameter may be set to either 1 or 2. Processing buffer 1 is the visible buffer while
the contents of buffer 2 are not visible on the display.  If "buf" is omitted from the command line, RNMR will list the
parameters of buffer 1; RNMR does not prompt the user for "buf".

If a title has been specified earlier for this buffer (e.g. by a `SA`, `SS`, or `SB` operation), RNMR will use this
title on the printout. At console (\>) level, if no title has been specified,  RNMR will prompt the user for a title
after the `LP` command is entered.  Similarly, an `LP` command in a macro will prompt the user for a missing title if
the `LP` command is followed by the text line operator ";;" as shown below:

    LP
    ;;

If `LP` is issued from a macro without a subsequent ";;" text substitution command, RNMR will use the buffer's current
title on the `LP` printout.  If a new, nonblank title is entered for the `LP` printout and "buf" is currently visible,
RNMR will display the new title at the top of the screen.  Each time `LP` is executed, RNMR opens a new ASCII text file
called `LP`.TMP to store the parameter summary until it can be printed.  If the printing is successful, `LP`.TMP is
deleted on completion of the print job.  If the print job is aborted or otherwise fails to complete successfully, the
`LP`.TMP will remain on disk and may be printed manually.

The following buffer parameters are listed in the `LP` printout:

    CURRENT BUFFER TITLE

RECORD AND BLOCK NUMBER, OWNER, AND DATE
Direction 1 is always indicated by "\*" in the block number display and corresponds to the dimension visible on the
screen for one-dimensional displays.  For example, if record 5 is a two-dimensional blocked record and `DIRB` 2 is
currently 12, the `LP` summary will include the line:

    REC     5     (*    ,   1)

when listing block 1 of record 5.  Conversely, if `DIRB` 2 is set to 21, the summary will include:

    REC     5     (1    ,   * )

to indicate that direction 1 is mapped to dimension 2.  If the record containing the data in buffer "buf" is
onedimensional, no block numbers will be reported.

NUCLEUS
For each synthesizer that has been assigned a nucleus, RNMR lists that nucleus, its Hertz-to-PPM multiplicative factor
(nominal NMR frequency), offset (as set by the F command), and PPM reference frequency.  RNMR also indicates which
synthesizer is mapped to dimension 1 (the observe dimension).  Both the offset and the PPM reference frequency are
reported in Hz to a maximum of one decimal place.  The PPM reference frequency is defined as the frequency in Hz of zero
PPM.

POWER LEVELS
If computer controlled transmitter power has been implemented on the current spectrometer, RNMR will list the power
levels in dB for each channel, as set by the `PWR` command.  Each channel (OBS and DEC) has two independent power
levels (1 and 2), so four power levels will be reported.

RECEIVER GAIN (`GAIN`)
RNMR reports the receiver gain in dB only if S-bus gain control has been implemented on the current spectrometer.

SWEEP WIDTH (`SW`)
The sweep width reported by `LP` is identically equal to 1.0E+06 divided by the hardware dwell time in microseconds.
RNMR reports the sweep width in the current frequency unit (`UNIT /FREQ`) to the current number of decimal places for
that unit (`NDEC`).

FILTER FACTOR (`FLF`)
The filter factor is a measurement of the bandwidth of the audio filters used to acquire the data.  If the filter factor
is 0.0, then the filters were disabled entirely.  Otherwise, they were set to the nearest cutoff setting at least as
wide as FLF X (SW/2.0). If the calculated filter bandwidth exceeds 50000.0 Hz, then the filters were disabled
entirely.  Note that larger values of "factor" give wider filter cutoffs.  If S-bus filter bandwidth control is not
implemented on the current spectrometer, RNMR will always report an `FLF` of 1.0.

ACQUIRED SIZE (`SIZE`)
This parameter is the number of points actually acquired by the spectrometer hardware, regardless of truncation of
extension after executing `GAV`.

ACQUISITION TIME (AT)
The acquisition time is defined as the total length of the FID acquired by the spectrometer hardware and is equal to the
hardware dwell time (`DW`) times the acquired size (`SIZE`).  This value does not reflect any changes in the number of
buffer data points made by truncating or extending the FID after executing `GAV`.  The acquisition time is reported in
seconds to a maximum of 3 decimal places.

 PULSE PROGRAM NAME (`EX`)
This parameter is the name of the pulse program that was loaded when the buffer data was read from the averager with
`GAV`.  When an NMR1-format file is read into a buffer and `LP` is then executed, RNMR will list the NMR1 header
parameter "fdExperimentName" as the pulse program name.

PULSE LENGTHS
In an RNMRP `LP` summary, the first eight pulse lengths (P 1 through P 8) are listed as they were set when the buffer
data was acquired.  Pulses 1 through 4 are listed from left to right on the first line of the pulse length summary,
while the second line lists the values of pulses 5 through 8.  All pulse lengths are reported in microseconds.  An `LP`
summary of pulse lengths in RNMR has a similar format, except that all 16 RNMR-accessible pulses are listed.

DELAY LENGTHS
In an RNMRP `LP` summary, the first eight delay lengths (D 1 through D 8) are listed as they were set when the buffer
data was acquired.  Delays 1 through 4 are listed from left to right on the first line of the delay length summary,
while the second line lists the values of delays 5 through 8.  All delay lengths are reported in milliseconds.  An `LP`
summary of delay lengths in RNMR has a similar format, except that all 16 RNMR-accessible delays are listed.

LOOP VALUES
RNMRP lists the values of loops 1 through 4 (`LS 1` through `LS 4`) from  left to right. RNMR lists all 16 accessible
loop values on the `LP` summary sheet.

PP FLAG STATES
The logical states of pulse programmer flags 1 through 16 (`PPFLG 1` through `PPFLG 16`) are indicated from left to
right on the `LP` summary sheet.  If a particular flag was in the ON state when the buffer data was acquired, it is
marked as "T" on the `LP` summary; if the flag was OFF, it is marked as "F".

DECOUPLER ENABLE STATE (`DEC`)
This parameter indicates whether decoupling was enabled (`DEC ON`)  or disabled (`DEC OFF`) when the buffer data was
acquired.

DECOUPLE FLAG STATES (`DECFLG`)
RNMR reports the state of the four decouple flags (`DECFLG 1` through `DECFLG 4`) from left to right on the `LP` summary
sheet.  By convention, these flags are used in pulse programs to enable or disable decoupling during individual sections
of a pulse sequence, while `DEC` enables or disables all decoupling throughout the sequence.

RECYCLE DELAY (RDLY)

ACQUISITION MODES
The averager acquisition modes (`AMD /ACQ`, or simply `AMD`) are listed so that the number of modes is equal to the
buffer `NAMD /ACQ` value.  That is, regardless of how the `AMD` modes were entered by the user, `NAMD` modes will be
displayed.  These modes represent the sequence of complex numbers by which successive FID's are multiplied before signal
averaging.  For a given experiment, the `AMD` modes are selected so that the desired NMR signal adds constructively from
shot to shot.

BLOCKED ACQUISITION MODES
The blocked acquisition modes (`AMD /BLK`) are listed so that the number of modes is equal to the buffer `NAMD /BLK`
value.  That is, regardless of how the `AMD /BLK` modes were entered by the user, `NAMD /BLK` modes will be displayed.
These modes represent the sequence of complex numbers by which FID's in are multiplied before signal averaging.  For a
given experiment, the `AMD` modes are selected so that the desired NMR signal adds constructively from shot to shot.

 PULSE PROGRAMMER MODES

NUMBER OF DELAY SHOTS (`NDLY`)
This parameter is the number of delay shots taken before the beginning of signal acquisition.  These shots are used to
reach equilibrium when the recycle delay is not long compared to the spin-lattice relaxation time T1.  The delay shots
do not contribute to the time-averaged NMR signal.

NUMBER OF SHOTS TAKEN (NACQ)
NACQ need not be equal to either the `NA` or `NWAIT` settings at the time the data was acquired.  NACQ is the value of
the shot counter when the acquisition was terminated.

CURRENT BUFFER DIMENSION (DIM)
This parameter specifies which dimension of a multidimensional data set is stored in buffer "ibuf".  The buffer
dimension will depend on mapping between directions and dimensions at the time data was written into the buffer.  This
mapping is displayed and modified by the command `DIRB`.

BUFFER DOMAIN (DOM)
The buffer domain parameter is the domain (TIME or FREQ) of the data in buffer "ibuf".  This should agree with the
output of the command `SHOW BUF DOM`.

CURRENT BUFFER SIZE (`SIZE`)
This is the current number of data points in each block of the processing buffer.  Due to truncation operations such as
`XT` and extension operations such as `ZF`, this size may not agree with the acquisition size listed earlier in the `LP`
summary.  The `SIZE` value reported in the summary should agree with the output of the command `SHOW BUF SIZE`.

TIME OR FREQUENCY LIMITS (LLIM and RLIM)
RNMR lists the left and right time or frequency limits for the buffer data in the current unit with the current maximum
number of decimal places for that unit.  These limits pertain to the entire contents of the buffer and may or may not be
equal to the current display limits, as shown by the `LIM` command.

CONSTANT AND LINEAR PHASE FACTORS (PHI0 and PHI1)
The current buffer phasing parameters are reported in degrees.  These parameter may also be displayed by using the `TP`
command.

BUFFER SCALE FACTOR (SF)
This parameter stores the relative intensity of a spectrum, permitting spectra to be presented on an absolute intensity
scale.  The buffer scale factor is also available by using the command `SC`.
## LPA
List acquisition buffer parameters

Category: Acquisition

Format: `LPA`

Prerequisites: RNMR only

Description:
`LPA` prints a summary of acquisition parameter values on the current printer, as selected with the command `LPDEV`.
These parameters are the latest settings of the pulse programmer, averager, and other spectrometer hardware.  The exact
format of the `LPA` summary varies from spectrometer to spectrometer due to differences in implementation of
RNMR-controlled hardware.  If a title has been specified earlier using the `TITLEA` command, RNMR  will use this title
on the printout.  At console (\>) level, if no title has been specified, RNMR will prompt the user for a title after the
`LPA` command is entered.  Similarly, an `LPA` command in a macro will prompt the user for a missing title if the `LPA`
command is followed by the text line operator ";;" as shown below:

    LPA
    ;;

If `LPA` is issued from a macro without a subsequent ";;" text substitution command, RNMR will use the current `TITLEA`
value on the `LPA` printout.  If a new, nonblank title is entered for the `LPA` printout and the acquisition buffer is
currently visible, RNMR will display the new title at the top of the screen.  Each time `LPA` is executed, RNMR opens a
new ASCII text file called `LP`.TMP to store the parameter summary until it can be printed.  If the printing is
successful, `LP`.TMP is deleted on completion of the print job.  If the print job is aborted or otherwise fails to
complete successfully, the `LP`.TMP will remain on disk and may be printed manually.

The following buffer parameters are listed in the `LPA` printout:

CURRENT BUFFER TITLE

USER AND DATE

NUCLEUS
For each synthesizer that has been assigned a nucleus, RNMR lists that nucleus, its Hertz-to-PPM multiplicative factor
(nominal NMR frequency), offset (as set by the F command), and PPM reference frequency.  RNMR also indicates which
synthesizer is mapped to dimension 1 (the observe dimension).  Both the offset and the PPM reference frequency are
reported in Hz to a maximum of one decimal place.  The PPM reference frequency is defined as the frequency in Hz of zero
PPM.

POWER LEVELS
If computer controlled transmitter power has been implemented on the current spectrometer, RNMR will list the power
levels in dB for each channel, as set by the `PWR` command.  Each channel (OBS and `DEC`) has two independent power
levels (1 and 2), so four power levels will be reported.

RECEIVER GAIN (`GAIN`)
RNMR reports the receiver gain in dB only if S-bus gain control has been implemented on the current spectrometer.

SWEEP WIDTH (`SW`)
The sweep width reported by `LPA` is identically equal to 1.0E+06 divided by the hardware dwell time in microseconds.
RNMR reports the sweep width in the current frequency unit (`UNIT /FREQ`) to the current number of decimal places for
that unit (`NDEC`).

FILTER FACTOR (`FLF`)
The filter factor is a measurement of the bandwidth of the  audio filters used to acquire the data.  If the filter
factor is 0.0, then the filters were disabled entirely.  Otherwise, they were set to the nearest cutoff setting at least
as wide as FLF X (SW/2.0).  If the calculated filter bandwidth exceeds 50000.0 Hz, then the filters were disabled
entirely.  Note that larger values of "factor" give wider filter cutoffs.  If S-bus filter bandwidth control is not
implemented on the current spectrometer, RNMR will always report an `FLF` of 1.0.

ACQUIRED SIZE (`SIZE`)
This parameter is the number of points actually acquired by the spectrometer hardware.

ACQUISITION TIME (AT)
The acquisition time is defined as the total length of the FID acquired by the spectrometer hardware and is equal to the
hardware dwell time (`DW`) times the acquired size (`SIZE`). The acquisition time is  reported in seconds to a maximum
of 3 decimal places.

The following parameters are reported by `LPA` only if S-bus lock control has been implemented on the current
spectrometer.

LOCK STATUS (`LCK`)
If the lock was enabled when the `LPA` command was issued, RNMR will report `LCK    = ON`, otherwise the summary will
specify `LCK    = OFF`.

LOCK SWEEP ENABLE STATUS (`SWP`)
If the lock sweep was enabled when the `LPA` command was issued, RNMR  will report "`SWP    = ON`", otherwise the
summary will specify "`SWP    = OFF`".

LOCK POWER (`PWRL`)
RNMR reports the lock power setting in dB to one decimal place.

LOCK RECEIVER GAIN (`GAINL`)
RNMR reports the lock receiver gain setting in dB to one decimal place.

LOCK SWEEP WIDTH (`SWL`)
The lock sweep width is reported on an arbitrary scale from 0 to 100 with a precision of one decimal place.

LOCK POSITION (`POSL`)
The lock position is the frequency of the center of the lock sweep range, expressed as a between -500 and 500 inclusive
and reported to two decimal places.

LOCK RECEIVER PHASE (`PHL`)
The lock receiver phase is adjusted using the `PHL` command to make the lock signal positive and absorptive.  This phase
is reported in degrees with a resolution of +/- 1 degree.

LOCK LEVEL METER LIMITS (MTRMIN and MTRMAX)
MTRMIN and MTRMAX are the minimum and maximum lock level meter settings, measured in percent and reported to one decimal
place.

PULSE PROGRAM NAME (`EX`)
This parameter is the name of the pulse program that was loaded when the `LPA` command was executed.

PULSE LENGTHS
In the `LPA` summary, all 32 pulse lengths are listed, including the  RNMR-accessible pulse lengths (P 1 through P 16)
and the lengths of the internal pulses (numbers 17 through 32).  These pulse lengths are listed in groups of four from
left to right and top to bottom.  All pulse lengths are  reported in microseconds with a precision of 0.1 microseconds.

DELAY LENGTHS
In the `LPA` summary, all 32 delay lengths are listed, including the RNMR-accessible delay lengths (D 1 through D 16)
and the lengths of the internal delays (numbers 17 through 32).  These delay lengths are listed in groups of four from
left to right and top to bottom.  All delay lengths are  reported in milliseconds with a precision of 0.1 milliseconds.

LOOP VALUES
In the `LPA` summary, all 32 loop values are listed, including the RNMR-accessible loop values (`LS` 1 through `LS` 16)
and the values of the internal loops (numbers 17 through 32).  These loop values are listed in groups of four from left
to right and top to bottom.

PP FLAG STATES
The logical states of all 32 pulse programmer flags are indicated from left to right and from top to bottom on the
`LPA` summary sheet.  These include both the flags which may be set with the `PPFLG` command (`PPFLG 1` through
`PPFLG 16`) and the flags which are reserved for use within pulse programs.  If a particular flag was in the ON
state when the `LPA` command was issued, it is marked as "T" on the `LPA` summary; if the flag was OFF, it is marked
as "F".

DECOUPLER ENABLE STATE (`DEC`)
This parameter indicates whether decoupling was enabled (`DEC ON`) or disabled (`DEC OFF`) when the `LPA` command was
issued.

DECOUPLE FLAG STATES (`DECFLG`)
RNMR reports the state of the four decouple flags (`DECFLG 1` through `DECFLG 4`) from left to right on the `LPA`
summary sheet.  By convention, these flags are used in pulse programs to enable or disable decoupling during individual
sections of a pulse sequence, while `DEC` enables or disables all decoupling throughout the sequence.

RECYCLE DELAY (RDLY)

ACQUISITION MODES
The averager acquisition modes (`AMD /ACQ`, or simply `AMD`) are listed so that the number of modes is equal to the
current `NAMD /ACQ` value.  That is, regardless of how the `AMD` modes were entered by the user, `NAMD` modes will be
displayed.  These modes represent the sequence of complex numbers by which successive FID's are multiplied before signal
averaging.  For a given experiment, the `AMD` modes are selected so that the desired NMR signal adds constructively from
shot to shot.

BLOCKED ACQUISITION MODES
The blocked acquisition modes (`AMD /BLK`) are listed so that the number of modes is equal to the buffer `NAMD /BLK`
value.  That is, regardless of how the `AMD` /BLK modes were entered by the user, `NAMD /BLK` modes will be displayed.
These modes represent the sequence of complex numbers by which FID's in are multiplied before signal averaging.  For a
given experiment, the `AMD` modes are selected so that the desired NMR signal adds constructively from shot to shot.

PULSE PROGRAMMER MODES

NUMBER OF SHOTS BETWEEN DISPLAY UPDATES (`NDSP`)
If `NDSP` is zero, the display was not updated during acquisition.  Otherwise, the display was updated once every `NDLY`
shots while acquisition was in progress.

NUMBER OF DELAY SHOTS (`NDLY`)
This parameter is the number of delay shots taken before the beginning of signal acquisition.  These shots are used to
reach equilibrium when the recycle delay is not long compared to the spin-lattice relaxation time T1.  The delay shots
do not contribute to the time-averaged NMR signal.

NUMBER OF SHOTS BETWEEN WAITS (`NWAIT`)
When the `WAIT` command is issued during a signal acquisition, RNMR takes `NWAIT` shots before exiting `WAIT` and
returning control to the user or executing the next line in the current macro.  If the number of shots to acquire (`NA`)
is not -1 and is less than `NWAIT`, or if `NWAIT` is zero, `NA`  shots are taken instead.

NUMBER OF SHOTS TO ACQUIRE (`NA`)
When acquisition is started with `DG`, `ZG`, `NG`, or `GO`, acquisition will be terminated automatically after `NA`
shots have been acquired.  The acquisition may be terminated earlier by a subsequent `QUIT` or `ABORT` command.

NUMBER OF SHOTS TAKEN (NACQ)
NACQ need not be equal to either the `NA` or `NWAIT` settings at the time the data was acquired. NACQ is the value of
the shot counter when the acquisition was terminated.
## LPB
Perform backward linear prediction on FID

Category: Data Manipulation

Format: `LPB` irlim nmm m

Defaults: 1 MIN((ISIZE-IRLIM)/4,8) (ISIZE-IRLIM)-NMM

Prerequisites: Time domain data in processing buffer 1 (TIME)

Description:
`LPB` performs backwards linear prediction.  Based on the specified number of current data points, `LPB` calculates the
values of the FID at earlier times.  In a linear prediction calculation, the FID is modeled as the sum of a finite
number of exponentially damped complex sine waves with different intensities, phases, and damping factors.  Determining
the best fit for the parameters of these components is done by diagonalizing a matrix of numbers with dimension N-M by
N-M, where N-M is the number of components and M is the number of data points to fit.  The elements of the diagonalized
matrix are then used to calculate the complex intensities of a small number of points at the beginning of the FID.
`LPB` replaces these points with their calculated values, leaving the total number of points in the FID constant.  By
using backward linear prediction, one may correct FID data points which were corrupted by probe or filter ring-down.
`LPB` operates only on the data in the visible processing buffer (buffer 1).  The user need not be viewing this buffer
to use `LPB`.

The first parameter of `LPB`, "irlim", is the point number of the  rightmost point to be updated by linear prediction.
`LPB` will replace data points 1 through "irlim" with values calculated from a certain number of the remaining points.
If "irlim" is not specified on the command line, RNMR will correct only the leftmost point of the FID; the default value
of "irlim" is 1 and RNMR will not prompt for "irlim" if it is omitted.  Legal values for "irlim" are positive integers
from 1 to one-eighth (1/8) the number of points in the FID.

The second parameter, "nmm", is the number of spectral components to be used in the linear prediction calculation, N-M.
This parameter also determines the size of the matrix that RNMR must diagonalize in order to calculate the intensities
of points 1 through "irlim".  Thus, larger values of "nmm" will result in much longer calculation times.  If "nmm" is
not specified on the command line, RNMR will set "nmm" to either the largest integer less than or equal to
(ISIZE-IRLIM)/4 or to 8, whichever is smaller.  For example, if "irlim" was set to its default value of 1 and the size
of the FID is 512, the default value of "nmm" will be 8.  Conversely, if "irlim" is 1 and there are only 32 points in
the FID, "nmm" will default to MIN((32-1)/4,8)=MIN(7,8)=7.  When "nmm" is omitted, RNMR uses the default value without
prompting the user. Legal values of "nmm" are positive integers from 1 to 32.  Consequently, the maximum size of the
matrix to be diagonalized in the linear prediction algorithm is 32.

The third parameter, "m", is the number of points to the right of each predicted point that will be used in the linear
prediction calculation.  That is, "m" determines the number of data points that `LPB` must fit. For example, if "irlim"
is 2, point 2 will be calculated from the complex intensities of points 3 through 2+M, and point 1 will be calculated
from points 2 through 1+M, using the predicted value of point 2.  If "m" is omitted from the command line, RNMR sets "m"
to ISIZE-IRLIM-NMM where ISIZE is the number of data points in the FID; RNMR does not prompt for a value for "m" if one
was not supplied on the command line.  Legal values of "m" are positive integers greater than or equal to "nmm" such
that NMM+M is less than or equal to ISIZE-IRLIM.  That is, the number of data points to fit must be at least the number
of components (to ensure a unique fit) and N must be no greater than the number of points NOT replaced by `LPB`.
Once the values of "irlim", "nmm", and "m" have been selected, `LPB` performs backward linear prediction
on each block of buffer 1 independently. The following algorithm is used for each block:

1.	RNMR multiples the matrix X by its transpose, where X is defined by:

        X(I,J)=DATA(I+J), I=1,2,...,NMM, J=1,2,...,M

2.	The resulting matrix, (X)\*(XT) is diagonalized to give its eigenvalues and eigenvectors.

3.	RNMR counts the number of nonzero eigenvalues, yielding the rank of the diagonalized matrix.  An eigenvalue is
considered nonzero if it is greater than NMM\*LAMBDA(NMM)/10000, where NMM is the number of spectral components in the
fit and LAMBDA is the vector of eigenvalues returned by the diagonalization routine.  The rank of the diagonalized
matrix is an integer between zero and NMM.

4.	A vector is constructed with length equal to the rank determined in step 3.  This vector is equal to the product:

        (TEMP1)=(LAMBDA^-1)*(UT)*(DATA)
where LAMBDA^-1 is the inverse of the vector of eigenvalues of rank NMM-RANK+1 to NMM and UT is the transpose of the
eigenvector matrix.

5.	The vector calculated in step 4 is used to compute an NMM-element vector:

        (TEMP2)=(U)*(LAMBDA^-1)*(UT)*(DATA)               =(U)*(TEMP1)

6.	The linear prediction coefficients are calculated by multiplying the conjugate of the data vector DATA with the
vector TEMP2.  These coefficients are factors by which the first M data points to the right of each predicted point are
multiplied and summed to give the data points 1 through IRLIM.

7.	Starting with the rightmost data point to be predicted, IRLIM, RNMR calculates data points IRLIM to 1 by summing the
products of the linear prediction coefficients with the first M points to the right of the point to be predicted.  As
each point is calculated, from left to right, the updated data is used to calculate the next point, u0ntil the first
data point in the buffer has been updated.  Thus, each point from IRLIM to 1 is calculated from the coefficient vector
computed in step 6 and the first M points to the right of that point.

If the processing buffer is currently visible, RNMR will update the display to show the data as updated by `LPB`.
## LPC
Perform long pulse phase and amplitude correction

Category: Data Manipulation

Format: `LPC` flip fnull

Defaults: 90.0 FNYQ

Prerequisites: Frequency domain data in processing buffer 1 (FREQ)

Description:
`LPC` performs a long pulse correction apodization, correcting both the amplitude and phase of the spectrum.  This
apodization is intended to alleviate distortions caused by incomplete excitation of the spectrum by weak pulses.  `LPC`
operates only on data in the visible processing buffer (buffer 1).  The user need not be viewing this buffer to use
`LPC`.

The first argument of `LPC` is "flip", the on-resonance flip angle of  the pulse used to excite the spectrum.  If this
parameter is not specified on the command line, RNMR will prompt for a flip angle with a default of 90 degrees.
Legal values for "flip" are real numbers greater than zero and  less than or equal to 90 degrees.
The second parameter, "fnull", is the frequency of the first null in the RF excitation, which is also a measure of the
RF field strength.  This frequency should be expressed in the current frequency units, which may be Hz, kHz, MHz, or
PPM.  If the user does not specify "fnull" on the command line, RNMR will prompt for a null frequency.  The default
value for this frequency is the offset frequency minus the Nyquist frequency  (FNYQ = 0.5\*SW); the offset frequency
is defined as the frequency of the carrier in the current unit and is zero unless this unit is PPM and the buffer has
been assigned to synthesizer 1 through 4. Legal values for "fnull" are real numbers that satisfy:

    2.0 .GE. RATIO .GE. 0.1

where RATIO is defined by:

    RATIO = ABS(FNULL-OFFSET)/FNYQ

That is, after subtracting any offset, the magnitude of "fnull" may be from 10% to 200% of the Nyquist frequency. Note
that if the user accepts  the default value of "fnull", the above condition is always satisfied.  For each data point in
the first block of processing buffer 1,
## LPCA
Perform long pulse amplitude correction

Category: Data Manipulation

Format: `LPCA` flip fnull

Defaults: 90.0 FNYQ

Prerequisites: FREQ

Description:
Performs amplitude portion of long pulse correction. flip is flip angle on resonance, fnull is null frequency.
## LPCP
Perform long pulse phase correction

Category: Data Manipulation

Format: `LPCP` flip fnull

Defaults: 90.0 FNYQ

Prerequisites: FREQ

Description:
Performs phase portion of long pulse correction. flip is flip angle on resonance, fnull is null frequency.
## LPDEV
Select text printer device

Category: Printing

Format: `LPDEV` device

Defaults: current

Description:
`LPDEV` selects the printer to be used for text output from the commands `LP`, `LPA`, `LPK`, `LPK2D`.  The choice of
printers is the same for each spectrometer, but each spectrometer may be assigned a different default  printer when RNMR
is initialized.  The file RNMR:[RNMR]CFGQUE.DAT contains a list of all printers that may be selected by `LPDEV`.  The
"LPDEV" parameter in the file RNMR:[RNMR]CFGTBL.DAT sets the default print device  at RNMR startup time.

`LPDEV` takes one parameter, "device", which is the name of the print device to be selected for all subsequent text
printing.  If this argument is missing from the command line, RNMR will prompt for a device with the current print
device as the default.  This default will be the device assigned to the current spectrometer in CFGTBL.DAT unless the
print device has been modified by an earlier `LPDEV` command in the current RNMR or RNMRP session.  The legal choices of
text printer device are currently:

Device Name | Printer | Location
----------- | ------- | --------
LJ3 | HP LJ3 | 4119
LJ4 | HP LJ4 | 5119
LJ5 | HP LJ5 | 0249

## LPF
Perform forward linear prediction on FID

Category: Data Manipulation

Format: `LPF` irlim nmm m

Defaults: ISIZE+1 MIN(ISIZE/4,8) ISIZE-NMM

Prerequisites: Time domain data in processing buffer 1 (TIME)

Description:
`LPF` performs forward linear prediction.  Based on a specified number of current data points, `LPF` calculates the
values of the FID at later times.  In a linear prediction calculation, the FID is modeled as the sum of a finite number
of exponentially damped complex sine waves with different intensities, phases, and damping factors.  Determining the
best fit for the parameters of these components is done by diagonalizing a matrix of numbers with dimension NM by N-M,
where N-M is the number of components and M is the number of data points to fit.  The elements of the diagonalized
matrix are then used to calculate the complex intensities of points to be added to the end of the FID, increasing the
total number of points in the buffer.  Unlike `LPB`, forward linear prediction does not modify the values of any of the
original data points.  By using `LPF`, one may decrease the number of data points in a given dimension that must be
acquired to avoid truncation errors.  This ability is particularly useful in obtaining multidimensional data sets since
the number of slices that must be physically acquired, and thus the spectrometer time required, is reduced.  For
well-behaved FID's, the number of data points may often be doubled with forward linear prediction.  `LPF` operates only
on the data in the visible processing buffer (buffer 1). The user need not be viewing this buffer to use `LPF`.

The first parameter of `LPF`, "irlim", is the number of points desired after linear prediction.  `LPF` will calculate
points SIZE+1 through "irlim" based on a specified number of points in the original FID.  If "irlim" is not specified
on the command line, `LPF` will predict only one point at the end of the FID, increasing the number of data points by
one. Note that RNMR will not prompt for "irlim" if it is omitted.  Legal values of "irlim" are positive integers from
SIZE to SIZEA, where SIZE is the number of points in the current FID, as displayed by the command `SHOW BUF SIZE`
and SIZEA is the number of points allocated in buffer 1, as displayed and set by `DBSZ`.

The second parameter, "nmm", is the number of spectral components to be used in the linear prediction calculation, N-M.
This parameter also determines the size of the matrix that RNMR must diagonalize in order to calculate the intensities
of points SIZE+1 through "irlim".  Thus, larger values of "nmm" will result in much longer calculation times.  If
"nmm" is not specified on the command line, RNMR will set "nmm" to either the largest integer less than or equal to
SIZE/4 or to 8, whichever is smaller.  For example, if there are currently 512 points in the FID, the default value of
"nmm" will be 8.  Conversely, if there are only 16 points in the FID, then "nmm" will default to MIN(4,8)=4.  When "nmm"
is omitted, RNMR uses the default value without prompting the user.  Legal values of "nmm" are positive integers from 1
to 32.  Consequently, the maximum size of the matrix to be diagonalized in the linear prediction algorithm is 32.

The third parameter, "m", is the number of points to the left of each predicted point that will be used in the linear
prediction calculation.  That is, "m" determines the number of data points that `LPF` must fit.  For example, if "irlim"
is 514 and SIZE is 512, point 513 will be calculated from the complex intensities of points 513-M through 512, and
point 514 will be calculated from points 514-M through 513, using the predicted value of point 513.  If "m" is omitted
from the command line, RNMR sets "m" to SIZE-NMM where SIZE is the number of data points in the FID and NMM is the
value for the N-M parameter described above; RNMR does not prompt for a value for "m" if one was not supplied on the
command line.  Legal values of "m" are positive integers greater than or equal to "nmm" such that NMM+M is less than or
equal to the current size.  That is, the number of data points to fit must be at least the number of components (to
ensure a unique fit) and N must be no greater than the current number of points in the FID.

Once the values of "irlim", "nmm", and "m" have been selected, `LPF` performs forward linear prediction on each block of
buffer 1 independently.  The following algorithm is used for each block:

1.	RNMR multiples the matrix X by its transpose, where X is defined by:

        X(I,J)=DATA(I+M-J), I=1,2,...,NMM                            J=1,2,...,M

2.	The resulting matrix, (X)\*(XT) is diagonalized to give its eigenvalues and eigenvectors.

3.	RNMR counts the number of nonzero eigenvalues, yielding the rank of the diagonalized matrix.  An eigenvalue is
considered nonzero if it is greater than NMM\*LAMBDA(NMM)/10000, where NMM is the number of spectral components in the
fit and LAMBDA is the vector of eigenvalues returned by the diagonalization routine.  The rank of the diagonalized
matrix is an integer between zero and NMM.

4.	A vector is constructed with length equal to the rank determined in step 3. This vector is equal to the product:

        (TEMP1)=(LAMBDA^-1)*(UT)*(DATA)
where LAMBDA^-1 is the inverse of the vector of eigenvalues of rank NMM-RANK+1 to NMM and UT is the transpose of the
eigenvector matrix.

5.	The vector calculated in step 4 is used to compute an NMM-element vector:

        (TEMP2)=(U)*(LAMBDA^-1)*(UT)*(DATA)
               =(U)*(TEMP1)

6.	The linear prediction coefficients are calculated by multiplying the conjugate of the data vector DATA with the
vector TEMP2. These coefficients are factors by which the data points at the end of the FID are multiplied and summed to
give the data points SIZE+1 through IRLIM.

7.	Starting with the leftmost data point to be predicted, SIZE+1, RNMR calculates data points SIZE+1 to IRLIM by
summing the products of the linear prediction coefficients with the first M points to the left of the point to be
predicted. As each point is calculated, from right to left, the updated data is used to calculate the next point, until
point IRLIM has been calculated. Thus, each point from SIZE+1 to IRLIM is calculated from the coefficient vector
computed in step 6 and the first M points to the left of that point.

If the processing buffer is currently visible, RNMR will update the display to show the data as extended by `LPF`. `LPF`
increases the active size of buffer 1 to IRLIM.
## LPK
List Peaks

Category: Printing

Format: `LPK`

Description:
`LPK` prints a list of peak positions and intensities for the first 50 peaks within the current display limits (`LIM`)
above the current peak pick threshold (`TH`).  The peak list is printed on the current text output device, as selected
by the command `LPDEV`.  `LPK` only lists peaks within the current display limits for the data in processing buffer 1.
Recall that buffer 1 is the visible buffer, while the data in buffer 2 cannot be viewed directly.  The user need not be
viewing the processing buffer to use `LPK`.  If a title has been specified earlier for this buffer (e.g. by a `SA`,
`SS`, or `SB` operation), RNMR will use this title on the printout.  At console (\>) level, if no title has been
specified,  RNMR will prompt the user for a title after the `LPK` command is entered.  Similarly, an `LPK` command in a
macro will prompt the user for a missing title if the `LPK` command is followed by the text line operator ";;" as shown
below:

    LPK
    ;;

If `LPK` is issued from a macro without a subsequent ";;" text substitution command, RNMR will use the buffer's current
title on the `LPK` printout.  If a new, nonblank title is entered for the `LPK` printout and "buf" is currently visible,
RNMR will display the new title at the top of the screen.

Each time `LPK` is executed, RNMR opens a new ASCII text file called LPK.TMP to store the peak summary until it can be
printed. If the printing is successful, `LPK`.TMP is deleted on completion of the print job.  If the print job is
aborted or otherwise fails to complete successfully, the LPK.TMP will remain on disk and may be printed manually.

`LPK` lists peaks in the real part of the data in processing buffer 1 unless the user has selected the imaginary part by
entering `BUF IMAG`.  Peaks are located and listed only for the first block of buffer 1 between the current display
limits, as set and displayed by the `LIM` command.
To abort the peak listing in progress, the user may press <CTRL-Z\> or "Q" at any time before the console prompt ("\>")
is returned.  If the user aborts `LPK` before the first peak is located, then no listing will be printed.  Otherwise,
RNMR will print a listing of all the peaks it found prior to the interrupt.

`LPK` uses the following algorithm to find peaks within the current display limits:

1.	Starting with the first point to right of the left cursor and proceeding to the last point to the left of the right
cursor, `LPK` examines each visible point in processing buffer 1.  Consequently, neither of the current cursor positions
can be a peak.

2.	RNMR examines the intensities of the two points on either side of the current point and decides whether the current
point is a peak.  If I is the intensity of the test point and IL and IR are the intensities of the first points to the
left and right of the test point, respectively, then the test point is a peak if:

        (ABS(I) .GT. IL) .AND. (ABS(I) .GE. IR)      .AND. (ABS(I) .GE. TH)   if I .GE. 0
    or

        (ABS(I) .GT. -IL) .AND. (ABS(I) .GE. -IR)      .AND. (ABS(I) .GE. TH)   if I .LT. 0
where `TH` is the current peak pick threshold, as set and displayed by the command `TH`.  That is, for a positive point
to be a peak, its intensity must be greater than or equal to the peak pick threshold, greater than the intensity of the
adjacent point on the left, and greater than or equal to the intensity of the point on the right.  Conversely, for a
negative point to be a peak, its intensity must be less than or equal to the negative of the peak pick threshold, less
than the intensity of the first point to the left, and less than or equal to the intensity of the first point to the
right.

3.	For each peak found, RNMR writes a line to `LP`.TMP.  The first column in the `LPK` printout will specify the peak
number, starting at one for the leftmost peak.  If the current unit is PPM, the second column of the `LPK` printout will
list the peak position in PPM while the third column will list this position in the current default frequency unit, as
set by the command `UNIT /FREQ /DFLT`.  If the current unit is not PPM, the second column will list the peak
position in the current unit while the third column will specify "--------" for each peak. RNMR will list all peak
positions with the maximum number of decimal places currently set for the appropriate units at RNMR startup time or as
modified by the `NDEC` command.  The fourth column of the `LPK` printout specifies the peak height for each peak,
reported to a maximum of 3 decimal places.

4.	RNMR stops listing peaks after finding the first 50 peaks or after testing the next to the last point currently
displayed. If no peaks were found, an error message is displayed:

        (LPK   ) NO PEAKS
In this case, RNMR does not print a peak list.  Conversely, if more  than 50 peaks were found, RNMR displays the
message:

        (LPK   ) TOO MANY PEAKS
along with the number of peaks actually found between the display limits.  When this occurs, RNMR prints a listing of
the first 50 peaks from left to right and does not list the remaining peaks.

Each `LPK` printout begins with a header which includes the buffer title, record and block numbers, record owner, and
date, as well as titles for each column specifying the domain (time or frequency) and units for the peak data to follow.
 When reading the record and block number at the top of the `LPK` printout, note that direction 1 is always indicated by
"\*" in the block number display and corresponds to the dimension visible on the screen for onedimensional displays.
For example, if buffer 1 contains data from record 5, which is two-dimensional, and `DIRB` 2 is currently 12, the `LPK`
summary will include the line:

        REC     5       (*    ,   1)

when listing the peaks in block 1 of record 5.  Conversely, if `DIRB` 2 is set  to 21, the summary will include:

    REC     5       (1    ,   * )

to indicate that direction 1 is mapped to dimension 2.  If buffer 1 contains data from a one-dimensional record, RNMR
will not list any block numbers.

Wherever possible, `LPK` lists peak positions and intensities as floating point numbers with the maximum number of
decimal places: 3 for intensity and "ndec" for peak position, where "ndec" is the value returned by the `NDEC` command
for the appropriate time or frequency unit.  However, when a time, frequency or intensity value is too large or too
small to represent with this number of decimal places, RNMR will begin to drop decimal places to fit the number into an
8-character field.  If RNMR cannot write the number into an eight character field after dropping all decimal places
(`NDEC 0`), the number will be written in scientific notation.
## LPK2D
List peaks in two dimensions

Category: Printing

Format: `LPK2D` rec blk

Defaults: current 1

Description:
`LPK2D` prints a list of peak positions and intensities for the first 250 peaks found within a 2D slice of a blocked
record above the current peak pick threshold (`TH`).  By setting `CONMD` to POS, NEG, or ABS beforehand, the user may
modify the selection of 2D peaks for a given threshold value.  Only peaks within the current display limits (as set and
shown by the command `LIMB`) will be listed by `LPK2D`.  The peak list is printed on the current text output device, as
selected by the command `LPDEV`.

The first argument of `LPK2D`, "rec", is the record number of a blocked  record of dimension 2 or higher with NDIMX at
least 2.  Note that NDIMX is the number of dimensions that may be simultaneously accessed and is a unchangeable
characteristic of a blocked record set when that record is allocated.  If a value for NDIMX is not specified on the
command line, RNMR will prompt for a record number.  If the user presses <RETURN\> at this prompt, RNMR will locate and
list peaks for the current record number, as set and displayed by the command `PTRA`.  Since none of the scratch records
hold two-dimensional data, the legal values for "rec" are integers between 5 and 200.  The record number specified must
belong to a nonempty blocked record.

The second parameter, "blk", specifies the block of record "rec" to list.  This block number is used to select
twodimensional slices from a three or four-dimensional blocked record.  If record "rec" contains two-dimensional data,
"blk" should be 1.  For a three dimensional record, "blk" selects a plane from the data cube and may be set to any
integer value from 1 to SIZE3 where SIZE3 is the size in the dimension mapped to direction 3 by the `DIRB` command.  If
"rec" has four dimensions, values of "blk" from 1 to SIZE3 select planes with minimum height in the fourth direction,
blocks SIZE3+1 to 2\*SIZE3 select planes from the second cube of the 4D hypercube, and so forth.  Thus, by incrementing
"blk" from 1 to SIZE3\*SIZE4, one may select all the data in a 4D data set one plane at a time.  If "iblk" is not
specified, `LPK2D` will list two dimensional peaks in the first plane of record "rec"; RNMR will not prompt for "iblk".
Legal values of "iblk" are integers greater than or equal to zero. If "iblk" is zero, RNMR will list the peaks in the
next 2D slice of record "rec", where the current slice number is set and displayed by the command `PTRB` "rec".

Before locating the peaks within the current display limits for the selected slice, RNMR checks several parameters.
First, RNMR verifies that record "rec" has at least two dimensions. If the record is one dimensional, RNMR warns of this
condition by displaying an error message:

    (CVTBBX) TOO FEW DIMENSIONS

Note that `LPK2D` does not require NDIMX greater than one for record "rec" since the peak picking algorithm only
requires slices of the data along the first direction.  The block number specified by "iblk" must not be greater than
the total number of allocated blocks in record "rec". If "iblk" is out of bounds, RNMR will display an error message:

    (CVTBBX) BLOCK OUT OF BOUNDS

Similarly, if not all of the allocated blocks have been used, RNMR further requires that "iblk" be a nonempty block of
record "rec". If "iblk" is less than or equal to the number of allocated blocks in record "rec" but is greater than the
number of blocks actually used, RNMR will return an error message:

    (INI2DX) BLOCK OUT OF BOUNDS

Note that this may happen when `LPK2D` is called repeatedly with "iblk" equal to zero to find all 2D peaks in a 3D or 4D
record; after the last slice has been processed, all subsequent attempts to execute `LPK2D` will give the block out of
bounds error until the block pointer is reset with `PTRB`.  If "iblk" is left at its default value of one, the user
should not encounter this error, even if record "rec" contains no data.  To check the number of blocks allocated and
used for record "rec", use the command `SIZEB` "rec". If record "rec" is empty, RNMR will display the error message:

    (INI2DX) DIMENSION EMPTY

The user must ensure not only that NDIM for record "rec" is at least two but also that the record can be accessed for
two dimensional processing with the current `DIRB` mapping. If the NDIMX parameter was set  equal to the number of
dimensions when the record was allocated, then this is guaranteed. However, if NDIMX is less than the number of
dimensions in the record, not all choices of `DIRB` will allow peak listing with `LPK2D`. If `DIRB` is not set to a
legal value for processing record "rec", RNMR will yield the error message:

    (INI2DX) DIMENSION INACCESSIBLE

followed by the number of the inaccessible dimension.  The available choices for `DIRB` will depend on the NDIMX value
with which the record was allocated; `ALLB` always maps directions 1,2,3, and 4 to dimensions 1,2,3, and 4 respectively,
regardless of the `DIRB` setting at allocation time.  For example, if a three dimensional record was allocated with
NDIMX 2, the user will be able to list 2D peaks in planes of the data cube with `DIRB 3` set to 123, 132, 213, or 231
but not 312 or 321.  That is, any `DIRB` setting beginning with 1 or 2 is acceptable but 3 may not be used since the
third dimension is not accessible.  Similarly, for 4D records allocated with NDIMX 2, `DIRB 4` may be any sequence
beginning with 1 or 2 and if NDIMX was 3, the `DIRB` sequence may begin with 1, 2, or 3.  Thus, the legal choices of
`DIRB` are those in which the first direction is accessible (the accessible directions for a given blocked record are
those mapped to dimensions 1,2,...,NDIMX).

When `LPK2D` is used to examine a new archive record, RNMR updates the current record pointer to "rec".  The value of
this pointer may be set or shown using the command `PTRA`.  Similarly, RNMR updates the `PTRB` block pointer to indicate
the block of record "rec" being processed by `LPK2D`.  Thus, multiple calls to `LPK2D` with "iblk" equal to zero result
in listing 2D peaks in successive planes of a 3D or 4D record since RNMR updates the block pointer with each call.  The
following macro code example uses this technique to generate 2D peak listings for each plane of a 3-dimensional record.

    ! LIST ALL 2D PEAKS AT EACH HEIGHT OF A 3D DATA SET    (RECORD 29)
    DIRB 3 123         ! SET DIRECTION FOR BLOCKED ACCESS
    SET IMSG OFF 1 2   ! GET SIZE OF DIMENSION 3 (#BLKS USED)
    SIZEB 29 3
    SET IMSG ON
    PTRB 29 0 >         ! SET READ POINTER TO FIRST BLOCK
    SETIDN BLOCK 	      ! CURRENT BLOCK NUMBER WILL BE PRINTED TO SCREEN
    DO /IDN /LCL 1,%2,BLK2D  ! LIST PEAKS IN EACH 2D SLICE
    LPK2D 29 &BLK2D
    ENDDO

The `LPK2D` peak listing sheets will be printed in order from the bottom slice to the top slice of the 3D data cube.
Note that neither the current record or block numbers are stored on disk, so they will be set back to zero the next time
an RNMR or RNMRP session is initiated.  In order to remind the user of which dimensions in record "rec" will be searched
for 2D peaks, RNMR displays the dimensions assigned to directions 1 and 2 as two informational messages.  For example,
if record "rec" has two dimensions and `DIRB 2` is 12, RNMR will display:

    DIR 1 =        1
    DIR 2 =        2

RNMR limits the number of points in direction 1 to a maximum of 4096. To check the direction 1 size of a blocked record
"rec", enter the command `SIZEB "rec" 1`.  `LPK2D` lists 2D peaks in the real part of record "rec" unless the user has
selected the imaginary part by entering "`BUF` IMAG".  Peaks are located and listed only for the region of the data
within the current display limits, as set and displayed by the `LIMB` command.
To abort the peak listing in progress, the user may press <CTRL-Z\> or "Q" at any time before the console prompt is
returned.  If the user aborts `LPK2D` before the first peak is located, then no listing will be printed. Otherwise, RNMR
will print a listing of all the peaks it found prior to the interrupt.  Each time `LPK2D` is executed, RNMR opens a new
ASCII text file called `LP`.TMP to store the peak summary until it can be printed.  If the printing is successful,
`LP`.TMP is deleted on completion of the print job.  If the print job is aborted or otherwise fails to complete
successfully, the `LP`.TMP will remain on disk and may be printed manually.  `LPK2D` uses the following algorithm to
find peaks within the current display limits:

1.	Each slice from the first slice above the bottom display limit to the last slice below the top display limit is
examined sequentially.  For each of these slices, RNMR examines the data points starting with the first point  to the
right of the left display limit and proceeding to the last point to the left of the right display limit.  Consequently,
no point lying on the current left, right, top, or bottom cursors can be a point.

2.	RNMR examines the intensities of the four points above, below, to the left, and to the right of each point in the
search region described above.  If the current contour mode setting is positive (`CONMD POS`), then RNMR tests the
actual intensity of the current point, TEST=I.  If the `CONMD` setting is negative (NEG) then the negative of the data
point is tested, TEST=-I.  Finally, if the contour mode is currently set to absolute (`CONMD ABS`), RNMR examines the
absolute value of the data point, TEST=ABS(I).

3.	The test value, TEST, is compared to the current peak pick threshold, as set and displayed by the command `TH`.  If
TEST is less than the peak pick threshold, the current point is not listed as a peak and RNMR proceeds to the next point
to the right or to the next slice upward in search of 2D peaks.  Note that the current `CONMD` setting modifies the
effect of the peak pick threshold.  For `CONMD POS`, the intensity of a point must be greater than or equal to the
threshold for that point to be a peak, but for `CONMD` NEG, the intensity must be less than or equal to minus the
threshold.

4.	If the original value of the current point, I, is positive or zero, that point will be listed as a peak if:

        (I .GT. L) .AND. (I .GE. R) .AND. (I .GT. D) .AND. (I .GE. U)
where L, R, D, and U are the intensities of the nearest points to the left, right, below, and above the current point.
The real or imaginary part of each intensity will be used according to the current `BUF` setting.  Conversely, if the
original value of the current point is  negative, the current point will be listed as a peak if:

        (I .GT. -L) .AND. (I .GE. -R) .AND. (I .GT. -D) .AND. (I .GE. -U)
where L, R, D, and U are the intensities of the nearest points to the left, right, below, and above the current point.
The real or imaginary part of each intensity will be used according to the current `BUF` setting.

5.	For each peak found, RNMR writes a line to LP.TMP.  The first column in the `LPK2D` printout will specify the peak
number, starting at one for the leftmost, bottom peak.  If the current unit in direction 1 is PPM, the second column of
the `LPK2D` printout will list the peak position in PPM while the third column will list this position in the current
default frequency unit, as set by the command `UNIT /DFLT`.  If the direction 1 unit is not PPM, the second column
will list the peak position in the current unit while the third column will specify "--------" for each peak.
Similarly, columns 4 and 5 will contain the peak position along direction 2 in current and default units, respectively.
Again, if the current unit for direction 2 is not PPM, column 5 will specify "--------" for each peak.  Note that the
command `UNIT /DIM2 /DFLT` sets and displays the fallback unit RNMR will use if `UNIT /DIM2` is PPM.  RNMR will list
all peak positions with the maximum number of decimal places currently set for the appropriate units at RNMR startup
time or as modified by the `NDEC` command.  The sixth column of the `LPK2D` printout specifies the peak height for each
peak, reported to a maximum of 3 decimal places.

6.  RNMR stops listing peaks after finding the first 250 peaks or after testing the last point in the search range
described above.  If no peaks were found, an error message is displayed:

    (LPK2D   ) NO PEAKS
In this case, RNMR does not print a peak list.  Conversely, if more  than 250 peaks were found, RNMR displays the
message:

    (LPK2D   ) TOO MANY PEAKS
along with the number of peaks actually found between the display limits.  When this occurs, RNMR prints a listing of
the first 250 peaks from left to right, bottom to top, and does not list the remaining peaks.

Each `LPK2D` printout begins with a header which includes the buffer title, record and block numbers, record owner, and
date, as well as titles for each column specifying the domain (time or frequency) in each direction and units for the
peak data to follow.  When reading the record and block number at the top of the `LPK2D` printout, note that directions
1 and 2 are always indicated by "\*" in the block number display and correspond to the dimensions searched for peaks by
`LPK2D`. For example, if record 5 has three dimensions and `DIRB 3` is currently 123, the `LPK2D` summary will include
the line:

    REC     5       (*    ,*    ,1)

when listing the peaks in block 1 of record 5. Conversely, if `DIRB 3` is set  to 321, the summary will include:

    REC     5       (1    ,*    ,* )

to indicate that direction 3 is mapped to dimension 1.  If record "rec" has only two dimensions, RNMR will not display
any block numbers.  Wherever possible, `LPK2D` lists peak positions and intensities as  floating point numbers with the
maximum number of decimal places: 3 for  intensity and "ndec" for peak position, where "ndec" is the value returned by
the `NDEC` command for the appropriate time or frequency unit.  However, when a time, frequency or intensity value is
too large or too small to represent with this number of decimal places, RNMR will begin to drop decimal places to fit
the number into an 8-character field.  If RNMR cannot write the number into an eight character field after dropping all
decimal places (`NDEC 0`), the number will be written in scientific notation.
## LS
Set pulse programmer loop value

Category: Acquisition

Format: `LS` loop val

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD) RNMR only

Description:
`LS` sets the value of a specified pulse program loop counter.  Pulse program loops are specified in the PP source code
by LOOP statements and assigned default values by DEF statements.  Upon loading a pulse program with the RNMR command
`EX`, these loops are initialized with any default values that were declared in the PP source code.  To modify or check
the current value of a loop, the RNMR commands `LS` and `LI` may be entered whenever a pulse program is loaded; the
acquisition need not be stopped to use these commands.

The first parameter of `LS` is "loop", the number of the loop to be set.  If "loop" is not specified on the command
line, RNMR will prompt for a loop number. If the user presses <RETURN\> at this prompt, RNMR will select loop 1.  The
legal values for "loop" are integers between 1 and 16, inclusive.  While the pulse programmer supports 32 loops, only
the first 16 can be set from RNMR; loops 17 through 32 may be used internally in a pulse program but are not accessible
to RNMR.

The second parameter, "val", is the value to which the specified loop will be set.  If "val" is not specified on the
command line, RNMR will prompt for a loop value with the current value as the default.  That is, entering `LS` without a
loop value "val" will display the current value of that loop.  Legal values for "val" are positive integers between 0
and 32767, inclusive.  Note that RNMR will update the pulse programmer hardware unless the user omits "val" on the
command line and  presses <RETURN\> at the loop value prompt, even if the user entered the  current value for the
selected loop.

Once "loop" and "val" have been entered, RNMR updates the loop in  the pulse programmer parameter buffer   After
adjusting a loop with the `LS` command during acquisition, several seconds will usually elapse before the pulse
programmer responds to the change.  However, if the loop value is modified before acquisition is started, the first shot
should reflect the new loop setting.  If the new loop value is zero, the pulse programmer will simply skip all
instructions within that loop as soon as the hardware is updated.
## LSTD
Define global list

Category: Lists

Format: `LSTD` list

Defaults:

Description: 1
Creates global list. There are 4 lists available.
## LSTDP
Define global list using Processing Display

Category: Lists

Format: `LSTDP` list#

Defaults: 1

Prerequisites: PRO

Description:
Creates global list of time or freq values. There are 4 lists available

Subcommands:

Command | Description
------- | -----------
CR      | Terminate
B       | Move to bottom of list
C       | Display current entry
D       | Delete entry
I       | Insert entry
L       | Display last entry
N       | Display next entry
Q       | Terminate
T       | Move to top of list
Z       | Call `ZO`

## LSTE
Edit global list

Category: Lists

Format: `LSTE` list#

Defaults: 1

Description:
Edit global list.

Subcommands:

Command | Description
------- | -----------
CR      | Terminate
B       | Move to bottom of list
C       | Display current entry
D       | Delete entry
I       | Insert entry
L       | Display last entry
N       | Display next entry
Q       | Terminate
R       | Replace entry
T       | Move to top of list

## LSTL
List global list

Category: Lists

Format: `LSTL` list#

Defaults:

Description:
Lists global list.
## LW
Calculate line width 	              1

Category: Data Analysis

Format: `LW` left_lim right_lim pcnt_ht

Defaults: left_cur right_cur 50

Description:
Obtains width of line at specified height in the current unit.  If arguments are not specified, they will be prompted
for.  Only the first peak (above threshold) encountered, going from left to right, will be evaluated.

# M
---
## MAG
Calculate magnitude of data

Category: Data Manipulation

Format: `MAG`

Description:
Obtains magnitude of data.

    MAG = SQRT(REAL^2 + IMAG^2)
## MAPN
Append text to macro

Category: Macro

Format: `MAPN` macnam

Defaults: TEMP

Description:
Appends text to end of macro.
## MAXV
Calculate maximum

Category: Data Manipulation

Format: `MAXV` src# dst#

Defaults: 2 1

Description:
Obtains maximum of complex source buffer and complex destination buffer:

    DST = MAX(DST,SRC)

Comparison is based on magnitudes.
## MCPY
Copy macro

Category: Macro

Format: `MCPY` macnam1 macnam2

Defaults:

Description:
Copies macro. 	                TEMP    TEMP
## MD
Define macro

Category: Macro

Format: `MD` macnam

Defaults:

Description:
Defines macro.
## MDL
Delete macro 	            TEMP

Category: Macro

Format: `MDL` macnam

Defaults:

Description:
Deletes macro.
## MDMP
Dump macro 	             TEMP

Category: Macro

Format: `MDMP` filnam

Defaults: TEMP

Description:
Dumps macro instructions to file in current directory.  File type will be TXT.
## ME
Edit macro

Category: Macro

Format: `ME` macnam

Defaults:

Description:
Edits macro. 	            TEMP

Subcommands:

Command | Description
------- | -----------
CR      | Terminate
B       | Move to bottom of macro
C       | Display current line
D       | Delete line
I       | Insert line
L       | Display last line
N       | Display next line
Q       | Terminate
R       | Replace line
T       | Move to top of macro

## MEDBF
Median baseline fix spectrum

Category: Data Manipulation

Format: `MEDBF` window std_dev

Defaults: 70 5.0

Description:
Baseline fix spectrum based on algorithm presented by M. Friedrichs, J. Biomol. NMR 5 147-153 (1995)  The algorithm
tracks the baseline by calculating, at each point, the median of the extrema within a certain window size set by the
argument window.  This set of median values is then convoluted with a Gaussian of standard deviation given by the
argument std_dev.  These final values are then subtracted from the data values.  The values of the window and the
standard deviation are both in terms of points, rather than the current units.  The user will be prompted for both
values if they are not given.

The success of this method depends on proper choice of the window size.  The window should be chosen such that the
number of local extrema arising from noise dominates the median statistic.  If the window is too small and the number of
signal peaks in a given window is comparable to the number of noise peaks, the algorithm will be biased upwards and
attempt to bring the signals down to the baseline.  On the other hand, if the window is too large, the baseline will not
reflect the local baseline structure.  Likewise, the standard deviation should be chosen such that it is not too large
and thus broadening out the local correction over too wide a region.  The user should be careful in the use of this
algorithm in cases where zero filling before Fourier transformation has taken place, since such a procedure in effect
increases the number of points between noise extrema.  Zero filling to sizes 4 or more times the acquired FID are cause
for caution.
## MEXIT
Exit macro

Category: Macro

Format: `MEXIT`

Description:
Performs unconditional exit from current macro.  All remaining repeats are cancelled.
## MINV
Calculates minimum

Category: Data Manipulation

Format: `MINV` src# dst#

Defaults: 2 1

Description:
Obtains minimum of complex source buffer and complex destination buffer.

        DST = MIN(DST,SRC)

Comparison is based on magnitudes.
## ML
List macro

Category: Macro

Format: `ML` macnam

Defaults:

Description:
Lists macro.
## MLOA
Load macro 	           TEMP

Category: Macro

Format: `MLOA` filename

Defaults: TEMP

Description:
Loads macro instructions from file in current directory.  File type must be TXT.  File can contain one or more macro
definitions.
## MNMX
Calculate minimum and maximum

Category: Data Analysis

Format: `MNMX` gbl#1 gbl#2

Defaults: 0 0

Description:
Finds minimum and maximum values of displayed data and saves in gbl#1 and gbl#2 respectively.  0 gbl# causes no
transfer.
## MO
Exit

Category: Misc.

Format: `MO`

Prerequisites: HALT

Description:
Terminates program.
## MOVV
Move buffer

Category: Data Manipulation

Format: `MOVV` src# dst#

Defaults: 2 1

Description:
Moves complex source buffer to complex destination buffer.  DST = SRC
## MRN
Rename macro

Category: Macro

Format: `MRN` macnam1 macnam2

Defaults:

Description:
Renames macro.
## MTR
Set lock meter limits 	             TEMP    TEMP

Category: Lock

Format: `MTR` minlim maxlim

Defaults: current current

Description:
Sets lock meter limits.  Minimum limit is 0.0.  Maximum limit is 100.0.
## MULV
Multiply buffer

Category: Data Manipulation

Format: `MULV` src# dst#

Defaults: 2 1

Description:
Real multiplies complex destination buffer by complex source buffer.

        REAL(DST) = REAL(DST) * REAL(SRC)
        IMAG(DST) = IMAG(DST) * IMAG(SRC)
## MXEQ
Macro execute

Category:

Format: `MXEQ`

Defaults:

# N
---
## NA
Set number of shots to acquire

Category: Acquisition

Format: `NA` `NA`

Defaults: current

Description:
Sets maximum number of shots to acquire.
## NABLK
Set number of acquisition blocks

Category: Acquisition

Format: `NABLK` nablk

Defaults: current

Description:
Sets number of acquisition blocks. `NABLK` 0 indicates maximum possible  number of acquisition blocks.
## NAMD
Set number of acquisition modes

Category: Acquisition

Format: `NAMD` namd

Defaults: current

Description:
Sets number of acquisition and pulse program modes to use, i.e. the length of the phase cycle.
## NCON
Set number of contour levels

Category: `ZO2DC`

Format: `NCON` [qual] ncon
	Qualifiers: 	/LIN    /LOG
 	Qualifier defaults:        current (originally /LOG)

Defaults: current

Description:
Sets number of contour levels.  Contour level spacing is determined by qualifiers.
## NDEC
Set number of decimal places

Category: Misc.

Format: `NDEC` unit ndec

Defaults: current current

Description:
Sets number of decimal places to be displayed for unit.
## NDLY
Set number of shots to discard

Category: Acquisition

Format: `NDLY` ndly

Defaults: current

Description:
Sets number of shots to discard before acquiring.
## NDSP
Set number of shots between display update

Category: Acquisition

Format: `NDSP` ndsp

Defaults: current

Description:
Sets number of shots to acquire before display update.
## NG
Continue acquisition

Category: Acquisition

Format: `NG` ndly `NA`

Defaults: current current

Prerequisites: LOAD HALT

Description:
Continues acquisition after delay.
## NOP
Null operation

Category: Misc.

Format: `NOP`

Description:
Performs null operation.
## NORM
Set scale to normalize display

Category: Display Control

Format: `NORM`

Description:
Normalizes data so that largest peak within display limits has magnitude 1.0.
## NUC
Set synthesizer nucleus

Category: Acquisition

Format: `NUC` syn# nucnam

Defaults: current current

Prerequisites: HALT

Description:
Sets synthesizer nucleus.
## NUCD
Define nucleus table entry

Category: Nuclei

Format: `NUCD` nucnam MHz ref

Defaults: none 1.0 0.0

Description:
Defines or modifies nucleus table entry.  MHz is nucleus frequency in MHz.. ref is nucleus reference frequency in
current units.  If nucleus table entry does not exist first set of defaults applies, else second set.
## NUCDL
Delete nucleus table entry

Category: Nuclei

Format: `NUCDL` nucnam

Description:
Deletes nucleus table entry.
## NWAIT
Set number of shots to wait

Category: Acquisition

Format: `NWAIT` nwait

Defaults: current

Description:
Sets number of shots to wait before `WAIT` is satisfied. nwait = 0 indicates na.

# O
---
## OFF
Set offset from reference frequency

Category: Acquisition

Format: `OFF` syn# off

Defaults: current current

Description:
Defines nucleus reference frequency by assigning value to synthesizer offset frequency.  The nucleus reference frequency
modified is that associated with the processing buffer synthesizer.
## OFFA
Set offset from reference frequency

Category: Acquisition

Format: `OFFA` syn# off

Defaults: current current

Description:
Defines nucleus reference frequency by assigning value to synthesizer offset frequency.  The nucleus reference frequency
modified is that associated with the acquisition buffer synthesizer.
## ONERR
Set macro error handler

Category: Macro

Format: `ONERR` label

Defaults: no default

Prerequisites: Macro only (MAC)

Description:
Specifies a statement label to which a macro will jump in the event of an error condition or control-z.
## OPNARV
Open archive

Category: Data Storage

Format: `OPNARV` [qual] archive name
	Qualifiers: 	 	   /RD /WRT
Qualifier defaults: 	 	   /RD   	Defaults : 	 	               1     TEMP

Description:
Opens an archive with access specified by the qualifiers /RD and /WRT.
## OPNB
Open block parameters

Category:

Format:

Defaults:
## OPNDSP
Open display

Category: `OPNB`

Format:

Defaults:
## OPNPLT
Open plot stream 	`OPNDSP`

Category: Printing

Format:

Description: `OPNPLT`
Opens plotter file.  All plots between `OPNPLT` and `CLSPLT` will appear on one sheet of paper.
## OPNRD
Open file stream for reading

Category: File IO

Format: `OPNRD` filename
Default : 	             TEMP Description:
`OPNRD` opens an ASCII file for read-only access by the command `RDWRT`.
## OPNWRT
Open file stream for writing

Category: File IO

Format: `OPNWRT` filename

Defaults: DATA

Description:
Opens `WRT` file.  The file type will be WRT. All write commands between `OPNWRT` and `CLSWRT` will appear in one
file.

# P
---
## P
Set pulse length

Category: Acquisition

Format: `P` pls# usec

Defaults: 1 current

Prerequisites: LOAD

Description:
Sets pulse time in usec.
## PADJ
Interactively adjust pulse length

Category: Acquisition

Format: `PADJ` pls#

Defaults: 1

Prerequisites: ACQ LOAD

Description:
Sets pulse time in usec after prompt.
## PARB
Set blocked record parameters

Category: Blocked Records

Format: `PARB` rec# dir dim dom syn first step

Defaults: irrec 1 current current current current current

Description:
Sets parameters for blocked record.
## PC
Incremental phase correction

Category: Data Manipulation

Format: `PC` dphi0 dphi1

Defaults: 0 0

Description:
Performs incremental phase correction.
## PEN
Select plot pen

Category: Printing

Format: `PEN` pen#

Defaults: current

Description:
Selects pen for plotting.  For laser plotters, pen#=1 selects a thin line and pen#=2 selects a thick line.
## PGSIZE
Set page size for plot

Category: Printing

Format: `PGSIZE` xsiz ysiz

Defaults: current current

Description:
Sets plotter page size in inches.  Plot size is reset to maximum.
## PH
Interactive phase correction

Category: Data Manipulation

Format: `PH`

Description:
Performs interactive phase correction.

Subcommands:

Command | Description
------- | -----------
CR | Terminate with current phase values
C  | Select constant value for change
D  | Select decrement direction
I  | Select increment direction
L  | Select linear value for change
P  | Select current cursor position as pivot for linear value
Q  | Terminate with original phase values
V  | Change phase value after prompt
Z  | Call `ZO`

## PHL
Interactive lock channel phase correction

Category: Lock

Format: `PHL`

Prerequisites: LCK

Description:
Performs interactive lock channel phase correction.

Subcommands:

Command | Description
------- | -----------
CR | Terminate with current phase values
D  | Select decrement direction
I  | Select increment direction
Q  | Terminate with original phase values
V  | Change phase value after prompt

## PLDEV
Select plotting device

Category: Printing

Format: `PLDEV` device

Defaults: current

Description:
Sets plotter device.  The legal choices of plotter device are currently:

Device Name | Printer | Location
----------- | ------- | --------
LJ3 | HP LJ3 | 4119
LJ4 | HP LJ4 | 5119
LJ5 | HP LJ5 | 0249

## PLOT
Plot current 1D display

Category: Printing

Format: `PLOT`

Description:
Plots current display. Q and <CNTL-Z\> will abort plot.
## PLOTC
Plot contour display

Category: Printing

Format: `PLOTC` rec#

Defaults: current

Description:
Plots two-dimensional contour display.  Q and <CNTL-Z\> will abort plot.
## PLSIZE
Set plot size

Category: Printing

Format: `PLSIZE` xsiz ysiz

Defaults: current current

Description:
Sets plot size in inches.
## POSL
Set lock channel center position

Category: Lock

Format: `POSL` pos

Defaults: current

Description:
Sets lock channel center position.  Minimum position is -50.0.  Maximum position is 50.0.
## PPFLG
Set state of pulse program flag

Category: Acquisition

Format: `PPFLG` flag# state

Defaults: 1 current

Prerequisites: LOAD HALT

Description:
Sets state of specified pulse program flag.  State may be ON or OFF.  There are 16 flags available.
## PPMD
Set pulse program phase mode

Category: Acquisition

Format: `PPMD` gate# spec1 spec2 ... spec8

Defaults: 1 none none ... none

Prerequisites: HALT

Description:
Sets phase of pulse program gate for acquisition. Each spec can specify 1,2,4 or 8 modes.  Each mode is an integer from
1 to 4.  The meaning of the mode is determined by the definition of the pulse program.  The total number of modes
specified must be a power of 2, .le. 64.  Modes entered are replicated to define full set of 64 modes.  If no modes are
entered current modes are printed, 16 at a time.
## PROF
Calculate profile of blocked 2D record

Category: Data Manipulation

Format: `PROF` rec#

Defaults: current

Description:
The profile of a blocked record is obtained.  Each point of the result is the maximum of all corresponding points in the
blocks.  Comparison is based on magnitudes.
## PROFB
Calculate profile of blocked 3D or 4D record

Category: Data Manipulation

Format: `PROFB`

Defaults:
## PROJ
Calculate projection of blocked 2D record

Category: Data Manipulation

Format: `PROJ` rec#

Defaults: current

Description:
The projection of a blocked record is obtained.  Each point of the result is the sum of all corresponding points in the
blocks.
## PROJB
Calculate projection of blocked 3D or 4D record

Category: Data Manipulation

Format: `PROJB`
## PRTARG
Print arguments

Category: Misc.

Format: `PRTARG` arg1 arg2 ... arg10

Defaults: none none none

Description:
The specified arguments are printed.
## PS
Set phase

Category: Data Manipulation

Format: `PS` phi0 phi1

Defaults: cur_gbl cur_gbl

Description:
Performs phase correction to specified phase values.
## PSX
Set acquisition transmitter phase

Category: Acquisition

Format: `PSX` ichan ipsx phase

Defaults: 1 current current

Description:
Sets acquisition transmitter phase.
## PSXEX
Load transmitter phase program from PAM memory

Category:

Format: `PSXEX`

Defaults:
## PTRA
Set read and write archive pointers

Category: Data Storage

Format: `PTRA` read_rec# write_rec#

Defaults: current current

Description:
Sets "current" archive record.
## PTRB
Set read and write blocked record pointers

Category: Blocked Record

Format: `PTRB` rec# rblk# wblk#

Defaults: current 0 0

Description:
Sets pointers to indicate last block in blocked record read and written.
         	blk#    =0      indicates start of record          	blk#    =-1     indicates no change
## PWR
Set transmitter coarse power level

Category: Acquisition

Format: `PWR` chan index db

Defaults: 1 1 current

Description:
Sets observe or decouple channel transmitter relative power level in decibels.  The allowed values for index are 1 (for
high power values) and 2 (for low power values).  The range of db is 70.0 to 100.0 in increments of 10.0.
## PWXEX
Load power program  	Category:

Format: `PWXEX`

Defaults:
## PWRL
Set lock channel power level

Category: Lock

Format: `PWRL` dB

Defaults: current

Description:
Sets lock channel transmitter relative power level in decibels.  The maximum power is 100.0 db.
## PWX
Set transmitter fine power level

Category: Acquisition

Format: `PWR` chan index db

Defaults: 1 1 current

Description:
Sets observe or decouple channel transmitter relative power level in decibels.  The index value corresponds to a
specified level used in the command SETPWX in the pulse program.  The maximum power is 100.0 db.

# Q
---
## QC
Perform software quadrature phase correction

Category: Data Manipulation

Format: `QC`

Prerequisites: TIME

Description:
Software quadrature phase detection is performed.  The cross correlation coefficient between the real and imaginary
buffers is obtained and the appropriate fraction of the imaginary buffer subtracted from the real buffer.
## QUIT
Quit acquisition

Category: Acquisition

Format: `QUIT`

Description:
Halts acquisition after next complete cycle.

Subcommands:
   	Q       Halt after next shot.

# R
---
## RCVMIX
Set receiver quadrature mixing

Category:

Format: `RCVMIX`

Defaults:

Description: Staff only!
## RCVOFF
Set receiver offset

Category:

Format: `RCVOFF`

Defaults:

Description: Staff only!
## RD
Set recycle delay

Category: Acquisition

Format: `RD` sec

Defaults: current

Prerequisites: HALT


Description:
Sets pulse program recycle delay in seconds.
## RDWRT
Read `WRT` file opened by `OPNRD`

Category: File IO

Format: `RDWRT` arg1 arg2 arg3 ...

Defaults: none

Qualifiers:

Qulaifier | Description
--------- | -----------
/EOF=label | jump to (label) if end-of-file detected
/ERR=label | jump to (label) on error
/GBL | transfer tokens to global arguments
/LCL | transfer tokens to local arguments (default)

Description:
Reads a record from a file opened by `OPNRD`.  Tokens are transferred to arguments arg1, arg2, arg3, etc.  `RDWRT`
accepts spaces, commas, or tabs as token delimiters in a record.  Multiple qualifiers may be specified.  Qualifiers /EOF
and /ERR may only be used in a macro.  Labels specified with /EOF and /ERR are checked for syntax but not for existence
when the `RDWRT` command is issued.  If qualifier /EOF is not specified with a label, then an end-of-file condition will
produce an error.  Similarly, an unhandled read error will give an RNMR error message.  Note that the comment characters
";" and "!" will be removed  from the record before its tokens are transferred into local or global arguments.
## REF
Set reference frequency

Category: Frequency Control

Format: `REF` nucnam ref

Defaults: current current

Description:
Sets processing buffer nucleus reference frequency.  ref is nucleus reference frequency in current units.
## REFA
Set reference frequency for acquisition buffer

Category: Acquisition

Format: `REFA` nucnam ref

Defaults: current current

Description:
Sets acquisition buffer nucleus reference frequency.  ref is nucleus reference frequency in current units.
## RGPIB
Read string from GPIB device

Category: Hardware

Format: `RGPIB` device

Defaults: no default

Description:
Reads string from GPIB device.
## RMS
Calculate root-mean-square value of data

Category: Data Analysis

Format: `RMS` llim rlim

Defaults: current current

Description:
Computes root-mean-square value of specified region.
## ROT
Rotate spectrum

Category:

Format: `ROT`

Defaults:
## RPPSB
Read data byte from pulse programmer spectrometer bus

Category: Hardware

Format: `RPPSB` iadr

Default : 	              0

Prerequisites: Pulse programmer spectrometer bus control implemented (CGFSB2).

Description:
`RPPSB` reads a data byte from the pulse programmer spectrometer bus.
## RSB
Read data byte from spectrometer bus

Category: Hardware

Format: `RSB` addr

Defaults: 0

Description:
Reads data byte from specified spectrometer bus address.
## RSTLCK
Restore lock values from file

Category: Lock

Format: `RSTLCK` file-name

Defaults: TEMP

Prerequisites: Spectrometer configured for RNMR lock control

Description:
Restores lock values from a file.
## RSTSHM
Restore shim values from file

Category: Shim

Format: `RSTSHM` file-name

Defaults: TEMP

Prerequisites: Spectrometer configured for RNMR shim control

Description:
Restores shim values from a file.
## RWDRD
Rewind `WRT` file opened by `OPNRD`

Category: File IO

Format: `RWDRD`

Description:
Rewinds a file opened by the `OPNRD` command.
## RWDWRT
Rewind `WRT` file opened by `OPNRD`

Category: File IO

Format: `RWDWRT`

Description:
Rewinds a file opened by the `OPNWRT` command.

# S
---
## SA
Save data to archive record

Category: Data Storage

Format: `SA` rec# buf#

Defaults: next 1

Description:
Writes data to archive record from buffer.
## SAV
Save data and parameters to averager

Category: Acquisition

Format: `SAV` buf#

Prerequisites: TIME HALT

Description:
Transfers buffer data and parameters to averager.
## SAVARV
Save archive

Category: Data Storage

Format: `SAVARV` archive

Defaults: 1

Description:
Saves any changes made to the specified archive to the file containing that archive.
## SAVLCK
Save lock values to file

Category: Lock

Format: `SAVLCK` file-name

Defaults: TEMP

Prerequisites: Spectrometer configured for RNMR lock control

Description:
Saves lock values to a file.
## SAVSHM
Save shim values to file

Category: Shim

Format: `SAVSHM` file-name

Defaults: TEMP

Prerequisites: Spectrometer configured for RNMR shim control

Description:
Saves shim values in a file.
## SB
Save data to blocked record

Category: Blocked Record

Format: `SB` rec# blk# buf#

Defaults: current next 1

Description:
Writes data to block of blocked record from buffer.
## SC
Scale data

Category: Data Manipulation

Format: `SC` sf

Defaults: 1.0

Description:
Scales data by specified scale factor.
## SET
Set system state

Category: Misc.

Format: `SET` flgnam ...

Description:
Sets state of system flag. Arguments may be one of the following:

Flag | Description
---- | -----------
AUTOZ  | Sets state of background hardware auto-shimming routine. State my be ON or OFF. Z1 is optimized based on the lock level.
DSP    | Sets state of display enable flag. State may be ON or OFF. Flag is set on when lowest console level is reached.
IMSG   | Sets state of informational message flag.  State may be ON or OFF. Flag is set on when lowest console level is reached. If flag is off any values which would have been printed by the message are transferred to successive global arguments beginning with gbl#1 and ending with gbl#2, if gbl#1 and gbl#2 are nonzero.
LCKMTR | Sets state of lock meter display.  State may be ON or OFF. The lock meter is displayed as both graphically (a horizontal bar which monitors the lock level) and numerically.
TIMER  | Sets state of timer. State may be ON or OFF. An informational message is written when timer is set to OFF.
TRACE  | Sets state of DEBUG trace enable flag.  State may be ON or OFF. Flag is set off when lowest console level is reached. If flag is on each macro line will be listed before being executed.

System flags DSP, IMSG, EMSG,

Each system flag is stored within RNMR as via counters that are incremented or decremented by the `SET` commands.  For
each function (IMSG, EMSG, DSP, etc.) there are two counters: one for console level and one for all macro levels.  The
console counter is initialized with the value 1 when RNMR starts up and its current value becomes the macro counter
level whenever a macro is called.  `SET` commands at console level increment or decrement the appropriate console
counter, while `SET` commands within a macro level increment or decrement the macro counter.  When an event (such as a
display update or an error or informational message) is processed, RNMR takes action according to the current value of
the counter at the current command level.
## SETIDN
Set identification values

Category: Data Storage

Format: `SETIDN` idn1 idn2

Defaults: none none

Description:
Sets display identification section values.  The display identification section is the upper left corner of the display.
idn=\* indicates no change.
## SETV
Set data values between limits

Category: Data Manipulation

Format: `SETV` llim rlim valr vali

Defaults: current display 0.0 0.0 Qualifiers: /REAL (default) /IMAG (default)

Description:
`SETV` sets data values for all points in a specified region of an FID or spectrum to a given complex number.
## SETVP
Set data values for specified points

Category: Data Manipulation

Format: `SETV` llim npt valr vali

Defaults: current display 0.0 0.0
Qualifiers: 	/REAL (default)       /IMAG (default) Description:
`SETVP` sets data values for all points in a specified region of an FID or spectrum to a given complex number.  The
region to be modified begins at "llim" and is "npt" points long.
## SG
Start acquisition without accumulation

Category: Acquisition

Format: `SG`

Prerequisites: LOAD HALT

Description:
Starts acquisition with no accumulation of data.
## SHFT
Shift data

Category: Data Manipulation

Format: `SHFT` shft

Defaults: dstep

Description:
Shifts data left or right specified amount with zero filling.
         	shft    <0      indicates right shift          	shft    \>0      indicates left shift
## SHM
Set shim values

Category: Shim

Format: `SHM` shim-name value

Defaults: Z1 current

Prerequisites: Spectrometer configured for RNMR shim control

Description:
Sets the value of a particular shim.
## SHOW
Show information

Category: Misc.

Format: `SHOW` option
Default : 	              `BUF`

Description:
`SHOW` shows information on various RNMR entities.  At present, the only option available is BUF; `SHOW BUF`
displays various attributes of the visible processing buffer.
## SINEB
Perform Sine-bell apodization

Category: Data Manipulation

Format: `SINEB` factor time

Defaults: 0.0 (size+1)\*step

Prerequisites: TIME


Description:
Performs sine-bell apodization.  The phase of the initial point of the apodization function is defined by:

    PHI=ATAN2(factor,1.0-factor^2)

time is the time value at which the apodization function becomes zero.
## SIZE
Set acquisition size

Category: Acquisition

Format: `SIZE` size

Defaults: current

Prerequisites: HALT

Description:
Sets size of acquisition in points. size must be a power of 2 less than or equal to 8192.
## SIZEB
Displays size of blocked record

Category: Blocked Record

Format: `SIZEB` rec#

Defaults: current

Description:
Displays size information for blocked record.  The information returned is as follows:

Value | Description
----- | -----------
NBLKA | Number of blocks allocated
NBLK  | Number of blocks actually used
SIZEA | Allocated size of a block in points
SIZE  | Actual size of a block in points

## SP
Display archive space information

Category: Data Storage

Format: `SP` [qual] archive type
	Qualifiers: 	         /SYSTEM /USER
Qualifier defaults:         /USER

Defaults: 1 FREE

Description:
Lists archive space information.

 /SYSTEM qualifier refers to largest possible archive.  /USER qualifier refers to current archive.

type may be one of the following:

Type | Description
---- | -----------
FREE | Free space in blocks
MAX  | Largest free space in blocks
TITLE | Free titles
TOTAL | Total size of archive in blocks
USED | Used space in blocks

## SPAWN
Spawn subprocess

Category: Pipe OS

Format: `SPAWN`

Description:
Spawns subprocess to execute `DCL` commands. Enter LOGOUT at `DCL` prompt to return to RNMR.
## SPLN
Perform cubic spline correction

Category: Data Manipulation

Format: `SPLN` list#

Defaults: 1

Prerequisites: FREQ

Description:
Performs cubic spline baseline correction.  Specified list contains knot positions from left to right.
## SQZ
Squeeze archive (de-allocate unused space)

Category: Data Storage

Format: `SQZ`

Description:
Squeezes archive.  All unused space in the archive is removed.
## SRFLG
Set spectrum reverse flag

Category: Misc.

Format: `SRFLG` syn# state

Defaults: current current

Description:
Sets state of specified spectrum reverse flag.  State may be ON or OFF.
## SS
Save data to scratch record

Category: Data Storage

Format: `SS` rec# buf#

Defaults: 1 1

Description:
Writes buffer to scratch record.
## SSA
Save data to averager scratch record

Category: Acquisition

Format: `SSA` rec# buf#

Defaults: 1 1

Description:
Writes buffer to averager scratch record.
## STK
Add to plot stream stack

Category: Printing

Format: `STK`

Description:
Stack plots current display.
## STKOFF
Set stack plot offset

Category: Printing

Format: `STKOFF` xoff yoff

Defaults: current current

Description:
Sets plotter stack offset values in inches.
## SUBV
Subtract data buffers

Category: Data Manipulation

Format: `SUBV` src# dst#

Defaults: 2 1

Description:
Subtracts complex source buffer from complex destination buffer.        DST = DST - SRC
## SW
Set sweep width

Category: Acquisition

Format: `SW` freq.

Defaults: current

Prerequisites: HALT

Description:
Sets total sweep width for acquisition.
## SWL
Set lock channel sweep width

Category: Lock

Format: `SWL` width

Defaults: current

Description:
Sets lock channel total sweep width.  Maximum sweep width is 1000.0.
## SWP
Enable or disable lock sweep

Category: Lock

Format: `SWP` state

Defaults: current

Description:
Sets state of lock channel sweep.  State may be ON or OFF.
## SYM2D
Symmetrize 2D data set

Category: Data Manipulation

Format: `SYM2D` rec#

Defaults: current

Description:
Symmetrizes 2D data in blocked record.  Record must be square.  Symmetrization is performed with `MINV` function.

# T
---
## TALARM
Set temperature for probe heater alarm

Category: Heater

Format: `TALARM` temperature

Defaults: current

Prerequisites: Spectrometer configured for RNMR heater control

Description:
Sets heater alarm temperature.
## TCL
Set lock channel time constant

Category: Lock

Format: `TCL` tc
	Default : 	        current

Prerequisites: RNMR lock channel control implemented (CFGLK)

Description:
`TCL` sets the lock channel time constant.
## TH
Set threshold for peak selection

Category: Display Control

Format: `TH` val

Defaults: current

Description:
Sets threshold value for peak selection.
## TILT
Tilt blocked record

Category: Data Manipulation

Format: `TILT` rec# tfctr

Defaults: current 1.0

Description:
Tilts blocked record by 0.0 to 45.0 degrees. tfctr is fraction of 45 degree tilt.  Blocked record must be frequency
domain in both dimensions and the middle block must have frequency 0.0.
## TITLE
Set title

Category: Data Storage

Format: `TITLE` buf#

Defaults: 1

Description:
Changes processing buffer title.
## TITLEA
Set acquisition title

Category: Acquisition

Format: `TITLEA`

Description:
Changes acquisition buffer title.
## TM
Perform trapezoidal multiplication apodization

Category: Data Manipulation

Format: `TM` lfract rfract

Defaults: 0.0 0.0

Description:
Performs trapazoidal multiplication apodization.  lfract selects the leftmost fraction of the data to be multiplied by a
linearly increasing function from 0.0 to 1.0.  rfract selects the rightmost fraction of the data to be multiplied by a
linearly decreasing function from 1.0 to 0.0.
## TP
Show phase correction values

Category: Display Control

Format: `TP`

Description:
Lists current phase correction values.
## TPPI
Convert TPP`-format FID to complex FID

Category: Foreign

Format: `TPPI`

Prerequisites: Time domain data in processing buffer 1 (TIME)

Description:
`TPPI` converts a TPPI-format FID to a complex FID.
## TSET
Set heater set-point temperature

Category: Heater

Format: `TSET` temperature

Defaults: current

Prerequisites: Spectrometer configured for RNMR temperature control

Description:
Sets desired heater temperature.
## TST
Conditionally execute a block of commands based on a test

Category: Macro

Format: `TST` [qual] name args...

Qualifiers: /TRUE /FALSE

Qualifier defaults: /TRUE

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`TST` begins a `TST` block which is then ended by `ENDTST` and may optionally contain an `ELSTST` command. `TST` checks
a condition and then either runs the commands between `TST` and `ELSTST` or the commands between `ELSTST` and `ENDTST`.
It is good practice to indent these commands in order to improve readability. `TST` accepts a qualifier which is /TRUE
by default and a name which determines what type of test `TST` performs. This is followed by a variable number of
parameters depending on which type of test is being performed. Certain tests will also accept additional qualifiers,
which should be specified after name.

When the qualifier is /TRUE, `TST` will run the commands between `TST` and `ELSTST` if the test returns true and the
commands between `ELSTST` and `ENDTST` if it returns false. /FALSE reverses this behaviour. /FALSE is mostly useful when
you only have one set of commands that you want to execute commands when the test is false. For example, the following:

    tst lcl a
      msg "The value of a is &a"
    elstst
      msg "local argument a does not exist"
    endtst

will test if local argument a exists and then either print its value or the fact that it does not exist.

The following tests are available in both RNMRA and RNMRP:

Test Name | Description | Parameters | Default | Qualifiers | Default
--------- | ----------- | ---------- | ------- | ---------- | -------
ARV       | Checks archive | ARV | 1 | /VALID, /RD, /WRT, /CLS | /RD
CND       | Checks condition flag | CND | 1 | None | None
REC       | Checks record | REC | IRREC | /RD, /WRT, /SCR, /PERM, /VALID, /NOALLOC, /ALLOC, /ARC, /BLK | /RD, /ALLOC
FIL       | Checks for existence of file | NAM | None | None | None
RD        | Checks for file open for `RDWRT` command | None | None | None | None
WRT       | Checks for file open for `WRT` command  | None | None | None | None
ASKYN     | Checks for yes/no response | PRMPT | 'Enter response:' | /NO, /YES | /NO
DFLT      | Tests arg for explicit default | ARG | None | None | None
EQ        | Compares two args for equality | ARG1, ARG2 | None, None | /FLT, /INT, /LOG, /NUM, /STR, /CASE, /NOCASE, /PAD, /NOPAD | /INT, /STR, /NOCASE, /PAD
FLG       | Checks flag | NAM | None | None | None
GBL       | Checks for existence of global argument | NAM | None | None | None
LAB       | Checks for existence of label | LAB | None | None | None
LCL       | Checks for existence of local ARGUMENT | NAM | None | /LEV=<ilev> | /LEV=1
LIM       | Checks numeric value is within limits |  VAL,LIM1,LIM2 | \* , \* , \* | /FLT, /INT | /INT
LST       | Checks for existence of list | NAM | None | None | None
MAC       | Checks for existence of macro | NAM | None | None | None
SYM       | Checks for existence of symbol | NAM | None | None | None
TBL       | Checks for existence of user name table | TBL | None | None | None
TBLARG    | Checks for existence of user name table argument | TBL, NAM | None, None | None | None

The following tests are available in RNMRA but not in RNMRP:

Test Name | Description | Parameters | Default | Qualifiers | Default
--------- | ----------- | ---------- | ------- | ---------- | -------
CFG       | Checks for existence of subsystem | NAM | None | None | None
PPS       | Checks for existence of pp symbol | TYP, NAM | None, None | None | None
SIG       | Checks for signal | NAM | None | None | None

The flags for `TST ARV` have the following meanings:

Flag | Description
---- | -----------
/VALID | Check for validity of the archive number
/RD | Check for write access
/WRT | Check for read access
/CLS | Check if the archive is closed

The flags for `TST REC` have the following meanings:

Flag | Description
---- | -----------
/RD | Check for write access
/WRT | Check for read access
/SCR | Check if it is a scratch record written using `SS`
/PERM | Check if it is a permanent record
/VALID | Check for validity of the record number
/NOALLOC | Check if it has not been allocated
/ALLOC | Check if it has been allocated
/ARC | Check if it is a non-blocked record written with `SA`
/BLK | Check if it is a blocked record written using `SB`

The flags for `TST ASKYN` have the following meanings:

Flag | Description
---- | -----------
/NO  | Default value of the prompt is NO
/YES  | Default value of the prompt is YES

The flags for `TST EQ` have the following meanings:

Flag | Description
---- | -----------
/FLT | Number mode uses floating point numbers (also sets /NUM)
/INT | Number mode uses integers (also sets /NUM)
/LOG | Use logical mode (args must be 1 or 0)
/NUM | Use number mode (args must be either integers or floats depending on /INT or /FLT)
/STR | Use string mode
/CASE | Use case sensitive string comparison
/NOCASE | Use non-case sensitive string comparison
/PAD | Pad strings with spaces before comparison
/NOPAD | Don't pad strings with spaces before comparison

The flags for `TST LCL` have the following meanings:

Flag | Description
---- | -----------
/LEV | Select the command level to check for the local argument. 1 indicates the current macro, 2 the macro that called the current macro, 3 the macro that called that macro, etc. The value must be an integer ranging from 1 to the depth of the call stack.

The flags for `TST LIM` have the following meanings:

Flag | Description
---- | -----------
/FLT | Use floating point numbers
/INT | Use integers

Note that these qualifiers are evaluated in the order they are provided and can override each other's behavior. For
example in the command:

    tst eq /log /str &a &b

/STR will override /LOG and `TST` will do string comparison.

`TST` is a replacement for the old if commands such as `IFEQ`. If you need the old behavior of jumping to labels instead
of executing code blocks use `GOTST`.
## TSTEX
Test pulse program

Category:

Format: `TSTEX`
## TVAL
Show heater temperature

Category: Heater

Format: `TVAL`

Prerequisites: Spectrometer configured for RNMR temperature control

Description:
Returns actual heater temperature.
## TWIST
Twist blocked record


Category: Data Manipulation

Format: `TWIST` rec#

Defaults: current

Description:
Twists blocked record.  Strictly speaking this is a shearing operation.  Each DIM2 FID is twisted by an amount equal to
its DIM1 frequency.

# U
---
## UNIT
Set units

Category: Display Control

Format: `UNIT` [qual] unit
	Qualifiers: 	            /DFLT   /DIM1   /DIM2   /FREQ   /TIME
Qualifier defaults:         current dimension         current domain Defaults:          current Description:
Sets time or frequency unit.  Valid time domain units are USEC, MSEC, and SEC.  Valid frequency domain units are HZ,
kHz, MHz, and PPM.  The /DFLT qualifier is used to specify a unit to be used when the primary unit is not acceptable.
All primary units are valid default units with the exception of PPM.
## UPDARV
Update archive

Category: Data Storage

Format: `UPDARV` archive

Defaults: 1

Description:
Updates any changes made to the specified archive from the file containing that archive.
## USER
Set user name

Category: Data Storage

Format: `USER` user

Defaults:

Description: current
Sets user name for record protection.

# V
---
## VAL
Set data value

Category: Data Manipulation

Format: `VAL` xval valr vali

Defaults: current_cursor current current

Description:
`VAL` sets the data value of a specific FID or spectrum point to a specified complex number (valr,vali).  The point to
be modified is selected by its time or frequency value "xval" rather than its point number.
## VIEW
Set display source

Category: Display Control

Format: `VIEW` view

Defaults: current

Description:
Sets display source.  The options are be ACQ, LCK, or PRO.

# W
---
## WAIT
Halt when number of shots satisfies `NWAIT`

Category: Acquisition

Format: `WAIT`

Description:
Halts acquisition after nwait satisfied.

Subcommands:
          	1st Q    Halt after next complete cycle           	2nd Q    Halt after next shot
## WAVV
Perform weighted addition of data

Category: Data Manipulation

Format: `WAVV` isrc idst

Defaults: 1 2

Description:
`WAVV` performs a weighted addition of two complex buffers, "isrc" and "idst", modifying the destination buffer:

    DST = DST*NA_DST/(NA_DST+NA_SRC) + SRC*NA_SRC/(NA_DST+NA_SRC) * (SF_DST/SF_SRC)

This addition permits the proper addition of two FID's or spectra with different scale factors and/or number of
acquisitions; each data set is weighted appropriately.
## WGPIB
Write to GPIB device

Category: Hardware

Format: `WGPIB` device

Defaults: no defaults

Description:
Writes string to GPIB device.
## WTTIM
Wait for specified number of seconds

Category: Timing

Format: `WTTIM`
## WNDLIM
Set vertical window limits

Category: Display Control

Format: `WNDLIM` wndmin wndmax

Defaults: current current

Description:
Sets vertical window limits.  wndmin=\* indicates current data minimum.  wndmax=\* indicates current data maximum.
## WPK
Write peaks in current display to `WRT` file

Category: File IO

Format: `WPK`

Description:
Writes peaks in current display to `WRT` file.  A maximum of 50 peaks will be written.
## WPK2D
Write 2D peaks to `WRT` file

Category: File IO

Format: `WPK2D` rec#

Defaults: current

Description:
Writes two-dimensional peaks to `WRT` file.  A maximum of 250 peaks will be written.
## WPPSB
Write to pulse programmer spectrometer bus

Category: Hardware

Format: `WPPSB` iadr data

Defaults: 0 0

Prerequisites: Pulse programmer spectrometer bus control implemented (CGFSB2).

Description:
`WPPSB` writes a data byte to the pulse programmer spectrometer bus.
## WRFEX
Load waveform RF program

Category: Waveform

Format: `WRFEX`

Defaults:

Prerequisites: Waveform generator implemented and HALT
## WRT
Write to `WRT` file opened by `OPNWRT`

Category: File IO

Format: `WRT` arg1 arg2 ... arg10

Defaults: none none ... none

Description:
Writes arguments to `WRT` file. If no arguments are specified a line will be prompted for and written.
## WSB
Write to spectrometer bus

Category: Hardware

Format: `WSB` addr data

Defaults: 0 0

Description:
Writes data byte to specified spectrometer bus address.
## WTSET
Wait for heater to stabilize at setpoint

Category: Heater

Format: `WTSET`

Prerequisites: Spectrometer configured for RNMR temperature control.

Description:
Waits for heater to stabilize at setpoint temperature.
## WWASH
Set state of plot whitewash flag

Category: Printing

Format: `WWASH` state

Defaults: current

Description:
Sets state of stacked plot whitewash flag.  State may be ON or OFF.
## WWF
Waveform program

Category: Waveform

Format: `WWF`

Defaults:

Prerequisites: Waveform generator implemented
## WWFEX
Load waveform program

Category: Waveform

Format: `WWFEX`

Defaults:

Prerequisites: Waveform generator implemented and HALT

# X
---
## XT
Extract data within specified limits

Category: Data Manipulation

Format: `XT` llim rlim

Defaults: current current

Description:
Region from llim to rlim is extracted from data.  All other data points are discarded.
## XTP
Extract data for specified number of points

Category: Data Manipulation

Format: `XTP` llim npt

Defaults: current 64

Description:
Region beginning at llim, npt points in length, is extracted from data. All other data points are discarded.
## XTPC
Extract number of points at specified center

Category: Data Manipulation

Format: `XTPC` cntr npt

Defaults: display display

Description:
Region centered at cntr, npt points in length, is extracted from data.  All other data points are discarded.
## XVAL
Convert from point index to unit value

Category: Data Analysis

Format: `XVAL` ixval
Default : 	        current_cursor_position Description:
`XVAL` returns the time or frequency value of the specified point number (index value).  This command may be used with
`IXVAL`, which returns a point number given the time or frequency value, to locate and examine data points in a buffer
one by one within a specific time or frequency range.  `XVAL` returns a value using the time or frequency scale of the
visible processing buffer (buffer 1).  `XVAL` takes one parameter, "ixval", which is the point number to be converted to
a time or frequency value.  If "ixval" is not specified on the command line, RNMR will prompt for an index value with
the current cursor 1 position in buffer 1 as the default.  If the current cursor position is "\*", then the default for
"ixval" is the time or frequency of the leftmost data point.  If the requested value of "ixval" is negative, or if
"ixval" is "\*", `XVAL` will return the value of data point 1.  Similarly, if "ixval" is larger than the buffer size,
`XVAL` will return the time or frequency value of the rightmost data point. `XVAL` does not accept noninteger "ixval"
arguments.  The time or frequency value corresponding to the point number "ixval" is reported to the user as an
informational message.  Note that "ixval" need not lie within the current display limits, as set and displayed by the
`LIM` command.

# Z
---
## ZE
Zero processing buffer

Category: Data Manipulation

Format: `ZE`

Description:
Processing buffer is zeroed.
## ZER
Zero averager and shot counter

Category: Acquisition

Format: `ZER`

Prerequisites: HALT

Description:
Averager and shot counter are zeroed.
## ZF
Zero fill FID to number of points

Category: Data Manipulation

Format: `ZF` size

Defaults: current

Prerequisites: TIME

Description:
FID is zero filled up to size. Size must be power of 2 less than or equal to 32768.
## ZG
Zero averager and begin acquisition

Category: Acquisition

Format: `ZG` NA

Defaults: current

Prerequisites: LOAD HALT

Description:
Starts acquisition.
## ZO
Zoom

Category: Display Control

Format: `ZO`

Prerequisites: PRO

Description:
Positions cursors on display.

Subcommands:

Command | Description
------- | -----------
CR      | Terminate
0-3     | Move 10^digit points
E       | Expand display between cursors
F       | Contract to display full buffer
H       | List point values on line printer
L       | Select left movement
M 1     | Select 1 cursor display
M 2     | Select 2 cursor display (shows expand region)
O       | Enter offset value after prompt
P       | Move to next peak
Q       | Terminate
R       | Select right movement
S       | Switch active cursor
T       | Enter threshold value after prompt
V       | Enter cursor value after prompt
W       | Write point values to `WRT` file

## ZO2D
Zoom on 2D data set

Category: Display Control

Format: `ZO2D` rec#

Defaults: current

Prerequisites: PRO

Description:
Performs two-dimensional zooming on blocked record.

Subcommands:

Command | Description
------- | -----------
CR      | Terminate
0-3     | Move 10^digit blocks
D1      | Select 1st dimension
D2      | Select 2nd dimension
F       | Select forward direction
Q       | Terminate
R       | Select reverse direction
S       | Switch dimensions
V       | Enter other dimension value after prompt
Z       | Call `ZO`

## ZO2DC
Zoom on 2D contour display

Category: `ZO2DC`

Format: `ZO2DC` rec#

Defaults: current

Prerequisites: PRO

Description:
Performs two-dimensional contour zooming on blocked record.

Subcommands:

Command | Description
------- | -----------
CR      | Terminate
0-3     | Move 10^digit points
D       | Select down movement
E       | Expand display between cursors
F       | Contract to display full record
H       | List point values on line printer
L       | Select left movement
M 1     | Select 1 cursor display
M 2     | Select 2 cursor display (shows expand region)
M C     | Select contour mode
M I     | Select image mode
O       | Enter offset value after prompt
P       | Move to next peak
Q       | Terminate
R       | Select right movement
S       | Switch active cursors
T       | Enter threshold value after prompt
U       | Select up movement
V       | Enter cursor value after prompt
W       | Write point values to `WRT` file

## ZOA
Zoom on acquisition display

Category: Acquisition

Format: `ZOA`

Prerequisites: ACQ

Description:
Positions cursors on acquisition display.

Subcommands:

Command | Description
------- | -----------
CR      | Terminate
0-3     | Move 10^digit points
E       | Expand display between cursors
F       | Contract to display full buffer
H       | List point values on line printer
L       | Select left movement
O       | Enter offset value after prompt
P       | Move to next peak
Q       | Terminate
R       | Select right movement
S       | Switch active cursor
T       | Enter threshold value after prompt
V       | Enter cursor value after prompt
W       | Write point values to `WRT` file

## ZOL
Zoom on lock display

Category: Lock

Format: `ZOL`

Prerequisites: `LCK`


Description:
Positions cursors on lock display.

Subcommands:

Command | Description
------- | -----------
CR      | Terminate
0-2     | Move 10^digit points
C       | Contract display by factor of 2
E       | Expand display by factor of 2
F       | Contract to display maximum sweep width
L       | Select left movement
P       | Enter position value after prompt
Q       | Terminate
R       | Select right movement
W       | Enter sweep width value after prompt


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
`CASE` executes the block of commands that falls between it and either the next `CASE` command or `ENDSEL` if the value
used in the `SEL` block matches val. If val is omitted then `CASE` will act as if it matches for any value. `CASE` must
be between a `SEL` and a matching `ENDSEL`.
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
record # in archive 2 can be specified either as 2:# or by adding 200 to #. Similarly, last-rec may be any integer from
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

## CATLST
List catalog of lists

Category: Lists

Format: `CATLST` first last

Qualifiers: /PRT /TTY /VAL /WND /WRT

Qualifier Defaults: /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATLST` displays a catalog of the currently defined lists by name from first to last in alphabetical order.
If first is omitted from the command line, then the catalog will begin with the first entry in the list table.
RNMR will not prompt for first. Similarly, if last is not specified, `CATLST` will list all lists. If only one
argument is specified, `CATLST` will list information about only that single list. Each list is listed by
name along with its maximum size and its current size.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/VAL      | Also list the values in the list
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## CATMAC
List catalog of macros

Category: Macros

Format: `CATMAC` first last

Qualifiers: /PRT /SYS /TTY /USR /WND /WRT

Qualifier Defaults: /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATMAC` displays a catalog of the currently defined macros by name from first to last in alphabetical order.
If first is omitted from the command line, then the catalog will begin with the first entry in the macro table.
RNMR will not prompt for first. Similarly, if last is not specified, `CATMAC` will list all macros. If only one
argument is specified, `CATMAC` will list information about only that single macro. Each macro is listed by
name along with whether it is a user or system macro and the file where it is stored. The file will only be listed if
the macro has been called during the current RNMR session.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/SYS      | List system macros
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/USR      | List user macros
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

Note that if neither /USR nor /SYS is specified `CATMAC` will list both, which is the same behavior as if both are
specified.
## CATNUC
List catalog of nuclei

Category: Nuclei

Format: `CATNUC` first last

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATNUC` displays a catalog of the currently defined nuclei by name from first to last in alphabetical order. If first
is omitted from the command line, then the catalog will begin with the first entry in the nucleus table. RNMR will not
prompt for first. Similarly, if last is not specified, `CATNUC` will list all nuclei. If only one argument is specified,
`CATNUC` will list information about only that single nucleus. Each nucleus is listed by name along with its current
frequency (value used to convert between PPM and Hz) in MHz and its reference frequency in Hz.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## CATPPS
List catalog of PP symbols

Category: Pulse Program

Format: `CATPPS` type first last

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: none none ZZZZZZZZZZZZZZZZ

Description:
`CATPPS` displays a catalog of the currently defined PP symbols. The catalog is organized by PP symbol type and then
each type section is organized by name from first to last in alphabetical order. If type is omitted from the command
line then `CATPPS` will display all types of symbols. If a type is specified then only the section of the catalog
corresponding to that type will be listed. If first is omitted from the command line, then the catalog will begin with
the first entry in each included section. RNMR will not prompt for first. Similarly, if last is not specified, `CATPPS`
will list all entries in each included section. If only one of first and last is specified, `CATPPS` will list
information about only that single PP symbol in each included section. Each PP symbol is listed by name along with its
location.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## CATSYM
List catalog of nuclei

Category: Nuclei

Format: `CATSYM` first last

Qualifiers: /FLT /INT /NDEC /PRT /TTY /WND /WRT

Qualifier Defaults: /NDEC=1 /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATSYM` displays a catalog of the currently defined symbols by name from first to last in alphabetical order. If first
is omitted from the command line, then the catalog will begin with the first entry in the symbol table. RNMR will not
prompt for first. Similarly, if last is not specified, `CATSYM` will list all symbols. If only one argument is specified,
`CATSYM` will list information about only that single symbol. Each symbol is listed by name along with its current
value. Floating point symbols will be displayed with a number of decimal places set by /NDEC.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/FLT      | List floating point symbols
/INT      | List integer symbols
/NDEC     | Set the number of decimal places for displaying floating point symbols
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

Note that if neither /FLT nor /INT is specified `CATSYM` will list both, which is the same behavior as if both are
specified.
## CATTBL
List catalog of name tables

Category: Table

Format: `CATTBL` tbl first last

Qualifiers: /PRT /TTY /VAL /WND /WRT

Qualifier Defaults: /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATTBL` displays a catalog of the currently defined tables by name from first to last in alphabetical order. A single
table to display may be selected using the tbl argument. /VAL will cause `CATTBL` to list the values in the tables. If
first is omitted from the command line, then the values will begin with the first entry in the table. RNMR will not
prompt for first. Similarly, if last is not specified, `CATTBL` will list all values in the table. If only one of first
and last is specified, `CATTBL` will list information about only that single value. Each table is listed by name along
with its maximum size and its current size.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/VAL      | Also list the values in the tables
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

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
the wide result using `SC` and subtracting the two resulting FID's. This apodization is useful for separating out
spectral components with greatly different line widths and for masking the effects of probe ring-down. `CD` does not
require the user to be viewing the processing block (`VIEW PRO`), but apodization is only performed on the processing
block. The narrow line broadening narrow and the wide line broadening wide are real numbers expressed in the current
default frequency units (as displayed and set by `UNIT /FREQ /DFLT`). If either of these parameters are not specified,
RNMR will prompt for its value with 0.0 as the default. Each linewidth entered must be between -1000 Hz and 1000 Hz,
inclusive. The parameter wfract specifies the fraction of the wide component (with linewidth "wide") in the
apodization. This fraction is a real number between 0.0 and 1.0, inclusive. If wfract is not specified, then RNMR
will prompt for its value with 0.000 as the default.

The apodization vector is calculated for each data point according to the formula:

    VEC(N) = EXP(-PI*L1*T(N)) - WFRACT*EXP(-PI*L2*T(N))         N=1,...,SIZE

where L1 and L2 are the narrow and wide line widths, respectively, and T(N) is the time value of data point N in the
FID. Each block of the processing buffer is separately multiplied by the apodization vector VEC(N), yielding an
apodized complex FID. If the processing buffer is currently visible, `CD` always updates the display upon completion.
## CHN
Map logical and physical channels to one another

Category: Acquisition

Format: `CHN` args

Qualifiers: /LOG /PHY /SEQ

Qualifier Defaults: /SEQ

Defaults: current

Prerequisites: Acquisition stopped (HALT) RNMRA only

Description:
RNMR pulse sequences specify pulses to be run on logical channels. Logical channel 1 is always the observe channel and
the other logical channels may be used for other nuclei. These logical channels are distinct from the hardware channels
in the console which are physically connected to the desired amplifiers, duplexers, and ultimately probe inputs. `CHN`
sets the mapping between the logical and physical channels, so that the pulses are generated on the right channel in the
console.

The /LOG and /PHY qualifiers are used to set the mapping for a single channel while the /SEQ option sets all the
channels at once. /LOG accepts two arguments: the first being a logical channel and the second being a physical channel
to map it to. /PHY works the same as /LOG but the first argument should be the physical channel and the second argument
should be the logical channel.

/SEQ, which is the default qualifier, expects a sequence of physical channels consisting of up to the number of channels
in the system. The sequence of channels will be mapped to the logical channels starting from 1. For example:

    CHN 31

will map logical channel 1 to physical channel 3 and logical channel 2 to physical channel 1.
## CLSARV
Close archive

Category: Data Storage

Format: `CLSARV` archive

Defaults: 1

Description:
`CLSARV` closes an archive. The archive is specified as an integer ranging from 1 to 4. An attempt to close an archive
which is not open will result in an error.
## CLSB
Close blocked record

Category: Data Storage

Format: `CLSB` record

Defaults: wrec

Description:
`CLSB` closes an open blocked record. The default value is the most recently written to record. `CLSB` will error if the
specified record is not an open blocked record.
## CLSDSP
Close display

Category: Display

Format: `CLSDSP`

Description:
Close display opened with `OPNDSP`. `CLSDSP` will error if no export file is open.
## CLSEXP
Close export file

Category: File IO

Format: `CLSEXP`

Description:
Close export file opened with `OPNEXP`. `CLSEXP` will error if no export file is open.
## CLSIMP
Close import file

Category: File IO

Format: `CLSIMP`

Description:
Close import file opened with `OPNIMP`. `CLSIMP` will error if no export file is open.
## CLSPLT
Close plotter stream and print

Category: Printing

Format: `CLSPLT`

Description:
`CLSPLT` writes out the current plot buffer and submits the resulting file for printing or plotting, terminating the
plot sequence that began with `OPNPLT`. All plots between `OPNPLT` and `CLSPLT` will appear on one sheet of paper.
`CLSPLT` is legal only if the plot file is currently open. If the plotter or printer selected by `PLDEV` is not
currently idle, `CLSPLT` sends the appropriate control sequences to put it in idle mode. Next, the current plot buffer,
containing the code for each spectrum or FID to be plotted, is written out to a temporary plot file, PL.TMP, in the
user's directory. This plot file is then submitted to the appropriate queue for printing or plotting. Upon successful
generation of the plot, the plot file is deleted.
## CLSRD
Close file opened for read

Category: File IO

Format: `CLSRD`

Description:
`CLSRD` closes a file opened by `OPNRD` for reading with `RDWRT`. If `CLSRD` is entered when no file is open for read,
RNMR will display an error message.
## CLSWRT
Close file which has been opened for writing

Category: File IO

Format: `CLSWRT`

Description:
`CLSWRT` closes a file opened by `OPNWRT` for writing with the `WRT` command. All output from `WRT` commands issued
between `OPNWRT` and `CLSWRT` will appear in one file. If `CLSWRT` is entered when no file is open for write, RNMR will
display an error message.
## CMUL
Multiply buffer by complex constant

Category: Data Manipulation

Format: `CMUL` valr valphi buf

Defaults: 1.0 0.0 1

Description:
`CMUL` multiplies the contents of a buffer by a complex constant, updating the buffer. This constant is specified in
polar form:

    REAL(CONST) = VALR*COS(VALPHI*PI/2)
    IMAG(CONST) = VALR*SIN(VALPHI*PI/2)

The first parameter, "valr" is a real number which is the magnitude of the complex constant. If this parameter is
omitted, the magnitude will be 1.0; RNMR will not prompt for "valr". The second parameter, "valphi" is a real number
which is the polar angle phi of the complex constant in degrees. If this parameter is omitted, this angle will be 0.0;
RNMR will not prompt for "valphi". The last parameter, "buf" selects which processing buffer should be multiplied and
updated; the visible buffer is buffer 1. The buffer number may be either 1 or 2. If "buf" is omitted, buffer 1 will be
processed; RNMR will not prompt for "buf". `CMUL` multiplies each block of the selected processing buffer by the
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

The arguments "SRC" and "DST" specify the numbers of the buffers to be multiplied. Each buffer number may be either 1
or 2; buffer 1 is the visible processing buffer. If either argument is omitted, RNMR will prompt for a buffer number.
The default source is buffer 2 while the default destination is buffer 1. While `CMULV` operates only on processing
buffers, the user need not be viewing the processing buffers to perform the multiplication. For two buffers to be
multiplied, they must have the same domain (time or frequency) and the same active size (though not necessarily the
same allocated size). If the destination buffer is partitioned into two or more blocks, each block is separately
multiplied by the corresponding block of the source buffer. The number of blocks in the source buffer need not be the
same as that in the destination buffer. RNMR uses the formula below to match source blocks with destination blocks:

    IBLK_SRC = MOD(IBLK_DST-1,NBLK_SRC) + 1,    IBLK_DST=1,...,NBLK_DST

If the processing buffer is currently visible and "dst" is 1, `CMULV` always updates the display upon completion.
## CND
Set condition flag

Category: Misc.

Format: `CND` cnd# state

Defaults: 1 current

Description:
`CND` sets the state of the specified condition flag to ON or OFF. The first parameter, cnd# specifies which of the
64 available condition flags is to be set. Accordingly, cnd# may be any integer from 1 to 64. If this parameter is
omitted, RNMR will prompt for a flag number with 1 as the default. The second parameter, "state" specifies the logical
state to  which the condition flag should be set. The acceptable choices of this parameter are ON and OFF. If "state" is
omitted, RNMR will prompt for the state of the `CND` flag with the current state as the default.
## CNVFL
Convolution filter spectrum

Category: Data Manipulation

Format: `CNVFL` kmax

Qualifiers: /KRNL=(GAUSS,SINEB) /PASS=(HIGH,LOW) /END=(EXT,LP,ZER)

Qualifier Defaults: /KRNL=GAUSS /PASS=HIGH /END=EXT

Defaults: 8

Description:
`CNVFL` convolves the data in processing buffer 1 with a filter kernel. The argument kmax sets the maximum filter
component. The filter kernel will contain nkrnl=2\*kmax+1 points. kmax can range from 1 to 32.

/KRNL selects either a gaussian or sinebell function to use for the filter kernel. A convolution filter cannot calculate
values at the edges of the data. /END determines what is done with these points. The minimum size of the buffer relative
to the kernel size also depends on /END. The following options area available:

Option | Description | Minimum Buffer Size
------ | ----------- | -------------------
EXT    | Extrapolate to fill in the points | 4*kmax+1
LP     | Apply linear prediction to fill in the points | 2*kmax+128
ZER    | Set the points to 0 | 2*kmax+1

/PASS determines what is done with the result of the convolution. /PASS=HIGH subtracts the result from the buffer while
/PASS=LOW replaces the buffer with the result.
## COLOR
Set data display colors

Category: Display Control

Format: `COLOR` red green blue

Qualifiers: /BG /CURSOR /IMAG /REAL

Qualifier defaults: /REAL

Defaults: current current current

Description:
`COLOR` sets the color of elements of the display. /BG sets the color of the background and /CURSOR sets the color of all cursors. /REAL and /IMAG set the color of the real and imaginary data respectively.

The red/green/blue values may each range from 0 to 100. That is, to specify pure red, use 100 0 0.

The default colors are:

Option | Default Color
------ | -------------
/BG    | 0 0 0 (Black)
/CURSOR | 100 100 100 (White)
/REAL  | 0 100 0 (Green)
/IMAG  | 100 0 0 (Red)

## CONJG
Complex conjugate data

Category: Data Manipulation

Format: `CONJG`

Description:
`CONJG` complex conjugates processing buffer 1. The user need not be viewing the processing buffer in order to use
`CONJG`. If the buffer is partitioned into two or more blocks, `CONJG` separately conjugates each block. If the
processing buffer is currently visible, `CONJG` always updates the display upon completion.
## CONLIM
Set contour plot height limits

Category: `ZO2DC`

Format: `CONLIM` min max

Defaults: current current

Description:
`CONLIM` sets intensity limits for contour plotting. Contours will only be drawn for intensities between these limits.
If either min or max is omitted from the command line, RNMR will prompt for the contour limit with its current value as
the default. Contour levels are real numbers and are displayed to a maximum of three decimal places. If the user accepts
the defaults for both min and max, no changes are made to the current contour limits. If both min and max are 0.0
(`CONLIM` 0 0), then RNMR sets max to 1.0; min remains 0.0. Thus, `CONLIM 0 0` resets the contour limits to their system
default values. If min and max are not both zero, max must be strictly greater than min. When a contour plot is
generated, the maximum contour level will be max while the minimum contour level will approach but not equal min.
## CONMD
Set contour plotting mode

Category: `ZO2DC`

Format: `CONMD` mode

Defaults: current

Description:
`CONMD` sets the contour plotting mode. The argument mode may be entered as ABS, NEG, or POS. If mode is omitted, RNMR
will prompt for a contour plotting mode with the current mode as the default. If the user accepts this default, no
changes are made.
## COSSQ
Perform cosine squared apodization

Category: Data Manipulation

Format: `COSSQ` time0

Defaults: (size+1)\*step

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`COSSQ` multiplies processing buffer 1 by a cosine squared function which goes to zero at time0.
## CPXV
Complex merge two buffers

Category: Data Manipulation

Format: `CPXV` src dst

Defaults: 2 1

Description:
`CPXV` combines the real parts of two buffers to form the real and imaginary parts of the destination buffer:

 	DST = COMPLEX(REAL(DST),REAL(SRC))

 or
    REAL(DST) = REAL(DST)
    IMAG(DST) = REAL(SRC)

The arguments SRC and DST specify the numbers of the buffers to be processed. Each buffer number may be either 1 or
2; buffer 1 is the visible processing buffer. If either argument is omitted, RNMR will prompt for a buffer number. The
default source is buffer 2 while the default destination is buffer 1. While `CPXV` operates only on processing buffers,
the user need not be viewing the processing buffer to perform the operation. For two buffers to be merged with `CPXV`,
they must have the same domain (time or frequency) and the same active size (though not necessarily the same allocated
size). If the destination buffer is partitioned into two or more blocks, each block is separately merged with the
corresponding block of the source buffer. The number of blocks in the source buffer need not be the same as that in the
destination buffer. RNMR uses the formula below to match source blocks with destination blocks:

 	IBLK_SRC = MOD(IBLK_DST-1,NBLK_SRC) + 1,  IBLK_DST=1,...,NBLK_DST

If the processing buffer is currently visible and dst is 1, `CPXV` always updates the display upon completion.
## CPY
Copy record

Category: Data Storage

Format: `CPY` src dst

Defaults: current_read_record next_available_record

Description:
`CPY` copies the archive record src into record dst. Unlike `ALLCPY`, `CPY` copies both title parameters and data from
source to destination. The first parameter, src is the number of the record to be copied. If no source record number is specified, RNMR will prompt for src with the current read record (as displayed and set by `PTRA`) as the default.

The second parameter, dst is the number of the destination record, i.e. the record which will contain a copy of src. If
dst is not specified, is 0, or is not empty, then RNMR will attempt to put the copy of src into the next available
record; RNMR does not prompt for a destination record number.

Record numbers are specified as integers with every set of 200 values corresponding to an archive. Records 1-200 are
archive 1, 201-400 are archive 2 etc. A record in a given archive may also be specified as arv:rec. For example 205 and
2:5 are the same record. `CPY` cannot copy to or from scratch records which are the first 4 records in an archive.

When `CPY` is asked to use the next available record for dst, a search is made for an empty record starting with the
current read record. The search proceeds toward record 200 and starts over at record 5 if no empty records are found
ahead of the current record. If no empty records can be located, then an error message is displayed. In this case, the
user must either delete an existing record (`DL`) or start a new archive.

If RNMR does not have write access to dst an error message will be printed and neither the existing data nor parameters
of dst will be overwritten. If the data file (\*DATA.DAT) is extended to hold the copy of src, then RNMR will display a
message reporting the new data file size in blocks (512 bytes per block).

Once the copy operation has been completed, `CPY` updates the current read record pointer to dst. Afterwards, `PTRA`
will display the number of the record which received the copy of src. If dst was zero or omitted, `CPY` displays the
destination record number as an informational message.
## CPYMAC
Copy macro

Category: Macro

Format: `CPYMAC` name1 name2

Defaults: temp temp

Description
`CPYMAC` copies the contents of macro name1 into a new macro name2.
## CRS
Set cursor positions

Category: Display Control

Format: `CRS` cursor1_pos cursor2_pos

Defaults: current current

Description:
`CRS` takes two parameters, crs1 and crs2, which are cursor 1 and 2 positions, respectively. These positions are
expressed in the current unit for the visible buffer (ACQ, PRO, or LCK) with the current maximum number of decimal
places for that unit. The current unit is set and displayed by the `UNIT` command and the maximum number of decimal
places is set and displayed by `NDEC`. If crs1 or crs2 is missing from the command line, RNMR will display the current
value for the missing position and prompt for a new value. For each display limit, the user should enter a value
expressed in  the current time or frequency unit or "\*" to select the leftmost position. If the user requests a
position to the left of the leftmost point in the data buffer, the cursor will be positioned at the leftmost data point.
Similarly, if the position specified is beyond the rightmost data point, the cursor will be position at the rightmost
data point. If the user specifies a position that is within the range of the data buffer but which does not correspond
to a specific data point, RNMR will set that position to the time or frequency of the closest data point to the right of
the value specified.
## CRSA
Set acquisition cursor positions

Category: Display Control

Format: `CRS` cursor1_pos cursor2_pos

Defaults: current current

Prerequisites: RNMRA only

Description:
`CRSA` functions identically to `CRS`, but sets the position of cursors visible during acquisition.
## CRTARV
Create archive

Category: Data Storage

Format: `CRTARV` archive name

Defaults: 1 TEMP

Description:
`CRTARV`creates and opens a new archive with read/write access.
## CRTFIL
Create text file

Category: File IO

Format: `APNFIL` fspec

Qualifiers: /END=<end\>

Qualifier Defaults: /END=''

Defaults: temp.dat

Description:
`CRTFIL` creates a text file with the name fspec. /END sets a string which marks the end of what is to be written to the file.
`CRTFIL` behaves slightly differently if called at the command line or in a macro. At the command line if no file is
specified RNMR will prompt for a file with temp.dat as a default. If the file does not already exist and RNMR succeeds
in creating it, RNMR will pop up a window where text can be entered to write to the file. Otherwise an error will be
thrown.

When called from a macro `CRTFIL` will not prompt for a file name. The lines to be written should be provided on the
lines following `CRTFIL` in the macro and should start with ;;. The first line will be interpreted as a file name if
none is provided as an argument. `CRTFIL` will stop writing lines when it either reaches a line that matches <end\> or
runs out of lines. /TTY will make RNMR pop up a window much like the behavior at the command line even
when `CRTFIL` is called from a macro. RNMR will still expect the file name to passed in the same way as when /TTY is not
used. An example of use in a macro is given here:

    CRTFIL TEMP.TXT
    ;;Write this to temp.txt
    ;;Also write this

Text written when `CRTFIL` is called from a macro will be all caps regardless of the capitalization in the macro.
## CRTLST
Create list

Category: List Handling

Format: `CRTLST` nam maxval

Defaults: temp 32

Description:
`CRTLST` creates a new list named nam that can hold a maximum of maxval entries. RNMR will prompt for nam and maxval if
they are not provided. If a list with the same name already exists `CRTLST` will error.
## CRTMAC
Create macro

Category: Macro

Format: `CRTMAC` nam

Qualifier Defaults: /END=''

Defaults: temp

Description:
`CRTMAC` creates a macro with the name nam. /END sets a string which marks the end of what is to be written to the macro.
`CRTMAC` behaves slightly differently if called at the command line or in a macro. At the command line if no name is
specified RNMR will prompt for a name with temp as a default. If the macro does not already exist and RNMR succeeds
in creating it, RNMR will pop up a window where text can be entered to write to the macro. Otherwise an error will be
thrown.

When called from a macro `CRTMAC` will not prompt for a macro name. The lines to be written should be provided on the
lines following `CRTMAC` in the macro and should start with ;;. The first line will be interpreted as a macro name if
none is provided as an argument. `CRTMAC` will stop writing lines when it either reaches a line that matches <end\> or
runs out of lines. /TTY will make RNMR pop up a window much like the behavior at the command line even
when `CRTMAC` is called from a macro. RNMR will still expect the macro name to passed in the same way as when /TTY is
not used. An example of use in a macro is given here:

    CRTmac TEMP
    ;;This will me in macro temp
    ;;so will this

Text written when `CRTMAC` is called from a macro will be all caps regardless of the capitalization in the macro.
## CRTTBL
Create name table

Category: Table

Format: `CRTTBL` nam maxval

Defaults: temp 32

Description:
`CRTTBL` creates a new name table named nam that can hold a maximum of maxval entries. RNMR will prompt for nam and
maxval if they are not provided. If a name table with the same name already exists `CRTTBL` will error.
## CVTMD
Set modes for blocked record index conversion

Category: Blocked Records

Format: `CVTMD` sizmd blkmd

Defaults: current current

Description:
`CVTMD` sets modes for blocked record index conversion. The first parameter, sizmd is the record size conversion mode.
If sizmd is omitted, RNMR will prompt for a mode with the current size conversion mode as the default. The legal choices
for sizmd are SIZEA, SIZE, and CVTSZ. The second parameter, blkmd is the record blocking conversion mode. If blkmd is
omitted, RNMR will prompt for a mode with the current mode as the default. The legal values for blkmd are 0, 1, 2, 3, or
4.
## CVTSZ
Set sizes for blocked record index conversion

Category: Blocked Records

Format: `CVTSZ` ndim size(1) size(2) size(3) size(4)

Defaults: 2 current current current current

Description:
`CVTSZ` sets the sizes for a blocked record index conversion. The first parameter, ndim is the number of dimensions for
the conversion. If ndim is not specified, RNMR will prompt for its value with a default value of 2. The allowed values
of ndim are 1, 2, 3, or 4. The remaining parameters are the sizes in each of the ndim dimensions. RNMR expects to find
ndim integers greater than or equal to 1 following ndim.  These sizes are to be entered in order of dimension, starting
with dimension 1. If one or more of these is omitted, RNMR will prompt for its value with the current conversion size in
the appropriate dimension as the default.
##CVTUNIT
Convert a value between units

Category: Data Manipulation

Format: `CVTUNIT` srcunit dstunit val

Description:
`CVTUNIT` converts val from srcunit to dstunit.
# D
---
## D
Set pulse programmer delay

Category: Acquisition

Format: `D` dly msec

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD); RNMRA only

Description:
`D` is an old command for setting the length of pulse program delays. It has been replaced with the `DLY` command and is
currently simply an alias to it. As such `DLY` should be used in place of `D`
## DATE
Print the current date and time as an informational message

Category: Misc.

Format: `DATE`

Qualifiers: /DATE /TIME /EPOCH

Qualifier Defaults: /DATE /TIME

Description:
`DATE` prints information about the current date and time as informational messages. The following pieces of information
are printed depending on the qualifiers that are used.

Qualifier | Information
--------- | -----------
/DATE     | The current date
/TIME     | The current time of day
/EPOCH    | The current Unix epoch time

By default `DATE` prints the date and time of day.
## DBSZ
Set data buffer size and partitioning

Category: Misc.

Format: `DBSZ` buf size nblk

Defaults: 1 current current

Description:
`DBSZ` sets the allocated size and partitioning of a processing data buffer. Each processing buffer may be partitioned
into multiple blocks of equal size such that the total number of data points in all blocks does not exceed 32768. By
partitioning the data buffer into two or more segments, multiple data sets may be similarly processed using a single
RNMR command. This "vector processing" capability allows multidimensional processing to be performed many blocks at a
time at a considerable savings in computation time due to the reduction in the number of commands that must be
interpreted by RNMR.

The first parameter, buf selects which data buffer is to be resized.  If this parameter is omitted, RNMR will prompt
for its value with a default of 1. The allowable values of buf are 1 and 2, thus `DBSZ` can resize only the two
processing buffers. Note that buffer 1 is the visible processing buffer.

The second parameter, size sets the allocated size for each block of buffer buf. If this parameter is omitted, RNMR will
prompt for its value with the current allocated size as the default.  The user may enter any integer from 0 to 32768 for
size; a size value of 0 is interpreted as 32768, the maximum permissible data buffer size.

The last parameter, nblk sets the number of blocks into which data buffer pro is to be divided. If this parameter is
omitted, RNMR will prompt for the number of blocks with the current nblk as the default. The user may enter any positive
integer including zero for nblk. A value of zero for this parameter requests that NBLK be set to 32768/SIZE, which gives
the maximum possible number of data blocks for a given choice of size. If both size and nblk are set to zero
(`DBSZ * 0 0`), then the appropriate data buffer is partitioned into one block of allocated size 32768. If no
modifications were made to size or nblk, `DBSZ` does nothing. Otherwise, RNMR verifies that SIZE X NBLK does not exceed
the maximum data buffer size of 32768. Once either the size or number of blocks of the selected data buffer has been
modified, the active size of the buffer is set to its allocated size and the active number of blocks is set to 1. Later
on, the active size may be decreased below the allocated size and the number of blocks may be increased. After the size
and partitioning have been modified, the data buffer is filled with zeroes. If the selected processing buffer buf is
currently visible, `DBSZ` updates the display.
## DCDB
Convert block indices to values

Category: Misc.

Format: `DCDB` rec ndim ind

Defaults: last_read 1 1

Description:
`DCDB` decodes a linear block index ind into a vector of actual values associated with each dimension of the blocked
record. The conversion uses information about the block layout of a record rec which defaults to the last record that
was read. For example when used on a dataset from a multi dimensional experiment stored as a blocked record, `DCDB` will
convert a linear block index into indirect dimension time values.

The value of ndim must not exceed the number of block dimensions. For a 2D dataset this would be 1 for a 3D it would be
2 etc. ndim specifies how many dimensions are accounted for before the linear index. For example in a 3D data set ndim
set to 1 will indicate that only the direct dimension is already accounted for and the linear index is over the last two
dimensions. The result will be two values corresponding to the position of the other two dimensions. A value of 2 on the
other hand would consider the linear index to only be over the final dimension and only one value will be printed.

The value of ind must not exceed the product of the sizes of the dimensions that the linear index is over. For example
in a 3D data set with 32X64 blocks ind can be up to 2048 when ndim is 1 but only up to 64 if ndim is 2.
## DCDBP
Convert linear block index to vector indices

Category: Misc.

Format: `DCDBP` rec ndim ind

Defaults: last_read 1 1

Description:
`DCDBP` converts a linear block index ind into a vector of indices for each block dimension. The conversion uses
information about the block layout of a record rec which defaults to the last record that was read.

The value of ndim must not exceed the number of block dimensions. For a 2D dataset this would be 1 for a 3D it would be
2 etc. ndim specifies how many dimensions are accounted for before the linear index. For example in a 3D data set ndim
set to 1 will indicate that only the direct dimension is already accounted for and the linear index is over the last two
dimensions. The result will be two values corresponding to the position of the other two dimensions. A value of 2 on the
other hand would consider the linear index to only be over the final dimension and only one value will be printed.

The value of ind must not exceed the product of the sizes of the dimensions that the linear index is over. For example
in a 3D data set with 32X64 blocks ind can be up to 2048 when ndim is 1 but only up to 64 if ndim is 2.
## DCDREC
Convert record number into archive and archive record index

Category: Misc.

Format: `DCDREC` rec

Defaults: 1

Description:
`DCDREC` accepts a record rec as an argument. It then prints the archive number that that record is in and the index of
the record within that archive. Since record numbers in archives other than 1 are represented by adding 200 for each
archive this can be a useful conversion back to just the archive and record number. For example if rec is 205 it will
print that the archive is 2 and the record index is 5.
## DCL
Execute a shell command in background

Category: Misc.

Format: `DCL`

Description:
`DCL` spawns a subprocess to execute a single shell command. This command is useful for performing background tasks
 which do not require a separate terminal session. `DCL` also allows a macro to compose and execute commands
 transparently. If the `DCL` command is used at console level, RNMR will prompt the user for the command line to be
 executed. This may be any valid shell command up to 80 characters long. If the user presses <RETURN\> when prompted for
 a command, no subprocess is created and the console prompt is returned. If `DCL` is used from within a macro, RNMR
 expects the command to be delimited by two semicolons on the line following `DCL`. The entire line after ;; constitutes
 the command string, as illustrated below:

    DCL
    ;;CP XYZ.DAT NEW_NAME.DAT

If the double semicolon delimiter ;; is not found on the line after `DCL`, or if there are no characters on the line
following ;;, `DCL` does nothing and the macro execution continues. The command line may contain local and global
argument substitutions, e.g.

    DCL
    ;;SOME_COMMAND &ABC %XYZ

The local and global arguments specified will be evaluated and filled in before the command line is passed to `DCL`.
The subprocess created by `DCL` is unable to either read from or write to the terminal. Consequently, any attempt by the
spawned process to read from the terminal will result in an immediate end of file during read condition, and any data
directed to the terminal will be lost. While the subprocess is executing the specified command, no new RNMR commands may
be entered. During execution, <CTRL-Z\> may not be used to cancel the subprocess, but any acquisition in progress
continues without interruption.  If the subprocess exits on error, RNMR will display an error message indicating the
error condition returned.  If `DCL` was called from within a macro, the current macro error handler (as set by `ONERR`)
is executed.
## DEPAKE
Perform depaking of powder pattern spectrum

Format `DEPAKE`

Prerequisites: Frequency domain data in processing buffer (FREQ)

Description:
`DEPAKE` applies a depaking routine to the visible processing buffer to remove the effects of a pake pattern from the
spectrum. The visible processing buffer must contain frequency domain data and its size must be a power of 2.
## DF
Differentiate data

Category: Data Manipulation

Format: `DF`

Prerequisites: Frequency domain data in processing buffer (FREQ)

Description:
`DF` differentiates data in the visible processing buffer (buffer 1). While the user is not required to view the
processing buffer in order to use `DF`, `DF` acts only on that buffer. Differentiation of a spectrum is often useful in
resolving subtle features on broad lines since inflection points on the source spectrum become peaks in its derivative.
If the processing buffer is partitioned into two or more blocks, `DF` differentiates each block independently. If the
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
## DFLGBL
Define global argument with default value

Category: Arguments

Format: `DFLGBL` nam val prompt

Qualifiers: /FLT /INT /NDEC /STR

Qualifier Defaults: /NDEC=1 /STR

Defaults: temp '' none

Description:
If a global argument with name nam already exists `DFLGBL` will do nothing, otherwise it will create a global argument
named nam. If nam is omitted RNMR will prompt for it with TEMP as a default. If no prompt is provided then `DFLGBL` will
create the argument with value val, otherwise it will prompt the user to enter a value with val as the default.

The qualifiers influence how `DFLGBL` interprets val as follows:

Qualifier | Description
--------- | -----------
/FLT      | Treat val as a floating point number
/INT      | Treat val as an integer
/STR      | Treat val as a string
/NDEC     | Set the number of decimal places to keep in /FLT mode

When using /FLT or /INT basic arithmetic operations may be performed (+, - , /, \*). They will be performed in order
from left to right without regard for order of operations except for parentheses. For example:

    DFLGBL /INT A 2*(2-1)

will create global argument a with a value of 2.
## DFLLCL
Define local argument with default value

Category: Arguments

Format: `DFLLCL` nam val prompt

Qualifiers: /FLT /INT /NDEC /STR

Qualifier Defaults: /NDEC=1 /STR

Defaults: temp '' none

Description:
If a local argument with name nam already exists `DFLLCL` will do nothing, otherwise it will create a local argument
named nam. If nam is omitted RNMR will prompt for it with TEMP as a default. If no prompt is provided then `DFLLCL` will
create the argument with value val, otherwise it will prompt the user to enter a value with val as the default.

The qualifiers influence how `DFLLCL` interprets val as follows:

Qualifier | Description
--------- | -----------
/FLT      | Treat val as a floating point number
/INT      | Treat val as an integer
/STR      | Treat val as a string
/NDEC     | Set the number of decimal places to keep in /FLT mode

When using /FLT or /INT basic arithmetic operations may be performed (+, - , /, \*). They will be performed in order
from left to right without regard for order of operations except for parentheses. For example:

    DFLLCL /INT A 2*(2-1)

will create local argument a with a value of 2.
## DFLT
Prompt for local variable with default

Category: Arguments

Format: `DFLT` lclnam lclval prompt

Defaults: TEMP none none

Prerequisites: Macro only (MAC)

Description:
`DFLT` is an old command for creating a local variable if one does not already exist with an optional prompt. It has
been replaced with the `DFLLCL` command and is currently simply an alias to it. As such `DFLLCL` should be use in place
of `DFLT`.
## DFLTBL
Define name table argument with default value

Category: Tables

Format: `DFLTBL` tbl nam val prompt

Qualifiers: /FLT /INT /NDEC /STR

Qualifier Defaults: /NDEC=1 /STR

Defaults: temp temp '' none

Description:
If name table tbl already has an argument with name nam `DFLTBL` will do nothing, otherwise it will create an argument
named nam in tbl. If tbl or nam is omitted RNMR will prompt for it with TEMP as a default. If no prompt is provided then
`DFLTBL` will create the argument with value val, otherwise it will prompt the user to enter a value with val as the
default.

The qualifiers influence how `DFLTBL` interprets val as follows:

Qualifier | Description
--------- | -----------
/FLT      | Treat val as a floating point number
/INT      | Treat val as an integer
/STR      | Treat val as a string
/NDEC     | Set the number of decimal places to keep in /FLT mode

When using /FLT or /INT basic arithmetic operations may be performed (+, - , /, \*). They will be performed in order
from left to right without regard for order of operations except for parentheses. For example:

    DFLTBL /INT A B 2*(2-1)

will create argument a in name table b with a value of 2.
## DFNGBL
Define global argument

Category: Arguments

Format: `DFNGBL` nam val

Qualifiers: /FLT /INT /NDEC /STR

Qualifier Defaults: /NDEC=1 /STR

Defaults: temp current

Description:
`DFNGBL` creates a global argument with name nam and value val. If nam is not provided RNMR will prompt for it with a
default of temp. If val is not provided RNMR will prompt for it with the current value of global argument nam as the
default.

The qualifiers influence how `DFNGBL` interprets val as follows:

Qualifier | Description
--------- | -----------
/FLT      | Treat val as a floating point number
/INT      | Treat val as an integer
/STR      | Treat val as a string
/NDEC     | Set the number of decimal places to keep in /FLT mode

When using /FLT or /INT basic arithmetic operations may be performed (+, - , /, \*). They will be performed in order
from left to right without regard for order of operations except for parentheses. For example:

    DFNGBL /INT A 2*(2-1)

will create global argument a with a value of 2.
## DFNLCL
Define local argument

Category: Arguments

Format: `DFNLCL` nam val

Qualifiers: /FLT /INT /NDEC /STR

Qualifier Defaults: /NDEC=1 /STR

Defaults: temp current

Description:
`DFNLCL` creates a local argument with name nam and value val. If nam is not provided RNMR will prompt for it with a
default of temp. If val is not provided RNMR will prompt for it with the current value of local argument nam as the
default.

The qualifiers influence how `DFNLCL` interprets val as follows:

Qualifier | Description
--------- | -----------
/FLT      | Treat val as a floating point number
/INT      | Treat val as an integer
/STR      | Treat val as a string
/NDEC     | Set the number of decimal places to keep in /FLT mode

When using /FLT or /INT basic arithmetic operations may be performed (+, - , /, \*). They will be performed in order
from left to right without regard for order of operations except for parentheses. For example:

    DFNLCL /INT A 2*(2-1)

will create local argument a with a value of 2.
## DFNLST
Define list value

Category: Lists

Format: `DFNLST` nam pos val

Defaults: temp 1 current

Description:
`DFNLST` sets the value at position pos in list nam. If nam is not provided RNMR will prompt for it with a default of
temp. If pos is not provided RNMR will prompt for it with a default of 1. If val is not provided RNMR will prompt for it
with the current value at position pos in list nam as the default.
## DFNSYM
Define symbol

Category: Arguments

Format: `DFNSYM` nam val

Qualifiers: /FLT /INT /NDEC

Qualifier Defaults: /INT /NDEC=1

Defaults: temp current

Description:
`DFNSYM` creates a symbol with name nam and value val. If nam is not provided RNMR will prompt for it with a
default of temp. If val is not provided RNMR will prompt for it with the current value of symbol nam as the
default.

The qualifiers influence how `DFNSYM` interprets val as follows:

Qualifier | Description
--------- | -----------
/FLT      | Treat val as a floating point number
/INT      | Treat val as an integer
/NDEC     | Set the number of decimal places to keep in /FLT mode

When using /FLT or /INT basic arithmetic operations may be performed (+, - , /, \*). They will be performed in order
from left to right without regard for order of operations except for parentheses. For example:

    DFNSYM /INT A 2*(2-1)

will create symbol a with a value of 2.
## DFNTBL
Define name table argument

Category: Tables

Format: `DFNTBL` tbl nam val

Defaults: temp temp current

Description:
`DFNTBL` sets the value of argument nam in table tbl. If tbl or nam is not provided RNMR will prompt for it with a
default of temp. If val is not provided RNMR will prompt for it with the current value of argument nam in table tbl as
the default.
## DFNPPS
Define pulse programmer symbol table entry

Category: Tables

Format: `DFNPPS` typ nam val

Defaults: temp temp current

Prerequisites: RNMRA only

Description:
`DFNPPS` sets the value of the pulse programmer symbol of type typ and name nam. If typ or nam is not provided RNMR will
prompt for it with a default of temp. If val is not provided RNMR will prompt for it with the current value of the pulse
programmer symbol of type typ and name nam as the default.
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
`DIRB` sets the order in which the dimensions of a blocked record are accessed. Dimensions of a multidimensional record
are always viewed with direction 1 as the "display" dimension and higher directions as the "blocked" dimensions. `DIRB`
assigns dimensions to directions, controlling both the orientation in which the data set is viewed in `ZO2D`, `ZO2DC`,
and `PLOTC` and the order in which the data points are accessed for processing. For example, it is possible to view a
two dimensional data set either along the acquisition dimension (dimension 1) or along the blocked dimension (dimension
2). Since direction 1 is always the "display" direction, the first view is specified by `DIRB 2 12` and the second view
by `DIRB 2 21`.

The first parameter for `DIRB`, ndim, is the number of dimensions to be sequenced. Each number of dimensions from one
to four is assigned a modifiable direction sequence. The ndim parameter selects which sequence is to be modified. If
ndim is omitted, RNMR will prompt for the number of dimensions with a default of 2. The legal values of ndim are 1, 2,
3, and 4.

The second parameter, seq assigns each dimension a direction. If this parameter is omitted, RNMR will prompt for a
direction sequence with the current sequence for ndim dimensions as the default. This sequence is a string of ndim
integers from 1 to ndim with no repeats. For example, if ndim is 2, the legal direction sequences are 12 and 21, while
for an ndim value of 3, seq may be 123, 132, 213, 231, 312, or 321.  If seq fails to assign each dimension a direction,
then RNMR completes the sequence with the missing dimensions in ascending order. Thus, if ndim is 4 and the user enters
the direction sequence 32, RNMR fills in the missing two fields to make the sequence 3214. If the user accepts the
current direction sequence for ndim dimensions, no changes are made.
## DL
Delete records

Category: Data Storage

Format: `DL` first last

Defaults: iwrec none

Description:
`DL` deletes all archive records by record number from first to last. Deleting records marks the appropriate title
records and blocks of the data file (\*DATA.DAT) as available for reuse. Neither the size of the title file nor the data
file is reduced by `DL`; in order to compress the data file by eliminating deallocated blocks, use `SQZ` (an RNMR
command) or SQZARC (from the shell).

Since both first and last are record numbers, each must be an integer from 1 to 200, inclusive. Further, last must be
greater than or equal to first. If first and last are equal, only one record is deleted. If first is omitted, RNMR will
prompt for the number of the first record to be deleted with a default of the last record that was written to. However,
if last is omitted, RNMR will not prompt for its value and only one record, first, will be deleted.

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
## DLTFIL
Delete file

Category: File IO

Format: `DLTFIL` file

Defaults: temp.dat

Description:
`DLTFIL` deletes a specified file. If no file is provided RNMR will prompt for a file to delete with temp.dat as a
default. Be cautious when using `DLTFIL` as RNMR will not prompt for confirmation and will permanently delete the
specified file.
## DLTLST
Delete list

Category: File IO

Format: `DLTLST` nam

Defaults: temp

Description:
`DLTLST` deletes a specified list. If no list is provided RNMR will prompt for a list to delete with temp as a default.
## DLTMAC
Delete list

Category: Macro

Format: `DLTMAC` nam

Defaults: temp

Description:
`DLTMAC` deletes a specified macro. If no macro is provided RNMR will prompt for a macro to delete with temp as a
default.
## DLTTBL
Delete name table

Category: Tables

Format: `DLTTBL` nam

Defaults: temp

Description:
`DLTTBL` deletes a specified name table. If no table is provided RNMR will prompt for a table to delete with temp as a
default.
## DLY
Set pulse programmer delay

Category: Acquisition

Format: `DLY` name time

Qualifiers: /DLY /PLS

Qualifier Defaults: /DLY

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD); RNMRA only

Description:
`DLY` sets the length of a pulse program delay indicated by name. /DLY will interpret time in milliseconds while /PLS will interpret time in microseconds. The length of a delay can range from 0 to 40 seconds. A pulse program must be loaded using `PPEX` in order for `DLY` to be used to set the length of any delays.

Due to restrictions on the speed of the pulse programmer delays are rounded to the nearest 10 microseconds. Delays may be entered with more precision than this limit, but the additional precision will have no effect on the actual length of the delay.
## DO
Begin macro `DO` loop

Category: Macro

Format: `DO`  beg end nam

Qualifiers: /GBL /LCL /SYM

Qualifier defaults: /LCL

Defaults: 1 beg none

Prerequisites: Macro only (MAC)

Description:
`DO` begins a `DO` loop in a macro. All macro commands between `DO` and `ENDDO` will be repeated according to the
user's specifications for beg and end. The loop counter will have the value beg on the first pass through the do loop.
It will be incremented by one on each subsequent pass and will have the value of end on the final pass. Thus beg and end
specify how many time to execute the loop. If beg is omitted it will be set to 1. If end is omitted it will be set to
beg (i.e. one cycle will be done). If end is less than beg no pass through the `DO` loop will occur. Both beg and end
must be integers.

Optionally, `DO` may create and increment a local argument, global argument, or symbol to store the current iteration
count by specifying am. If nam is omitted no loop counter variable will be created Note that any modifications to this
variable by commands between `DO` and `ENDDO` will not affect the number of repetitions.

`DO` loops may be nested up to a depth of 16. Jumps out of `DO` loops are permitted, but a jump into a `DO` loop is not
allowed except as part of an extended range. It is legal to jump out of a `DO`/`ENDDO` loop then jump back in again
after executing one or more statements. The range of the `DO`/`ENDDO` loop is thus extended to include all the
statements after the jump out and before the jump back in. Jumps into a `DO` loop are not allowed when that `DO`
command has not yet been processed, though the error will not be detected until the matching `ENDDO` statement is
executed.
## DW
Set dwell time for data sampling during acquisition

Category: Acquisition

Format: `DW` usec

Defaults: current

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`DW` sets the dwell time for analog-to-digital conversion, in microseconds. The dwell time is defined to be the time
per point used in digitizing the FID. This time is related to the sweep width after Fourier transformation by
SW=1.0E+06/DW. The `DW` command takes one parameter, "usec" which is the dwell time in microseconds. If this parameter
is omitted, RNMR will prompt for a dwell time with the current `DW` as the default. Note that although pulselengths are
specified only to one decimal place in microseconds, dwell times are considered precise to 0.01 usec. If the user
accepts the current dwell time (by pressing <RETURN\> at the `DW` prompt), no changes are made. Otherwise, the user must
enter the new dwell time as a floating point number strictly greater than zero. The dwell time "usec" requested by the
user may be adjusted by RNMR to meet certain analog-to-digital converter (ADC) restrictions. If RNMR is forced to adjust
the dwell time from the value requested by the user, an informational message is displayed reporting the adjusted dwell
time.

On spectrometers with audio filters under computer control via S-bus, changing the dwell time resets the filter cutoff
frequencies. The filter setting is identical for the real and imaginary channels. Since the filter frequencies are
digitally programmed, only discrete cutoff values (in increments of 200.0 Hz up to 50000.0 Hz) are allowed. Accordingly,
RNMR sets the filters to the closest available values given the new dwell time and the current filter factor (as
displayed and set by `FLF`). If the filter factor is 0.0, then the filters are disabled entirely. Otherwise, they are
set to the nearest cutoff setting at least as wide as FLF X (SW/2.0). If the calculated filter bandwidth exceeds
50000.0 Hz, then the filters are disabled entirely. Whenever the dwell time is changed, the shot counter and averager
are zeroed. Finally, if the acquisition buffer is currently visible, `DW` always updates the display.

# E
---
## ECDB
Convert dimension values to linear block index

Category: Misc.

Format: `ECDB` rec ndim val...

Defaults: last_read 1 first...

Description:
`ECDB` takes a series of values (val...) corresponding to each block dimension of a blocked record and converts the
position they refer to into a linear block index. The conversion uses information about the block layout of a record rec
which defaults to the last record that was read. For example when used on a dataset from an unprocessed multi
dimensional experiment stored as a blocked record, `ECDB` will convert a set of indirect dimension time values into a
linear block index.

The value of ndim must not exceed the number of block dimensions. For a 2D dataset this would be 1 for a 3D it would be
2 etc. ndim specifies how many dimensions are accounted for before the linear index. For example in a 3D data set ndim
set to 1 will indicate that only the direct dimension is already accounted for and the linear index is over the last two
dimensions. This will use two input values corresponding to the positions in the other two dimensions. A value of 2 on
the other hand would consider the linear index to only be over the final dimension and only one value will be used.

If fewer values are provided than are needed for the conversion RNMR will prompt for the remaining values with the first
point in the value corresponding to the first point in the relevant dimension as the default. The values will be rounded
to the nearest point in the block grid for conversion. Values that are outside of the range of dataset will round to the
point on the edge of the dataset.
## ECDBP
Convert vector indices to linear block index

Category: Misc.

Format: `ECDBP` rec ndim ind...

Defaults: last_read 1 1...

Description:
`ECDBP` takes a series of indices (ind...) corresponding to each block dimension of a blocked record and converts the
position they refer to into a linear block index. The conversion uses information about the block layout of a record rec
which defaults to the last record that was read.

The value of ndim must not exceed the number of block dimensions. For a 2D dataset this would be 1 for a 3D it would be
2 etc. ndim specifies how many dimensions are accounted for before the linear index. For example in a 3D data set ndim
set to 1 will indicate that only the direct dimension is already accounted for and the linear index is over the last two
dimensions. This will use two input indices corresponding to the positions in the other two dimensions. A value of 2 on
the other hand would consider the linear index to only be over the final dimension and only one index will be used.

If fewer indices are provided than are needed for the conversion RNMR will prompt for the remaining values with 1 as the default
the first. The indices must not exceed the size of the dataset.
## ECDREC
Encode archive index

Category: Data Storage

Format: `ECDREC` arv rec

Defaults: 1 1

Description:
`ECDREC` takes an archive arv and a record number rec within that archive and encodes it in a form that can be used to
access that record. For example:

    ECDREC 2 7

will print 2:7 as informational message. 2:7 can be used anywhere a record must be specified to refer to record 7 in
archive 2. RNMR will prompt for both the archive and record number with a default of 1 if they are not specified.
## ECHO
Rearrange buffer to simulate echo data

Category: Data Manipulation

Format: `ECHO` time

Defaults: center

Prerequisites: Time domain

Description:
`ECHO` takes a time domain buffer with an FID in it and simulates an echo signal from it. The original FID will be
shifted to the left by an amount specified by time. The portion of the buffer vacated by this shift is filled with the
complex conjugate of the reverse of the data that was in this region in the original FID. If time is not provided RNMR
will prompt for it with a time value corresponding to the center of the buffer.
## EDTFIL
Edit text file

Category: File IO

Format: `EDTFIL` fspec

Defaults: temp.dat

Description:
`EDTFIL` opens a pop up window to edit the text file specified by fspec. If no file is specified RNMR will prompt for
one with temp.data as a default.
## EDTLST
Edit list

Category: Lists

Format: `EDTLST` nam

Defaults: temp

Description:
`EDTLST` opens a pop up window to edit the list specified by nam. If no list is specified RNMR will prompt for one with
temp as a default.
## EDTMAC
Edit macro

Category: Lists

Format: `EDTMAC` nam

Defaults: temp

Description:
`EDTMAC` opens a pop up window to edit the macro specified by nam. If no macro is specified RNMR will prompt for one
with temp as a default.
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

Qualifiers: /PROMPT /NOPROMPT

Qualifier Defaults: /NOPROMPT

Defaults: current

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`EM` performs exponential multiplication apodization. In this apodization, the FID is multiplied by a decaying real
exponential function. This results in a broadening of spectral lines after Fourier transformation which masks noise at
the expense of resolution. When a perfect, non-decaying complex sine wave is exponentially multiplied and Fourier
transformed, the result is a perfect Lorentzian line-shape. While the user need not be currently viewing the processing
buffer in order to use `EM`, `EM` operates only on processing buffer 1.

`EM` takes one argument, lb which is the line broadening factor expressed in the current default frequency units (Hz,
kHz, or MHz), as set and displayed by `UNIT /FREQ` or by `UNIT /FREQ /DFLT` if `UNIT /FREQ` is PPM. The legal values of
lb are real numbers between -1000 Hz and 1000 Hz, inclusive.  If lb is omitted, RNMR will not prompt for a value unless
the /PROMPT qualifier is used but rather will perform the apodization with the current line broadening factor, as set
and displayed by the command `LB`. If a legal value of lb is specified, the current line broadening factor will be
updated before exponential multiplication of the data. `EM` multiplies each block of processing buffer 1 by the real
function:

    F(I) = EXP(-PI*(I-1) * LB/SW)

where I is the index of the data point (I=1,2,...), `LB` is the line broadening factor, and `SW` is the buffer sweep
width. If the processing buffer is currently visible, `EM` always updates the display.
## ENDDO
End a macro `DO` loop

Category: Macro

Format: `ENDDO`

Prerequisites: Macro only (MAC)

Description:
`ENDDO` marks the end of a macro `DO` loop. All commands between `DO` and `ENDDO` are executed repeatedly according to
the parameters of the `DO` command. For usage details see the description of `DO`.
## ENDSEL
End a macro `SEL` block

Category: Macro

Format: `ENDSEL`

Prerequisites: Macro only (MAC)

Description:
`ENDSEL` marks the end of a macro `SEL` block. All `CASE` commands for the `SEL` block must precede `ENDSEL`. For usage
details see the description of `SEL`.
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

Format: `EX` nam

Defaults: current

Prerequisites: Acquisition stopped (HALT), RNMRA only

Description:
`EX` is an old command for loading a pulse program. It has been replaced with the `PPEX` command and is currently simply
an alias to it. As such `PPEX` should be used in place of `EX`.
## EXIT
Exit program

Category: Misc.

Format: `EXIT` resp

Qualifiers: /ERROR

Qualifier Defaults: none

Defaults: no

Prerequisites: Command line only

Description
`EXIT` exits RNMR. the argument resp should be a yes/no (or y/n) to indicate whether to actually exit RNMR or not. If
resp is not provided RNMR will prompt for it with no as a default.

If /ERROR is used RNMR will return with a status of 2 to indicate an error. Otherwise it will exit with a status of 1.
## EXP
Export buffer to foreign format

Category: Foreign

Format: `EXP` format fspec

Defaults: ascii default_name

Description:
`EXP` exports the contents of processing buffer 1 to a disk file in a foreign (non-RNMR) format. This exportation allows
one-dimensional data to be transferred from RNMR to another processing program or from one RNMR archive to another via
`IMP`.

If no format is specified RNMR will prompt for it with a default of ASCII. The currently supported foreign formats are:

- ASCII
- BINARY
- BRUKER
- MESTRE
- NV
- PIPE
- SIFT
- UCSF
- VNMR

Note that while the user need not be viewing the processing buffer to use `EXP`, `EXP` exports only the contents of
processing buffer 1. If the `EXP` command is used at console level and fspec is not provided, RNMR will prompt the user
for the name of the file to contain the exported data. The default file name in the prompt will depend upon the archive
and record currently being viewed in processing buffer 1. By default `EXP` will store data in the user's foreign
directory.

Unlike `OPNWRT`, `EXP` will create a new version of the output file if there already exists a file in the current
directory with the name entered by the user. Note that if processing buffer 1 is divided into two or more blocks, `EXP`
writes out data from the first block only.
## EXP1D
Export 1D data to foreign format

Category: Foreign

Format: `EXP1D` format rec slice fspec

Defaults: pipe last_read 1 default_name

Description:
`EXP1D` exports a one-dimensional slice of a blocked archive record to a file in a foreign (non-RNMR) format. This
exportation allows one-dimensional data to be transferred from RNMR to another processing program or from one RNMR
archive to another via `IMP1D`.

If no format is specified RNMR will prompt for it with a default of pipe. The currently supported foreign formats are:

- ASCII
- BINARY
- BRUKER
- NV
- PIPE
- SIFT
- UCSF
- VNMR

The second parameter, rec specifies the number of a blocked archive record containing the data to be exported. If this
parameter is omitted, RNMR will prompt for a source record number with the current read record (as displayed and set by
`PTRA`) as the default.

The last parameter, slice specifies which 1D slice of a 2D, 3D, or 4D source record should be written out in the foreign
format. If the source record has only one dimension, slice must be 1. If slice is omitted RNMR will not prompt for it
and will export the first slice. Note that the current mapping of dimensions to directions (as displayed and set by
`DIRB`) will affect the selection of which one-dimensional block of the record comprises the 1D slice and will thus be
exported. Slice is interpreted as a linear index over the 2nd/3rd/4th dimensions.

If the `EXP1D` command is used at console level and fspec is not provided, RNMR will prompt the user for the name of the
file to contain the exported data. The default file name in the prompt will depend upon the record number, slice and the
name of the archive the record is in. By default `EXP1D` will store data in the user's foreign directory.

Unlike `OPNWRT`, `EXP1D` will create a new version of the output file if there already exists a file in the current
directory with the name entered by the user.

Upon completion, the current read block of the record, as set and displayed by `PTRB`, is set to the slice that was
exported. In addition, the current read record, as set and displayed by `PTRA`, is set to rec.
## EXP2D
Export 2D data to foreign format

Category: Foreign

Format: `EXP2D` format rec slice fspec

Defaults: pipe last_read 1 default_name

Description:
`EXP2D` exports a two-dimensional slice of a blocked archive record to a file in a foreign (non-RNMR) format. This
exportation allows two-dimensional data to be transferred from RNMR to another processing program or from one RNMR
archive to another via `IMP2D`.

If no format is specified RNMR will prompt for it with a default of pipe. The currently supported foreign formats are:

- ASCII
- BINARY
- BRUKER
- NV
- PIPE
- SIFT
- UCSF
- VNMR

The second parameter, rec specifies the number of a blocked archive record containing the data to be exported. If this
parameter is omitted, RNMR will prompt for a source record number with the current read record (as displayed and set by
`PTRA`) as the default.

The last parameter, slice specifies which 2D slice of a 3D or 4D source record should be written out in the foreign
format. If the source record has only two dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it
and will export the first slice. Note that the current mapping of dimensions to directions (as displayed and set by
`DIRB`) will affect the selection of which one-dimensional blocks of the record comprise the 2D slice and will thus be
exported. Slice is interpreted as a linear index over the 3rd/4th dimensions.

If the `EXP2D` command is used at console level and fspec is not provided, RNMR will prompt the user for the name of the
file to contain the exported data. The default file name in the prompt will depend upon the record number, slice and the
name of the archive the record is in. By default `EXP2D` will store data in the user's foreign directory.

Unlike `OPNWRT`, `EXP2D` will create a new version of the output file if there already exists a file in the current
directory with the name entered by the user.

Upon completion, the current read block of the record, as set and displayed by `PTRB`, is set to the slice that was
exported. In addition, the current read record, as set and displayed by `PTRA`, is set to rec.
## EXP3D
Export 3D data to foreign format

Category: Foreign

Format: `EXP2D` format rec slice fspec

Defaults: pipe last_read 1 default_name

Description:
`EXP3D` exports a three-dimensional slice of a blocked archive record to a file in a foreign (non-RNMR) format. This
exportation allows three-dimensional data to be transferred from RNMR to another processing program or from one RNMR
archive to another via `IMP3D`.

If no format is specified RNMR will prompt for it with a default of pipe. The currently supported foreign formats are:

- ASCII
- BINARY
- BRUKER
- NV
- PIPE
- SIFT
- UCSF

The second parameter, rec specifies the number of a blocked archive record containing the data to be exported. If this
parameter is omitted, RNMR will prompt for a source record number with the current read record (as displayed and set by
`PTRA`) as the default.

The last parameter, slice specifies which 3D slice of a 4D source record should be written out in the foreign format. If
the source record has only three dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it and will
export the first slice. Note that the current mapping of dimensions to directions (as displayed and set by `DIRB`) will
affect the selection of which one-dimensional blocks of the record comprise the 3D slice and will thus be
exported. Slice is interpreted as a linear index over the 4th dimension.

If the `EXP3D` command is used at console level and fspec is not provided, RNMR will prompt the user for the name of the
file to contain the exported data. The default file name in the prompt will depend upon the record number, slice and the
name of the archive the record is in. By default `EXP3D` will store data in the user's foreign directory.

Unlike `OPNWRT`, `EXP3D` will create a new version of the output file if there already exists a file in the current
directory with the name entered by the user.

Upon completion, the current read block of the record, as set and displayed by `PTRB`, is set to the slice that was
exported. In addition, the current read record, as set and displayed by `PTRA`, is set to rec.
# F
---
## F
Set synthesizer offset frequency

Category: Frequency Control

Format: `F` chan freq

Defaults: 1 current

Prerequisites: For RNMRA: Acquisition stopped (HALT). For RNMRP:	no restrictions

Description:
`F` sets the frequency offset of a spectrometer synthesizer. When `F` is used in RNMRA `F` resets the actual output
frequency as well as the scale offset for processing. In RNMRP, the `F` command only affects the frequency scale offset.

The synthesizer to be set is selected by chan which refers to a logical channel. If chan is omitted, RNMR will prompt
for a synthesizer number with 1 as the default. Since RNMR currently supports up to four synthesizers, legal values of
chan are integers from 1 to 4. The synthesizer selected must have an assigned nucleus. To assign a nucleus to a
synthesizer, use the command `NUC`.

The frequency offset will be set to freq. If freq is omitted RNMR will prompt for it with the current offset as the
default. The offset is in the current frequency unit as set and displayed by `UNIT /FREQ`, and takes into account the
reference frequency for the nucleus assigned to the channel. The frequency offset set by `F` is considered to be precise
to 0.1 Hz, regardless of the choice of frequency units or number of decimal places (`NDEC`).

The actual frequency output by the spectrometer is a function of the reference frequency and PPM to Hz conversion factor
of the synthesized nucleus as well as the offset selected by the `F` command:

    Factual(Hz) = 1.0E+06*FPPM(MHz) + FREQ(Hz) + FREF(Hz)

where FPPM is the PPM to Hz conversion factor and FREF is the reference frequency of the nucleus assigned to the
selected synthesizer and FREQ is the frequency entered with the `F` command. Thus, if `NUC 1` is H1 with
`NUCD H1 359.600 250.0`, and `UNIT /FREQ` is Hz, entering `F 1 1000.0` gives an actual channel 1 frequency of
359.6012500 MHz. The PPM to Hz conversion factor thus provides the base frequency, which is offset by small amounts
using the `F` command.

In RNMRP, `F` modifies the offset of processing buffer 1. The user need not be viewing this buffer to use the `F`
command. The actual offset will be set to FREQ(Hz) + FREF(Hz), where FREF is the reference frequency for the nucleus
assigned to chan. If the processing buffer is currently visible, `F` will update the display whenever the offset is
modified to show the new frequency scale. All other aspects of the `F` command are identical in RNMR and RNMRP. Thus,
the `F` command in RNMRP serves to make corrections to the frequency scales stored with experimental spectra.
## FLAG
Set pulse program flag on or off

Category: Acquisition

Format: `FLAG` ind val

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD); RNMRA only

Description:
`FLAG` sets the pulse program flag specified by ind either on or off based on val. If ind is not provided RNMR will
prompt for it with a default of 1. If val is not provided RNMR will prompt for it with the current value of the flag as
the default. The legal values of val are on and off.
## FLF
Set filter factor

Category: Acquisition

Format: `FLF` factor

Defaults: current

Prerequisites: Acquisition stopped (HALT) RNMRA only

Description:
On spectrometers with S-bus interfaced acquisition filters, `FLF` sets the filter bandwidth factor. This factor is used
to compute the cutoff frequencies for both the real and imaginary channel filters. `FLF` takes one parameter, factor
which specifies the filter cutoff scaling factor. If this parameter is omitted, RNMR will prompt for a factor with the
current filter factor as the default. The allowable values for factor are real numbers from 0.0 to 5.0, inclusive. Since
the filter frequencies are digitally programmed, only discrete cutoff values (in increments of 200.0 Hz up to 50000.0
Hz) are allowed. Accordingly, RNMR sets the filter cutoffs to the closest available value given the current dwell time
(as displayed and set by `DW`) and the filter factor (as displayed and set by `FLF`). If the filter factor is 0.0, then
the filters are disabled entirely. Otherwise, they are set to the nearest cutoff setting at least as wide as
FLF X (SW/2.0). If the calculated filter bandwidth exceeds 50000.0 Hz, then the filters are disabled entirely. Note that
larger values of factor give wider filter cutoffs. The filter factor is saved to archive records by the commands `SA`,
`SB`, and `SS` and is reported for those records by `LP`, even if S-bus filter control is not implemented in the
spectrometer running RNMR.
## FMX
Set frequency modulation value

Category:

Format: `FMX` chan ind val

Defaults: 1 1 current

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
The transmitter frequency can be changed between different values during a pulse sequence by using the `SETFMX` command
in the pulse sequence. The offset value that is switched to is set using `FMX`. The chan and ind parameters are used to
specify which frequency offset is being set. `SETFMX` has an index as a parameter and that index corresponds to ind. The
offsets are set separately for each channel and chan specifies the logical channel. If chan or ind is not specified RNMR
will prompt for it with 1 as a default. The offset value to be set is specified by val. If val is not provided RNMR will
prompt for it with the current offset as the default.
## FMXEX
Load frequency modulation program

Category:

Format: `FMXEX`

Defaults:
## FOLD
Fold data buffer

Category: Data Manipulation

Format: `FOLD` nsect

Defaults: 1

Description:
`FOLD` divides processing buffer 1 into nsect evenly spaced sections and then averages the sections. If nsect is not
specified RNMR will prompt for it with a default of 1. If nsect is equal to 1 then `FOLD` has no effect.
## FSYS
Set spectrometer system frequency

Category: Frequency Control

Format: `FSYS` nuc hi lo

Defaults: current current current

Description:
`FSYS` sets the spectrometer system frequency by setting the PPM to Hz conversion factor (hi) and reference frequency
(lo) in Hz for a particular nucleus (nuc). The system frequency depends only on the strength of the magnetic field for
the spectrometer running RNMR. All nucleus table entries are referenced to the system frequency so that when `FSYS` is
called, the PPM to Hz conversion factors and reference frequencies of all known nuclei are modified appropriately.

If nuc is not provided RNMR will prompt for it with the curent reference nucleus as the default. If hi or lo is not
provided RNMR will prompt for them with the current values for the specified nucleus. The hi frequency must be between
1.0 and 1000.0 inclusive while lo must be between -1E6 and 1E6 inclusive.

`FSYS` stores the new system frequency and updates the nucleus table. Both the reference frequency and PPM to Hz
conversion factor of each nucleus are updated. While `FSYS` changes the frequency values of each nucleus, the
synthesizers are not updated with these new frequencies until the user issues a `NUC`, `F`, or `FSYN` command for each
synthesizer.
## FT
Fourier transform FID

Category: Data Manipulation

Format: `FT` size fctr1

Qualifiers: /REAL /SCALE

Qualifier Defaults: /SCALE=NORM

Defaults: next_power_2 0.5

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`FT` performs a Fourier transform on time domain data in processing buffer 1. Prior to the transformation the time
domain data is zero filled to size and the first point is scaled by fctr1.

If size is provided it must be a power of 2. If size is not provided then RNMR will not prompt for it and will use the
next power of 2 that is larger than the size of the buffer. If fctr1 is not provided RNMR will not prompt for it and
will use 0.5. The value of fctr1 must be greater than 0.

The /REAL qualifier will cause `FT` to perform a real Fourier transform using only the real part of the buffer.
Otherwise a complex Fourier transform will be applied. /SCALE determines how the result of the transform will be scaled
as follows:

/SCALE | Description
------ | -----------
NORM   | Normalizes buffer
ABS    | Scales to absolute scale factor
NONE   | Does not scale

Since time domain data is presented with minimum time on the left while frequency data is presented with maximum
frequency on the left (by long standing NMR convention), the default action of `FT` is to reverse the order of the data
after transformation. This is done by conjugating the FID before the Fourier transform is calculated. `FT` also negates
every other point in the FID.

If the processing buffer is currently visible, `FT` always updates the display to show the transformed data. If
processing buffer 1 is partitioned into two or more blocks, `FT` acts separately on each block. Thus, multiple FID's
may be transformed to yield multiple spectra with a invocation of the `FT` command. `FT` may only be used to transform
time domain data into the frequency domain. To perform the reverse transformation, use `IFT`.

# G
---
## GA
Get archive record data

Category: Data Storage

Format: `GA` rec buf

Defaults: current 1

Description:
`GA` reads data from an archive record to a processing buffer. The parameters and data of the buffer are replaced with
corresponding values read from the disk record. Most RNMR commands require that data stored in an archive file be read
into a buffer before further processing may be performed.

The first parameter, rec specifies the number of a archive record containing the data to be exported. If this
parameter is omitted, RNMR will prompt for a source record number with the current read record (as displayed and set by
`PTRA`) as the default. Unlike most other RNMR commands, pressing <RETURN\> at the REC prompt to accept the current read
record does cause RNMR to refresh the buffer. `GA` cannot be used to read scratch records which must be accessed with
`GS` or blocked records which must be accessed with `GB`.

The second parameter, buf specifies which processing buffer should receive the data and parameters from record rec. If
buf is omitted, the archive record will be read into processing buffer 1. RNMR does not prompt for buf.

In order to read record rec into buffer buf, the allocated size of the buffer must be greater than or equal to the size
of the archive record. To check and, if necessary, modify the allocated buffer size, use the command `DBSZ`.

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
assigned to each synthesizer in the disk archive. For each synthesizer with an assigned nucleus, RNMR defines (or
redefines) the table entry for that nucleus with its reference frequency and PPM to Hz conversion factor as stored in
the disk archive.  For each synthesizer, the buffer frequency table is initialized with all values marked as undefined
(\*) and the buffer inherits the nucleus, offset, and phase sense (SR flag) assigned to  that synthesizer. Other
hardware acquisition parameters (e.g. `PWR`, `GAIN`, `DW`, etc.) are inherited by the buffer without change so that the
user may list the parameters for a given archive record by entering `GA` then `LP`. Note that the title entries for
each archive record store the values of only the first eight pulses, delays, and loops, so the values of P 9 through P
16, etc. will not be transferred to the buffer's parameter table and will not be printed out by `LP`. Despite this, the
values of all 32 PP flags are stored on disk and are transferred by `GA`.

Whether record rec has already been read into buffer buf or not, RNMR sets the observe (direction 1) synthesizer number
of the buffer equal to the corresponding value for the record. When a new record is read into the buffer, the software
acquisition parameters (e.g. `NAMD`, `NA`, `NWAIT`, etc.) are transferred from the source record to the buffer parameter
table. `GA` always updates the buffer to reflect the archive record's first direction size, domain, time or frequency
scale, and dimension, and phase and scale factors.  After the data is read from the archive record to the processing
buffer, the active size of the buffer becomes the size of the record. `GA` updates the current read record pointer (as
displayed and set by `PTRA`) to rec and updates the display if processing buffer buf is currently visible.
## GAIN
Set receiver gain

Category: Acquisition

Format: `GAIN` gain

Defaults: current

Prerequisites: RNMRA only

Description:
`GAIN` sets the observe channel receiver gain. `GAIN` takes one parameter, gain which is the relative receiver gain. If
this parameter is omitted, RNMR will prompt for the receiver gain with the current gain as the default. The receiver
gain is a real number between 0.0 and 100.0, inclusive and is considered precise to 0.1.
## GAINL
Set lock receiver gain

Category: Lock

Format: `GAINL` gain

Defaults: current

Prerequisites: RNMR lock control. (RNMRA only.)

Description:
`GAINL` sets the lock channel receiver relative gain. This command sets the gain only if RNMR lock channel control has
been implemented on the spectrometer running RNMR. Unlike `GAIN`, the current value of `GAINL` is not stored in the
title records and is not available from `LP`.

`GAINL` takes one parameter, gain which is the relative receiver gain. If this parameter is omitted, RNMR will prompt
for the receiver gain with the current gain as the default. The receiver gain is a real number between 0.0 and 100.0,
inclusive and is considered precise to 1.0.
## GAV
Get data from averager

Category: Acquisition

Format: `GAV` iblk ipro

Defaults: 1 1

Prerequisites: pulse program must currently be loaded and acquisition must be stopped. (RNMRA only.)

Description:
`GAV` transfers data and parameters from the averager to a processing buffer. `GAV` must be used in order to process
data acquired by the spectrometer hardware. The averager memory may be logically partitioned into two or more blocks so
that multiple FID's with different experimental parameters can be acquired at once, without the need to start and stop
acquisition many times. Once acquisition is stopped, `GAV` transfers one of these blocks to the processing buffer
according to the user's choice of iblk and ipro. The number of averager blocks is displayed and set by the RNMR command
`NABLK`, while the number of buffer segments is set by `DBSZA` (for the acquisition buffer) and `DBSZ` (for the
processing buffers).

`GAV` initially transfers averager data and the first 16 pulse programmer parameters (pulse, delay, loop, and flag
values) from the averager hardware to RNMR's averager data buffer. Next, certain averager buffer parameters are
initialized, as described below. Finally, the data and all parameters from the acquisition buffer are copied to the
specified processing buffer. Because `GAV` transfers all the acquisition buffer parameters to a processing buffer after
spectrometer data has been acquired, setting an acquisition parameter before collecting data ensures that it will be
inherited by the processing buffer upon completion of the experiment. For example, one may ensure that data to be
collected will be saved to disk with a given title by using `TITLEA` to set the acquisition buffer title before starting
an experiment. Once this is done, `GAV` will transfer this title to the processing buffer, so no `TITLE` command need
be issued before saving the experiment to disk.  This is equivalent to entering the title using the `TITLE` command
after `GAV` and before saving to disk.  Acquisition buffer commands which may be used to set up an experiment in this
way include `IDNA`, `OFFA`, `REFA`, and `TITLEA`.

The first parameter, iblk specifies the averager block to be transferred to a processing buffer. If iblk is omitted RNMR
will not prompt for it and will transfer block 1.

The second parameter, ipro specifies which processing buffer is to receive the averager parameters and data. If this
parameter is omitted, the averager will be transferred to processing buffer 1 (the visible processing buffer). RNMR
will not prompt for ipro.

Before transferring data, RNMR checks that the size of each averager block (as displayed and set by `DBSZA`) does not
exceed the size of each block in the averager data buffer (as displayed and set by `SIZE`).

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

When `GAV` transfers the averager data to the destination buffer, the data are scaled by 1/(IA\*ADCMAX) where IA is the
number of signal averaged shots actually taken and ADCMAX is the largest intensity that the spectrometer's analog to
digital converter (ADC) can represent.  If a given ADC yields N-bit signed integer data, then ADCMAX = 2.0\*\*(N-1).  If
no signal averaged shots were taken, the data are scaled by 1/ADCMAX instead. If the processing buffer ipro is currently
visible, `GAV` updates the display to show the data transferred from the averager.
## GB
Get blocked record data

Category: Data Storage

Format: `GB` rec blk buf nblk

Defaults: current next 1 1

Description:
`GB` reads data from a blocked record to a processing buffer. The parameters and data of the buffer are replaced with
corresponding values read from the disk record. Most RNMR commands require that data stored in a blocked record be read
into a buffer before further processing may be performed. Since processing buffers are one-dimensional, the user must
specify which one-dimensional slice(s) of the blocked record is to be read into the buffer. In RNMR, this specification
is accomplished with one parameter, the block number. As the block number is incremented from 1, 1D slices along the
first direction are selected for increasing depth in the second direction and minimum height in directions 3 and 4.
Next, 1D slices are read from the next lowest plane in direction 3 with minimum height in direction 4.  When all slices
have been read for minimum height in direction 4, retrieval continues with the next lowest cube. In this way, every
slice along direction 1 is read out with depth in direction 2 varying fastest and height in direction 4 varying most
slowly. Thus, if the block number is incremented to a adequately large number, all data points in the record will have
been selected. Note that the assignment of data points to block numbers is dependent on the direction-to-dimension
mapping set and displayed for each number of dimensions by `DIRB`. As a result, neither the number of blocks in a
record nor the mapping of data points to block numbers is constant.

The first parameter, rec is the record to be retrieved. Scratch records (1-4) must be read with `GS` instead of `GB`.
Archive records (created by `SA` or `CPY` with an archive record source) must be read with `GA`. If rec is omitted, RNMR
will prompt for a record number with the current read record (as displayed and set by `PTRA`) as the default.

The second parameter, blk is used to select the first block of record rec to be transferred. If this parameter is
omitted, RNMR will not prompt for a block number. Instead, blk will default to zero. When blk is set to zero, either
explicitly or by default, the first record block transferred will be determined by the current `PTRB` setting. The
`PTRB` command displays and sets a pointer which marks the current read and write blocks of a given blocked record.
When blk is 0, RNMR begins the transfer with the first block after the current read block (`PTRB`+1).

The third parameter, buf specifies which processing buffer should receive the data and parameters from record rec. If
buf is omitted, the specified blocks of the source record will be read into processing buffer 1. RNMR does not prompt
for buf.

The final parameter, nblk specifies the number of blocks to read from record rec into buffer buf. Since the processing
buffer may be partitioned into two or more segments using the command `DBSZ`, one may read more than one block from rec
into buf with a single invocation of `GB`. This feature is particularly useful when performing operations uniformly on a
multidimensional data set. For example, one may perform a 1K Fourier transform on a blocked record eight blocks at a
time by partitioning the processing buffer into eight segments (e.g. `DBSZ` 1 1024 8) and reading in data eight blocks
at a time (e.g. `GB` 29 0 1 8) for transformation. In this manner, the number of commands to be executed by the
processing macro is reduced by a factor of eight, greatly decreasing the required computation time. If nblk is omitted,
`GB` will transfer only one block, blk, from rec to buf. RNMR does not prompt for the nblk parameter.

Before each block is transferred from rec to buf, RNMR checks that the requested block number is not greater than the
number of blocks in the specified record. The requested block must also have been used, that is it not only must have
been allocated but data must have been stored in it.

Since blocks are transferred one at a time, RNMR reads in as many blocks as possible from those requested by the user.
If at any point one of the error conditions described above occurs, the transfer stops. In this case, all the blocks
that transferred successfully may be processed as usual, but the screen display is not updated.

In order to read one-dimensional slices from a blocked record, RNMR requires that the record has NDIMX sufficiently
large that direction 1 is accessible. NDIMX is the number of dimensions that may be simultaneously accessed in a
blocked record and is a permanent attribute of the record set at allocation time. Regardless of NDIMX, it is always
possible to access a block of data along the first dimension of any given record, but accessing one-dimensional slices
along the higher dimensions requires higher values of NDIMX. In conclusion, in order to read slices along dimension N,
one must have allocated the source record with NDIMX at least N. When NDIMX is too small to allow the requested
retrieval, RNMR displays the error message:

    (RARCX ) DIMENSION INACCESSIBLE

If this error occurs, the user should make sure that direction 1 is assigned the desired dimension by using the `DIRB`
command. If the current `DIRB` setting is correct, then it will be necessary to allocate a copy of the source record
with higher NDIMX using `ALLCPY` and to then copy the data from the source record to the new record using `GB` with an
allowed `DIRB` setting.

The number of points actually used in direction 1 must not exceed the allocated size of each partition in processing
buffer buf. This restriction is enforced because RNMR will attempt to transfer each requested block of the record rec to
a block of the processing buffer. When there are too many points in each block to perform the transfer, RNMR gives an
error message:

    (CKTBPB) SIZE TOO LARGE

 To check and set the allocated size of the processing buffer, use the command `DBSZ` buf.

If the last record read into buffer buf is different from rec, then the following buffer parameters are replaced
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
direction 1 of rec.

When a new record is read into a processing buffer by `GB`, RNMR checks the nucleus assigned to each synthesizer in the
disk archive. For each synthesizer with an assigned nucleus, RNMR defines (or redefines) the table entry for that
nucleus with its reference frequency and PPM to Hz conversion factor as stored in the disk archive. Note that if the
archive contains one or more nucleus entries which are already in the current RNMR nucleus table or if the nucleus table
is full, RNMR will redefine `NUC UNKN` with the nucleus parameters stored with the disk archive. For each synthesizer,
the buffer frequency table is initialized with all values marked as undefined (\*) and the buffer inherits the nucleus,
offset, and phase sense (SR flag) assigned to that synthesizer. Other hardware acquisition parameters (e.g. `PWR`,
`GAIN`, `DW`, etc.) are inherited by the buffer without change so that the user may list the parameters for a given
blocked record by entering `GB` then `LP`. Note that the title entries for each record store the values of only the
first eight pulses, delays, and loops, so the values of P 9 through P 16, etc. will not be transferred to the buffer's
parameter table and will not be printed out by `LP`. However, the values of all 32 PP flags are stored on disk and are
transferred by `GB`. The parameters stored with a given blocked record are set when the first block is stored using `SB`
and are not updated or augmented as additional blocks are written to disk.  Thus, when `LP` lists the parameters of a
blocked record, the parameters reported may not be correct for blocks other than the first stored block.

Whether record rec has already been read into buffer buf or not, RNMR sets the observe (direction 1) synthesizer number
of the buffer equal to the corresponding value for the record. When a new record is read into the buffer, the software
acquisition parameters (e.g. `NAMD`, `NA`, `NWAIT`, etc.) are transferred from the source record to the buffer parameter
table. `GB` always updates the buffer to reflect the archive record's first direction size, domain, time or frequency
scale, and dimension, and phase and scale factors. After the data is read from the archive record to the processing
buffer, the active size of the buffer becomes the size of the record. As each block is successfully transferred from
record rec to buffer `BUF`, RNMR sets the block read pointer to the number of the block just read. This pointer
indicates the current block of a given record and may be set as desired manually with the command `PTRB`. Upon
successful completion, `GB` updates the current read record pointer (as displayed and set by `PTRA`) to rec and updates
the display if processing buffer buf is currently visible.
## GBLARG
Set value of global argument

Category: Arguments

Format: `GBLARG` nam val

Defaults: temp current

Description:
`GBLARG` is an old command for defining global arguments. It has been replaced with the `DFNGBL` command and is
currently simply an alias to it. As such `DFNGBL` should be used in place of `GBLARG`.
## GBLDL
Delete global argument

Category: Arguments

Format: `GBLDL` first last

Defaults: temp first

Description:
`GBLDL` is an old command for deleting global arguments. It has been replaced with the `REMGBL` command and is currently
simply an alias to it. As such `REMGBL` should be used in place of `GBLDL`.
## GENCS
Generate complex sine wave

Category: Data Manipulation

Format: `GENCS` freq phase sw

Defaults: 1.0 0.0 current

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`GENCS` generates a complex sine wave of specified frequency and phase. This sine wave has unit amplitude and replaces
any data currently in the visible processing buffer (buffer 1). Using `GENCS` to create a complex sine and applying
`SC`, `EM`, and `GM` to scale and broaden the data, one may produce a simulated FID with any desired frequency, phase,
amplitude, and Gaussian and Lorentzian line widths. These simulated FID's may be added together to give a waveform
corresponding to a multiline spectrum. Such a simulation is generated by the system macro CONV, which reads frequencies,
amplitudes, and line widths from a text file and uses `GENCS` and other commands to calculate the FID.

The first parameter of `GENCS` is freq, which specifies the frequency of the complex sine wave to be generated. This
frequency should be expressed in the current frequency unit, as set and displayed by the command `UNIT /FREQ`.
Currently, the available units are Hz, kHz, MHz, and PPM. If freq. is omitted, RNMR will prompt for a frequency with
a default of 1 in the current frequency units with the current number of decimal places (as displayed and set by
`NDEC`).

The second parameter, phase, specifies the phase of the complex sine wave in degrees. If this parameter is omitted, RNMR
will generate a complex sine with zero phase; RNMR does not prompt for phase.

The third parameter is the sweep width for the complex sine wave. This sweep width determines the time per point for the
data to be generated and is expressed in the current frequency units. If sw is omitted, RNMR will generate a complex
sine wave with the current buffer sweep width. Legal values for sw are real numbers strictly greater than zero. If a
valid value of sw is entered, RNMR resets the sweep width of the visible processing buffer to sw.

When `GENCS` is executed, the first point of the buffer is always identified with zero time, regardless of its original
time value. Each partition of the visible processing buffer receives an identical complex sine wave whose points are
given by:

    I(k) = EXP(i(phase + (k-1)dphi))  k= 1,...,SIZE

where dphi is 360\*freq/sw. If the frequency scale of the buffer is reversed, phase and dphi will be negated before
computing the complex sine. This will occur when the buffer synthesizer is 0 or when the spectrum reverse flag (`SRFLG`)
for the buffer synthesizer is false.

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
## GENPWDR
Generate complex powder pattern

Category: Data Manipulation

Format: `GENPWDR` freq phase sw fctr

Defaults: 1.0 0.0 current 1.0

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`GENPWDR` generates a complex time domain signal corresponding to a powder pattern. This signal has unit amplitude and
replaces any data currently in the visible processing buffer (buffer 1). The parameter freq sets the width of the powder
pattern in the current frequency units. If freq is omitted RNMR will prompt for it with a default of 1. The parameter
phase controls the phase of the generated signal. If phase is omitted RNMR will not prompt for it and will use a phase
of 0. THe parameter sw is the sweep width in the current frequency units and determines the time per point of the
generated signal. If sw is omitted RNMR will not prompt for it and will use the current buffer sweep width. Legal values
for sw are real numbers strictly greater than zero. If a valid value of sw is entered, RNMR resets the sweep width of
the visible processing buffer to sw. The parameter fctr is a factor controlling the number of orientations that are
considered when generating the signal. The number of orientations is equal to 3*freq*dstep*1e-3*fctr*size or 1 whichever
is larger. Values of fctr must be between 0.5 and 2.0 inclusive.
## GM
Gaussian multiply FID

Category: Data Manipulation

Format: `GM` lb

Qualifiers: /PROMPT /NOPROMPT

Qualifier Defaults: /NOPROMPT

Defaults: current

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`GM` performs a Gaussian multiplication apodization. In this  apodization, the FID is multiplied by a decaying real
Gaussian function. This results in a broadening of spectral lines after Fourier transformation which masks noise at the
expense of resolution. When Gaussian multiplication is applied to a perfect, non-decaying complex sine wave and a
Fourier transform is performed, the result will be a perfect Gaussian line shape. While the user need not be currently
viewing the processing buffer in order to use `GM`, `GM` operates only on processing buffer 1.

`GM` takes one argument, lb which is the line broadening factor expressed in the current default frequency units (Hz,
kHz, or MHz), as set and displayed by `UNIT /FREQ` or by `UNIT /FREQ /DFLT` if `UNIT /FREQ` is PPM. The legal values of
lb are real numbers between -1000 Hz and 1000 Hz, inclusive. If lb is omitted, RNMR will not prompt for a value unless
the /PROMPT qualifier is used but rather will perform the apodization with the current line broadening factor, as set
and displayed by the command `LB`. If a legal value of "lb" is specified, the current line broadening factor will be
updated before Gaussian multiplication of the data. `GM` multiplies each block of processing buffer 1 by the real
function:

    F(I) = EXP-(0.5*PI*(I-1)* LB/SW)^2)

where I is the index of the data point (I=1,2,...), `LB` is the line broadening factor, and `SW` is buffer sweep width.
If the processing buffer is currently visible, `GM` always updates the display.
## GMV
Calculate geometric mean

Category: Data Manipulation

Format: `GMV` src dst

Defaults: 2 1

Description:
`GMV` computes the geometric mean of a complex source buffer src and a complex destination buffer dst and places the
result in the destination buffer:

    DST = SIGN(DST) * SQRT(ABS(DST*SRC))

The geometric means of the real and imaginary parts of the data are computed separately. The arguments src and dst
specify the numbers of the buffers to be processed. If either argument is omitted, RNMR will prompt for a buffer number.
The default source is buffer 2 while the default destination is buffer 1. While `GMV` operates only on processing
buffers, the user need not be viewing the processing buffers to perform the computation. For two buffers to be processed
with `GMV`, they must have the same domain (time or frequency) and the same active size (though not necessarily the same
allocated size). If the destination buffer is partitioned into two or more blocks, each block is separately multiplied
with the corresponding block of the source buffer. The number of blocks in the source buffer need not be the same as
that in the destination buffer. RNMR uses the formula below to match source blocks with destination blocks:

    IBLK_SRC = MOD(IBLK_DST-1,NBLK_SRC) + 1, IBLK_DST=1,...,NBLK_DST

If the processing buffer is currently visible and "dst" is 1, `GMV` always updates the display upon completion.
## GO
Start or resume acquisition

Category: Acquisition

Format: `GO` na

Defaults: current

Prerequisites: (LOAD) by `EX`; the acquisition must be stopped; RNMR only.

Description:
`GO` instructs RNMR to continue acquisition after acquisition has been stopped by `QUIT`. Continuing shots will be
added to the current averager memory and the shot counter will be incremented upward from its current value.

`GO` takes one parameter, na, which is the total number of shots to be taken. Shots already taken before `GO` count
towards this limit. If na is omitted, the current shot limit as set and displayed by `NA` will determine how many
additional shots will be taken; RNMR does not prompt for na.  Legal values for na are -1 and integers greater than or
equal to 1. If na is -1, RNMR will continue acquisition with no limit to the number of shots taken; acquisition will
continue until stopped by `QUIT` or `WAIT`. Before resuming acquisition, RNMR checks that the number of shots already
taken is less than the requested shot limit specified by the `NA` command or the na parameter of `GO`. Unless `NA` or na
is -1, acquisition will not be started if this condition is not satisfied. If na is specified and is greater than the
current number of shots completed, RNMR will replace the current shot limit with na. When acquisition is continued with
`GO`, no delay shots are taken even if `NDLY` is greater than zero. To continue acquisition with one or more delay
shots, use the command `NG`. Unless no shots have been taken yet, `GO` will continue acquisition until `NA` shots have
been completed, regardless of whether `GO` is executed from console ("\>") level or from a macro; this is unlike the
behavior of `DG`.

If `GO` is used to start acquisition before any shots have been completed, data will be acquired until `NA` averaged
shots are complete if `GO` is executed from console level. If `GO` is called from a macro in this situation, acquisition
will continue until `NWAIT` or `NA` shots have been taken, whichever is smaller. If `NWAIT` is 0, then `NA` will
determine the number of shots taken from a macro, and similarly, `NWAIT` shots will be taken if `NA` is -1 and `NWAIT`
is nonzero. In summary, if no shots have been taken, `GO` acts like `ZG` except that neither the averager nor the
acquisition title parameters nor the display is initialized by `GO`. `GO` resets the following averager parameters
to their current settings in RNMR:

Parameter | Description
--------- | -----------
`NABLK`   | Number of averager blocks (logical avg. memory partitions)
`NAMD`    | Length of phase cycle
`NDLY`    | Number of dummy shots to take on `DG` or `NG`
`NDSP`    | Number of shots to take for each display update

Before acquisition is resumed, `GO` also resets the frequency table pointer for each synthesizer so that frequencies
will be generated starting with the first table entry. Once acquisition is restarted, each shot will increment the shot
indicator in the upper right hand corner of the display. If the acquisition block is visible, the current sum of FID's
will be updated on the screen every two seconds or once per shot, whichever is slower.
## GOSUB
Perform call within macro

Category: Macro

Format: `GOSUB` label

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`GOSUB` jumps to a label within a macro much like `GOTO`. When `MEXIT` is encountered after the jump execution will
return to the line following the `GOSUB` call instead of exiting the macro. This allows for setting up and calling
subroutines within a macro.

The parameter label is the name of the macro label to which execution should jump. If label is not specified, execution
will continue at the next line of the current macro. Note that execution will still return to the line after the `GOSUB`
call at the next `MEXIT` even if no label was provided.
## GOTO
Go to statement label in macro

Category: Macro

Format: `GOTO` label

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`GOTO` performs an unconditional jump within a macro. The parameter label is the name of the macro label to which
execution should jump. If label is not specified, execution will continue at the next line of the current macro.
## GOTST
Perform a conditional jump within a macro based on a test

Category: Macro

Format: `GOTST` name args... label1 label2

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
## GREF
Restore processing buffer reference from nucleus table

Category: Frequency Control

Format: `GREF` nuc

Defaults: *

Description:
`GREF` changes the reference frequency (or frequencies) in a processing buffer to match what is stored in the nucleus
table. If nuc is * `GREF` changes the frequency for every channel. Otherwise a valid nucleus must be passed. If nuc is
omitted RNMR will prompt for it with a default of \*. `GREF` only changes the reference frequency parameter for the
processing buffers and does not update the synthesizers.
## GREFA
Restore acqusition buffer reference from nucleus table

Category: Frequency Control

Format: `GREFA` nuc

Qualifiers: /RESET

Qualifier Defaults: none

Prerequisites: RNMRA only

Defaults: *

Description:
`GREFA` changes the reference frequency (or frequencies) in the acquisition buffer to match what is stored in the
nucleus table. If nuc is * `GREFA` changes the frequency for every channel. Otherwise a valid nucleus must be passed. If
nuc is omitted RNMR will prompt for it with a default of \*. `GREFA` only changes the reference frequency parameter for
the acquisition buffer. If /RESET is used `GREFA` will also change the synthesizer frequency and FMU frequency.
## GS
Get data from scratch record

Category: Data Storage

Format: `GS` rec buf

Defaults: 1 1

Description:
`GS` reads data from a scratch record to a processing buffer. The scratch records are records 1 through 4 and may be
deleted but may not be allocated with `ALLB` or `ALLCPY`. Unlike archive records, scratch records may be freely
overwritten; new data and parameters may be written to a scratch record without deleting it first, even if the record is
not owned by the current user. `GS` replaces the parameters and data of the buffer with corresponding values read from
the disk record. Most RNMR commands require that data stored in a disk file be read into a buffer before further
processing may be performed.

The first parameter, rec is the number of the record to be retrieved. The allowable values for rec are integers between
1 and 4, inclusive. The archive records (5-200) must be read with `GA` or `GB` instead of `GS`. If rec is omitted, RNMR
will read data from scratch record 1; RNMR does not prompt for rec.

The second parameter, buf specifies which processing buffer should receive the data and parameters from record rec. If
buf is omitted, the archive record will be read into processing buffer 1. RNMR does not prompt for buf.
In order to read record rec into buffer buf, the allocated size of the buffer must be greater than or equal to the size
of the archive record. To check and, if necessary, modify the allocated buffer size, use the command `DBSZ`.

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

`GS` always sets the buffer IDIMX parameter to 1; IDIMX specifies which dimension of a multidimensional source record is
currently stored in the buffer. When a new record is read into a processing buffer by `GS`, RNMR checks the nucleus
assigned to each synthesizer in the disk record. For each synthesizer with an assigned nucleus, RNMR defines (or
redefines) the table entry for that nucleus with its reference frequency and PPM to Hz conversion factor as stored in
the disk record. Note that if the record contains one or more nucleus entries which are already in the current RNMR
nucleus table or if the nucleus table is full, RNMR will redefine `NUC UNKN` with the nucleus parameters stored with the
disk archive. For each synthesizer, the buffer frequency table is initialized with all values marked as undefined (\*)
and the buffer inherits the nucleus, offset, and phase sense (SR flag) assigned to that synthesizer. Other hardware
acquisition parameters (e.g. `PWR`, `GAIN`, `DW`, etc.) are inherited by the buffer without change so that the user may
list the parameters for a given scratch record by entering `GS` then `LP`. Note that the title entries for each scratch
record store the values of only the first eight pulses, delays, and loops, so the values of P 9 through P 16, etc. will
not be transferred to the buffer's parameter table and will not be printed out by `LP`. Despite this, the values of all
32 PP flags are stored on disk and are transferred by `GS`.

Whether record rec has already been read into buffer buf or not, RNMR sets the observe (direction 1) synthesizer number
of the buffer equal to the corresponding value for the record.  When a new record is read into the buffer, the software
acquisition parameters (e.g. `NAMD`, `NA`, `NWAIT`, etc.) are transferred from the source record to the buffer parameter
table. `GS` always updates the buffer to reflect the scratch record's first direction size, domain, time or frequency
scale, and dimension, and phase and scale factors. After the data is read from the scratch record to the processing
buffer, the active size of the buffer becomes the size of the record. `GS` updates the display if processing buffer buf
is currently visible. Unlike `GA`, `GS` does not update the record read pointer, which is set and displayed by the
command `PTRA`.

# H
---
## HELP
Get online help

Format: `HELP`

Description:
`HELP` obtains information from the RNMR on-line help library. Instructions on navigating the help library are shown at
the bottom of the help window. Note that the information in the help library may not be fully up to date.
## HILB
Perform Hilbert transform on spectrum

Category: Data Manipulation

Format: `HILB`

Prerequisites: Frequency domain data in processing buffer 1 (FREQ)

Description:
`HILB` performs a Hilbert transform on a spectrum. As a consequence of Fourier transformation, the real and imaginary
parts of a complex spectrum are Hilbert transform pairs. Thus, it should be possible to discard the imaginary channel
and then recreate it by performing a Hilbert transform on the real part of the data. Typically, this is done after a
spectrum has received linear phase correction, cubic spline baseline correction, or any other manipulation that results
in the real and imaginary channels no longer being Hilbert transform pairs. Without correction by `HILB`, the inverse
Fourier transform of this data would be incorrect, as evidenced by divergence of the data at long times. `HILB` replaces
the imaginary part of the buffer data with the Hilbert transform of the real part, and leaves the real part of the
buffer unchanged.

The active size of the visible processing buffer must be a power of two greater than or equal to 4. RNMR performs a
Hilbert transform on each block of the visible processing buffer. If the processing buffer is currently visible
(`VIEW PRO`), then RNMR updates the screen display following `HILB`.
## HILBZ
Perform Hilbert transform on zero-filled spectrum

Category: Data Manipulation

Format: `HILBZ`

Prerequisites: Frequency domain data in processing buffer 1 (FREQ)

Description:
`HILBZ` performs a Hilbert transform on a zero filled spectrum. As a consequence of Fourier transformation, the real and
imaginary parts of a complex spectrum are Hilbert transform pairs. Thus, it should be possible to discard the imaginary
channel and then recreate it by performing a Hilbert transform on the real part of the data. Typically, this is done
after a spectrum has received linear phase correction, cubic spline baseline correction, or any other manipulation that
results in the real and imaginary channels no longer being Hilbert transform pairs. Without correction by `HILBZ`, the
inverse Fourier transform of this data would be incorrect, as evidenced by divergence of the data at long times. `HILBZ`
replaces the imaginary part of the buffer data with the Hilbert transform of the real part, and leaves the real part of
the buffer unchanged.

The active size of the visible processing buffer must be a power of two greater than or equal to 4. RNMR performs a
Hilbert transform on each block of the visible processing buffer. If the processing buffer is currently visible
(`VIEW PRO`), then RNMR updates the screen display following `HILBZ`.
## HTR
Enable or disable probe heater

Category: Heater

Format: `HTR` state

Defaults: current

Prerequisites: RNMR heater control. RNMRA only

Description:
`HTR` sets the heater enable flag on or off. This flag enables or disables computer control of the probe temperature.
When the `HTR` command is issued, RNMR checks the current status of the probe heater. If the heater is in ERROR status,
RNMR reports the error and resets the heater status. `HTR` takes one parameter, state, which is ON if heater control
is enabled and OFF otherwise. If state is omitted, RNMR will prompt for the heater enable state with the current
state as the default. The legal values of state are ON and OFF only.
## HTRSTS
Return probe heater status

Category: Heater

Format: `HTRSTS`

Prerequisites: RNMR heater control. RNMRA only

Description:
`HTRSTS` returns the current probe heater status in an informational message. `HTRSTS` directs RNMR to inquire the
heater status directly from the spectrometer hardware. If the status returned by the temperature controller indicates
an error, RNMR will reset the heater status without printing an error message. The heater status value read from the
hardware is displayed via an informational message as a two-character hexadecimal string.

# I
---
## IBOX
Set volume parameters for nD volume integration

Category: Data Manipulation

Format: `IBOX` dim size

Defaults: 1 current

Description:
`IBOX` sets the integration block size for a dimension dim to size. If dim is omitted RNMR will prompt for it with a
default of 1. If size is omitted RNMR will prompt for it with a default of the current integration block size for dim.
## IDN
Set processing buffer identification fields

Category: Data Storage

Format: `IDN` idn val prompt

Defaults: 1 current 'Enter identifier value:'

Description:
`IDN` sets the value of an identifier field for the visible processing buffer. These values are saved in the title
record when the data is saved and may be used to store any desired ancillary information about an experiment, such as
pH, temperature, or sample spinning speed. Currently, there are four identifiers available. `IDN` modifies only the
visible processing buffer (buffer 1), however the user need not be viewing this buffer to use `IDN`.

The first parameter, idn, selects which identifier field is to be modified. The legal values for idn are the integers 1
through 4. If idn is not specified, RNMR will prompt for an identifier number with a default value of 1.

The second parameter, val, is the value to set the identifier field to. If val is omitted, RNMR will prompt for it with
the current value as a default and the third parameter, prompt, as the prompt string. If prompt is omitted the default
prompt string is 'Enter identifier value:'.

Each `IDN` field stores a maximum of 8 characters and is written to the appropriate title record when the visible
processing buffer is saved to disk using the `SA`, `SB`, and `SS` commands. Thus, the identifier fields may be used to
note user-defined conditions for each record. When RNMR starts up, each identifier field is blank. Processing buffer
identifier fields may be displayed and modified only by the `IDN` command.
## IDNA
Set acquisition buffer identification fields

Category: Acquisition

Format: `IDNA` idn val prompt

Defaults: 1 current 'Enter identifier value:'

Prerequisites: RNMRA only.

Description:
`IDNA` sets the value of an identifier field for the acquisition buffer. Following the get averager (`GAV`) command,
these values are saved in the title record when the data is saved and may be used to store any desired ancillary
information about an experiment, such as pH, temperature, or MAS spinning speed. Currently, there are four identifiers
available. `IDNA` modifies only the acquisition buffer, however the user need not be viewing this buffer to use `IDNA`.
When the user transfers averager data and parameters to a processing buffer with `GAV`, the `IDNA` fields are saved to
the corresponding `IDN` fields of that processing buffer. Thus, the user may set up identifier field values (to be
saved to disk after acquisition) before beginning an experiment.

The first parameter, idn, selects which identifier field is to be modified. The legal values for idn are the integers 1
through 4. If idn is not specified, RNMR will prompt for an identifier number with a default value of 1.

The second parameter, val, is the value to set the identifier field to. If val is omitted, RNMR will prompt for it with
the current value as a default and the third parameter, prompt, as the prompt string. If prompt is omitted the default
prompt string is 'Enter identifier value:'.

Each `IDNA` field stores a maximum of 8 characters and is a parameter of the acquisition buffer. When RNMR starts up,
each identifier field is blank. Acquisition buffer identifier fields may be displayed and modified only by the `IDNA`
command.
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

Qualifiers: /REAL /SCALE

Qualifier Defaults: /SCALE=NORM

Defaults: next_power_2 1.0

Prerequisites: Frequency domain data in visible processing buffer (FREQ)

Description:
`IFT` performs an inverse Fourier transform on frequency domain data in processing buffer 1. Prior to the transformation
the frequency domain data is zero filled to size and after the transformation the first point is divided by fctr1.

If size is provided it must be a power of 2. If size is not provided then RNMR will not prompt for it and will use the
next power of 2 that is larger than the size of the buffer. If fctr1 is not provided RNMR will not prompt for it and
will use 0.5. The value of fctr1 must be greater than 0.

The /REAL qualifier will cause `IFT` to perform a real inverse Fourier transform using only the real part of the buffer.
Otherwise a complex inverse  Fourier transform will be applied. /SCALE determines how the result of the transform will
be scaled as follows:

/SCALE | Description
------ | -----------
NORM   | Normalizes buffer
ABS    | Scales to absolute scale factor
NONE   | Does not scale

Since time domain data is presented with minimum time on the left while frequency data is presented with maximum
frequency on the left (by long standing NMR convention), the default action of `IFT` is to conjugate the data after
transformation.  This ensures that performing an `IFT` followed by an `FT` will give the same frequency data order.

Use of `IFT` resets the constant and linear phase values of the  processing buffer (phi0 and phi1) to zero. If the
processing buffer is currently visible, `IFT` always updates the display to show the transformed data. If processing
buffer 1 is partitioned into two or more blocks, `IFT` acts separately on each block. Thus, multiple spectra may be
transformed to yield multiple FID's with one invocation of the `IFT` command. `IFT` may only be used to transform
frequency domain data into the  time domain.  To perform the forward transformation, use `FT`.
## IMP
Import data from foreign format

Category: Foreign

Format: `IMP` format

Defaults: NMR1

Description:
`IMP` imports the contents of a disk file in a foreign (non-RNMR) format to processing buffer 1. This importation allows
one-dimensional data to be transferred to RNMR from another processing program or from one RNMR archive to another via
`EXP`.  Since the foreign data is only read into memory by `IMP`, the user must use `SA`, `SB`, or `SS` to store the
imported data permanently.

If no format is specified RNMR will prompt for it with a default of ASCII. The currently supported foreign formats are:

- ASCII
- BINARY
- BRUKER
- SIFT
- VNMR

Note that while the user need not be viewing the processing buffer to use `IMP`, `IMP` imports data only to processing
buffer 1. If the `IMP` command is used at console level and fspec is not provided, RNMR will prompt the user for the
name of the file containing the data to be imported. The default file name in the prompt will depend upon the archive
and record that was last written to. By default `IMP` will search for data in the user's foreign
directory.

If the processing buffer is currently visible on the screen, RNMR will update the display once the `IMP` operation is
complete.
## IMP1D
Import data from foreign format

Category: Foreign

Format: `IMP1D` format rec slice fspec

Defaults: sift last_written 1 default_name

Description:
`IMP1D` imports the contents of a disk file in a foreign (non-RNMR) format and saves it in a specified one-dimensional
slice of blocked record rec. This importation allows one-dimensional data to be transferred to RNMR from another
processing program or from one RNMR archive to another via `EXP1D`.

If no format is specified RNMR will prompt for it with a default of sift. The currently supported foreign formats are:

- SIFT

The second parameter, rec specifies the number of a blocked archive record in which the imported data should be stored.
If this parameter is omitted, RNMR will prompt for a source record number with the current write record (as displayed
and set by `PTRA`) as the default.

The last parameter, slice specifies which 1D slice of a 2D, 3D, or 4D source record the foreign data should be written
to. If the source record has only one dimension, slice must be 1. If slice is omitted RNMR will not prompt for it and
will write to the first slice. Note that the current mapping of dimensions to directions (as displayed and set by
`DIRB`) will affect the selection of which one-dimensional block of the record comprises the 1D slice and will thus be
written to. Slice is interpreted as a linear index over the 2nd/3rd/4th dimensions.

If the `IMP1D` command is used at console level and fspec is not provided, RNMR will prompt the user for the name of the
file containing the data to be imported. The default file name in the prompt will depend upon the record number, slice
and the name of the archive the record is in. By default `IMP1D` will search for data in the user's foreign directory.

Upon completion, the current write block of the record, as set and displayed by `PTRB`, is set to the slice that was
exported. In addition, the current write record, as set and displayed by `PTRA`, is set to rec.
## IMP2D
Import data from foreign format

Category: Foreign

Format: `IMP2D` format rec slice fspec

Defaults: sift last_written 1 default_name

Description:
`IMP2D` imports the contents of a disk file in a foreign (non-RNMR) format and saves it in a specified two-dimensional
slice of blocked record rec. This importation allows two-dimensional data to be transferred to RNMR from another
processing program or from one RNMR archive to another via `EXP2D`.

If no format is specified RNMR will prompt for it with a default of sift. The currently supported foreign formats are:

- SIFT

The second parameter, rec specifies the number of a blocked archive record in which the imported data should be stored.
If this parameter is omitted, RNMR will prompt for a source record number with the current write record (as displayed
and set by `PTRA`) as the default.

The last parameter, slice specifies which 2D slice of a 3D or 4D source record the foreign data should be written to. If
the source record has only two dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it and will
write to the first slice. Note that the current mapping of dimensions to directions (as displayed and set by `DIRB`)
will affect the selection of which one-dimensional blocks of the record comprises the 2D slice and will thus be
written to. Slice is interpreted as a linear index over the 3rd/4th dimensions.

If the `IMP2D` command is used at console level and fspec is not provided, RNMR will prompt the user for the name of the
file containing the data to be imported. The default file name in the prompt will depend upon the record number, slice
and the name of the archive the record is in. By default `IMP2D` will search for data in the user's foreign directory.

Upon completion, the current write block of the record, as set and displayed by `PTRB`, is set to the slice that was
exported. In addition, the current write record, as set and displayed by `PTRA`, is set to rec.
## IMP3D
Import data from foreign format

Category: Foreign

Format: `IMP3D` format rec slice fspec

Defaults: sift last_written 1 default_name

Description:
`IMP3D` imports the contents of a disk file in a foreign (non-RNMR) format and saves it in a specified three-dimensional
slice of blocked record rec. This importation allows two-dimensional data to be transferred to RNMR from another
processing program or from one RNMR archive to another via `EXP3D`.

If no format is specified RNMR will prompt for it with a default of sift. The currently supported foreign formats are:

- SIFT

The second parameter, rec specifies the number of a blocked archive record in which the imported data should be stored.
If this parameter is omitted, RNMR will prompt for a source record number with the current write record (as displayed
and set by `PTRA`) as the default.

The last parameter, slice specifies which 2D slice of a 4D source record the foreign data should be written to. If the
source record has only three dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it and will write
to the first slice. Note that the current mapping of dimensions to directions (as displayed and set by `DIRB`) will
affect the selection of which one-dimensional blocks of the record comprises the 3D slice and will thus be written to.
Slice is interpreted as a linear index over the 4th dimension.

If the `IMP3D` command is used at console level and fspec is not provided, RNMR will prompt the user for the name of the
file containing the data to be imported. The default file name in the prompt will depend upon the record number, slice
and the name of the archive the record is in. By default `IMP3D` will search for data in the user's foreign directory.

Upon completion, the current write block of the record, as set and displayed by `PTRB`, is set to the slice that was
exported. In addition, the current write record, as set and displayed by `PTRA`, is set to rec.
## INFLVL
Set info level

Category: Misc.

Format: `INFLVL` nam lev

Defaults: none current

Description:
`INFLVL` sets info levels that are then used by other RNMR commands to decide how much information to print to the
console. The first parameter, nam, specifies which info level to set. If nam is omitted RNMR will prompt for it with no
default. The second parameter, lev, is the level to set and should be an integer that is 0 or greater. If lev is omitted
RNMR will prompt for it with the current value as a default.
## INTG
Compute integral of spectrum

Category: Data Manipulation

Format: `INTG`

Prerequisites: Frequency domain data in processing buffer (FREQ)

Description:
`INTG` calculates and displays the indefinite integral (antiderivative) of the data in the visible processing buffer
(buffer 1) within the current display limits, as displayed and set by `LIM`. By integrating a spectrum, one may measure
the total intensity of each peak. For calculating the integrated intensity of individual peaks, one may compute the
definite integral within specified frequency limits using the command `INTRG`. `INTG` acts only on the first processing
buffer. The user need not be currently viewing this buffer (`VIEW PRO`) to use `INTG`. Only the portion of the data
lying between the current display limits will be integrated by `INTG`. If the left display limit is currently "\*",
`INTG` will begin the integration at the leftmost point in the data buffer. Similarly, if the right display limit is
"\*", `INTG` will integrate up to the last point in the buffer. To prepare the data for integration, `INTG` performs a
baseline fix apodization. This step eliminates any constant offset after integration. If the processing buffer is
divided into two or more blocks, a separate baseline fix is performed for each block. The baseline is corrected before
integration by subtracting a straight line from the data between the left and right display limits.

After baseline fixing, each block of the processing buffer is separately integrated.  This integration consists of
replacing each data point within the region to be integrated by the sum of all points from the left display limit to
that data point, including the endpoints.

After integration, the data is normalized so that the largest point in the first block (between the current display
limits) has a real absolute value intensity of 1. If the largest real absolute value intensity is zero, the data is not
rescaled. If the data is rescaled, RNMR updates the buffer scale factor, as displayed by `SC`. If the processing buffer
is currently visible, RNMR updates the display after executing `INTG`.
## INTRG
Integrate region of spectrum

Category: Data Analysis

Format: `INTRG` llim rlim

Qualifiers: /COMPLEX,/IMAG,/REAL

Qualifier Defaults: current_display

Defaults: current_display_limits

Description:
`INTRG` calculates the definite integral of the data in the visible processing buffer (buffer 1) within specified time
or frequency limits. To calculate and display the indefinite integral of a spectrum within the current display limits,
use the command `INTG`. While `INTRG` acts only on the first processing buffer, the user need not be currently viewing
this buffer (`VIEW PRO`) to use `INTRG`.

The parameters of the `INTRG` command are llim and rlim, the left and right integration limits. These limits are
specified in the current time or frequency unit, as set and displayed by the `UNIT` command. If either or both of these
limits are omitted RNMR will not prompt for them and will use the current display limits. If either limit is beyond the
size of the dataset, the first/last point in the data set will be the integration limit instead.

If the integration limits are within the range of the data buffer but do not correspond to a specific data point, RNMR
will set that limit to the time or frequency of the closest data point to the right of the value specified. `INTRG`
calculates the definite integral between the adjusted left and right limits in the first block of the visible processing
buffer. This integral is defined as the sum of each data point between llim and rlim, inclusive. The integral is
reported as an informational message with a maximum of two decimal places. If the integral cannot be reported as a
floating point number in an eight character field, it is reported in scientific notation.

The qualifiers determine which part of a complex buffer is integrated as follows:

Qualifier | Integrand
--------- | ---------
/COMPLEX  | Complex magnitude
/IMAG     | Imaginary part
/REAL     | Real part

The default integrand is the same as the current display mode as displayed and set by the `BUF` command.
## INSLST
Insert value into list

Category: Lists

Format: `INSLST` nam pos val

Defaults: temp 1 current

Description:
`INSLST` inserts the value val at position pos in list nam. All of the values in the list from position pos onward are
moved by one element and val is stored at pos. The parameter pos cannot exceed the largest filled position in the list.
If nam is omitted RNMR will prompt for it with temp as a default. If pos is omitted RNMR will prompt for it with 1 as a
default. If val is omitted RNMR will prompt for it with the current value at position pos in list nam.
## IXVAL
Convert from unit value to point index

Category: Data Analysis

Format: `IXVAL` xval
Default : current_cursor_position

Description:
`IXVAL` returns the point number (index value) of the specified time or frequency point. This command may be used with
`XVAL`, which returns the time or frequency value given a point number, to locate and examine data points in a buffer
one by one within a specific time or frequency range.

`IXVAL` returns a point number using the time or frequency scale of the visible processing buffer (buffer 1). `IXVAL`
takes one parameter, xval, which is the time or frequency value to be converted to a point number. This value should be
specified in the current time or frequency unit for processing buffer 1. If xval is not specified RNMR will prompt it
with the current cursor 1 position in buffer 1 as the default. If the current cursor position is \*, then the default
for xval is the time or frequency of the leftmost data point.

If xval is outside of the dataset then `IXVAL` will return either 1 or the size of the buffer. If xval is within the
range of the data buffer but does not correspond to a specific data point, RNMR will return the point number of the
first data point to the right of the time or frequency specified. The point number corresponding to the adjusted time or
frequency  value xval is reported to the user as an informational message. Note that xval need not lie within the
current display limits, as set and displayed by the `LIM` command.

# K
---
## KEYARG
Declare names of macro keyword arguments

Category: Arguments

Format: `KEYARG` nam...

Defaults: none

Description:
`KEYARG` is used to declare the names of the keyword arguments passed to a macro. Keywords are passed to macros much
like qualifiers are passed to RNMR commands. For example:

    TEMP /A=2 /B

calls macro TEMP and passes two keyword arguments A and B and a value of 2 for argument A. This will create the
following local arguments within macro TEMP.

- A=2
- B=''
- KEY$1='/VAR=2'
- KEY$2='/B'

Calling `KEYARG A B` within TEMP will delete KEY$1 and KEY$2 and leave A and B untouched.

# L
---
## LB
Set line broadening factor

Category: Data Manipulation

Format: `LB` lb

Defaults: current

Description:
`LB` sets the line broadening factor used for exponential and Gaussian multiplication apodizations (`EM` and `GM`). This
factor can either be set with the `LB` command or by entering the line broadening factor as a parameter with the `EM` or
`GM` commands. Thus, `EM 1`, `GM 1`, and `LB 1` all set the line broadening factor to 1.0 for subsequent apodizations.

`LB` has one parameter, lb, which is the line broadening factor, expressed in the current default frequency unit. This
unit is set by the command `UNIT /FREQ /DFLT` and can be any frequency unit except PPM. If lb is omitted, RNMR will
prompt for it with the current line broadening factor as the default. the line broadening factor must be between -1000
and 1000.
## LCK
Enable or disable lock feedback loop

Category: Lock

Format: `LCK` state

Defaults: current

Prerequisites: RNMR lock control. RNMRA only.

Description:
`LCK` enables or disables the magnetic field-frequency lock on spectrometers with software lock control enabled. `LCK`
takes one parameter, state, which may be specified as  either ON or OFF to enable or disable the lock, respectively.
If "state" is omitted RNMR will prompt for it with the current lock state as the default.
## LCKCTL
Open lock control pop up menu

Category: Lock

Format: `LCKCTL`

Prerequisites: RNMR lock control. RNMRA only.

Description:
`LCKCTL` opens a pop-up menu containing lock controls.
## LCKMTR
Enable lock meter

Category: Lock

Format: `LCKMTR`

Prerequisites: RNMR lock control. RNMRA only.

Description:
`LCKMTR` enables the lock meter.
## LCKVAL
Read lock value

Category: Lock

Format: `LCKVAL`

Prerequisites: RNMR lock control. RNMRA only.

Description:
`LCKVAL` displays the real and imaginary components of the current lock value as informational messages.
## LCLARG
Set local argument value

Category: Arguments

Format: `LCLARG` nam val

Defaults: temp current

Description:
`LCLARG` is an old command for defining local arguments. It has been replaced with the `DFNLCL` command and is
currently simply an alias to it. As such `DFNLCL` should be used in place of `LCLARG`.
## LCLDL
Delete local argument

Category: Arguments

Format: `LCLDL` first last

Defaults: temp first

Description:
`LCLDL` is an old command for deleting global arguments. It has been replaced with the `REMLCL` command and is currently
simply an alias to it. As such `REMLCL` should be used in place of `LCLDL`.
## LI
Increment pulse programmer loop value

Category: Acquisition

Format: `LI` loop incr

Defaults: 1 1

Prerequisites: Pulse program loaded (LOAD), RNMRA Only

Description:
`LI` is an old command for incrementing a loop value by an integer incr. It has been replaced with the `LOOP /INCR`
command and is currently simply an alias to it. As such `LOOP /INCR` should be used in place of `LI`.
## LIM
Set processing buffer display limits

Category: Display Control

Format: `LIM` llim rlim

Defaults: current current

Description:
`LIM` sets the display limits for the visible processing buffer. `LIM` takes two parameters, llim and rlim, which are
the left and right display limits, respectively. These limits are expressed in the current unit for the visible
processing buffer. The current unit is set and displayed by the `UNIT` command. If llim or rlim is omitted RNMR will
prompt for it with the current left or right display limit as a default. A value outside of the dataset or "\*" will use
the leftmost or rightmost point in the buffer. Values that are within the range of the dataset but that do not
correspond exactly to a point will use the closest point to the right of the specified value.

Note that the command `LIM * *` directs RNMR to set the display limits so that all points in the data buffer are
visible. Unless display updating has been set off with the `SET DSP` command, RNMR will update the display to show the
data between llim and rlim.
## LIMA
Set acquisition buffer display limits

Category: Display Control

Format: `LIMA` llim rlim

Defaults: current current

Prerequisites: RNMRA only.

Description:
`LIMA` sets the display limits for the acquisition buffer. `LIMA` takes two parameters, llim and rlim, which are the
left and right display limits, respectively. These limits are expressed in the current unit for the acquisition buffer.
The current unit is set and displayed by the `UNIT` command. If llim or rlim is omitted RNMR will prompt for it with the
current left or right display limit as a default. A value outside of the dataset or "\*" will use the leftmost or
rightmost point in the buffer. Values that are within the range of the dataset but that do not correspond exactly to a
point will use the closest point to the right of the specified value.

Note that the command `LIM * *` directs RNMR to set the display limits so that all points in the data buffer are
visible. Unless display updating has been set off with the `SET DSP` command, RNMR will update the display to show the
data between llim and rlim.
## LIMB
Set blocked record display limits

Category: Display Control

Format: `LIMB` rec dim llim rlim

Defaults: current 1 current current

Description:
`LIMB` sets display limits for a blocked record rec along dimension dim. The parameters llim and rlim are the left and
right display limits. If rec is omitted RNMR will prompt for it with the current read record pointer as set by `PTRA` as
the default. `LIMB` may only be used on blocked records. If dim is omitted RNMR will prompt for it with 1 as a default.
The value of dim cannot exceed the number of dimensions in the blocked record. If llim or rlim is omitted RNMR will
prompt for it with the current left or right display limit as a default. A value outside of the dataset or "\*" will use
the leftmost or rightmost point available. Values that are within the range of the dataset but that do not correspond
exactly to a point will use the closest point to the right of the specified value.
## LOG
Write line to log file

Category: Misc.

Format: `LOG` line

Defaults: none

Prerequisites: Logging enabled

Description:
`LOG` writes a line to the log file. If no line is specified RNMR will prompt for it. `LOG` cannot be used unless
logging is enabled.
## LOOP
Set or increment pulse program loop counter

Category: Acquisition

Format: `LOOP` loop val

Qualifiers: /INCR

Qualifier Defaults: none

Defaults: 1 current/1

Prerequisites: Pulse program loaded (LOAD), RNMRA Only

Description:
`LOOP` either sets a pulse program loop to val or if /INCR is used increments it by val. If loop is omitted RNMR will
prompt for it with 1 as a default. If val is omitted RNMR will prompt for it with the current loop value as the default
unless /INCR is used in which case RNMR will not prompt for val and will set it to 1.

The final loop value must be between 0 and 65,535 inclusive. If /INCR is used `LOOP` will display the final loop value
as an informational message.
## LP
List processing buffer parameters

Category: Data Storage

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Format: `LP` buf

Defaults: 1

Description:
`LP` displays a summary of processing buffer parameter values. When processing spectrometer data offline, many
experimental parameters can only be determined from the `LP` summary since RNMRP lacks commands to display and set many
acquisition parameters. The exact format of the `LP` summary varies from spectrometer to spectrometer due to differences
in implementation of RNMR-controlled hardware. `LP` takes one parameter, buf, which is the number of the processing
buffer whose parameters will be listed. Processing buffer 1 is the visible buffer while the contents of the other
processing buffers are not visible on the display. If buf is omitted from the command line, RNMR will list the
parameters of buffer 1; RNMR does not prompt the user for buf.

The following buffer parameters are listed in the `LP` display:

CURRENT BUFFER TITLE

ARCHIVE, RECORD, BLOCK NUMBER, OWNER, AND DATE:
Direction 1 is always indicated by "\*" in the block number display and corresponds to the dimension visible on the
screen for one-dimensional displays. For example, if record 5 is a two-dimensional blocked record and `DIRB` 2 is
currently 12, the `LP` summary will include the line:

    TEMP     5     (*    ,   1)

when listing block 1 of record 5 in archive TEMP. Conversely, if `DIRB` 2 is set to 21, the summary will include:

    TEMP     5     (1    ,   * )

to indicate that direction 1 is mapped to dimension 2. If the record containing the data in buffer buf is one
dimensional, no block numbers will be reported.

SYNTHESIZER PARAMETERS:
For each synthesizer, RNMR lists its nucleus, its Hertz-to-PPM multiplicative factor (nominal NMR frequency), PPM
reference frequency, and offset (as set by the `F` command). Both the offset and the PPM reference frequency are
reported in Hz to a maximum of one decimal place. The PPM reference frequency is defined as the frequency in Hz of zero
PPM. RNMR also indicates the mapping between physical and logical channels (as set by the `CHN` command) and which
synthesizer is mapped to dimension 1 (the observe dimension).

TRANSMITTER PARAMETERS:
A series of parameters are listed for each transmitter. Three categories of parameters (FMX, PSX, and PWX) are presented
in a similar format. First the name of the program (the last loaded by `FMXEX` etc) is listed. Then the value of 64
FMX/PSWX/PWX values are listed. Finally the low and high coarse power levels as set by `PWR` are listed. These
parameters are listed separately for each transmitter.

RECEIVER PARAMETERS:
The following set of receiver parameters will be listed:

- Gain
- Spectral width
- Filter factor
- Size
- Acquisition time

PULSE PROGRAMMER PARAMETERS:
The pulse program name will be listed followed by 64 pulse values, 64 delay values, 64 loop values, and 64 flag states.
The recycle delay is also listed.

ACQUISITION MODES:
The averager acquisition modes (`AMD /ACQ`, or simply `AMD`) are listed so that the number of modes is equal to the
buffer `NAMD /ACQ` value. That is, regardless of how the `AMD` modes were entered by the user, `NAMD` modes will be
displayed. These modes represent the receiver phase cycle sequence.

BLOCKED ACQUISITION MODES:
The blocked acquisition modes (`AMD /BLK`) are listed so that the number of modes is equal to the buffer `NAMD /BLK`
value. That is, regardless of how the `AMD /BLK` modes were entered by the user, `NAMD /BLK` modes will be displayed.
These modes represent the hypercomplex acquisition receiver phase cycling sequence.

PULSE PROGRAMMER MODES:
The ppmd values for each step of the phase cycle are listed. There will be 16 lists of values.

BLOCKED ACQUISITION PULSE PROGRAMMER MODES:
The block ppmd values for each step of the phase cycle are listed. There will be 16 lists of values.

NAMD PARAMETERS:
The following set of receiver parameters will be listed:

- Number of acquisition phase cycle modes
- Number of block phase cycle modes
- Number of TPPI modes
- Number of incr modes

ACCUMULATION PARAMETERS:
The following set of accumulation parameters will be listed:

- Number of dummy scans performed
- Number of scans averaged

PROCESSING PARAMETERS:
The following set of processing parameters will be listed:

- Number of dimensions
- Domain,
- Size
- Display limits
- Phase correction factors
- Scale factor

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## LPA
List acquisition buffer parameters

Category: Acquisition

Format: `LPA`

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Prerequisites: RNMRA only

Description:
`LPA` displays a summary of processing buffer parameter values. These parameters are the latest settings of the pulse
programmer, averager, and other spectrometer hardware.  The exact format of the `LPA` summary varies from spectrometer
to spectrometer due to differences in implementation of RNMR-controlled hardware.

The following buffer parameters are listed in the `LPA` printout:

CURRENT BUFFER TITLE

USER AND DATE

SYNTHESIZER PARAMETERS:
For each synthesizer, RNMR lists its nucleus, its Hertz-to-PPM multiplicative factor (nominal NMR frequency), PPM
reference frequency, and offset (as set by the `F` command). Both the offset and the PPM reference frequency are
reported in Hz to a maximum of one decimal place. The PPM reference frequency is defined as the frequency in Hz of zero
PPM. RNMR also indicates the mapping between physical and logical channels (as set by the `CHN` command) and which
synthesizer is mapped to dimension 1 (the observe dimension).

TRANSMITTER PARAMETERS:
A series of parameters are listed for each transmitter. Three categories of parameters (FMX, PSX, and PWX) are presented
in a similar format. First the name of the program (the last loaded by `FMXEX` etc) is listed. Then the value of 64
FMX/PSWX/PWX values are listed. Finally the low and high coarse power levels as set by `PWR` are listed. These
parameters are listed separately for each transmitter.

RECEIVER PARAMETERS:
The following set of receiver parameters will be listed:

- Gain
- Spectral width
- Filter factor
- Size
- Acquisition time

LOCK PARAMETERS:
The following set of lock parameters will be listed:

- Status (ON/OFF)
- Sweep (ON/OFF)
- Power
- Gain
- Sweep width
- Position
- Receiver phase
- TC
- PID values
- Meter values (min and max)

PULSE PROGRAMMER PARAMETERS:
The pulse program name will be listed followed by 64 pulse values, 64 delay values, 64 loop values, and 64 flag states.
The recycle delay is also listed.

WAVEFORM GENERATOR PARAMETERS:
The WRF program as set by `WRFEX` is listed followed by the 64 WRF values for each WFG. Then the WWF program as set by
`WWFEX` is listed followed by the 64 WWF values for each WFG.

ACQUISITION MODES:
The averager acquisition modes (`AMD /ACQ`, or simply `AMD`) are listed so that the number of modes is equal to the
buffer `NAMD /ACQ` value. That is, regardless of how the `AMD` modes were entered by the user, `NAMD` modes will be
displayed. These modes represent the receiver phase cycle sequence.

BLOCKED ACQUISITION MODES:
The blocked acquisition modes (`AMD /BLK`) are listed so that the number of modes is equal to the buffer `NAMD /BLK`
value. That is, regardless of how the `AMD /BLK` modes were entered by the user, `NAMD /BLK` modes will be displayed.
These modes represent the hypercomplex acquisition receiver phase cycling sequence.

PULSE PROGRAMMER MODES:
The ppmd values for each step of the phase cycle are listed. There will be 16 lists of values.

BLOCKED ACQUISITION PULSE PROGRAMMER MODES:
The block ppmd values for each step of the phase cycle are listed. There will be 16 lists of values.

NAMD PARAMETERS:
The following set of receiver parameters will be listed:

- Number of acquisition phase cycle modes
- Number of block phase cycle modes
- Number of TPPI modes
- Number of incr modes

ACCUMULATION PARAMETERS:
The following set of accumulation parameters will be listed:

- Number of shots between display update
- Number of dummy scans performed
- Number of scans to wait with `WAIT` command
- Number of scans to acquire (`NA`)
- Number of scans acquired

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## LPB
Perform backward linear prediction on FID

Category: Data Manipulation

Format: `LPB` rlim m n

Defaults: 1 MIN((SIZE-RLIM)/4,8) Min((SIZE-RLIM)-M,512)

Prerequisites: Time domain data in processing buffer 1 (TIME)

Description:
`LPB` performs backwards linear prediction. Based on the specified number of current data points, `LPB` calculates the
values of the FID at earlier times. In a linear prediction calculation the points in the FID are modelled as a linear
combination of an adjacent series of points in the FID. In the case of backwards linear prediction these points come
after the point to be predicted. A set of coefficients used in this linear combination is fit such that this linear
combination is accurate for a set of known good points in the FID and then in the case of backward linear prediction,
they are used to replace points at the beginning of the FID.

The first parameter, rlim, is the number of points to replace at the beginning of the FID. If rlim is omitted RNMR will
not prompt for it and will replace only the first point in the FID. The value of rlim cannot exceed an eighth of the
size of the FID.

The second parameter, m, specifies how many known points are used for fitting the linear prediction coefficients. If m
is omitted RNMR will not prompt for it and will use either a quarter of the points that are not to be replaced or 8
whichever is smaller. The value of m may not exceed 32 or the number of points that are not being replaced.

The third parameter, n, is the number of points to take a linear combination of and therefore the number of coefficients
to fit. For example if rlim is 1 then the first point will be replaced with a linear combination of points 2 to m+1. If
n is not specified RNMR will not prompt for it and will use either the number of points that are not to be replaced
minus m or 512 whichever is smaller.

The linear prediction process is based around the following linear equation:

    X*COEF=DATA(RLIM+1:RLIM+M)

X is a M by N matrix where X(I,J)=DATA(I+J+RLIM). COEF is a N element vector of unknown coefficients. This models each
of the M points after rlim as a linear combination of the N points that follow it. The COEFF values are solved for using
a singular value decomposition (SVD) of X. Once the coefficients are known RNMR fills in the points from rlim back to
the beginning of the FID. That is the point rlim is predicted using the N points after it and then the point to the left
of rlim is predicted using the N points after it (including the predicted value of point rlim) and so on until all the
points are predicted. If the processing buffer is currently visible, RNMR will update the display to show the data as
updated by `LPB`.
## LPC
Perform long pulse phase and amplitude correction

Category: Data Manipulation

Format: `LPC` flip fnyq fnull

Defaults: 90.0 first -fnyq

Prerequisites: Frequency domain data in processing buffer 1 (FREQ)

Description:
`LPC` performs a long pulse correction apodization, correcting both the amplitude and phase of the spectrum. This
apodization is intended to alleviate distortions caused by incomplete excitation of the spectrum by weak pulses. `LPC`
operates only on data in the visible processing buffer (buffer 1). The user need not be viewing this buffer to use
`LPC`.

The first argument of `LPC` is flip, the on-resonance flip angle of the pulse used to excite the spectrum. If this
parameter is not specified on the command line, RNMR will prompt for a flip angle with a default of 90 degrees. The
value of flip must be between 0.0 and 90.0 degrees.

The second parameter, fnyq, is the frequency of the point in the spectrum that corresponds to the Nyquist frequency. If
fnyq is omitted, RNMR will prompt for it with the frequency of the first point in the buffer as a default. The value of
fnyq must be greater than the carrier frequency.

The third parameter, fnull, is the frequency within the spectrum of the first null in the RF excitation, which is also a
measure of the RF field strength. If fnull is omitted RNMR will prompt for it with the fnyq mirrored across the carrier
as a default. The value of fnull is restricted such that the following relationship holds:

    0.1 ≤ ABS(FNULL-OFFSET)/(FNYQ-OFFSET) ≤ 2.0

Both fnyq and fnull are specified in the current frequency unit as set and displayed by `UNIT /FREQ`. If the processing
buffer is currently visible, RNMR will update the display after performing the apodization.
## LPCA
Perform long pulse amplitude correction

Category: Data Manipulation

Format: `LPCA` flip fnyq fnull

Defaults: 90.0 first -fnyq

Prerequisites: Frequency domain data in processing buffer 1 (FREQ)

Description:
`LPCA` performs the amplitude portion of long pulse correction apodization. This apodization is intended to alleviate
distortions caused by incomplete excitation of the spectrum by weak pulses. `LPCA` operates only on data in the visible
processing buffer (buffer 1). The user need not be viewing this buffer to use `LPCA`.

The first argument of `LPCA` is flip, the on-resonance flip angle of the pulse used to excite the spectrum. If this
parameter is not specified on the command line, RNMR will prompt for a flip angle with a default of 90 degrees. The
value of flip must be between 0.0 and 90.0 degrees.

The second parameter, fnyq, is the frequency of the point in the spectrum that corresponds to the Nyquist frequency. If
fnyq is omitted, RNMR will prompt for it with the frequency of the first point in the buffer as a default. The value of
fnyq must be greater than the carrier frequency.

The third parameter, fnull, is the frequency within the spectrum of the first null in the RF excitation, which is also a
measure of the RF field strength. If fnull is omitted RNMR will prompt for it with the fnyq mirrored across the carrier
as a default. The value of fnull is restricted such that the following relationship holds:

    0.1 ≤ ABS(FNULL-OFFSET)/(FNYQ-OFFSET) ≤ 2.0

Both fnyq and fnull are specified in the current frequency unit as set and displayed by `UNIT /FREQ`. If the processing
buffer is currently visible, RNMR will update the display after performing the apodization.
## LPCP
Perform long pulse phase correction

Category: Data Manipulation

Format: `LPCP` flip fnyq fnull

Defaults: 90.0 first -fnyq

Prerequisites: Frequency domain data in processing buffer 1 (FREQ)

Description:
`LPCP` performs the phase portion of long pulse correction apodization. This apodization is intended to alleviate
distortions caused by incomplete excitation of the spectrum by weak pulses. `LPCP` operates only on data in the visible
processing buffer (buffer 1). The user need not be viewing this buffer to use `LPCP`.

The first argument of `LPCP` is flip, the on-resonance flip angle of the pulse used to excite the spectrum. If this
parameter is not specified on the command line, RNMR will prompt for a flip angle with a default of 90 degrees. The
value of flip must be between 0.0 and 90.0 degrees.

The second parameter, fnyq, is the frequency of the point in the spectrum that corresponds to the Nyquist frequency. If
fnyq is omitted, RNMR will prompt for it with the frequency of the first point in the buffer as a default. The value of
fnyq must be greater than the carrier frequency.

The third parameter, fnull, is the frequency within the spectrum of the first null in the RF excitation, which is also a
measure of the RF field strength. If fnull is omitted RNMR will prompt for it with the fnyq mirrored across the carrier
as a default. The value of fnull is restricted such that the following relationship holds:

    0.1 ≤ ABS(FNULL-OFFSET)/(FNYQ-OFFSET) ≤ 2.0

Both fnyq and fnull are specified in the current frequency unit as set and displayed by `UNIT /FREQ`. If the processing
buffer is currently visible, RNMR will update the display after performing the apodization.
## LPDEV
Select text printer device

Category: Printing

Format: `LPDEV` device

Defaults: current

Description:
`LPDEV` selects the printer to be used for text output. The choice of printers is the same for each spectrometer, but
each spectrometer may be assigned a different default printer when RNMR is initialized. The file
/opt/rnmr/spec/common/rnmra/cfgque.dat contains a list of all printers that may be selected by `LPDEV`.

`LPDEV` takes one parameter, device, which is the name of the print device to be selected for all subsequent text
printing. If this argument is missing from the command line, RNMR will prompt for a device with the current print
device as the default. The legal choices of text printer device are currently:

- E460A
- E460B
- LJ2430
- LJ2430B
- LJ4050
- LJ5

## LPF
Perform forward linear prediction on FID

Category: Data Manipulation

Format: `LPF` rlim m n

Defaults: ISIZE+1 MIN(SIZE/4,8) MIN(SIZE-M,512)

Prerequisites: Time domain data in processing buffer 1 (TIME)

Description:
`LPF` performs forward linear prediction. Based on the specified number of current data points, `LPF` calculates
values oto extend the FID. In a linear prediction calculation the points in the FID are modelled as a linear
combination of an adjacent series of points in the FID. In the case of forward linear prediction these points come
before the point to be predicted. A set of coefficients used in this linear combination is fit such that this linear
combination is accurate for a set of known good points in the FID and then in the case of forward linear prediction,
they to extend the FID.

By using forward linear prediction, one may decrease the number of data points in a given dimension that must be
acquired to avoid truncation errors. This ability is particularly useful in obtaining multidimensional data sets since
the number of slices that must be physically acquired, and thus the spectrometer time required, is reduced. For
well-behaved FID's, the number of data points may often be doubled with forward linear prediction. `LPF` operates only
on the data in the visible processing buffer (buffer 1). The user need not be viewing this buffer to use `LPF`.

The first parameter, rlim, is the number of points desired after linear prediction. `LPF` will calculate points SIZE+1
through rlim based on a specified number of points in the original FID. if rlim is omitted only one point will be
predicted. The value of rlim cannot be smaller than the current size of the FID as shown by `SHOW BUF SIZE` or larger
than the allocated size of the buffer as displayed and set by `DBSZ`.

The second parameter, m, specifies how many known points are used for fitting the linear prediction coefficients. If m
is omitted RNMR will not prompt for it and will use either a quarter of the FID or 8 whichever is smaller. The value of
m may not exceed 32 or the number of points in the FID.

The third parameter, n, is the number of points to take a linear combination of and therefore the number of coefficients
to fit. If n is not specified RNMR will not prompt for it and will use either the size of the FID minus m or 512
whichever is smaller.

The linear prediction process is based around the following linear equation:

    X*COEF=DATA(N+1:N+M)

X is a M by N matrix where X(I,J)=DATA(I+J-1). COEF is a N element vector of unknown coefficients. This models each of
the M points after point N as a linear combination of the N points that precede it. The COEFF values are solved for
using a singular value decomposition (SVD) of X. Once the coefficients are known RNMR fills in the points from SIZE+1 to
rlim. That is the point just after the FID is predicted using the N before after it and then point SIZE+2 is predicted
using the N points before it (including the predicted value of point SIZE+1) and so on until all the points out to rlim
are predicted. This process will change the active size of the buffer to rlim. If the processing buffer is currently
visible, RNMR will update the display to show the data as updated by `LPF`.
## LPK
List Peaks

Category: Data Analysis

Format: `LPK`

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Description:
`LPK` displays a list of peak positions and intensities for the first 50 peaks within the current display limits (`LIM`)
above the current peak pick threshold (`TH`). `LPK` only lists peaks within the current display limits for the data in
processing buffer 1. The user need not be viewing the processing buffer to use `LPK`.

The first line displayed by `LPK` will be the current buffer title. The following line will contain the archive, record,
block number, owner, and date. Direction 1 is always indicated by "\*" in the block number display and corresponds to
the dimension visible on the screen for one-dimensional displays. For example, if record 5 is a two-dimensional blocked
record and `DIRB` 2 is currently 12, the `LPK` display will include the line:

    TEMP     5     (*    ,   1)

when listing block 1 of record 5 in archive TEMP. Conversely, if `DIRB` 2 is set to 21, the display will include:

    TEMP     5     (1    ,   * )

to indicate that direction 1 is mapped to dimension 2. If the record containing the data in buffer buf is one
dimensional, no block numbers will be reported.

`LPK` lists peaks in the real part of the data in processing buffer 1 unless the user has selected the imaginary part by
entering `BUF IMAG`. Peaks are located and listed only for the first block of buffer 1 between the current display
limits, as set and displayed by the `LIM` command.

`LPK` uses the following algorithm to find peaks within the current display limits:

1.	Starting with the first point to right of the left cursor and proceeding to the last point to the left of the right
cursor, `LPK` examines each visible point in processing buffer 1. Consequently, neither of the current cursor positions
can be a peak.

2.	RNMR examines the intensities of the two points on either side of the current point and decides whether the current
point is a peak. If I is the intensity of the test point and IL and IR are the intensities of the first points to the
left and right of the test point, respectively, then the test point is a peak if:

        (ABS(I) .GT. IL) .AND. (ABS(I) .GE. IR)      .AND. (ABS(I) .GE. TH)   if I .GE. 0
    or

        (ABS(I) .GT. -IL) .AND. (ABS(I) .GE. -IR)      .AND. (ABS(I) .GE. TH)   if I .LT. 0
where `TH` is the current peak pick threshold, as set and displayed by the command `TH`. That is, for a positive point
to be a peak, its intensity must be greater than or equal to the peak pick threshold, greater than the intensity of the
adjacent point on the left, and greater than or equal to the intensity of the point on the right. Conversely, for a
negative point to be a peak, its intensity must be less than or equal to the negative of the peak pick threshold, less
than the intensity of the first point to the left, and less than or equal to the intensity of the first point to the
right.

3.	For each peak found, RNMR displays a line corresponding to the peak. The first column in the `LPK` printout will
specify the peak number, starting at one for the leftmost peak. If the current unit is PPM, the second column of the
`LPK` printout will list the peak position in PPM while the third column will list this position in the current default
frequency unit, as set by the command `UNIT /FREQ /DFLT`. If the current unit is not PPM, the second column will list
the peak position in the current unit while the third column will specify "--------" for each peak. RNMR will list all
peak positions with the maximum number of decimal places currently set for the appropriate units at RNMR startup time or
as modified by the `NDEC` command. The fourth column of the `LPK` printout specifies the peak height for each peak,
reported to a maximum of 3 decimal places.

4.	RNMR stops listing peaks after finding the first 50 peaks or after testing the next to the last point currently
displayed. If no peaks were found, an error message is displayed:

        (LPK   ) NO PEAKS
In this case, RNMR does not print a peak list.  Conversely, if more  than 50 peaks were found, RNMR displays the
message:

        (LPK   ) TOO MANY PEAKS
along with the number of peaks actually found between the display limits. When this occurs, RNMR displays a listing of
the first 50 peaks from left to right and does not list the remaining peaks.

Wherever possible, `LPK` lists peak positions and intensities as floating point numbers with the maximum number of
decimal places: 3 for intensity and ndec for peak position, where ndec is the value returned by the `NDEC` command
for the appropriate time or frequency unit. However, when a time, frequency or intensity value is too large or too
small to represent with this number of decimal places, RNMR will begin to drop decimal places to fit the number into an
8-character field. If RNMR cannot write the number into an eight character field after dropping all decimal places
(`NDEC 0`), the number will be written in scientific notation.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## LPK2D
List peaks in two dimensions

Category: Data Analysis

Format: `LPK2D` rec slice

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: current 1

Description:
`LPK2D` displays a list of peak positions and intensities for the first 250 peaks found within a 2D slice of a blocked
record above the current peak pick threshold (`TH`). By setting `CONMD` to POS, NEG, or ABS beforehand, the user may
modify the selection of 2D peaks for a given threshold value. Only peaks within the current display limits (as set and
shown by the command `LIMB`) will be listed by `LPK2D`.

The first argument, rec, is the record number of a blocked record of dimension 2 or higher. If a value for rec is not
specified RNMR will prompt for a record number with the current read record as displayed by `PTRA` as a default.

The second parameter, slice, specifies which 2D slice of a 3D or 4D source record to list peaks from. If the source
record has only two dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it and will list peaks
from the first slice. Note that the current mapping of dimensions to directions (as displayed and set by `DIRB`) will
affect the selection of which one-dimensional blocks of the record comprise the 2D slice and will thus be searched for
peaks. Slice is interpreted as a linear index over the 3rd/4th dimensions.

The user must ensure that the record can be accessed for two dimensional processing with the current `DIRB` mapping. If
the NDIMX parameter was set  equal to the number of dimensions when the record was allocated, then this is guaranteed.
However, if NDIMX is less than the number of dimensions in the record, not all choices of `DIRB` will allow peak listing
with `LPK2D`. If `DIRB` is not set to a legal value for processing record rec, RNMR will yield the error message:

    (INI2DX) DIMENSION INACCESSIBLE

followed by the number of the inaccessible dimension. The available choices for `DIRB` will depend on the NDIMX value
with which the record was allocated; `ALLB` always maps directions 1,2,3, and 4 to dimensions 1,2,3, and 4 respectively,
regardless of the `DIRB` setting at allocation time. For example, if a three dimensional record was allocated with NDIMX
2, the user will be able to list 2D peaks in planes of the data cube with `DIRB 3` set to 123, 132, 213, or 231 but not
312 or 321. That is, any `DIRB` setting beginning with 1 or 2 is acceptable but 3 may not be used since the third
dimension is not accessible. Similarly, for 4D records allocated with NDIMX 2, `DIRB 4` may be any sequence beginning
with 1 or 2 and if NDIMX was 3, the `DIRB` sequence may begin with 1, 2, or 3. Thus, the legal choices of `DIRB` are
those in which the first direction is accessible (the accessible directions for a given blocked record are those mapped
to dimensions 1 to NDIMX). In order to remind the user of which dimensions will be searched for 2D peaks, RNMR displays
the dimensions assigned to directions 1 and 2 as two informational messages.

RNMR limits the number of points in direction 1 to a maximum of 4096. This size can be checked using the `SIZEB`
command. `LPK2D` lists 2D peaks in the real part of rec unless the user has selected the imaginary part by entering
`BUF IMAG`.

`LPK2D` uses the following algorithm to find peaks within the current display limits:

1.	Each 1D slice from the first slice above the bottom display limit to the last slice below the top display limit is
examined sequentially. For each of these slices, RNMR examines the data points starting with the first point to the
right of the left display limit and proceeding to the last point to the left of the right display limit. Consequently,
no point lying on the current left, right, top, or bottom cursors can be a point.

2.	RNMR examines the intensities of the four points above, below, to the left, and to the right of each point in the
search region described above. If the current contour mode setting is positive (`CONMD POS`), then RNMR tests the
actual intensity of the current point. If the `CONMD` setting is negative (NEG) then the negative of the data
point is tested. Finally, if the contour mode is currently set to absolute (`CONMD ABS`), RNMR examines the
absolute value of the data point.

3.	The test value is compared to the current peak pick threshold, as set and displayed by the command `TH`. If
TEST is less than the peak pick threshold, the current point is not listed as a peak and RNMR proceeds to the next point
to the right or to the next slice upward in search of 2D peaks. Note that the current `CONMD` setting modifies the
effect of the peak pick threshold. For `CONMD POS`, the intensity of a point must be greater than or equal to the
threshold for that point to be a peak, but for `CONMD NEG`, the intensity must be less than or equal to minus the
threshold.

4.	If the original value of the current point, I, is positive or zero, that point will be listed as a peak if:

        (I .GT. L) .AND. (I .GE. R) .AND. (I .GT. D) .AND. (I .GE. U)
where L, R, D, and U are the intensities of the nearest points to the left, right, below, and above the current point.
Conversely, if the original value of the current point is negative, the current point will be listed as a peak if:

        (I .GT. -L) .AND. (I .GE. -R) .AND. (I .GT. -D) .AND. (I .GE. -U)
where L, R, D, and U are the intensities of the nearest points to the left, right, below, and above the current point.

5.	For each peak found, RNMR displays a line corresponding to the peak. The first column in the `LPK2D` printout will
specify the peak number, starting at one for the leftmost, bottom peak. If the current unit in direction 1 is PPM, the
second column of the `LPK2D` display will list the peak position in PPM while the third column will list this position
in the current default frequency unit, as set by the command `UNIT /DFLT`. If the direction 1 unit is not PPM, the
second column will list the peak position in the current unit while the third column will specify "--------" for each
peak. Similarly, columns 4 and 5 will contain the peak position along direction 2 in current and default units,
respectively. Again, if the current unit for direction 2 is not PPM, column 5 will specify "--------" for each peak.
RNMR will list all peak positions with the maximum number of decimal places currently set for the appropriate units at
RNMR startup time or as modified by the `NDEC` command. The sixth column of the `LPK2D` printout specifies the peak
height for each peak, reported to a maximum of 3 decimal places.

6.  RNMR stops listing peaks after finding the first 250 peaks or after testing the last point in the search range
described above. If no peaks were found, an error message is displayed:

    (LPK2D   ) NO PEAKS
Conversely, if more  than 250 peaks were found, RNMR displays the
message:

    (LPK2D   ) TOO MANY PEAKS
along with the number of peaks actually found between the display limits. When this occurs, RNMR display a listing of
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

to indicate that direction 3 is mapped to dimension 1. If rec has only two dimensions, RNMR will not display any block
numbers. Wherever possible, `LPK2D` lists peak positions and intensities as floating point numbers with the maximum
number of decimal places: 3 for intensity and ndec for peak position, where ndec is the value returned by the `NDEC`
command for the appropriate time or frequency unit. However, when a time, frequency or intensity value is too large or
too small to represent with this number of decimal places, RNMR will begin to drop decimal places to fit the number into
an 8-character field. If RNMR cannot write the number into an eight character field after dropping all decimal places
(`NDEC 0`), the number will be written in scientific notation.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## LS
Set pulse programmer loop value

Category: Acquisition

Format: `LS` loop val

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD) RNMR only

Description:
`LS` is an old command for setting a pulse programmer loop value. It has been replaced with the `LOOP` command and is
currently simply an alias to it. As such `LOOP` should be used in place of `LS`.
## LSTFIL
List contents of a text file

Category: File IO

Format: `LSTFIL` fspec

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: temp.dat

Description:
`LSTFIL` lists the contents of a text file fspec. If fspec is omitted RNMR will prompt for it with temp.dat as a
default. `LSTFIL` displays the contents of a file in a read only fashion; the file cannot be changed. The qualifiers
specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## LSTLST
List contents of a list

Category: Lists

Format: `LSTLST` nam

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: temp

Description:
`LSTLST` lists the contents of a list nam. If nam is omitted RNMR will prompt for it with temp as a default. `LSTLST`
displays the contents of a list in a read only fashion; the list cannot be changed. The qualifiers specify how the list
is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## LSTMAC
List contents of a macro

Category: Macros

Format: `LSTMAC` nam

Qualifiers: /PRT /TTY /WND /WRT

Qualifier Defaults: /WND

Defaults: temp

Description:
`LSTMAC` lists the contents of a macro nam. If nam is omitted RNMR will prompt for it with temp as a default. `LSTMAC`
displays the contents of a macro in a read only fashion; the macro cannot be changed. The qualifiers specify how the
list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## LW
Calculate line width

Category: Data Analysis

Format: `LW` llim rlim pcnt_ht

Defaults: lcursor rcursor 50

Description:
`LW` calculates the width of a peak. `LW` will search from left to right between llim and rlim and selects the first
peak above the peak picking threshold as set and displayed by `TH`. If llim or rlim is not specified RNMR will not
prompt for it and will use the current cursor positions. The third parameter pcnt_ht is a the percentage of the peak
height at which the linewidth is measured. If pcnt_ht is omitted RNMR will not prompt for it and will use 50 percent.

# M
---
## MACARG
Redefine names of positional macro arguments

Category: Macros

Format: `MACARG` nam...

Defaults: none

Description:
`MACARG` renames local arguments created to hold the positional arguments passed into a macro. By default when a macro
is called with positional arguments they are stored in local arguments 1, 2, 3, etc. `MACARG` accepts a series of names
as arguments. The default argument names are replaced with the names passed to `MACARG`. The number of names need not
match the number of numbered arguments. Any names with no corresponding number local will be ignored.
## MAG
Calculate magnitude of data

Category: Data Manipulation

Format: `MAG`

Description:
`MAG` calculates the magnitude of the data in the visible processing buffer. The magnitude is placed in the real part of
the buffer and the imaginary part of the buffer is set to 0. The magnitude is defined as follows:

    MAG = SQRT(REAL^2 + IMAG^2)
## MAPN
Append text to macro

Category: Macro

Format: `MAPN` nam

Defaults: TEMP

Description:
`MAPN` is an old command for appending lines of text to a macro. It has been replaced with the `APNMAC` command and is
currently simply an alias to it. As such `APNMAC` should be used in place of `MAPN`.
## MASCMD
Send command to MAS controller

Category: Hardware

Format: `MASCMD` cmd arg

Defaults: test

Description:
`MASCMD` sends a command to the MAS controller and for some commands prints the response as an informational message.
Some commands require additional arguments to be sent to the MAS controller. If no command is specified RNMR will prompt
for one with test as a default. The following commands are available:

Command | Description | Args | Responses
------- | ----------- | ---- | ---------
AUTO    | Switch to auto mode | 0 | 0
BEAR    | Set bearing pressure | 1 | 0
BEAR_A  | Get bearing pressure | 0 | 1
BEAR_D  | Get bearing set point | 0 | 1
BEARS_A | Get bearing sense pressure | 0 | 1
DRIVE   | Set drive pressure | 1 | 0
DRIVE_A | Get drive pressure | 0 | 1
DRIVE_D | Get drive set point | 0 | 1
GOSET   | Go to the set spin rate | 0 | 0
MAIN_A  | Get main pressure | 0 | 1
MANUAL  | Switch to manual mode | 0 | 0
MINMAIN | Set minimum main pressure | 1 | 0
SPIN    | Set spin rate | 1 | 0
SPIN_A  | Get spin rate | 0 | 1
SPIN_D  | Get set spin rate | 0 | 1
TEST    | Test connection | 0 | 0

## MAXV
Calculate maximum

Category: Data Manipulation

Format: `MAXV` src dst

Defaults: 2 1

Description:
`MAXV` replaces the contents of buffer dst with the maximum of buffers src and dst.

    DST = MAX(DST,SRC)

The comparison is pointwise and based on magnitudes. If either argument is omitted, RNMR will prompt for a buffer
number. The default source is buffer 2 while the default destination is buffer 1. The src and dst buffers must have the
same domain and active size (though not necessarily the same allocated size).
## MCPY
Copy macro

Category: Macro

Format: `MCPY` name1 name2

Defaults: temp temp

Description:
`MCPY` is an old command for copying a macro. It has been replaced with the `CPYMAC` command and is currently simply an
alias to it. As such `CPYMAC` should be used in place of `MCPY`.
## MD
Define macro

Category: Macro

Format: `MD` nam

Defaults: temp

Description:
`MD` is an old command for defining to a macro. It has been replaced with the `CRTMAC` command and is currently simply
an alias to it. As such `CRTMAC` should be used in place of `MD`.
## MDL
Delete macro

Category: Macro

Format: `MDL` nam

Defaults: temp

Description:
`MDL` is an old command for deleting a macro. It has been replaced with the `REMMAC` command and is currently simply an
alias to it. As such `REMMAC` should be used in place of `MDL`.
## ME
Edit macro

Category: Macro

Format: `ME` macnam

Defaults: temp

Description:
`ME` is an old command for editing a macro. It has been replaced with the `EDTMAC` command and is currently simply an
alias to it. As such `EDTMAC` should be used in place of `ME`.
## MEDBF
Median baseline fix spectrum

Category: Data Manipulation

Format: `MEDBF` window std_dev

Defaults: 70 5.0

Description:
Baseline fix spectrum based on algorithm presented by M. Friedrichs, J. Biomol. NMR 5 147-153 (1995). The algorithm
tracks the baseline by calculating, at each point, the median of the extrema within a certain window size set by the
argument window. This set of median values is then convoluted with a Gaussian of standard deviation given by the
argument std_dev. These final values are then subtracted from the data values. The values of the window and the standard
deviation are both in terms of points, rather than the current units. The user will be prompted for both values if they
are not given.

The success of this method depends on proper choice of the window size. The window should be chosen such that the
number of local extrema arising from noise dominates the median statistic. If the window is too small and the number of
signal peaks in a given window is comparable to the number of noise peaks, the algorithm will be biased upwards and
attempt to bring the signals down to the baseline.  n the other hand, if the window is too large, the baseline will not
reflect the local baseline structure. Likewise, the standard deviation should be chosen such that it is not too large
and thus broadening out the local correction over too wide a region. The user should be careful in the use of this
algorithm in cases where zero filling before Fourier transformation has taken place, since such a procedure in effect
increases the number of points between noise extrema. Zero filling to sizes 4 or more times the acquired FID are cause
for caution.
## MEXIT
Exit macro

Category: Macro

Format: `MEXIT` vals...

Qualifiers: /ERROR

Qualifier Defaults: none

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`MEXIT` performs unconditional exit from current macro. All remaining repeats are cancelled. The values provided as
arguments to `MEXIT` will be stored as local variables at the site where the macro was called. They will be named RTN$1,
RTN$2, RT$3 etc. `RTNARG` can be used to easily rename these local variables. The /ERROR causes the macro to return as
an error causing the calling site to jump to the label set by `ONERR`.
## MINV
Calculates minimum

Category: Data Manipulation

Format: `MINV` src dst

Defaults: 2 1

Description:
`MINV` replaces the contents of buffer dst with the minimum of buffers src and dst.

    DST = MIN(DST,SRC)

The comparison is pointwise and based on magnitudes. If either argument is omitted, RNMR will prompt for a buffer
number. The default source is buffer 2 while the default destination is buffer 1. The src and dst buffers must have the
same domain and active size (though not necessarily the same allocated size).
## ML
List contents of a macro

Category: Macro

Format: `ML` nam

Defaults: temp

Description:
`ML` is an old command for listing the contents a macro. It has been replaced with the `LSTMAC` command and is currently
simply an alias to it. As such `LSTMAC` should be used in place of `ML`.
## MNMX
Calculate minimum and maximum in buffer region

Category: Data Analysis

Format: `MNMX` llim rlim

Qualifiers: /COMPLEX,/IMAG,/REAL

Qualifier Defaults: current_display

Defaults: current_display_limits

Description:
`MNMX` calculates the minimum and maximum of the data in the visible processing buffer (buffer 1) within specified time
or frequency limits. While `MNMX` acts only on the first processing buffer, the user need not be currently viewing
this buffer (`VIEW PRO`) to use `MNMX`.

The parameters of the `MNMX` command are llim and rlim, the left and right integration limits. These limits are
specified in the current time or frequency unit, as set and displayed by the `UNIT` command. If either or both of these
limits are omitted RNMR will not prompt for them and will use the current display limits. If either limit is beyond the
size of the dataset, the first/last point in the data set will be the limit instead.

If the limits are within the range of the data buffer but do not correspond to a specific data point, RNMR will set that
limit to the time or frequency of the closest data point to the right of the value specified. `MNMX` calculates the
maximum and minimum values between the adjusted limits. The values are reported as informational messages with a maximum
of two decimal places. If the values cannot be reported as floating point numbers in an eight character field, they are
reported in scientific notation.

The qualifiers determine which part of a complex buffer is integrated as follows:

Qualifier | Integrand
--------- | ---------
/COMPLEX  | Complex magnitude
/IMAG     | Imaginary part
/REAL     | Real part

The default integrand is the same as the current display mode as displayed and set by the `BUF` command.
## MO
Exit program

Category: Misc.

Format: `MO` resp

Defaults: no

Description:
`MO` is an old command for exiting RNMR. It has been replaced with the `EXIT` command and is currently simply an alias
to it. As such `EXIT` should be used in place of `MO`.
## MOV
Move record

Category: Data Storage

Format: `MOV` src dst

Defaults: irrec iwrec

Description:
`MOV` moves data from src record to dst record. If not provided RNMR will promt for src with the last read record as a
default. RNMR will not prompt for dst and will use the next available record as a default. Both src and dst must be
records in the same archive.

Records in archives other than 1 can be specified by either pre-pending the archive number and a ":" or specifying
numbers larger than 200. For example record # in archive 2 can be specified either as 2:# or by adding 200 to #.
## MOVV
Move buffer

Category: Data Manipulation

Format: `MOVV` src dst

Defaults: 2 1

Description:
Moves complex source buffer to complex destination buffer.  DST = SRC

`MOVV` replaces the contents of buffer dst with the contents of buffer src.

    DST = SRC

If either argument is omitted, RNMR will prompt for a buffer number. The default source is buffer 2 while the default
destination is buffer 1. The src and dst buffers must have the same domain and active size (though not necessarily the
same allocated size).
## MRGFS
Merge default file with file

Category: File IO

Format `MRGFS` fspecd fspec

Defaults: none

Description:
`MRGFS` merges a default file specification fspecd with fspec. A file consists of a name and extension (separated by the
last period). The parts of the merged file specification are obtained by preferentially selecting the parts from fspec.
If a part is not present in fspec, the part in fspecd is used. If the part is not present in either input it is omitted.
The merged file specification is printed as an informational message.
## MRN
Rename macro

Category: Macro

Format: `MRN` nam1 nam2

Defaults: temp temp

Description:
`MRN` is an old command for renaming a macro. It has been replaced with the `RENMAC` command and is currently
simply an alias to it. As such `RENMAC` should be used in place of `MRN`.
## MSG
Write message line to console

Category: Misc.

Format: `MSG` msgln

Defaults: None

Description:
`MSG` writes the contents of msgln to the console. If msgln is omitted RNMR will prompt for it.
## MULV
Multiply buffer

Category: Data Manipulation

Format: `MULV` src dst

Defaults: 2 1

Description:
`MULV` replaces the real and imaginary parts of buffer dst with the product of the respective parts of buffers src and
dst.

    REAL(DST) = REAL(DST) * REAL(SRC)
    IMAG(DST) = IMAG(DST) * IMAG(SRC)

The multiplication is pointwise. If either argument is omitted, RNMR will prompt for a buffer number. The default source
is buffer 2 while the default destination is buffer 1. The src and dst buffers must have the same domain and active size
(though not necessarily the same allocated size).

# N
---
## NA
Set number of shots to acquire

Category: Acquisition

Format: `NA` na

Defaults: current

Prerequisites: RNMRA only

Description:
`NA` sets the number of shots to acquire to na. If na is not provided RNMR will prompt for it with the current value as
a default. If na is -1 an indefinite number of scans will be collected until the user halts the acquisition.
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
## PPEX
Load a pulse program experiment

Category: Acquisition

Format: `PPEX` nam

Qualifiers: /INIT /NOINIT

Qualifier Defaults: /INIT

Defaults: current

Prerequisites: Acquisition stopped (HALT), RNMRA only

Description:
`PPEX` loads a pulse program named nam into the pulse programmer. If nam is omitted, RNMR will prompt for it with the
currently loaded PP (if any) as the default. Once `PPEX` has read the pulse program header, the title of the program (as
specified in the PP source code using the `TITLE` statement) is displayed as an informational message. This title is
usually a brief description of the function of the pulse program.

The /INIT qualifier causes the pulse program to be initialized by loading default values into the pulse programmer and
is active by default.
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
TBL       | Checks for existence of name table | TBL | None | None | None
TBLARG    | Checks for existence of name table argument | TBL, NAM | None, None | None | None

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

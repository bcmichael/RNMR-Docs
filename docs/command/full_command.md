
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
`ADDV` adds the contents of [processing buffers](syntax.md#buffers) src and dst and stores the result in dst.

        DST = DST + SRC

If either argument is omitted, RNMR will prompt for a buffer number. The default source is buffer 2 while the default
destination is buffer 1. The src and dst buffers must have the same domain and active size (though not necessarily the
same allocated size).
## AI
Scale to absolute intensity

Category: Display Control

Format: `AI` sfa

Defaults: current

Description:
`AI` scales data in the visible processing buffer to make the scale factor equal to a specified absolute scale factor,
sfa. If sfa is omitted RNMR will not prompt for it and will use the current absolute scale factor (as set and displayed
by `AK`). The scale factor must be greater than 0.0. The absolute scale factor (as set and displayed by `AK`) will also
be updated to the value of sfa.
## AK
Set absolute scale factor

Category: Display Control

Format: `AK` sfa

Defaults: current

Description:
`AK` sets the global absolute scale factor. If the absolute scale factor sfa is omitted RNMR will prompt for it with the
current global scale factor as a default. The global scale factor must be greater than 0.0. If a scale factor of 0 is
passed to `AK` the current scale factor of the visible processing buffer will be used.
## ALLB
Allocate a blocked record

Category: Blocked Records

Format: `ALLB` rec ndim size(1)...size(ndim) ndimx nsega

Defaults: wrec 2 64 ... 64 <ndim> 1

Description:
`ALLB` allocates a [blocked record](syntax#blocked_records). By allocating multidimensional records in advance, the user
is assured that there will be adequate disk space to hold all the data to be acquired.

The parameter rec is the [record number](syntax#records) to be allocated. If 0 is entered for this parameter or if no
record is specified RNMR will not prompt for it and will use the write record pointer (as displayed and set by `PTRA`).
If the specified record is already in use RNMR will use the next available record. If RNMR selects the record for either
of the above reasons the record number will be printed as an informational message after allocation is complete.

The parameter ndim specifies the number of dimensions and must be between 1 and 4 inclusive. If ndim is not specified
RNMR will prompt for it with 2 as a default. `ALLB` accepts ndim arguments to set the size of the allocated record along
each dimension. If any of these sizes are omitted RNMR will prompt for them with 64 as a default. The sizes must be
positive integers.

The next parameter, [ndimx](syntax#ndimx), is the number of dimensions of the blocked record that will be simultaneously
accessible. If ndimx is omitted RNMR will prompt for it with ndim as a default. The final parameter,
[nsega](syntax#nseg), is the number of segments to allocate in the records. If nsega is not specified RNMR will not
prompt for it and will allocate 1 segment.

In order for a blocked record to be successfully allocated there must be enough space in the archive (as displayed by
`SP`). The other parameters of the blocked record can be set using `PARB` or `SET REC`.
## ALLCPY
Allocate a copy of a blocked record

Category: Blocked Records

Format: `ALLCPY` srcrec dstrec isize(1) ... isize(ndim) ndimx nsega

Defaults: rrec wrec insize(1)...insize(ndim) <ndim> 1

Description:
`ALLCPY` allocates a [blocked record](syntax#blocked_records) dstrec copying the parameters but not the data from
blocked record srcrec. To copy both parameters and data, use the command `CPY`. The destination record may be given new
sizes, [number of accessible dimensions](syntax#ndimx), and [number of segments](syntax#nseg) in place of those used
in the source record.

If no source [record number](syntax#records) is specified RNMR will prompt for it with the current read record pointer
(as displayed and set by `PTRA`) as a default. If no destination record is specified RNMR will not prompt for it and
will use the write record pointer (as displayed and set by `PTRA`). If the specified destination record is already in
use RNMR will use the next available record. If RNMR selects the destination record for either of the above reasons the
record number will be printed as an informational message after allocation is complete.

`ALLCPY` can accept a number of sizes up to the number of dimensions in the source record. These sizes will be used in
place of the some or all of the sizes from the source record. If any sizes are not specified RNMR will not prompt for
them and will use the sizes from the source record for those dimensions.

The next parameter, ndimx, is the number of dimensions of the blocked record that will be simultaneously accessible. If
ndimx is omitted RNMR will not prompt for it and will use the number of dimensions regardless of the value of ndimx in
the source record. The final parameter, nsega, is the number of segments to allocate in the records. If nsega is not
specified RNMR will not prompt for it and will allocate 1 segment regardless of the value of nsega in the source record.

In order for a blocked record to be successfully allocated there must be enough space in the archive (as displayed by
`SP`).
## AMD
Set acquisition modes

Category: Acquisition

Format: `AMD` spec1 spec2 ... spec8

Qualifiers: /ACQ /BLK /MOD=MODMD

Qualifier Defaults: /ACQ /MOD=4

Defaults: none none ... none

Prerequisites: Acquisition stopped (HALT); RNMRA only

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

Category: Lists

Format: `APNLST` nam

Qualifiers: /END=<end\> /TTY

Qualifier Defaults: /END=''

Defaults: temp

Description:
`APNLST` appends lines to a list specified by nam. /END sets a string which marks the end of what is to be appended. If
no list is specified RNMR will prompt for a list name with a default of temp. The list must already have been created
using `CRTLST`. `APNLST` behaves slightly differently if called at the command line or in a macro. At the command line
RNMR will prompt for a line to append to the list with a default of <end\>. Otherwise an error will be thrown. RNMR
will continue to prompt for lines until a line is entered which matches <end\>. By default <end\> is an empty string and
`APNLST` will end if an empty line is provided.

When called from a macro `APNLST` will not prompt for a line to append unless the /TTY qualifier is used. Instead the
lines to be appended should be provided on the lines following `APNLST` in the macro and should start with ;;. `APNLST`
will stop appending lines when it either reaches a line that matches <end\> or runs out of lines. /TTY will make RNMR
prompt for the lines to enter much like the behavior at the command line even when `APNLST` is called from a macro.
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

Format: `ARV` arv

Qualifiers: /ACCESS /NAME

Qualifier Defaults: /NAME

Defaults: 1

Description:
`ARV` prints information about an [archive](syntax#archives) arv as an informational message. If no archive is specified
RNMR will prompt for it with 1 as a default. The default /NAME qualifier causes `ARV` to print the name of the specified
archive as an informational message. The /ACCESS qualifier causes `ARV` to print an integer indicating the level of
access to the archive. The integer codes are generated by using the least significant bit to indicate whether there is
read access to the archive and the next least significant bit to indicate write access. Numbers for which no archive is
open will have neither and there will never be write access without read access. This yields the following possible
codes:

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
primarily used for multi dimensional acquisition. `ASIG` acknowledges a signal and resets it. If no signal is specified
RNMR will prompt for it with a default of temp. The following signals are available:

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

Prerequisites: RNMR lock control; RNMR shim control; RNMRA only

Description:
`AUTOZ` sets up automatic Z shimming in RNMRA. In order for this to function RNMR must have access to both the lock and
shim controls. In order for `AUTOZ` to have any effect the automatic Z shimming flag (as set and displayed by
`SET AUTOZ`) must be on. If either the step or time is omitted RNMR will prompt for them with the current values as a
default. The step must be between 0.0 and 1.0 inclusive, while time must be between 4.0 and 100.0 inclusive.
# B
---
## BC
Baseline correct FID

Category: Data Manipulation

Format: `BC`

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`BC` performs a baseline correction to a complex FID in the visible processing buffer by subtracting the average of the
last 1/8th of the data points from the entire FID. To calculate the constant complex offset to be subtracted from the
entire FID, `BC` examines the final 1/8th of the FID data points with a minimum of 1 point if there are less than 8
points. The average of these points (a complex number) is subtracted from each (complex) point of the entire FID,
yielding a baseline corrected FID.
## BF
Baseline fix spectrum

Category: Data Manipulation

Format: `BF`

Prerequisites: Frequency domain data in processing buffer (FREQ)

Description:
`BF` performs a linear baseline fix by subtracting a straight line from the data in the visible processing buffer
between the current display limits.

`BF` uses the average of the leftmost and rightmost 5 points between the current display limits to determine the line to
subtract. If there are fewer than 5 points between the current display limits `BF` subtracts the average over all the
points instead of calculating a line. `BF` only subtracts from the points between the current display limits, leaving
everything outside of those limits untouched.
## BINCP
Perform binary pulse phase correction

Category: Data Manipulation

Format: `BINCP` fnyq fmax

Defaults: first (fnyq-orgn)/2+orgn

Prerequisites: Frequency data in processing buffer (FREQ)

Description:
`BINCP` performs the phase portion of a binary pulse correction on data in the visible processing buffer. When used with
the `BINCP` solvent suppression pulse sequence, this command corrects the phase of the off-resonant component of the
magnetization, which is preserved while the on-resonance solvent peak is cancelled out. The parameters fnyq and fmax are
the nyquist frequency of the visible processing buffer and the max frequency to be used for the correction. Both
parameters are specified in terms of current frequency units including the frequency offset of the origin of the buffer
(orgn). The default value of fnyq will be correspond to the frequency of the first point in the buffer. The default of
fmax is (fnyq-orgn)/2+orgn. Internally `BINCP` subtracts the origin from the values before using them. In order to make
the calculations more understandable all references to these parameters going forward will refer to the corrected values
with the origin subtracted out. The corrected fnyq must be greater than 0. The absolute value of the corrected fmax
divided by the corrected fnyq must be between 0.1 and 2.0.

To calculate the phase portion of the finite pulse correction, `BINCP` first calculates a constant phase and a phase
increment:

 	PHI = 270.0*DFRST/FMAX - 90.0
 	DPHI = 270.0*DSTEP/FMAX

where DSTEP is -1 times the frequency per point and DFRST is the frequency of the first point in the spectrum.

Each point I ranging from 1 to the size of the buffer is multiplied by a complex phase shift calculated as follows:

    EXP(i*(PHI + (I-1)* DPHI))

If the data point closest to zero frequency (without offset) is not the last point in the spectrum, then all points
in each block from zero to minimum (most negative) frequency are negated.
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
`BRUK` converts a BRUKER format (real) FID in the visible processing buffer into a complex FID. Upon conversion from
BRUKER to complex format, the size of the FID (number of points) is adjusted to the smallest power of 2 greater than or
equal to the original size. `BRUK` will convert the data only if this adjusted size is at least 4 points and not
greater than the allocated buffer size (`SHOW BUF SIZEA`). The data is zero filled from the current size to the adjusted
size. The actual conversion from BRUKER (real) to complex data follows the  algorithm below:

1.	The entire zero-filled BRUKER FID is conjugated.
2.	Starting with the second point, every other point in the FID is negated.

3.	A real Fourier transform is performed on the FID, yielding a complex vector with half the adjusted size of the source
FID.

4.	The resulting vector is inverse Fourier transformed.

5.	Starting with the second point, every other point in the FID is negated.

## BUF
View real or imaginary processing buffer

Category: Display Control

Format: `BUF` nam

Defaults: current

Description:
`BUF` selects whether the real or imaginary part of the visible processing buffer should be displayed. The parameter
nam may be set to real, imag, or complex to display the real part, imaginary part or both parts of the buffer
respectively. If nam is omitted RNMR will prompt for a response with the current buffer display type as a default.
## BUFA
View real or imaginary acquisition buffer

Category: Display Control

Format: `BUFA` nam

Defaults: current

Prerequisites: RNMRA only

Description:
`BUFA` selects whether the real or imaginary part of the acquisition buffer should be displayed. The parameter nam may
be set to real, imag, or complex to display the real part, imaginary part or both parts of the buffer respectively. If
nam is omitted RNMR will prompt for a response with the current buffer display type as a default.
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
`CALIB` is used with the calib pulse program to calibrate spectrometer phases. It is to be used only by the support
staff. The argument fcalib is a real number interpreted in the current frequency unit of the visible processing buffer.
If fcalib is omitted  RNMR will prompt for it with the current calibration frequency as a default. After conversion to
Hz, the calibration frequency must be nonzero.
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

Defaults: 0 200

Description:
`CAT` displays a catalog of records from first-rec to last-rec within a single archive. `CAT` takes two parameters,
which are the first and last [record numbers](syntax#records) to be displayed. If first-rec is set to record 0 (which
does not exist) in an archive, all of the records in that archive up to last-rec will be listed. In this case if
last-rec is omitted all the records in the archive are listed. If neither parameter is specified the default behavior is
to list all records in archive 1. If first rec is set to any other value and last-rec is omitted only that record will
be listed. The value of last-rec should be specified by the number within the archive even if it is not in archive 1.

For each nonempty record, `CAT` returns the record  number, owner, record length, record position within the archive,
date, and title. Note that `CAT` reports record length and position in units of blocks, which are 512 bytes long each.

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
`CATARV` displays a list of [archives](syntax#archives) from first-archive to last-archive. If only one argument is
specified, `CATARV` will list information about only that single archive. `CATARV` shows the archive number and if the
archive is open it also shows flags indicating the presence of read access and write access, as well as the name of the
archive.

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
If both arguments are omitted `CATGBL` will list all global arguments. If only one argument is specified, `CATGBL` will
list information about only that single argument. Each global argument is listed by name along with its current value.

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
If both arguments are omitted `CATLCL` will list all local arguments. If only one argument is specified, `CATLCL` will
list information about only that single argument. Each local argument is listed by name along with its current value.

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
`CATLST` displays a catalog of the currently defined lists by name from first to last in alphabetical order. If both
arguments are omitted `CATLST` will list all lists. If only one argument is specified, `CATLST` will list information
about only that single list. Each list is listed by name along with its maximum size and its current size.

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
`CATMAC` displays a catalog of the currently defined macros by name from first to last in alphabetical order. If both
arguments are omitted `CATMAC` will list all macros. If only one argument is specified, `CATMAC` will list information
about only that single macro. Each macro is listed by name along with whether it is a user or system macro and the file
where it is stored. The file will only be listed if the macro has been called during the current RNMR session.

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
`CATNUC` displays a catalog of the currently defined nuclei by name from first to last in alphabetical order. If both
arguments are omitted `CATNUC` will list all nuclei. If only one argument is specified, `CATNUC` will list information
about only that single nucleus. Each nucleus is listed by name along with its current frequency (value used to convert
between PPM and Hz) in MHz and its reference frequency in Hz.

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

Prerequisites: RNMRA only

Description:
`CATPPS` displays a catalog of the currently defined PP symbols. The catalog is organized by PP symbol type and then
each type section is organized by name from first to last in alphabetical order. If type is omitted from the command
line then `CATPPS` will display all types of symbols. If a type is specified then only the section of the catalog
corresponding to that type will be listed. If both first and last are omitted `CATPPS` will list all entries in each
included section. If only one of first and last is specified, `CATPPS` will list information about only that single PP
symbol in each included section. Each PP symbol is listed by name along with its location.

The qualifiers specify how the list is output as follows:

Qualifier | Output
--------- | ------
/PRT      | Print the list to the printer device as specified by `LPDEV`
/TTY      | Print the list to the RNMR command line, one line at a time. Press <RETURN\> or <SPACE\> to print the next line. Press "Q" or <CTRL-Z\> to quit.
/WND      | Display the list in a pop-up window. This is the default behavior.
/WRT      | Write the list to a `WRT` file. Errors if no file is open to write to.

## CATSYM
List catalog of symbols

Category: Arguments

Format: `CATSYM` first last

Qualifiers: /FLT /INT /NDEC /PRT /TTY /WND /WRT

Qualifier Defaults: /NDEC=1 /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATSYM` displays a catalog of the currently defined symbols by name from first to last in alphabetical order. If both
arguments are omitted `CATSYM` will list all symbols. If only one argument is specified `CATSYM` will list information
about only that single symbol. Each symbol is listed by name along with its current value. Floating point symbols will
be displayed with a number of decimal places set by /NDEC.

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

Category: Tables

Format: `CATTBL` tbl first last

Qualifiers: /PRT /TTY /VAL /WND /WRT

Qualifier Defaults: /WND

Defaults: none ZZZZZZZZZZZZZZZZ

Description:
`CATTBL` displays a catalog of the currently defined tables. A single table to display may be selected using the tbl
argument. If no tbl is specified all of the currently defined tables will be listed. /VAL will cause `CATTBL` to list
the values in the tables by name from first to last in alphabetical order. If both first and last are omitted `CATTBL`
will list all values in the tables. If only one of first and last is specified, `CATTBL` will list information about
only that single value. Each table is listed by name along with its maximum size and its current size.

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
`CD` performs a convolution difference apodization on an FID in the visible processing buffer. The apodization function
applied to the FID is given by:

    apodization = EM(narrow) - wfract*EM(wide)

Note that `CD` yields the same result as separately exponentially line broadening the original FID using `EM`, scaling
the wide result using `SC` and subtracting the two resulting FID's. This apodization is useful for separating out
spectral components with greatly different line widths and for masking the effects of probe ring-down. The narrow line
broadening and the wide line broadening are expressed in the current default frequency units (as displayed and set by
`UNIT /FREQ /DFLT`). If either of these parameters are not specified, RNMR will prompt for it with 0.0 as a default.
Each linewidth entered must be between -1000 Hz and 1000 Hz, inclusive. The parameter wfract specifies the fraction of
the wide component in the apodization. This fraction is a real number between 0.0 and 1.0, inclusive. If wfract is not
specified RNMR will prompt for it with 0.0 as the default.
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
should be the logical channel. With these qualifiers if the first argument is omitted RNMR will prompt for it with 1 as
a default. If the second argument is omitted RNMR will prompt for it with the current mapped value as a default.

/SEQ, which is the default qualifier, expects a sequence of physical channels consisting of up to the number of channels
in the system. The sequence of channels will be mapped to the logical channels starting from 1. For example:

    CHN 31

will map logical channel 1 to physical channel 3 and logical channel 2 to physical channel 1. If the sequence is omitted
RNMR will prompt for it with the current mapping sequence as a default.
## CLSARV
Close archive

Category: Data Storage

Format: `CLSARV` archive

Defaults: 1

Description:
`CLSARV` closes an archive. If no [archive](syntax#archives) is specified RNMR will prompt for it with 1 as a default.
An attempt to close an archive which is not open will result in an error.
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

Category: Display Handling

Format: `CLSDSP`

Description:
Close display opened with `OPNDSP`. `CLSDSP` will error if the display is not open.
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
Close import file opened with `OPNIMP`. `CLSIMP` will error if no import file is open.
## CLSPLT
Close plotter stream and print

Category: Plotting

Format: `CLSPLT`

Description:
`CLSPLT` writes out the current plot buffer and submits the resulting file for printing or plotting, terminating the
plot sequence that began with `OPNPLT`. All plots between `OPNPLT` and `CLSPLT` will appear as one plot.
`CLSPLT` will error if no plot is currently open. Depending on the state of the plotter flag (as set and displayed by
`SET PL`) the plot will either be saved to the plotter file (as set and displayed by `PLFIL`) or printed by the plotting
device (as set and displayed by `PLDEV`).
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

Format: `CMUL` mag phi buf

Defaults: 1.0 0.0 1

Description:
`CMUL` multiplies the contents of a [processing buffer](syntax#buffers) by a complex constant, updating the buffer. This
constant is specified in polar form:

    REAL(CONST) = MAG*COS(PHI*PI/2)
    IMAG(CONST) = MAG*SIN(PHI*PI/2)

If the magnitude is omitted RNMR will not prompt for it and will use 1.0. If the phase, phi, is omitted RNMR will not
prompt for it and will use 0.0. The phase is specified in degrees. If no buffer is specified RNMR will not prompt for it
and will operate on the visible processing buffer.
## CMULV
Complex multiply two buffers

Category: Data Manipulation

Format: `CMULV` src dst

Defaults: 2 1

Description:
`CMULV` complex multiplies the contents of [processing buffers](syntax.md#buffers) src and dst and stores the result in
dst.

    DST = DST * SRC

If either argument is omitted, RNMR will prompt for a buffer number. The default source is buffer 2 while the default
destination is buffer 1. The src and dst buffers must have the same domain and active size (though not necessarily the
same allocated size).
## CND
Set condition flag

Category: Misc.

Format: `CND` cnd state

Defaults: 1 current

Description:
`CND` sets the state of the specified condition flag to ON or OFF. The first parameter, cnd specifies which of the 64
available condition flags is to be set. Accordingly, cnd may be any integer from 1 to 64. If cnd is omitted RNMR will
prompt for it with 1 as a default. If state is omitted,RNMR will prompt for it with the current state as a default.
## CNVFL
Convolution filter spectrum

Category: Data Manipulation

Format: `CNVFL` kmax

Qualifiers: /KRNL=(GAUSS,SINEB) /PASS=(HIGH,LOW) /END=(EXT,LP,ZER)

Qualifier Defaults: /KRNL=GAUSS /PASS=HIGH /END=EXT

Defaults: 8

Description:
`CNVFL` convolves the data in the visible processing buffer with a filter kernel. The argument kmax sets the maximum
filter component. The filter kernel will contain nkrnl=2\*kmax+1 points. If kmax is omitted RNMR will prompt for it with
8 as a default. The value of kmax can range from 1 to 32 inclusive.

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
`COLOR` sets the color of elements of the display. /BG sets the color of the background and /CURSOR sets the color of
all cursors. /REAL and /IMAG set the color of the real and imaginary data respectively.

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
`CONJG` complex conjugates the data in the visible processing buffer updating the buffer.
## CONLIM
Set contour plot height limits

Category: `ZO2DC`

Format: `CONLIM` min max

Defaults: current current

Description:
`CONLIM` sets intensity limits for contour plotting. Contours will only be drawn for intensities between these limits.
If either min or max is omitted from the command line, RNMR will prompt for the contour limit with its current value as
the default. If both min and max are 0.0 RNMR sets max to 1.0; min remains 0.0. If min and max are not both zero, max
must be greater than min. When a contour plot is generated, the maximum contour level will be max while the minimum
contour level will approach but not equal min.
## CONMD
Set contour plotting mode

Category: `ZO2DC`

Format: `CONMD` mode

Defaults: current

Description:
`CONMD` sets the contour plotting mode. The argument mode may be entered as ABS, NEG, or POS. If mode is omitted RNMR
will prompt for a contour plotting mode with the current mode as a default.
## COSSQ
Perform cosine squared apodization

Category: Data Manipulation

Format: `COSSQ` time0

Defaults: (size+1)\*step

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`COSSQ` multiplies the data in the visible processing buffer by a cosine squared function which goes to zero at time0
updating the buffer.
## CPXV
Complex merge two buffers

Category: Data Manipulation

Format: `CPXV` src dst

Defaults: 2 1

Description:
`CPXV` combines the real parts of [processing buffers](syntax#buffers) src and dst to form the real and imaginary parts
of dst:

 	DST = COMPLEX(REAL(DST),REAL(SRC))

 or
    REAL(DST) = REAL(DST)
    IMAG(DST) = REAL(SRC)

If either argument is omitted, RNMR will prompt for a buffer number. The default source is buffer 2 while the default
destination is buffer 1. The src and dst buffers must have the same domain and active size (though not necessarily the
same allocated size).
## CPY
Copy record

Category: Data Storage

Format: `CPY` src dst

Defaults: rrec wrec

Description:
`CPY` copies [record](syntax#records) src into record dst. `CPY` copies both parameters and data from source to
destination. If no source [record number](syntax#records) is specified RNMR will prompt for it with the current read
record pointer (as displayed and set by `PTRA`) as a default. If no destination record is specified RNMR will not prompt
for it and will use the write record pointer (as displayed and set by `PTRA`). If the specified destination record is
already in use RNMR will use the next available record. If RNMR selects the destination record for either of the above
reasons the record number will be printed as an informational message after copying is complete.
## CPYMAC
Copy macro

Category: Macro

Format: `CPYMAC` name1 name2

Defaults: temp temp

Description
`CPYMAC` copies the contents of macro name1 into a new macro name2. If either name is omitted RNMR will prompt for it
with temp as a default.
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

Format: `CRTFIL` fspec

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

Qualifiers: /END=<end\>

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
currently simply an alias to it. As such `DLY` should be used in place of `D`.
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
default. `DLTMAC` will delete the file in which the macro is stored. To Remove the macro from RNMR without deleting the
file use `REMMAC`
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
`DLY` sets the length of a pulse program delay indicated by name. /DLY will interpret time in milliseconds while /PLS
will interpret time in microseconds. The length of a delay can range from 0 to 40 seconds. A pulse program must be
loaded using `PPEX` in order for `DLY` to be used to set the length of any delays.

Due to restrictions on the speed of the pulse programmer delays are rounded to the nearest 10 microseconds. Delays may
be entered with more precision than this limit, but the additional precision will have no effect on the actual length of
the delay.
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
shifted to the right by an amount specified by time. The portion of the buffer vacated by this shift is filled with the
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

Category: Macro

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

If an export file has been opened with `OPNEXP` the data will be stored in that file and `EXP` will neither use nor
prompt for fspec. The format must match the format specified in `OPNEXP`.

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

If an export file has been opened with `OPNEXP` the data will be stored in that file and `EXP1D` will neither use nor
prompt for fspec. The format must match the format specified in `OPNEXP`.

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

If an export file has been opened with `OPNEXP` the data will be stored in that file and `EXP2D` will neither use nor
prompt for fspec. The format must match the format specified in `OPNEXP`.

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

If an export file has been opened with `OPNEXP` the data will be stored in that file and `EXP2D` will neither use nor
prompt for fspec. The format must match the format specified in `OPNEXP`.

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

Prerequisites: For RNMRA: Acquisition stopped (HALT). For RNMRP: no restrictions

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

Prerequisites: (LOAD) by `EX`; the acquisition must be stopped (HALT); RNMRA only.

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

If an import file has been opened with `OPNIMP` the data will be stored in that file and `IMP` will neither use nor
prompt for fspec. The format must match the format specified in `OPNIMP`.

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

If an import file has been opened with `OPNIMP` the data will be stored in that file and `IMP1D` will neither use nor
prompt for fspec. The format must match the format specified in `OPNIMP`.

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

If an import file has been opened with `OPNIMP` the data will be stored in that file and `IMP2D` will neither use nor
prompt for fspec. The format must match the format specified in `OPNIMP`.

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

If an import file has been opened with `OPNIMP` the data will be stored in that file and `IMP3D` will neither use nor
prompt for fspec. The format must match the format specified in `OPNIMP`.

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

Format: `IXVAL` pos

Default : current_cursor_position

Description:
`IXVAL` returns the index of the data point nearest to a position specified in the current units of the visible
processing buffer. If no position is specified RNMR will prompt for it with the current cursor position as a default.
If the specified position is outside of the actual data in the visible processing buffer `XVAL` will return the index of
the closest point (the leftmost or rightmost point). The converted value is printed as an informational message.

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
`LOG` writes a line to the logging window. If no line is specified RNMR will prompt for it. `LOG` cannot be used unless
logging is enabled (`SET LOG ON`).
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
`LPDEV` sets the device to use for text printing. The currently available printing devices are:

- E460A
- E460B
- LJ2430
- LJ2430B
- LJ4050
- LJ5

If no device is specified RNMR will prompt for it with the current text printing device as a default. If the text
printing device is changed (device is not the current device) RNMR will set the text printing flag (as set and displayed
by `SET LP`) on, indicating that text should be physically printed by the printing device rather than saved to the text
printing file (as set and displayed by `LPFIL`).
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
## LPFIL
Set text printer file

Category: Printing

Format: `LPFIL` fspec

Defaults: current

Description:
`LPFIL` selects a file to use as the destination for printing text. Commands that would print text can write to the file
instead of sending the text to a printer. Subsequent text printing commands will overwrite the file. If no file is
specified RNMR will prompt for it with the current text printer file as a default.

If the text printer file is changed (fspec is not the current fspec) RNMR will set the text printer flag (as set and
displayed by `SET LP`) off, indicating that text should be saved to the text printing file rather than physically
printed by the printer device (as set and displayed by `LPDEV`).
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

Prerequisites: Acquisition stopped (HALT), RNMRA only

Description:
`NABLK` sets the number of blocks into which the aquisition buffer is partitioned. If nablk is not provided RNMR will
prompt for it with the current value as a default. If nablk is 0 the maximum possible number of acquisition blocks will
be used.
## NAMD
Set number of acquisition modes

Category: Acquisition

Format: `NAMD` namd

Qualifiers: /ACQ /BLK /TPPI

Qualifier Defaults: /ACQ

Defaults: current

Prerequisites: RNMRA only

Description:
`NAMD` sets the number of acquisition and pulse program modes to use, i.e. the length of the phase cycle. If nablk is
not provided RNMR will prompt for it with the current value as a default. The /BLK qualifier is used to set the number
of block acquisition modes and is typically used to set the number of steps in hypercomplex acquisition of
multidimensional spectra. The /TPPI qualifier is used to set the number of modes for TPPI acquisition.
## NCHN
Set number of channels

Category: Acquisition

Format: `NCHN` nchn

Defaults: current

Prerequisites: RNMRA only

Description:
`NCHN` sets the number of channels to be used. If nchn is not provided RNMR will prompt for it with the current value as
a default. Note that the number of channels is also set implicitly by the `CHN` command.
## NCON
Set number of contour levels

Category: `ZO2DC`

Format: `NCON` ncon

Qualifiers: /LIN /LOG

Qualifier defaults: current

Defaults: current

Description:
`NCON` sets the number of contour levels to use. If ncon is omitted RNMR will prompt for it with the current value as a
default. /LIN is used for linearly spaced contours while /LOG is used for logarithmically spaced contours.
## NDEC
Set number of decimal places

Category: Misc.

Format: `NDEC` unit ndec

Defaults: current current

Description:
`NDEC` sets the number of decimal places to use when displaying values with a given unit. If unit is omitted then RNMR
will prompt for it with the current time unit as a default. If ndec is omitted RNMR will prompt for it with the current
value as a default.
## NDLY
Set number of shots to discard

Category: Acquisition

Format: `NDLY` ndly

Defaults: current

Prerequisites: RNMRA only

Description:
`NDLY` sets the number of dummy scans to run before starting acquisition. If ndly is omitted RNMR will prompt for it
with the current value as a default.
## NDSP
Set number of shots between display update

Category: Acquisition

Format: `NDSP` ndsp

Defaults: current

Prerequisites: RNMRA only

Description:
`NDSP` sets the number of shots to acquire between display updates. If ndsp is omitted RNMR will prompt for it with the
current value as a default.
## NEG
Negates buffer

Category: Data Manipulation

Format: `NEG`

Description:
`NEG` replaces the contents of the visible processing buffer with itself multiplied by -1.
## NG
Continue acquisition

Category: Acquisition

Format: `NG` ndly na

Defaults: current current

Prerequisites: (LOAD) by `EX`; the acquisition must be stopped (HALT); RNMRA only.

Description:
`NG` continues an experiment much like `GO` but performs dummy scans. If either ndly or na is omitted RNMR will use the
stored values to determine the number of dummy scans/the scan limit respectively without prompting for values.
## NOISE
Generate complex random noise

Category: Data Manipulation

Format: `NOISE` sf

Defaults: 1.0

Description:
`NOISE` fills the visible processing buffer with randomly generated noise. The parameter sf is a scaling factor that is
applied to the noise. If sf is omitted RNMR will not prompt for it and will use 1.0 as the scalinf factor.
## NOP
Null operation

Category: Misc.

Format: `NOP`

Description:
`NOP` performs no operation.
## NORM
Set scale to normalize display

Category: Display Control

Format: `NORM`

Description:
`NORM` rescales the data in the visible processing buffer such that the point within the display limits that has the
largest magnitude has magnitude 1.0.
## NUC
Set synthesizer nucleus

Category: Acquisition

Format: `NUC` chan nucnam

Defaults: 1 current

Prerequisites: For RNMRA: Acquisition stopped (HALT). For RNMRP: no restrictions

Description:
`NUC` assigns a nucleus nucnam to a synthesizer. The synthesizer is selected by chan which refers to a logical channel.
If chan is omitted, RNMR will prompt for a synthesizer number with 1 as the default. Since RNMR currently supports up to
four synthesizers, legal values of chan are integers from 1 to 4. If nucnam is omitted RNMR will promt for it with the
current nucleus as a default. The nucleus is used to look up the parameters used for tasks such as converting Hz to ppm.
In RNMRA this includes determining the frequency used for the pulses.
## NUCD
Define nucleus table entry

Category: Nuclei

Format: `NUCD` nucnam hi lo

Defaults: none current(1.0) current(0.0)

Description:
`NUCD` defines or modifies a nucleus table entry for nucnam. If nucnam is omitted RNMR will prompt for it with UNKN as a
default. The PPM to Hz conversion factor in MHz for the nucleus is set by hi. If hi is omitted RNMR will prompt for it
with a default of either the current value if the nucleus already exists or 1.0 if it does not. The reference frequency
in Hz for the nucleus is set by lo. If lo is omitted RNMR will prompt for it with a default of either the current value
if the nucleus already exists or 0.0 if it does not.
## NUCDL
Delete nucleus table entry

Category: Nuclei

Format: `NUCDL` nucnam

Defaults: none

Description:
`NUCDL` deletes the nucleus entry table for nucnam. If nucnam is not specified RNMR will prompt for it.
## NWAIT
Set number of shots to wait

Category: Acquisition

Format: `NWAIT` nwait

Defaults: current

Description:
`NWAIT` sets the number of shots to wait before `WAIT` is satisfied. If nwait is omitted RNMR will prompt for it with
the current value as a default. If nwait is set to 0 `WAIT` will wait for na shots as set and displayed by the `NA`
command.
## NXTDO
Cycle macro `DO` loop

Category: Macro

Format: `NXTDO`

Prerequisites: Macro only (MAC)

Description:
`NXTDO` skips to the beginning of the next iteration of a macro `DO` loop without executing the rest of the commands in
the loop. `NXTDO` must fall between an instance of `DO` and its matching `ENDDO`.

# O
---
## OFF
Set offset from reference frequency

Category: Acquisition

Format: `OFF` syn off

Defaults: current current

Description:
Defines nucleus reference frequency by assigning value to synthesizer offset frequency. The nucleus reference frequency
modified is that associated with the processing buffer synthesizer.
## OFFA
Set offset from reference frequency

Category: Acquisition

Format: `OFFA` syn off

Defaults: current current

Description:
Defines nucleus reference frequency by assigning value to synthesizer offset frequency. The nucleus reference frequency
modified is that associated with the acquisition buffer synthesizer.
## ONERR
Set macro error handler

Category: Macro

Format: `ONERR` label

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`ONERR` specifies a statement label to jump to in the event of an error condition or control-z. If no label is provided
RNMR will not prompt for it and any previous error label set using `ONERR` will be unset.
## OPNARV
Open archive

Category: Data Storage

Format: `OPNARV` arv name

Qualifiers: /RD /WRT /FORCE

Qualifier Defaults: /WRT for arv 1: /RD for others

Defaults: 1 TEMP

Description:
`OPNARV` opens an archive for access by RNMR. The archive number is specified by arv and must be an integer from 1 to 4.
If no archive number is specified RNMR will prompt for it with a default of 1. The parameter name specifies the name of
the archive file that is to be opened. If no name is specified RNMR will prompt for it with a default of temp. The /RD
and /WRT qualifiers alter the access to the archive. /RD will cause the archive to be opened with read access. /WRT will
cause the archive to be opened with read and write access. If neither /RD or /WRT is specified then `OPNARV` will use
/WRT for archive 1 and /RD for all other archive numbers.

/FORCE will allow RNMR to open an archive with write access even if there is already a lock file present for it. These
lock files are intended to prevent multiple instances of RNMR from trying to write to the same archive simultaneously.
Use of /FORCE might be necessary if RNMR crashed and was unable to delete the lock file. This option should be used
carefully as opening an archive with write access in multiple instances of RNMR at the same time can lead to corruption
of data.
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
## OPNEXP
Open export file

Category: Foreign

Format: `OPNEXP` format fspec

Defaults: ascii temp.<format>

Description:
`OPNEXP` opens a file for data export. All export commands (`EXP`, `EXP1D`, etc.) between `OPNEXP` and `CLSEXP` will
export to this file. If no format is specified RNMR will prompt for it with a default of ASCII. The foreign formats
currently supported by `OPNEXP` are:

- ASCII
- BINARY
- BRUKER
- PIPE
- SIFT

All export commands using this file must use the same format as specified in `OPNEXP`. If no fspec is provided RNMR will
prompt for a file name with temp.<format> as the default. The file extension of this default is determined by the
format.
## OPNIMP
Open import file

Category: Foreign

Format: `OPNIMP` format fspec

Defaults: ascii temp.<format>

Description:
`OPNIMP` opens a file for data import. All import commands (`IMP`, `IMP1D`, etc.) between `OPNIMP` and `CLSIMP` will
import from this file. If no format is specified RNMR will prompt for it with a default of ASCII. The foreign formats
currently supported by `OPNIMP` are:

- ASCII
- BINARY
- BRUKER
- SIFT

All import commands using this file must use the same format as specified in `OPNIMP`. If no fspec is provided RNMR will
prompt for a file name with temp.<format> as the default. The file extension of this default is determined by the
format.
## OPNPLT
Open plot stream 	

Category: Printing

Format: `OPNPLT`

Description:
`OPNPLT` opens a plot stream. All plots between `OPNPLT` and `CLSPLT` will appear on one sheet of paper.
## OPNRD
Open file for reading

Category: File IO

Format: `OPNRD` filename

Default : temp.wrt

Description:
`OPNRD` opens an ASCII file for read-only access by the command `RDWRT`. If no file is specified RNMR will prompt for it
with a default of temp.wrt.
## OPNWRT
Open file stream for writing

Category: File IO

Format: `OPNWRT` filename

Qualifiers: /APPEND

Qualifier Defaults: none

Defaults: temp.wrt

Description:
`OPNWRT` opens a an ASCII file with write access. All write commands between `OPNWRT` and `CLSWRT` will appear in one
file. By default the file will be overridden if it already exists, but the /APPEND qualifier can be used to make write
commands append to the file instead.

# P
---
## P
Set pulse length

Category: Acquisition

Format: `P` pls usec

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD); RNMRA only

Description:
`P` is an old command for setting the length of pulses. It has been replaced with the `PLS` command and is currently
simply an alias to it. As such `PLS` should be used in place of `P`.
## PARB
Set blocked record parameters

Category: Blocked Records

Format: `PARB` rec dir dim dom syn first step

Defaults: irrec 1 current current current current current

Description:
`PARB` sets the parameters for interpreting a blocked record.
## PC
Incremental phase correction

Category: Data Manipulation

Format: `PC` dphi0 dphi1

Defaults: 0 0

Description:
`PC` performs an incremental phase correction using the provided zero order (dphi0) and first order (dphi1) phase
factors. The correction is incremental in the sense that it alters the current phase parameters by these values. RNMR
will not prompt for either of the arguments and will use 0 if they are omitted.
## PEN
Select plot pen

Category: Printing

Format: `PEN` pen

Defaults: current

Qualifiers: /DATA /LABEL

Qualifier Defaults: /DATA

Description:
`PEN` selects a pen for plotting. For laser plotters, pen#=1 selects a thin line and pen#=2 selects a thick line. /DATA
and /LABEL can be used to separately set the pen for the data and the labels in a plot. If no pen parameter is provided
RNMR will prompt for it with the current value as a default.
## PGSIZE
Set page size for plot

Category: Printing

Format: `PGSIZE` xsiz ysiz

Defaults: current current

Description:
`PGSIZE` sets the size of a plot page in inches. If either xsiz or ysiz are not provided RNMR will prompt for them with
the current value as a default.
## PH
Interactive phase correction

Category: Data Manipulation

Format: `PH`

Description:
`PH` performs interactive phase correction. While `PH` is active the following subcommands can be used to manipulate the
phase of the spectrum.

Subcommands:

Command | Description
------- | -----------
Enter | Terminate with current phase values
C  | Select constant phase value for change
D  | Select decrement direction
I  | Select increment direction
L  | Select linear phase value for change
P  | Select current cursor position as pivot for linear value
Q  | Terminate with original phase values
V  | Change phase value after prompt
Z  | Call `ZO` to enable moving the cursor
0-2 | Change current value by 10^N degrees

Either the zero or first order phase parameter can be changed up or down in steps of 1, 10, or 100. To move the pivot
point, use Z to call `ZO`. Then move the cursor and press enter to exit `ZO`. Finally press P to move the pivot to the
cursor.
## PIDL
Set lock PID gain factors

Format: `PIDL` fctrp fctri

Qualifiers: /P /I

Qualifier Defaults: /P /I

Defaults: current current

Prerequisites: RNMR lock control. RNMRA only.

Description:
`PIDL` sets the proportional and integral gain factors for the lock PID. /P and /I can be used to select which parameter
to update. If no qualifier is supplied RNMR will set both parameters. If a gain factor to be set is not provided RNMR
will prompt for it with the current value as a default.
## PLDEV
Select plotting device

Category: Printing

Format: `PLDEV` device

Defaults: current

Description:
`PLDEV` sets the device to use for plotting. The currently available plotting devices are:

- E460A
- E460B
- LJ2430
- LJ2430B
- LJ4050
- LJ5

If no device is specified RNMR will prompt for it with the current plotting device as a default. If the plotting device
is changed (device is not the current device) RNMR will set the plotter flag (as set and displayed by `SET PL`) on,
indicating that plots should be physically printed by the plotting device rather than saved to the plot file (as set and
displayed by `PLFIL`).
## PLFIL
Set plot file

Category: Printing

Format: `PLFIL` fspec

Defaults: current

Description:
`PLFIL` selects a file to use as the destination for plotting. Plotting commands can write plots to the file in a
postscript format instead of sending the plots to a printer. Subsequent plotting commands that are not between `OPNPLT`
and `CLSPLT` will overwrite the plot file. If no file is specified RNMR will prompt for it with the last plot file as a
default.

If the plot file is changed (fspec is not the current fspec) RNMR will set the plotter flag (as set and displayed by
`SET PL`) off, indicating that plots should be saved to the plot file rather than physically printed by the plotting
device (as set and displayed by `PLDEV`).
## PLOT
Plot current 1D display

Category: Printing

Format: `PLOT`

Description:
`PLOT` plots the current one dimensional display to either the plotting device specified by `PLDEV` or the file
specified by `PLFIL`.
## PLOTC
Plot 2D contours

Category: Printing

Format: `PLOTC` rec slice

Defaults: current 1

Description:
`PLOTC` plots a two dimensional contour plot of a blocked record to either the plotting device specified by `PLDEV` or
the file specified by `PLFIL`. If no record is specified RNMR will prompt for it with the current read record as a
default. The selected record must be a blocked record.

The last parameter, slice specifies which 2D slice of a 3D or 4D source record should be plotted. If the source record
has only two dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it and will plot the first slice.
Note that the current mapping of dimensions to directions (as displayed and set by `DIRB`) will affect the selection of
which one-dimensional blocks of the record comprise the 2D slice and will thus be plotted. Slice is interpreted as a
linear index over the 3rd/4th dimensions.
## PLS
Set pulse length

Category: Acquisition

Format: `PLS` name time

Qualifiers: /DLY /PLS

Qualifier Defaults: /PLS

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD); RNMRA only

Description:
`PLS` sets the length of a pulse indicated by name. /DLY will interpret time in milliseconds while /PLS will interpret
time in microseconds. The length of a pulse can range from 0 to 1200 microseconds. A pulse program must be loaded using
`PPEX` in order for `PLS` to be used to set the length of any pulses.
## PLSIZE
Set plot size

Category: Printing

Format: `PLSIZE` xsiz ysiz

Defaults: current current

Description:
`PLSIZE` sets the size of a plot in inches. If either xsiz or ysiz are not provided RNMR will prompt for them with
the current value as a default.
## POLAR
Convert buffer to poalr coordinates

Category: Data Manipulation

Format: `POLAR`

Description:
`POLAR` converts the data in the visible processing buffer into polar coordinates. The magnitude of the data is placed
in the real part of the buffer and the phase in the imaginary part of the buffer.
## POPLST
Pop a value from a list

Category: Lists

Format: `POPLST` nam

Qualifiers: /HEAD /TAIL

Qualifier Defaults: /TAIL

Defaults: temp

Description:
`POPLST` pops a value from the end of a list specified by nam. If no list is specified RNMR will prompt for it with temp
as a default. /HEAD or /TAIL may be used to determine which end of the list to pop a value from. By default RNMR pops
from the tail of the list. The value is removed from the list and printed as an informational message.
## POSL
Set lock channel center position

Category: Lock

Format: `POSL` pos

Defaults: current

Prerequisites: RNMR lock control. (RNMRA only.)

Description:
`POSL` sets the position of the center of the lock. The value must be between -50.0 and 50.0 inclusive. If no position
is specified RNMR will prompt for it with the current position as a default.
## PP
Interactive peak picking

Category: Data Manipulation

Format: `PP`

Description:
`PP` performs interactive peak picking. While `PP` is active the following subcommands can be used to manipulate the
spectrum.

Subcommands:

Command | Description
------- | -----------
Enter | Terminate
L  | Move left one peak
Q  | Terminate
R  | Move right one peak
T  | Set peak picking threshold
Z  | Call `ZO`

RNMR selects peaks based upon the following criteria. In order to be a peak a point must have an absolute intensity
greater than the threshold. If the intensity is negative it must be less than the intensity of the points immediately to
the left and right of it. If the intensity is positive it must be greater than the intensity of the points immediately
to the left and right of it.
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

Format: `PPFLG` ind val

Defaults: 1 current

Prerequisites: Pulse program loaded (LOAD); RNMRA only

Description:
`PPFLG` is an old command for setting the state of pulse program flags. It has been replaced with the `FLAG` command and is
currently simply an alias to it. As such `FLAG` should be used in place of `PPFLG`.
## PPMD
Set pulse program phase mode

Category: Acquisition

Format: `PPMD` nam spec1 spec2 ... spec8

Defaults: 1 none none ... none

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`PPMD` sets pulse program phase cycling. The parameter nam specifies which phase cycle to set. These phase cycles are
mapped to pulses in the pulse program. If no name is provided RNMR will prompt for it with 1 as a default. /MOD defines
the number of different phase values to be used. These phase values will be equally spaced so the default value of 4
yields 90° phase steps while for example 6 would yield 60° steps. Each element or mode of the `PPMD` sequence is a
number from 1 to the value specified by /MOD. With the default qualifier /ACQ these modes indicate a sequence of phase
shifts to apply on sequential shots.

The default value is /MOD=4, which yields phase values of (0°, 90°, 180°, 270°) corresponding to the numbers 1 through 4.
The maximum number of acquisition modes in a sequence is 64. If the number of modes entered is less than 64, the
specified modes will be replicated to a 64 mode sequence. For example, if the user specifies:

        PPMD 1111 3333

the eight modes specified are replicated by RNMR to give a full 64 step phase cycle:

     11113333 11113333 11113333 11113333
     11113333 11113333 11113333 11113333

While all sequences are replicated to 64 modes internally, only a number of steps equal to the active phase cycle length
(set by `NAMD`) are actually used. The sequence of modes may be broken up across multiple command line arguments as
shown in the example above. This can help improve readability.

If `PPMD` is called with no modes specifiers RNMR will not prompt for modes. Instead it will print the current phase
cycle out to the active phase cycle length with 16 modes per line.

The /BLK qualifier is used to setup additional phase shifts for different blocks of acquisition. The number of blocks
can be set using `NAMD /BLK`. This capability is typically used to set up phase differences used for the different steps
in hypercomplex acquisition of multi-dimensional spectra.
## PRGLST
Purge list

Category: Lists

Format: `PRGLST` nam

Defaults: temp

Description:
`PRGLST` removes all of the values from list nam. If nam is not specified RNMR will prompt for it with a default of
temp.
## PRGTBL
Purge name table

Category: Tables

Format: `PRGTBL` nam

Defaults: temp

Description:
`PRGTBL` removes all of the entries from name table nam. If nam is not specified RNMR will prompt for it with a default
of temp.
## PROF
Calculate profile of blocked 2D record

Category: Data Manipulation

Format: `PROF` rec slice

Defaults: current 1

Description:
`PROF` calculates a one dimensional profile of a two dimensional slice of a blocked record. Each point in the profile
will be set to the maximum value at that point across all of the blocks. If no record is specified RNMR will prompt for
it with the current read record as a default. The selected record must be a blocked record.

The last parameter, slice specifies which 2D slice of a 3D or 4D source record should be included. If the source record
has only two dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it and will use the first slice.
Note that the current mapping of dimensions to directions (as displayed and set by `DIRB`) will affect the selection of
which one-dimensional blocks of the record comprise the 2D slice and will thus be used to calculate the profile. Slice
is interpreted as a linear index over the 3rd/4th dimensions.
## PROFB
Calculate profile of blocked record along a dimension

Category: Data Manipulation

Format: `PROFB` src dst dim

Defaults: current next last

Defaults:
`PROJB` calculates the profile of a blocked record src along dimension dim and stores the result in blocked record dst.
If no source record is provided RNMR will prompt for it with the current read record as a default. The source record
must be a blocked record with size greater than one in the chosen dimension. Additionally the source record must have a
large enough NDIMX to access the record along the specified dimension. NDIMX is specified when the record is allocated
and determines along which directions the blocked record may be accessed. If no destination record is provided RNMR will
not prompt for it and will store the results in the next available record. If no dimension is passed RNMR will prompt
for it with the last accessible dimensions as a default. The interpretation of the dim parameter is also affected by the
dimension order set by `DIRB`. The result of the profile operation will have a size of one along the profile
dimension. Each point in the destination record will be set to the maximum value at that point across all of the blocks.
## PROG
Identify program

Category: Misc.

Format: `PROG`

Description:
`PROG` prints the identity of the program (RNMRA or RNMRP) and the modification time of the corresponding file to the
console.
## PROJ
Calculate projection of blocked 2D record

Category: Data Manipulation

Format: `PROJ` rec slice

Defaults: current 1

Description:
`PROJ` calculates a one dimensional projection of a two dimensional slice of a blocked record. Each point in the
projection will be set to the sum of the values at that point across all of the blocks. If no record is specified RNMR
will prompt for it with the current read record as a default. The selected record must be a blocked record.

The last parameter, slice specifies which 2D slice of a 3D or 4D source record should be included. If the source record
has only two dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it and will use the first slice.
Note that the current mapping of dimensions to directions (as displayed and set by `DIRB`) will affect the selection of
which one-dimensional blocks of the record comprise the 2D slice and will thus be used to calculate the projection.
Slice is interpreted as a linear index over the 3rd/4th dimensions.
## PROJB
Calculate projection of blocked record along a dimension

Category: Data Manipulation

Format: `PROFB` src dst dim

Defaults: current next last

Defaults:
`PROJB` calculates the projection of a blocked record src along dimension dim and stores the result in blocked record
dst. If no source record is provided RNMR will prompt for it with the current read record as a default. The source
record must be a blocked record with size greater than one in the chosen dimension. Additionally the source record must
have a large enough NDIMX to access the record along the specified dimension. NDIMX is specified when the record is
allocated and determines along which directions the blocked record may be accessed. If no destination record is provided
RNMR will not prompt for it and will store the results in the next available record. If no dimension is passed RNMR will
prompt for it with the last accessible dimensions as a default. The interpretation of the dim parameter is also affected
by the dimension order set by `DIRB`. The result of the projection operation will have a size of one along the
projection dimension. Each point in the destination record will be set to the sum of the values at that point across all
of the blocks.
## PRTARG
Print arguments

Category: Misc.

Format: `PRTARG` arg1 arg2 ... arg10

Defaults: none none none

Description:
`PRTARG` prints its arguments to standard out.
## PS
Set phase

Category: Data Manipulation

Format: `PS` phi0 phi1

Defaults: cur_gbl cur_gbl

Description:
`PS` phases the spectrum to the specified absolute phase values. If either phase parameter is omitted RNMR will not
prompt for them and will use the current global values. The global values are updated anytime a spectrum is phased. Thus
`PS` with no arguments can be used to phase a new data set after `FT` to the same phase values as the last thing that
was phased.
## PSHLST
Push a value to a list

Category: Lists

Format: `PSHLST` nam val

Qualifiers: /HEAD /TAIL

Qualifier Defaults: /TAIL

Defaults: temp none

Description:
`PSHLST` pushes a value to the end of a list specified by nam. If no list is specified RNMR will prompt for it with temp
as a default. If the values is omitted RNMR will prompt for it with no default. /HEAD or /TAIL may be used to determine
which end of the list to push a value to. By default RNMR pushes to the tail of the list.
## PSUBV
Subtract polar buffers

Category: Data Manipulation

Format: `PSUBV` src dst

Defaults: 2 1

Description:
`PSUBV` subtracts a polar src buffer from a polar dst buffer and stores the result in dst:

    REAL(DST)=SQRT(REAL(DST) * REAL(SRC))
    IMAG(DST)=IMAG(DST) - IMAG(SRC)

If either argument is omitted, RNMR will prompt for a buffer number. The default source is buffer 2 while the default
destination is buffer 1. The src and dst buffers must have the same domain and active size (though not necessarily the
same allocated size).
## PSX
Set transmitter phase

Category: Acquisition

Format: `PSX` chan psx phase

Defaults: 1 1 current

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`PSX` sets a transmitter phase. If chan or psx are omitted RNMR will prompt for them with a default of 1. If phase is
omitted RNMR will prompt for it with the current phase of that psx on that channel as a default.
## PSXEX
Load transmitter phase program from PAM memory.

Category:

Format: `PSXEX`

Defaults:
## PTRA
Set read and write archive pointers

Category: Data Storage

Format: `PTRA` read_rec write_rec

Defaults: current current

Description:
`PTRA` sets the read and write archive pointers. These pointers are the default values for most commands involving
records. If either pointer is omitted RNMR will prompt for it with the current value as a default. The read and write
archive pointers are also set anytime a command reads from or writes to a record respectively.
## PTRB
Set read and write blocked record pointers

Category: Blocked Record

Format: `PTRB` rec rblk wblk

Defaults: current current current

Description:
`PTRB` sets the read and write pointers for a blocked record. These pointers are used to determine the default values
for most commands involving loading from or saving to blocked records. If no record is specified RNMR will prompt for it
with the current read record as a default. The record must be a blocked record. If either pointer is omitted RNMR will
prompt for it with the current value as a default. The read and write blocked record pointers are also set anytime a
command reads from or writes to the blocked record respectively. Most commands that rely on these pointers will
increment them before use, so entering 0 for either pointer indicates to start from the beginning of the blocked record.
## PWR
Set transmitter coarse power level

Category: Acquisition

Format: `PWR` chan index pwr

Defaults: 1 1 current

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`PWR` sets a coarse power level for a transmitter. If no channel is specified RNMR will prompt for it with a default
value of 1. Each transmitter has two coarse power levels that can be used in a pulse sequence. An index of 1 corresponds
to pwrh and an index of 2 indicates pwrl. If no index is specified RNMR will prompt for it with a default of 1. The
power level must be between 0.0 and 100.0 inclusive. If no power level is provided RNMR will prompt for it with the
current value as a default.
## PWRL
Set lock channel power level

Category: Lock

Format: `PWRL` pwr

Defaults: current

Prerequisites: RNMR lock control. RNMRA only.

Description:
`PWRL` sets the lock channel power level. The power level must be between 0.0 and 100.0 inclusive. If no power level is
provided RNMR will prompt for it with the current value as a default.
## PWX
Set transmitter fine power level

Category: Acquisition

Format: `PWR` chan nam pwr

Defaults: 1 1 current

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`PWX` sets the fine power level for a pulse on a given channel. If either the channel or the name of the power level to
set is omitted RNMR will prompt for them with a default of 1. The power level must be between 0.0 and 100.0 inclusive.
If no power level is provided RNMR will prompt for it with the current value as a default.
## PWXEX
Load power program  	Category:

Format: `PWXEX`

Defaults:

# Q
---
## QC
Perform software quadrature phase correction

Category: Data Manipulation

Format: `QC`

Prerequisites: Time domain only (TIME)

Description:
`QC` performs software quadrature phase correction. The cross correlation coefficient between the real and imaginary
buffers is obtained and the appropriate fraction of the imaginary buffer subtracted from the real buffer.
## QUIT
Quit acquisition

Category: Acquisition

Format: `QUIT`

Description:
`QUIT` Halts acquisition after the next complete phase cycle. Pressing Q while `QUIT` is waiting to finish a phase cycle
causes RNMR to halt immediately after the next shot.

# R
---
## RCVMIX
Set receiver quadrature mixing

Category: Acquisition

Format: `RCVMIX` valr vali

Qualifiers: /REAL /IMAG

Qualifier Defaults: /REAL /IMAG

Defaults: current current

Prerequisites: RNMRA only

Description:
`RCVMIX` sets the receiver mix correction values for the real and imaginary channels. This operation should generally
only be performed by the staff. /REAL and /IMAG determine whether to set the real or imaginary value. If no qualifier is
used both will be set.
## RCVOFF
Set receiver offset

Category: Acquisition

Format: `RCVOFF` valr vali

Qualifiers: /REAL /IMAG

Qualifier Defaults: /REAL /IMAG

Defaults: current current

Prerequisites: RNMRA only

Description:
`RCVOFF` sets the receiver offset correction values for the real and imaginary channels. This operation should generally
only be performed by the staff. /REAL and /IMAG determine whether to set the real or imaginary value. If no qualifier is
used both will be set.
## RD
Set recycle delay

Category: Acquisition

Format: `RD` sec

Defaults: current

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`RD` sets the recycle delay in seconds. The recycle delay is precise to the nearest tenth of a second. If no value is
provided RNMR will prompt for it with the current recycle delay as a default.
## RDARV
Read archive name

Category: Data Storage

Format: `RDARV` arv argnam

Qualifiers: /LCL /GBL /ERR=<label>

Qualifier Defaults: /LCL

Defaults: 1 none

Description:
`RDARV` reads the name of an open archive specified by arv. If arv is not specified RNMR will prompt for it with a
default of 1. The name can be saved in either a global or local argument (as selected by the /LCL or /GBL qualifiers)
named argnam. By default it will be saved to a local variable. If no argnam is provided RNMR will not prompt for it and
will print the archive name as an informational message instead of saving it to an argument. /ERR can be used to set a
label to jump to in the event that the archive name cannot be read.
## RDLST
Read list from file

Category: Lists

Format: `RDLST` nam fspec

Defaults: temp <nam>

Description:
`RDLST` reads values into a list from a file. This can be used to reload values saved using `WRTLST`. The list must have
already been allocated using `CRTLST` prior to using `RDLST`. If no list name is specified RNMR will prompt for it with
default of temp. If no file is specified RNMR will prompt for it with the list name as a default. If the file name has
no extension RNMR will add .wrt to it.
## RDPPS
Read PP symbol

Category: Pulse Program

Format: `RDPPS` typ nam argnam

Qualifiers: /LCL /GBL /ERR=<label>

Qualifier Defaults: /LCL

Defaults: none

Prerequisites: RNMRA only

Description:
`RDPPS` reads the value of a pulse program symbol. The type of the symbol is specified by typ and the name of the symbol
by nam. If either of these parameters is omitted RNMR will prompt for them with no default. The value can be saved in
either a global or local argument (as selected by the /LCL or /GBL qualifiers) named argnam. By default it will be saved
to a local variable. If no argnam is provided RNMR will not prompt for it and will print the value as an informational
message instead of saving it to an argument. /ERR can be used to set a label to jump to in the event that the pulse
program symbol value cannot be read.
## RDPPSNAM
Read PP symbol name

Category: Pulse Program

Format: `RDPPSNAM` typ ind argnam

Qualifiers: /LCL /GBL /ERR=<label>

Qualifier Defaults: /LCL

Defaults: none 1 none

Prerequisites: RNMRA only

Description:
`RDPPSNAM` reads the name of a pulse program symbol specified by its index. The type of the symbol is specified by typ
and the index of the symbol by ind. If nam parameters is omitted RNMR will prompt for them with no default. If ind is
omitted RNMR will prompt for it with a default of 1. The name can be saved in either a global or local argument (as
selected by the /LCL or /GBL qualifiers) named argnam. By default it will be saved to a local variable. If no argnam is
provided RNMR will not prompt for it and will print the name as an informational message instead of saving it to an
argument. /ERR can be used to set a label to jump to in the event that the pulse program symbol name cannot be read.
## RDSTR
Read tokens from a string

Category: Misc.

Format: `RDSTR` str nam1 nam2...

Qualifiers: /LCL /GBL /FIRST=<ind>

Qualifier Defaults: /LCL /FIRST=1

Defaults: none

Description:
`RDSTR` reads individual tokens from a string supplied by the str argument. The tokens are saved in either global or
local arguments (as selected by the /LCL or /GBL qualifiers) whose names are set by nam1, nam2, etc. /FIRST selects the
first token to save. By default this is set to 1 and the first token is saved to nam1 and the second to nam2 and so on.
It can be set to higher values so as to skip some number of tokens. RNMR will not prompt for any of the arguments to
`RDSTR`.
## RDTBL
Read name table values from file

Category: Tables

Format: `RDTBL` nam fspec

Defaults: temp <nam>

Description:
`RDTBL` reads values into a name table from a file. This can be used to reload values saved using `WRTTBL`. The table
must have already been allocated using `CRTTBL` prior to using `RDTBL`. If no table name is specified RNMR will prompt
for it with a default of temp. If no file is specified RNMR will prompt for it with the table name as a default. If the
file name has no extension RNMR will add .wrt to it.
## RDWRT
Read line from file

Category: File IO

Format: `RDWRT` nam1 nam2...

Qualifiers: /EOF=<lab> /FIRST=<ind> /LINE=<nam> /GBL /LCL

Qualifier Defaults: /LCL /FIRST=1

Defaults: none

Prerequisites: File open via `OPNRD`

Description:
`RDWRT` reads a line from a file that was opened with `OPNRD`. The line is split into tokens that are saved in either
global or local arguments (as selected by the /LCL or /GBL qualifiers) whose names are set by nam1, nam2, etc. /FIRST
selects the first token to save. By default this is set to 1 and the first token is saved to nam1 and the second to nam2
and so on. It can be set to higher values so as to skip some number of tokens. /LINE skips this tokenizing behavior and
saves the whole line as a global or local argument whose name is the nam specified via /LINE=<nam>.

/EOF can be used to set a label to jump to in the event end of file is encountered. If this qualifier is not used EOF
will instead cause an error.

After `RDWRT` has executed the file position will be have moved such that calling `RDWRT` will read the next line. To
return to the beginning of the file use `RWDRD`.
## REMGBL
Remove global arguments

Category: Arguments

Format : `REMGBL` first last

Defaults: temp <first>

Description:
`REMGBL` removes all global variables that alphabetically fall between first and last inclusive. If first is not
specified RNMR will prompt for it with a default of temp. If last is not specified RNMR will not prompt for it and will
remove only an argument whose name exactly matches first.
## REMLCL
Remove local arguments

Category: Arguments

Format : `REMLCL` first last

Defaults: temp <first>

Description:
`REMLCL` removes all local variables that alphabetically fall between first and last inclusive. If first is not
specified RNMR will prompt for it with a default of temp. If last is not specified RNMR will not prompt for it and will
remove only an argument whose name exactly matches first.
## REMLST
Remove list value

Category: Lists

Format: `REMLST` nam ind

Defaults: temp 1

Description:
`REMLST` removes the value at position ind from list nam. If nam is not specified RNMR will prompt for it with a default
of temp. If ind is not specified RNMR will prompt for it with a default of 1. The specified ind should not exceed the
number of values in the list.
## REMMAC
Remove macro table entry

Category: Macro

Format: `REMMAC` nam

Defaults: temp

Description:
`REMMAC` removes macro nam from the macro table. The macro will be removed from RNMR and cannot be used without being
reloaded, but unlike `DLTMAC` the macro file will not be deleted.
## REMPPS
Remove pulse programmer symbols

Category: Pulse Program

Format : `REMPPS` typ first last

Defaults: temp temp <first>

Description:
`REMPPS` removes all pulse programmer symbols of a specified type that alphabetically fall between first and last
inclusive. If typ or first is not specified RNMR will prompt for it with a default of temp. If last is not specified
RNMR will not prompt for it and will remove only a pulse programmer symbol whose name exactly matches first.
## REMSYM
Remove symbols

Category: Arguments

Format : `REMSYM` first last

Defaults: temp <first>

Description:
`REMSYM` removes all symbols that alphabetically fall between first and last inclusive. If first is not specified RNMR
will prompt for it with a default of temp. If last is not specified RNMR will not prompt for it and will remove only a
symbol whose name exactly matches first.
## REMTBL
Remove name table entries

Category: Tables

Format : `REMTBL` nam first last

Defaults: temp temp <first>

Description:
`REMTBL` removes all entries in name table nam that alphabetically fall between first and last inclusive. If nam or
first are not specified RNMR will prompt for them with a default of temp. If last is not specified RNMR will not prompt
for it and will remove only an entry whose name exactly matches first.
## RENMAC
Rename macro

Category: Macro

Format: `RENMAC` nam1 nam2

Defaults: temp temp

Description:
`REMMAC` renames macro nam1 to nam2. If either name is omitted RNMR will prompt for it with a default of temp.
## RGPIB
Read string from GPIB device

Category: Hardware

Format: `RGPIB` device

Defaults: none

Prerequisites: RNMRA only

Description:
`RGPIB` reads a string from a GPIB device. If no device is specified RNMR will prompt for one with no default.
## RMS
Calculate root-mean-square value of data

Category: Data Analysis

Format: `RMS` llim rlim

Qualifiers: /REAL /IMAG /COMPLEX

Qualifier Defaults: current display

Defaults: current current

Description:
`RMS` computes the root mean square of the data in the visual processing buffer between llim and rlim. If either limit
is omitted RNMR will not prompt for it and will use the current left or right display limit. /REAL or /IMAG will compute
the rms of the real or imaginary part of the buffer respectively. /COMPLEX will compute the rms of the magnitude of the
buffer. The computed value will be printed as an informational message.
## ROT
Rotate spectrum

Category: Data Manipulation

Format: `ROT` drot

Defaults: dstep

Description:
`ROT` rotates the visible processing buffer by an amount (drot) specified in the current units of that buffer. A portion
of the buffer drot wide is moved from the left edge of the buffer to the right edge of the buffer. If drot is not
specified RNMR will prompt for it with a default that is equal to a single point rotation.
## ROTP
Rotate spectrum

Category: Data Manipulation

Format: `ROTP` nrot

Defaults: 1

Description:
`ROTP` rotates the visible processing buffer by an amount (nrot) specified in points. A portion of the buffer nrot
points wide is moved from the left edge of the buffer to the right edge of the buffer. If nrot is not specified RNMR
will prompt for it with a default of 1.
## RPPSB
Read data byte from pulse programmer spectrometer bus

Category: Hardware

Format: `RPPSB` adr

Default: 0

Prerequisites: Pulse programmer spectrometer bus control implemented (CGFSB2); RNMRA only

Description:
`RPPSB` reads a data byte from the pulse programmer spectrometer bus. The adr parameter specifies the address to read
the byte from and may range of 0 to 255 inclusive. If adr is omitted RNMR will prompt for it with a default of 0.
## RPTDO
Repeat iteration of macro `DO` loop

Category: Macro

Format: `RPTDO`

Prerequisites: Macro only (MAC)

Description:
`RPTDO` repeats an iteration of a macro `DO` loop. It returns to the beginning of the loop without executing the rest of
the commands in the loop or incrementing the loop counter. Take care as this behavior can easily lead to an infinite
loop. `RPTDO` must fall between an instance of `DO` and itsmatching `ENDDO`.
## RRKC
Read data from an RKC device

Category: Hardware

Format: `RRKC` device

Defaults: none

Prerequisites: RKC device implemented; RNMRA only

Description:
`RRKC` reads data from a RKC device. If no device is specified RNMR will prompt for one with no default.
## RSB
Read data byte from spectrometer bus

Category: Hardware

Format: `RSB` adr

Defaults: 0

Prerequisites: Spectrometer bus control implemented (CGFSB1); RNMRA only

Description:
`RSB` reads a data byte from the spectrometer bus. The adr parameter specifies the address to read the byte from and may
range of 0 to 255 inclusive. If adr is omitted RNMR will prompt for it with a default of 0.
## RSTBUF
Restore buffer values from file

Category: Misc.

Format: `RSTBUF` fspec buf

Defaults: temp 1

Description:
`RSTBUF` restores buffer values from a file fspec written using `SAVBUF` and applies them to processing buffer buf. If
no fspec is provided RNMR will prompt for it with temp as a default. If no bufer is specified RNMR will not prompt for
it and will apply the loaded values to processing buffer 1 (the visible process buffer).
## RSTGBL
Restore global arguments from file

Category: Arguments

Format: `RSTGBL` fspec

Defaults: temp

Description:
`RSTGBL` restores global arguments from a file fspec written using `SAVGBL`. If no fspec is provided RNMR will prompt
for it with temp as a default. Note that global arguments from the file will overwrite existing arguments with the same
name.
## RSTHTR
Restore heater values from file

Category: Heater

Format: `RSTHTR` fspec

Defaults: temp

Prerequisites: RNMR heater control; RNMRA only

Description:
`RSTHTR` restores heater values from a file fspec written using `SAVHTR`. If no fspec is provided RNMR will prompt
for it with temp as a default.
## RSTLCK
Restore lock values from file

Category: Lock

Format: `RSTLCK` fspec

Defaults: temp

Prerequisites: RNMR lock control; RNMRA only

Description:
`RSTLCK` restores lock values from a file fspec written using `SAVLCK`. If no fspec is provided RNMR will prompt
for it with temp as a default.
## RSTLST
Restore lists from file

Category: Lists

Format: `RSTLST` fspec

Defaults: temp

Description:
`RSTLST` restores all lists from a file fspec written using `SAVLST`. If no fspec is provided RNMR will prompt for it
with temp as a default. `RSTLST` will replace the full set of lists and their values as viewed by `CATLST /VAL` with the
contents of fspec. Any lists that were already populated will be lost.
## RSTSHM
Restore shim values from file

Category: Shim

Format: `RSTSHM` fspec

Defaults: temp

Prerequisites: RNMR shim control; RNMRA only

Description:
`RSTSHM` restores shim values from a file fspec written using `SAVSHM`. If no fspec is provided RNMR will prompt
for it with temp as a default.
## RSTTBL
Restore name tables from file

Category: Tables

Format: `RSTTBL` fspec

Defaults: temp

Description:
`RSTTBL` restores all name tables from a file fspec written using `SAVTBL`. If no fspec is provided RNMR will prompt for
it with temp as a default. `RSTTBL` will replace the full set of name tables and their values as viewed by `CATTBL /VAL`
with the contents of fspec. Any tables that were already populated will be lost.
## RTNARG
Renames return arguments

Category: Macro

Format: `RTNARG` nam1 nam2...

Defaults: none

Description:
`RTNARG` renames values that are returned from a macro via `MEXIT` arguments. These return arguments are initially
stored in local arguments RTN$1, RTN$2, RT$3 etc. `RTNARG` renames these arguments to nam1, nam2, nam3 etc.
## RWDRD
Rewind file opened by `OPNRD`

Category: File IO

Format: `RWDRD`

Description:
`RWDRD` rewinds a file that was opened by `OPNRD`. This returns to the beginning of the file such that the next call to
`RDWRT` will read the first line in the file.
## RWDWRT
Rewind file opened by `OPNWRT`

Category: File IO

Format: `RWDWRT`

Description:
`RWDWRT` rewinds a file that was opened by `OPNWRT`. This returns to the beginning of the file such that the next call
to `WRT` will write to the beginning of the file.

# S
---
## SA
Save data to archive record

Category: Data Storage

Format: `SA` rec buf

Defaults: wrec 1

Description:
`SA` saves the date in a processing buffer to an archive record. The record must be in an archive which RNMR has read
access to. If no record is provided RNMR will not prompt for it and will use the next available record. Records in
archives other than 1 can be specified by either pre-pending the archive number and a ":" or specifying numbers larger
than 200. For example record # in archive 2 can be specified either as 2:# or by adding 200 to #. `SA` cannot write to
scratch records which must be written using `SS` or to blocked records which must be written using `SB`.

If no buffer is specified RNMR will not prompt for it and will save the data from processing buffer 1 (the visible
processing buffer).
## SAV
Save data and parameters to averager

Category: Acquisition

Format: `SAV` blk buf

Prerequisites: Acquisition stopped (HALT); Time domain only (TIME); RNMRA only

Description:
`SAV` transfers data and parameters from a processing buffer to the averager. The averager memory may be logically
partitioned into two or more blocks so that multiple FID's with different experimental parameters can be acquired at
once, without the need to start and stop acquisition many times. `SAV` transfers data to one of these blocks from a
processing buffer according to the user's choice of blk and buf.

The first parameter, blk specifies the averager block to transfer the data to. If blk is omitted RNMR will not prompt
for it and will transfer to block 1.

The second parameter, buf specifies which processing buffer to send data from. If no buffer is specified RNMR will not
prompt for it and will transfer data from process buffer 1 (the visible processing buffer).
## SAVARV
Save archive

Category: Data Storage

Format: `SAVARV` arv

Defaults: 1

Description:
`SAVARV` saves an archive to disk. If no archive is specified RNMR will prompt for it with a default of 1. Archives will
be automatically saved in a number of situations, but it can be useful to manually save an archive especially when
opening an archive in read only mode in RNMRP while it is open with write access in RNMRA. Using `SAVARV` in RNMRA and
then `UPDARV` in RNMRP ensures that all changes made from RNMRA are visible in RNMRP.
## SAVBUF
Save buffer value to file

Category: Misc.

Format: `SAVBUF` fspec buf

Defaults: temp 1

Description:
`SAVBUF` saves values from a specified processing buffer buf to a file on disk fspec which can be later be loaded using
`RSTBUF`. If no file is specified RNMR will prompt for it with temp as a default. If no buffer is specified RNMR will
not prompt for it and will save values from processing buffer 1 (the visible processing buffer).
## SAVGBL
Save global arguments to file

Category: Arguments

Format: `SAVGBL` fspec

Defaults: temp

Description:
`SAVGBL` saves the value of all current global arguments to a file on disk fspec which can be later be loaded using
`RSTGBL`. If no file is specified RNMR will prompt for it with temp as a default.
## SAVHTR
Save heater values to file

Category: Heater

Format: `SAVHTR` fspec

Defaults: temp

Prerequisites: RNMR heater control; RNMRA only

Description:
`SAVHTR` saves heater values to a file on disk fspec which can be later be loaded using `RSTHTR`. If no file is
specified RNMR will prompt for it with temp as a default.
## SAVLCK
Save lock values to file

Category: Lock

Format: `SAVLCK` fspec

Defaults: temp

Prerequisites: RNMR lock control; RNMRA only

Description:
`SAVLCK` saves lock values to a file on disk fspec which can be later be loaded using `RSTLCK`. If no file is
specified RNMR will prompt for it with temp as a default.
## SAVLOG
Save logging to file

Category: Misc.

Format: `SAVLOG` fspec

Defaults: temp

Prerequisites: Logging enabled

Description:
`SAVLOG` saves the contents of the logging window to a file on disk fspec. If no file is specified RNMR will prompt for
it with temp as a default. `SAVLOG` cannot be used unless logging is enabled (`SET LOG ON`).
## SAVLST
Save lists to file

Category: Lists

Format: `SAVLST` fspec

Defaults: temp

Description:
`SAVLST` saves all current lists to a file on disk fspec which can be later be loaded using `RSTLST`. If no file is
specified RNMR will prompt for it with temp as a default.
## SAVSHM
Save shim values to file

Category: Shim

Format: `SAVSHM` fspec

Defaults: temp

Prerequisites: RNMR shim control; RNMRA only

Description:
`SAVSHM` saves shim values to a file on disk fspec which can be later be loaded using `RSTSHM`. If no file is
specified RNMR will prompt for it with temp as a default.
## SAVTBL
Save name tables to file

Category: Tables

Format: `SAVTBL` fspec

Defaults: temp

Description:
`SAVTBL` saves all current name tables to a file on disk fspec which can be later be loaded using `RSTTBL`. If no file
is specified RNMR will prompt for it with temp as a default.
## SB
Save data to blocked record

Category: Blocked Record

Format: `SB` rec blk buf nblk

Defaults: wrec next 1 1

Description:
`SB` saves the data in a processing buffer to a blocked record. The record must be in an archive which RNMR has read
access to. If no record is provided RNMR will not prompt for it and will use the next available record. Records in
archives other than 1 can be specified by either pre-pending the archive number and a ":" or specifying numbers larger
than 200. For example record # in archive 2 can be specified either as 2:# or by adding 200 to #. `SB` cannot write to
scratch records which must be written using `SS` or to archive records which must be written using `SA`.

The second parameter, blk, determines which block within the record the data is saved to. If blk is omitted or set to 0
RNMR will write to the next block of the record as specified by the blocked record write pointer. The blocked record
write pointer can be set and viewed using `PTRB`. After `SB` is complete this blocked record write pointer will point to
the block after the final block that was written to.

If no buffer is specified RNMR will not prompt for it and will save the data from processing buffer 1 (the visible
processing buffer).

A processing buffer may be partitioned into multiple blocks. The final parameter, nblck, determines how many of these
processing buffer blocks should be saved. If nblk is omitted RNMR will not prompt for it and will save only 1 block.
## SC
Scale data

Category: Data Manipulation

Format: `SC` sf

Qualifiers: /ABS /REL

Qualifier Defaults: /REL

Defaults: 1.0

Description:
`SC` vertically scales data in the visible processing buffer. By default `SC` uses the /REL option which multiplies the
data by the alue of sf. /ABS sets the absolute scale factor of the data. After scaling RNMR will print the new absolute
scale factor as an informational message. If sf is omitted RNMR will not prompt for it and will a scale factor of 1.0.
## SEL
Begin macro `SEL` block

Category: Macro

Format: `SEL` nam

Qualifiers: /LCL /GBL

Qualifier Defaults: /LCL

Defaults: none

Prerequisites: Macro only

Description:
`SEL` begins a macro `SEL` block which is ended by `ENDSEL`. The block uses a global or local argument (as selected by
the /LCL or /GBL qualifiers) named nam. By default a local argument is used. If no nam is provided RNMR will prompt for
it with no default. RNMR iterates sequentially through each instance of `CASE` between `SEL` and `ENDSEL`. For each
`CASE` the value of argument nam is compared to the value of the `CASE`. The first time a match is found all of the
commands are executed that fall between that `CASE` and either the next `CASE` or `ENDSEL` whichever comes first. Then
execution proceeds from the line after `ENDSEL`
## SET
Set system state

Category: Misc.

Format: `SET` nam ...

Defaults: none

Description:
`SET` sets the state of a variety of aspects RNMR. The parameter nam specifies what state to set. If nam is not
specified RNMR will prompt for it with no default. The majority of the options available for `SET` are flags which may
be set to either ON or OFF. If not specified RNMR will prompt for the state of the flag with the current value as a
default.

The following flags may be set only from RNMRA:

Name   | Flag | Description
----   | ---- | -----------
AUTOZ  | Automatic Z shimming | Turns automatic Z shimming (controlled via `AUTOZ`) on and off
HTR    | Heater computer control | Turns remote heater control on and off
MAS    | MAS controller computer control | Turns remot spinning control on and off
RKC    | RKC computer control | Turns remote RKC control on and off
RRI    | RRI computer control | turns remote RRI control on and off
SHM    | Shim computer control | Turns remote shim control on and off
TRM    | Terminal communication | Turns terminal communication on and off
WRFBUF | WRF buffer
WWF    | WWF buffer

RNMRA also has flags which are set on a per channel basis. When setting these flags RNMR will prompt for a channel with
1 as a default if no channel is specified. Then RNMR will prompt for a flag state with the current state as a default.
The following flags may be set in this fashion from RNMRA:

Name   | Flag | Description
----   | ---- | -----------
FMXBUF | FMX buffer
PSXBUF | PSX buffer
PWXBUF | PWX buffer

The following flags may be set from both RNMRA and RNMRP:

Name  | Flag | Description
----  | ---- | -----------
DSP   | Display enable |
LOG   | Logging window | When set on a window opens and `LOG` can be used to write logging lines to it that can be saved via `SAVLOG`. Closing the logging window will set the flag off.
LP    | Text printer | When the text printer flag is on text is printed to the printer device as set and displayed by `LPDEV`. When the flag is off text printed by commands is saved to the text printer file as set and displayed by `LPFIL`. Changing `LPDEV` or `LPFIL` sets the flag to on or off respectively.
MSG   | Message window | When set on a windows opens and all informational messages and messages written using `MSG` will appear in the window rather that being written to the console. Closing the message window will set the flag off.
PL    | Plotter | When the plotter flag is on plots are printed to the plotting device as set and displayed by `PLDEV`. When the flag is off plots are saved to the plot file as set and displayed by `PLFIL`. Changing `PLDEV` or `PLFIL` sets the flag to on or off respectively.
REF   | Display reference | When set on the current contents of the visible processing buffer are set to be the display reference. Whenever any dataset in the same domain (time or frequency) as the reference is displayed the reference data will also be shown. This reference data stays set until a different display reference is set or the flag is set off.
TIMER | Timer | When set off the amount of time since it was last set on in seconds is printed as an informational message.
TRACE | Trace | When enabled all commands that are executed as well as the command level they are executed from are printed as informational messages. This is very useful for tracing the execution of macros for debugging purposes.

There are also several other options that are not simply flags that can be turned on/off. The following options are
available in both RNMRA and RNMRP:

BUF item val

`SET BUF` sets various parameters of the visible processing buffer. The following items may be set with `SET BUF`:

Item  | Description
----  | -----------
DIM   | Buffer dimension
DOM   | Buffer domain (TIME, FREQ, UNKN)
FIRST | Position of first point
NACQ  | Number of acquisitions
SF    | Scale factor
SIZE  | Size in points
STEP  | Difference between position of sequential points
TITLE | Buffer title

INFO typ [nam] nam1...

`SET INFO` sets up handling of informational messages from the next command that is executed. The typ parameter
determines what type of location to send the message. The LST and TBL options use a nam parameter which determines
which list or name table to send values to. There can be multiple parameters nam1, nam2, etc. to setup multiple
informational messages from the same command. The following typ parameters are supported:

Item | Description
---- | -----------
GBL  | Save to global variables named nam1, nam2, etc.
LCL  | Save to local variables named nam1, nam2, etc.
LST  | Save to position nam1, nam2, etc. in list nam
OFF  | Do not print messages
ON   | Print messages
SYM  | Save to symbols named nam1, nam2, etc.
TBL  | Save to entry nam1, nam2, etc. in name table nam

REC rec dir item val

`SET REC` sets the value of various parameters in the title information of a record. It takes several arguments. The
first is a record to set a parameter for. Records in archives other than 1 can be specified by either pre-pending the
archive number and a ":" or specifying numbers larger than 200. For example record # in archive 2 can be specified
either as 2:# or by adding 200 to #. The second parameter is a direction which may be an integer from 1 and the number
of dimensions the record has. The third argument is which item to set the value of. Some items have only a single value
for the entire record which will be set regardless of which dimension is specified. The following items may be set with
`SET REC`:

Item   | Description
----   | -----------
ACQTYP | Acquisition type
DIM    | Dimension corresponding to the direction
DOM    | Domain of the direction (TIME, FREQ, UNKN)
FIRST  | Position of first point
NACQ   | Number of acquisitions (single parameter for all directions)
NSEG   | Number of segments (single parameter for all directions)
SF     | Scale factor to use when loading data (single parameter for all directions)
SIZE   | Size in points
STEP   | Difference between position of sequential points
SYN    | Synthesizer associated with direction
TITLE  | Title of record (single parameter for all directions)

## SETIDN
Set identification values

Category: Display

Format: `SETIDN` idn1 idn2

Defaults: none none

Prerequisites: Macro only

Description:
`SETIDN` sets the text in the identification fields in the top left of the RNMR display. `SETIDN` may only be called
from within a macro and the text set with it will be unset when the macro exits. The two arguments idn1 and idn2 are the
text for the two available identification fields. If these arguments are omitted RNMR will not prompt for them and will
not change the corresponding fields.
## SETV
Set data values between limits

Category: Data Manipulation

Format: `SETV` val llim rlim

Qualifiers: /COMPLEX /IMAG /REAL

Qualifier Defaults: current_display

Defaults: 0.0 current_display_limits

Description:
`SETV` sets the data values for all points in a specified region (between llim and rlim) of the visible processing
buffer to a given value. If val is omitted RNMR will prompt for it with 0.0 as a default. If either limit is omitted
RNMR will not prompt for them and will use the current display limits. The limits are specified in the current units of
the visible processing buffer. The /REAL, /IMAG, and /COMPLEX qualifiers select whether to set the real part, imaginary
part, or both parts of the buffer to the specified value. The default behavior is to set the currently visible part of
buffer as selected and shown by the `BUF` command.
## SETVP
Set data values for specified points

Category: Data Manipulation

Format: `SETVP` val llim npt

Qualifiers: /COMPLEX /IMAG /REAL

Qualifier Defaults: current_display

Defaults: 0.0 current_display_limit 1

Description:
`SETVP` sets the data values for all points in a specified region (npt points starting from llim) of the visible
processing buffer to a given value. If val is omitted RNMR will prompt for it with 0.0 as a default. If llim is omitted
RNMR will not prompt for them and will use the current display limit. The limit is specified in the current units of the
visible processing buffer. If the number of points to set, npt, is omitted RNMR will not prompt for it and will set a
single point. The /REAL, /IMAG, and /COMPLEX qualifiers select whether to set the real part, imaginary part, or both
parts of the buffer to the specified value. The default behavior is to set the currently visible part of buffer as
selected and shown by the `BUF` command.
## SG
Start acquisition without accumulation

Category: Acquisition

Format: `SG`

Prerequisites: Experiment loaded (LOAD); Acquisition  stopped (HALT); RNMRA only

Description:
`SG` starts acquisition but does not accumulate data from multiple shots.
## SHELL
Spawn shell

Category: Misc.

Format: `SHELL`

Description:
`SHELL` spawns a new terminal from which shell commands can be executed.
## SHFT
Shift data

Category: Data Manipulation

Format: `SHFT` shft

Defaults: step

Description:
`SHFT` shifts the data in the visible processing buffer by an amount shft specified in the current buffer units. If shft
is not specified RNMR will prompt for it with the current step, the value corresponding to a single point, as a default.
Shift values greater than zero will shift to the left while values less than zero will shift to the right. The portion
of the buffer left empty after the shift will be filled with zeros.
## SHFTP
Shift data by points

Category: Data Manipulation

Format: `SHFTP` shft

Defaults: 1

Description:
`SHFTP` shifts the data in the visible processing buffer by an amount shft specified in points. If shft is not specified
RNMR will prompt for it with 1 as a default. Shift values greater than zero will shift to the left while values less
than zero will shift to the right. The portion of the buffer left empty after the shift will be filled with zeros.
## SHM
Set shim value

Category: Shim

Format: `SHM` name value

Defaults: none current

Prerequisites: RNMR shim control; RNMRA only

Description:
`SHM` sets the value of a particular shim specified by name. If name is omitted RNMR will prompt for it with no default.
If value is omitted RNMR will prompt for it with the current value of the specified shim as a default. The shim value
may be between -100.0 and 100.0 inclusive.
## SHMCTL
Open interactive shim controls

Category: Shim

Format: `SHMCTL`

Prerequisites: RNMR shim control; RNMRA only

Description:
`SHMCTL` opens a pop up window for viewing and adjusting shim values. The same window is available via the shim option
in the controls drop down menu.
## SHOW
Show information

Category: Misc.

Format: `SHOW` option

Default: none

Description:
`SHOW` shows information on various RNMR entities. The following options are available in RNMRA and RNMRP:

BUF item

`SHOW BUF` displays various attributes of the visible processing buffer. The following items may be displayed with
`SHOW BUF`:

Item  | Description
----  | -----------
DIM   | Buffer dimension
DOM   | Buffer domain (TIME, FREQ, UNKN)
FIRST | Position of first point
LAST  | Position of last point
NACQ  | Number of acquisitions
SF    | Scale factor
SIZE  | Size in points
SIZEA | Allocated size in points
STEP  | Difference between position of sequential points

REC rec dir item

`SHOW REC` displays the value of various parameters in the title information of a record. It takes several arguments.
The first is a record to show a parameter for. Records in archives other than 1 can be specified by either pre-pending
the archive number and a ":" or specifying numbers larger than 200. For example record # in archive 2 can be specified
either as 2:# or by adding 200 to #. The second parameter is a direction which may be an integer from 1 and the number
of dimensions the record has. The third argument is which item to show the value of. Some items have only a single value
for the entire record which will be displayed regardless of which dimension is specified. The following items may be
displayed with `SHOW REC`:

Item   | Description
----   | -----------
ACQTYP | Acquisition type
DIM    | Dimension corresponding to the direction
DOM    | Domain of the direction (TIME, FREQ, UNKN)
FIRST  | Position of first point
NACQ   | Number of acquisitions (single parameter for all directions)
NDIM   | Number of dimensions (single parameter for all directions)
NDIMX  | Number of simultaneously accessible dimensions (single parameter for all directions)
NSEG   | Number of segments (single parameter for all directions)
NSEGA  | Number of allocated segments (single parameter for all directions)
NUC    | Nucleus
OFF    | Offset frequency
PPM    | PPM to Hz conversion factor
REF    | Reference frequency
SF     | Scale factor to use when loading data (single parameter for all directions)
SIZE   | Size in points
SIZEA  | Allocated size in points
SIZEB  | Size in blocks
STEP   | Difference between position of sequential points
SYN    | Synthesizer associated with direction
TITLE  | Title of record (single parameter for all directions)

In RNMRA the BUFA option is also available. BUFA behaves exactly the same as BUF but displays information about the
acquisition buffer instead of the visible processing buffer.
## SINEB
Perform Sine-bell apodization

Category: Data Manipulation

Format: `SINEB` factor time

Defaults: 0.0 (size+1)\*step

Prerequisites: Time domain data in processing buffer (TIME)

Description:
`SINEB` performs a sinebell apodization. The first parameter, factor, must be between 0.0 and 1.0 inclusive and
determines the initial phase of the sinebell. The initial phase is the arcsine of the factor. Thus a value of 0.0
indicates a sine function and a value of 1.0 indicates a cosine function. If factor is omitted RNMR will prompt for it
with 0.0 as a default. The second argument, time, indicates the time at which the sinebell reaches 0 thereby stretching
or squeezing the sinebell. All points from time on are set to 0. If time is omitted RNMR will prompt for it with
(size+1)\*step as a default. This default will end the sinebell at the last data point. RNMR multiplies the time domain
data in the visible processing buffer by the specified sinebell.
## SIZE
Set acquisition size

Category: Acquisition

Format: `SIZE` size

Defaults: current

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`SIZE` sets the number of point in signal to be acquired. If size is omitted RNMR will prompt for it with the current
size as a default. The value of size must be between 1 and 32768 inclusive.
## SIZEB
Displays size of blocked record

Category: Blocked Record

Format: `SIZEB` rec dir

Defaults: rrec 1

Description:
`SIZEB` displays information about the size of a blocked record. If no record is specified RNMR will prompt for it with
the current read record pointer as the default. Records in archives other than 1 can be specified by either pre-pending
the archive number and a ":" or specifying numbers larger than 200. For example record # in archive 2 can be specified
either as 2:# or by adding 200 to #. If no direction is specified RNMR will prompt for it with 1 as a default. If the
direction is between 1 and the number of dimensions in the blocked record RNMR will print the size and allocated size of
the blocked record in that direction as informational messages. If dir is 0 RNMR will print the number of segments in
the record and the number ofallocated segments. If dir is * RNMR will print the total number of blocks and total number
of allocated blocks in the record. No other values of dir are permitted.
## SIZLST
Display size of list

Category: Lists

Format: `SIZLST` list

Defaults: temp

Description:
`SIZLST` prints the size of a list and its allocated size as informational messages. If no list is specified RNMR will
prompt for it with a default of temp.
## SIZTBL
Display size of name table

Category: Tables

Format: `SIZTBL` tbl

Defaults: temp

Description:
`SIZTBL` prints the size of a name table and its allocated size as informational messages. If no table is specified RNMR
will prompt for it with a default of temp.
## SP
Display archive space information

Category: Data Storage

Format: `SP` arv

Qualifiers: /DATA /FILE /FREE /MAX /TITLE /USED

Qualifier defaults: /DATA /USED

Defaults: 1

Description:
`SP` prints information about the space in an archive as informational messages. If no archive is specified RNMR will
not prompt for it and will display information about archive 1. The qualifiers are used to determine what information to
display. /DATA and /TITLE select the type of information to return. /DATA returns information about the size of various
aspects of the archive in 512 byte blocks. /TITLE returns information about the number of records in the archive.

The other qualifiers determine the quantity to print as follows:

Name | /DATA | /TITLE
---- | ----- | ------
FILE | Allocated size of file | Number of allocated records
FREE | Allowed usable space (MAX-USED) | Allowed usable records (MAX-USED)
MAX  | Maximum allowable size | Maximum allowable number of records
USED | Size of filled space | Number of records in use

By default `SP` uses /DATA /USED and prints the size of the filled space in blocks as an informational message.
## SPLN
Spline baseline fix spectrum

Category: Data Manipulation

Format: `SPLN` list

Defaults: temp

Prerequisites: Frequency domain data in processing buffer (FREQ)

Description:
`SPLN` takes a list of points and subtracts a cubic spline fit to those points from the data in the visible processing
buffer. The list should contain numerical points from left to right specified in the current units of the buffer. If no
list is specified RNMR will prompt for it with temp as a default. `SPLN` can provide more accurate baseline subtraction
than `BF` if the baseline of a spectrum is not linear. The baseline subtraction will be affected by the selection of the
list of points used to fit the spline, so it is important to choose points that are not on peaks and cover all of the
features of the baseline.
## SQZ
Squeeze archive (de-allocate unused space)

Category: Data Storage

Format: `SQZ` arv

Defaults 1

Description:
`SQZ` squeezes and archive to reduce the size of the file stored on disk. After `SQZ` the number of records and data
blocks allocated in the file will match the number of used records and data blocks (`SP /USED` will equal `SP /FILE`).
If no archive is specified RNMR will prompt for it with 1 as a default.
## SREF
Save processing buffer reference to nucleus table

Category: Frequency Control

Format: `SREF` nuc

Defaults: *

Description:
`SREF` stores the reference frequency (or frequencies) in the visible processing buffer in the nucleus table. If nuc is
* `SREF` saves the frequency for every channel. Otherwise a valid nucleus must be passed. If nuc is omitted RNMR will
prompt for it with a default of \*.
## SREFA
Save acquisition buffer reference to nucleus table

Category: Frequency Control

Format: `SREFA` nuc

Defaults: *

Prerequisites: RNMRA only

Description:
`SREFA` stores the reference frequency (or frequencies) in the acquisition buffer in the nucleus table. If nuc is *
`SREFA` saves the frequency for every channel. Otherwise a valid nucleus must be passed. If nuc is omitted RNMR will
prompt for it with a default of \*.
## SS
Save data to scratch record

Category: Data Storage

Format: `SS` rec buf

Defaults: 1 1

Description:
`SS` saves the date in a processing buffer to a scratch record (records 1-4 in an archive). The record must be in an
archive which RNMR has read access to. If no record is provided RNMR will not prompt for it and will use record 1.
Records in archives other than 1 can be specified by either pre-pending the archive number and a ":" or specifying
numbers larger than 200. For example record # in archive 2 can be specified either as 2:# or by adding 200 to #. `SS`
cannot write to archive records which must be written using `SA` or to blocked records which must be written using `SB`.

If no buffer is specified RNMR will not prompt for it and will save the data from processing buffer 1 (the visible
processing buffer).
## STK
Add to plot stream stack

Category: Printing

Format: `STK`

Prerequisites: Plot stream open

Description:
`STK` allows plotting multiple 1D spectra offset from one another on a single plot. `STK` must fall between `OPNPLT` and
`CLSPLOT`. Each invocation of `STK` plots the current contents of the visible processing buffer offset from the previous
plot in X and Y by the values set by `STKOFF`. There are limits to the area of a plot which `STK` cannot exceed. Reduce
the size of the plots using `PLSIZE` and offsets using `STKOFF` to ensure that all of the stack plots fit within a 9x6
area.
## STKOFF
Set stack plot offset

Category: Printing

Format: `STKOFF` xoff yoff

Defaults: current current

Prerequisites: Plot stream closed

Description:
`STKOFF` sets the offset values in inches to be used when creating stack plots with `STK`. If either offset is omitted
RNMR will prompt for it with the current value as a default. `STK` cannot be used between `OPNPLT` and `CLSPLT`.
## STR
Perform string operation

Category: Misc.

Format: `STR` string beg end

Qualifiers: /DLT /EXT /INSBEG=<str> /INSEND=<str> /LC /LEN /LOC=<str> /REPL=<str> /UC

Qualifier Defaults: /EXT

Defaults: none <beg> <end>

Description:
`STR` performs a variety of operations on an input string and prints the result as an informational message. If any of
the arguments are omitted RNMR will not prompt for them. By default RNMR will use an empty string and the beginning and
ending of the string. The qualifiers control what operation is performed on the string as follows:

Qualifier | Description
--------- | -----------
/DLT      | Delete characters from beg to end
/EXT      | Extract characters from beg to end
/INSBEG   | Insert str before beg
/INSEND   | Insert str after end
/LC       | Convert characters from beg to end to lower case
/LEN      | Print length of substring from beg to end
/LOC      | Print index where str matches between beg and end (0 if no match)
/REPL     | Replace region between beg and end with str
/UC       | Convert characters from beg to end to upper case

## SUBV
Subtract data buffers

Category: Data Manipulation

Format: `SUBV` src dst

Defaults: 2 1

Description:
`SUBV` replaces the contents of buffer dst with the difference between the contents of buffers src and dst.

    DST = SRC - DST

If either argument is omitted, RNMR will prompt for a buffer number. The default source is buffer 2 while the default
destination is buffer 1. The src and dst buffers must have the same domain and active size (though not necessarily the
same allocated size).
## SW
Set sweep width

Category: Acquisition

Format: `SW` freq

Defaults: current

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`SW` sets the sweep width for acquisition to freq. This also changes the dwell time as set and displayed by `DW`. If
freq is omitted RNMR will prompt for it with the current sweep width as a default. The sweep width is in the current
frequency units. Due to limitations of the hardware RNMR may adjust the desired sweep width to the closest possible
sweep width. If such an adjustment occurs RNMR will print an informational message containing the adjusted sweep width.
## SWAPV
Swap data buffers

ategory: Data Manipulation

Format: `SUBV` src dst

Defaults: 2 1

Description:
`SWAPV` exchanges the contents of two processing buffers.

    SRC = DST
    DST = SRC

If either argument is omitted, RNMR will prompt for a buffer number. The default source is buffer 2 while the default
destination is buffer 1. The src and dst buffers must have the same domain and active size (though not necessarily the
same allocated size).
## SWL
Set lock channel sweep width

Category: Lock

Format: `SWL` width

Defaults: current

Prerequisites: RNMR lock control; RNMRA only

Description:
`SWL` sets lock sweep width. If width is omitted RNMR will prompt for it with the current value as a default. The sweep
width must be between 0.0 and 100.0 inclusive.
## SWP
Enable or disable lock sweep

Category: Lock

Format: `SWP` state

Defaults: current

Prerequisites: RNMR lock control; RNMRA only

Description:
`SWP` sets the state of the lock channel sweep. The state may be either ON or OFF. If no state is specified RNMR will
prompt for it witht hte current value as a default.

# T
---
## TALARM
Set temperature for probe heater alarm

Category: Heater

Format: `TALARM` temp

Defaults: current

Prerequisites: RNMR heater control; RNMRA only

Description:
`TALARM` sets the temperature limit for the heater alarm. If no temperature is provided RNMR will prompt for it with the
current alaram temperature as a default.
## TCL
Set lock channel time constant

Category: Lock

Format: `TCL` tc

Default: current

Prerequisites: RNMR lock control; RNMRA only

Description:
`TCL` sets the lock channel time constant. If the time constant is omitted RNMR will prompt for it with the current
value as a default.
## TH
Set threshold for peak selection

Category: Display Control

Format: `TH` val

Defaults: current

Description:
`TH` sets the threshold value used for peak picking. If no value is specified RNMR will prompt for it with the current
value as a default. The threshold is used whenever RNMR identifies peaks (`LPK`, `LPK2D`, P subcommand of `ZO`, next
peak button in zoom window). The magnitude of a point must be larger that the threshold in order to be considered a
peak.
## TILT
Tilt blocked record

Category: Data Manipulation

Format: `TILT` rec slice tfctr

Defaults: wrec 1 1.0

Description:
`TILT` tilts a two-dimensional slice of a blocked record by an angle between 0.0 and 45.0 degrees. If no record is
specified RNMR will prompt for it with the current write record pointer (as set and displayed by `PTRA`) as a default.
The first two dimensions of the blocked record must be frequency domain. The second parameter, slice, specifies which 2D
slice of a 3D or 4D source record should be tilted. If the source record has only two dimensions, slice must be 1. If
slice is omitted RNMR will not prompt for it and will tilt the first slice. Slice is interpreted as a linear index over
the 3rd/4th dimensions.

The final parameter, tfctr, determines what angle to tilt the record by. The angle is tfctr times 45.0 degrees. If tfctr
is omitted RNMR will not prompt for it and will use a value of 1.0 (45 degree tilt). The value of tfctr may be between
0.0 and 1.0 inclusive.
## TITLE
Set processing buffer title

Category: Data Storage

Format: `TITLE` title

Defaults: current

Description:
`TITLE` sets the title of the visible processing buffer. If no title is provided RNMR will prompt for it with the
current processing buffer title as a default.
## TITLEA
Set acquisition title

Category: Acquisition

Format: `TITLEA` title

Defaults: current

Prerequisites: RNMRA only

Description:
`TITLE` sets the title of the acquisition buffer. If no title is provided RNMR will prompt for it with the
current acquisition buffer title as a default.
## TM
Perform trapezoidal multiplication apodization

Category: Data Manipulation

Format: `TM` lfract rfract

Defaults: 0.0 0.0

Description:
`TM` performs a trapazoidal multiplication apodization. A fraction of the data on the left is multiplied by a linear
function that increases from 0.0 to 1.0 and a fraction of the data on the right is multiplied by a linear function that
decreases from 1.0 to 0.0. The parameters lfract an rfract determine what fraction of the data each linear function is
applied to. If either of these arguments is omitted RNMR will prompt for it with 0.0 as a default.
## TP
Show phase correction values

Category: Display Control

Format: `TP`

Description:
`TP` prints the current zero order and first order phase correction values as informational messages.
## TPPI
Convert TPPI-format FID to complex FID

Category: Foreign

Format: `TPPI`

Prerequisites: Time domain data in visible processing buffer (TIME)

Description:
`TPPI` converts a TPPI-format FID to a complex FID. This process uses only the real data in the visible processing
buffer. It treats every other point starting with point 1 as the real data and every other point starting with point 2
as the imaginary data. As a result the size of the visible processing buffer will be reduced by a factor of two.
Additionally, after combining the data into complex numbers every other point starting with point 2 is negated.
## TSET
Set heater set-point temperature

Category: Heater

Format: `TSET` temp

Defaults: current

Prerequisites: RNMR heater control; RNMRA only

Description:
`TSET` sets the target temperature for the heater. If no temperature is specified RNMR will prompt for it with the
current target temperature as a default.
## TST
Conditionally execute a block of commands based on a test

Category: Macro

Format: `TST` test args...

Qualifiers: /TRUE /FALSE

Qualifier defaults: /TRUE

Defaults: none

Prerequisites: Macro only (MAC)

Description:
`TST` begins a `TST` block which is then ended by `ENDTST` and may optionally contain an `ELSTST` command. `TST` checks
a condition and then either runs the commands between `TST` and `ELSTST` or the commands between `ELSTST` and `ENDTST`.

For example, the following:

    tst lcl a
      msg "The value of a is &a"
    elstst
      msg "local argument a does not exist"
    endtst

will test if local argument a exists and then either print its value or the fact that it does not exist.

/TRUE and /FALSE determine which block executed for which test result. With /TRUE `TST` will run the commands between
`TST` and `ELSTST` if the test returns true and the commands between `ELSTST` and `ENDTST` if it returns false. /FALSE
reverses this behavior. /FALSE is mostly useful when you only have one set of commands that you want to execute when the
test is false.

The argument test determines which type of test to perform. Depending on the test there are additional arguments and
additional qualifiers. The additional qualifiers should be passed after the test name but before the test arguments. If
no test name is specified RNMR will not prompt for it and will treat the test as having been true.

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

The qualifiers for `TST ARV` have the following meanings:

Flag | Description
---- | -----------
/VALID | Check for validity of the archive number
/RD | Check for write access
/WRT | Check for read access
/CLS | Check if the archive is closed

The qualifiers for `TST REC` have the following meanings:

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

The qualifiers for `TST ASKYN` have the following meanings:

Flag | Description
---- | -----------
/NO  | Default value of the prompt is NO
/YES  | Default value of the prompt is YES

The qualifiers for `TST EQ` have the following meanings:

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

The qualifiers for `TST LCL` have the following meanings:

Flag | Description
---- | -----------
/LEV | Select the command level to check for the local argument. 1 indicates the current macro, 2 the macro that called the current macro, 3 the macro that called that macro, etc. The value must be an integer ranging from 1 to the depth of the call stack.

The qualifiers for `TST LIM` have the following meanings:

Flag | Description
---- | -----------
/FLT | Use floating point numbers
/INT | Use integers

`TST` is a replacement for the old if commands such as `IFEQ`. If you need the old behavior of jumping to labels instead
of executing code blocks use `GOTST`.
## TVAL
Show heater temperature

Category: Heater

Format: `TVAL`

Prerequisites: RNMR heater control; RNMRA only

Description:
`TVAL` prints the current heater temperature as an informational message.
## TWIST
Twist blocked record

Category: Data Manipulation

Format: `TWIST` rec slice tfctr

Defaults: wrec 1 1.0

Description:
`TWIST` twists a two-dimensional slice of a blocked record. If no record is specified RNMR will prompt for it with the
current write record pointer (as set and displayed by `PTRA`) as a default. The first dimension of the blocked record
must be frequency domain and the second dimension must be time domain. The second parameter, slice, specifies which 2D
slice of a 3D or 4D source record should be twisted. If the source record has only two dimensions, slice must be 1. If
slice is omitted RNMR will not prompt for it and will twist the first slice. Slice is interpreted as a linear index over
the 3rd/4th dimensions.

The final parameter, tfctr, determines how much to twist the record. If tfctr is omitted RNMR will not prompt for it and
will use a value of 1.0. The value of tfctr may be between 0.0 and 1.0 inclusive.

# U
---
## UNECHO
Rearrange buffer to simulate FID from echo

Category: Data Manipulation

Format `UNECHO` time

Defaults: center

Prerequisites: Time domain

Description:
`UNECHO` takes echo signal in the visible processing buffer and simulates an FID from it. The parameter time should be
set to the middle of the echo. `UNECHO` will use a mixture of the data from the left anf right halves of the echo to
generate the FID. The part of the buffer beyond the size of the larger half of the echo will be set to 0. If time is not
provided RNMR will prompt for it with a time value corresponding to the center of the buffer.
## UNFOLD
Unfold data buffer

Category: Data Manipulation

Format: `UNFOLD` nsect

Defaults: 1

Description:
`UNFOLD` grows the visible processing buffer to hold nsect sections each with the prior size of the buffer. The data in
the buffer is then copied into each section. If nsect is not specified RNMR will prompt for it with a default of 1. If
nsect is equal to 1 then `UNFOLD` has no effect.
## UNIT
Set units

Category: Display Control

Format: `UNIT` unit

Qualifiers: /DFLT /FREQ /TIME /UNKN

Qualifier defaults: /TIME

Defaults: current

Description:
`UNIT` sets the unit for a given domain. /FREQ, /TIME, and /UNKN select which domain to set the unit for. /DFLT is used
to set the default unit for the selected domain. If no unit is specified RNMR will prompt for it with the current unit.

Valid time domain units are USEC, MSEC, and SEC. Valid frequency domain units are HZ, kHz, MHz, and PPM.
## UPDARV
Update archive

Category: Data Storage

Format: `UPDARV` archive

Defaults: 1

Description:
`UPDARV` updates an archive from its file on disk. This makes any changes that have been made to the file visible from
RNMR. If no archive is specified RNMR will prompt for it with a default of 1. This can be useful when using an archive
in read only mode in RNMRP while it is open with write access in RNMRA. Using `SAVARV` in RNMRA and then `UPDARV` in
RNMRP ensures that all changes made from RNMRA are visible in RNMRP.
## USER
Set user name

Category: Data Storage

Format: `USER` user

Defaults: current

Description:
`USER` sets the user name that is used for record protection. Usually this is set by the login macro on startup. If no
user is specified RNMR will prompt for it with the current user as a default. If there is no current user (as is the
case when first starting RNMR) the default will be \*\*\*\*\*\*\*. RNMR will continue to prompt until the user is not
\*\*\*\*\*\*\*\*.

# V
---
## VAL
Set data value

Category: Data Manipulation

Format: `VAL` pos valr vali

Qualifiers: /REAL /IMAG

Qualifier Defaults: /REAL /IMAG

Defaults: current_cursor current current

Description:
`VAL` sets the data value of a specific point in the visible processing buffer to a specified complex number
(valr+i*vali). The point to be modified is selected by its position in the current buffer units. If no position is
specified RNMR will prompt for it with the current cursor position as a default. /REAL and /IMAG select whether to
set the value of the real or imaginary part of the data point respectively. If neither is set `VAL` will set both. If
a value to set is omitted RNMR will prompt for it with the current value as a default.
## VIEW
Set display source

Category: Display Control

Format: `VIEW` view

Defaults: current

Description:
`VIEW` selects the buffer to view on the display. The valid options in RNMRA are pro or acq for the visible processing
buffer or acquisition buffer respectively. In RNMRP only pro is allowed. If no view is provided RNMR will prompt for it
with the current value.

# W
---
## WAIT
Halt when number of shots satisfies `NWAIT`

Category: Acquisition

Format: `WAIT`

Qualifiers: /ERR=<label>

Qualifier Defaults: none

Prerequisites: Acquisition running; RNMRA only

Description:
`WAIT` halts acquisition after nwait shots. /ERR may be used to specify a label to jump to in the event of an error.

Pressing Q while `WAIT` is active calls `QUIT` to halt acquisition after the phase cycle is completed. Remember that
another Q while `QUIT` is finishing the phase cycle halts immediately.

Pressing ^ while `WAIT` is active pauses the acquisition and returns control to the user at the command line. Entering
exit from this command line resumes acquisition.
## WAVB
Perform weighted average of blocked record

Category: Data Manipulation

Format: rec first last

Defaults: rrec 1 last

Description:
`WAVB` performs a weighted average of blocks from a blocked record and puts the result in the visible processing buffer.
The average is weighted such that any blocks with all zeros have a weight of 0 and all other blocks have a weight of 1.
If no record is specified RNMR will prompt for it with the read record pointer (as set and displayed by `PTRA`) as a
default. `WAVB` performs the average over blocks first to last. If first is omitted RNMR will prompt for it with 1 as a
default. If last is omitted RNMR will prompt for it with the number of blocks in the record as a default. Setting last
to 0 indicates to use the last block in the record.
## WAVV
Perform weighted addition of buffers

Category: Data Manipulation

Format: `WAVV` src dst

Defaults: 2 1

Description:
`WAVV` replaces the contents of buffer dst with the weighted average of buffers src and dst. The buffers are weighted
based upon the number of acquisitions in each buffer. The data from the src buffer is also scaled to the scale factor of
the dst buffer for averaging purposes.

    DST = DST*NA_DST/(NA_DST+NA_SRC) + SRC*NA_SRC/(NA_DST+NA_SRC) * (SF_DST/SF_SRC)

This permits the proper addition of two FID's or spectra with different scale factors and/or number of
acquisitions; each data set is weighted appropriately.

If either argument is omitted, RNMR will prompt for a buffer number. The default source is buffer 2 while the default
destination is buffer 1. The src and dst buffers must have the same domain and active size (though not necessarily the
same allocated size).
## WGPIB
Write line to GPIB device

Category: Hardware

Format: `WGPIB` dev cmd

Defaults: none

Prerequisites: RNMRA only

Description:
`WGPIB` writes a command line to a GPIB device. If no device is specified RNMR will prompt for it with no default. If no
command line is provided RNMR will prompt for one with no default.
## WNDLIM
Set processing view vertical window limits

Category: Display Control

Format: `WNDLIM` min max

Qualifiers: /FREQ /TIME /UNKN

Qualifier Defaults: /TIME

Defaults: current current

Description:
`WNDLIM` sets the vertical window limits when viewing the processing buffer. The min and max parameters set the lower
and upper bounds of the display. The value of max must be greater than the value of min. If either min or max is omitted
RNMR will prompt for it with the current window limit.

The window limits are set separately for data in different domains. /FREQ, /TIME, and /UNKN select which domain to set
the limits for.
## WNDLIMA
Set acquisition view vertical window limits

Category: Display Control

Format: `WNDLIMA` min max

Defaults: current current

Description:
`WNDLIMA` sets the vertical window limits when viewing the acquisition buffer. The min and max parameters set the lower
and upper bounds of the display. The value of max must be greater than the value of min. If either min or max is omitted
RNMR will prompt for it with the current window limit.
## WPK
Write peaks in current display to `WRT` file

Category: File IO

Format: `WPK`

Description:
`WPK` writes a list of peaks in the current display to a file opened with `WRT`. The peaks will be written in order from
left to right in the display. For each peak a line will be written with four values (peak number, position in current
frequency units, position in default frequency units, intensity). A maximum of 50 peaks will be written to the file. A
point is considered a peak if its magnitude is greater than the peak picking threshold (as set and displayed by `TH`)
and it is either a local maximum or minimum if its intensity is greater or less than zero respectively.
## WPK2D
Write 2D peaks to `WRT` file

Category: File IO

Format: `WPK2D` rec slice

Defaults: rrec 1

Description:
`WPK2D` writes a list within a 2D slice of a blocked record and within in the current display limits to a file opened
with `WRT`. For each peak a line will be written to the file containing the peak number, the position in each dimension
in the current and default frequency units and the peak intensity. A maximum of 250 peaks will be written to the file.

If no record is specified RNMR will prompt for it with the current read record pointer (as set and displayed by `PTRA`)
as a default. The second parameter, slice, specifies which 2D slice of a 3D or 4D source record to write peaks from. If
the source record has only two dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it and will
write peaks from the first slice. Note that the current mapping of dimensions to directions (as displayed and set by
`DIRB`) will affect the selection of which one-dimensional blocks of the record comprise the 2D slice and will thus be
searched for peaks. Slice is interpreted as a linear index over the 3rd/4th dimensions.

A point is considered a peak if its magnitude is greater than the peak picking threshold (as set and displayed by `TH`)
and it is either a local maximum or minimum if its intensity is greater or less than zero respectively. By setting
`CONMD` to POS, NEG, or ABS beforehand, the user may modify the selection of 2D peaks for a given threshold value.
## WPPSB
Write data byte to pulse programmer spectrometer bus

Category: Hardware

Format: `WPPSB` adr data

Defaults: 0 0

Prerequisites: Pulse programmer spectrometer bus control implemented (CGFSB2); RNMRA only

Description:
`WPPSB` writes a data byte from the pulse programmer spectrometer bus. The adr parameter specifies the address to write
the byte to and may range from 0 to 255 inclusive. The data parameter specifies what value to write to the bus and may
range from 0 to 255 inclusive. If adr or data is omitted RNMR will prompt for it with a default of 0.
## WRF
Set waveform reference values

Category: Waveform

Format: `WRF` chan ind val1 val2

Defaults: 1 1 current current

Prerequisites: Waveform generator implemented; Acquisition stopped (HALT); RNMRA only

Description:
`WRF` sets a wave form generator reference values. The chan and ind parameters are used to set which value on which
channel to adjust. If either chan or ind are omitted RNMR will prompt for them with a default of 1. The parameters val1
and val2 are the reference values. If either val1 or val2 are omitted RNMR will prompt for them with the current value
as a default.
## WRFEX
Load waveform RF program

Category: Waveform

Format: `WRFEX`

Defaults:

Prerequisites: Waveform generator implemented and HALT
## WRKC
Write data byte to RKC device

Category: Hardware

Format: `WRKC` dev data

Defaults: none

Prerequisites: RKC device implemented; RNMRA only

Description:
`WRKC` writes data from a RKC device. If no device  or data is specified RNMR will prompt for it with no default.
## WRRI
Write command line to RRI device and read response

Category: Hardware

Format: `WRRI` cmd

Defaults: none

Prerequisites: RRI device implemented; RNMRA only

Description:
`WRRI` writes data from a RRI device. If no command is specified RNMR will prompt for it with no default. The response
will be printed as an informational message.
## WRT
Write line to file opened by `OPNWRT`

Category: File IO

Format: `WRT` arg...

Defaults: none

Description:
`WRT` writes a line to a file opened by `OPNWRT`. When multiple arguments are passed to `WRT` they are all written to
the same line. Arguments are padded with spaces in multiples of 8. This means that for example if the first argument has
7 or less characters the second argument will start at the 9th character in the line. If it had 8-15 characters the
second argument would start at the 17th character and so on. The total length of the line cannot exceed 80 characters,
so `WRT` can accept a maximum of 10 arguments when each argument is less than 8 characters long. If no arguments are
provided RNMR will prompt for a single value to write.
## WRTLST
Write list to file

Category: Lists

Format: `WRTLST` nam fspec

Defaults: temp <nam>

Description:
`WRTLST` writes the contents of a list to a file. The values can be reloaded into a list using `RDLST`. If no list name
is specified RNMR will prompt for it with a default of temp. If no file is specified RNMR will prompt for it with the
list name as a default. If the file name has no extension RNMR will add .wrt to it.
## WRTTBL
Write name table to file

Category: Tables

Format: `WRTTBL` nam fspec

Defaults: temp <nam>

Description:
`WRTTBL` writes the contents of a name table to a file. The values can be reloaded into a name table using `RDTBL`. If
no table name is specified RNMR will prompt for it with a default of temp. If no file is specified RNMR will prompt for
it with the table name as a default. If the file name has no extension RNMR will add .wrt to it.
## WSB
Write data byte to spectrometer bus

Category: Hardware

Format: `WSB` adr data

Defaults: 0 0

Prerequisites: Spectrometer bus control implemented (CGFSB1); RNMRA only

Description:
`WSB` writes a data byte to the spectrometer bus. The adr parameter specifies the address to write the byte to and may
range from 0 to 255 inclusive. The data parameter specifies what value to write to the bus and may range from 0 to 255
inclusive. If adr or data is omitted RNMR will prompt for it with a default of 0.
## WTRM
Write command line to terminal and read response

Category: Hardware

Format: `WTRM` ind cmd

Defaults: 1 none

Prerequisites: RNMRA only

Description:
`WTRM` writes a command to a terminal and reads a response. The terminal is specified by its index. If no index is
specified RNMR will prompt for it with a default of 1. If no command is provided RNMR will prompt for it with no
default. THe response read form the terminal will be printed as an informational message.
## WTSET
Wait for heater to stabilize at setpoint

Category: Heater

Format: `WTSET`

Prerequisites: RNMR heater control; RNMRA only

Description:
`WTSET` waits for the heater temperature to reach its set point. Press Q while `WTSET` is active to quit waiting.
## WTTIM
Wait for specified number of seconds

Category: Misc.

Format: `WTTIM` dlytime

Defaults: 1.0

Description:
`WTTIM` waits an amount of time specified by dlytime. The time is specified in seconds and must be a positive number. If
no time is specified RNMR will prompt for it with a default of 1.0. ress Q while `WTTIM` is active to quit waiting.
## WWASH
Set state of plot whitewash flag

Category: Printing

Format: `WWASH` state

Defaults: current

Description:
`WWASH` sets the state of the white wash flag for stack plotting. The flag may be either on or off. If no state is
specified RNMR will prompt for it with the current state of the flag as a default. When stack plots are created with
`STK` subsequent plots are considered to be behind previous plots. If the whitewash flag is on the portions of the line
that are behind peaks in the previous plots are not drawn. If the whitewash flag is off the whole plot is drawn for each
stacked plot.
## WWF
Set waveform values

Category: Waveform

Format: `WWF` chan ind val1 val2

Defaults: 1 1 current current

Prerequisites: Waveform generator implemented; Acquisition stopped (HALT); RNMRA only

Description:
`WWF` sets wave form generator values. The chan and ind parameters are used to set which value on which channel to
adjust. If either chan or ind are omitted RNMR will prompt for them with a default of 1. The parameters val1 and val2
are the waveform values. If either val1 or val2 are omitted RNMR will prompt for them with the current value as a
default.
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

Defaults: current_display_limits

Description:
`XT` extracts the data in the visible processing buffer that lies between llim and rlim. The limits are specified in the
current units of the buffer. If either limit is omitted RNMR not prompt for it and will use the corresponding current
display limit. All of the data outside of the specified limits will be discarded. The size of the visible processing
buffer will shrink to match the size of the extracted data points.
## XTP
Extract data for points

Category: Data Manipulation

Format: `XTP` llim npt

Defaults: current_display_limit 1

Description:
`XTP` extracts a specified number data in the visible processing buffer starting from llim. The left limit is specified
in the current units of the buffer. If the left limit is omitted RNMR not prompt for it and will use the current left
display limit. If the number of points to extract is not specified RNMR will not prompt for it and will extract a single
point. All of the data outside of the specified points will be discarded. The size of the visible processing buffer will
shrink to match the size of the extracted data points.
## XVAL
Convert from point index to unit value

Category: Data Analysis

Format: `XVAL` ind

Default: current_cursor_position

Description:
`XVAL` converts a point index into a position in the current units of the visible processing buffer. If no point index
is specified RNMR will prompt for it with the current cursor position as a default. If the specified point is outside of
the actual data in the visible processing buffer `XVAL` will return the position of the closest point (the leftmost or
rightmost point). The converted value is printed as an informational message.

# Z
---
## ZER
Zero visible processing buffer

Category: Misc.

Format: `ZER`

Description:
`ZERA` sets the data in the visible processing buffer to 0 and initializes the buffer parameters.
## ZERA
Zero acquisition buffer and shot counter

Category: Acquisition

Format: `ZERA`

Prerequisites: Acquisition stopped (HALT); RNMRA only

Description:
`ZERA` sets the data in the acquisition buffer and the shot counter to 0 and initializes the acquisition buffer
parameters.
## ZF
Zero fill visible processing buffer

Category: Data Manipulation

Format: `ZF` size

Defaults: current

Description:
`ZF` zero fills the data in the visible processing buffer to a new size. The size must be greater than or equal to the
current number of data points in the buffer and must be a power of 2. The buffer will be extended to the new size and
all of the points beyond the original data are set to zero. If size is omitted RNMR will prompt for it with the smallest
power of 2 that is greater than the current data size. The current maximum size for a processing buffer is 32768, so
size may not exceed this value.
## ZG
Zero averager and begin acquisition

Category: Acquisition

Format: `ZG` na

Defaults: current

Prerequisites: Acquisition stopped (HALT); Pulse program loaded (LOAD); RNMRA only

Description:
`ZG` zeros the averager and starts acquisition without dummy scans. The parameter na sets the number of scans to
perform. If na is omitted RNMR will not prompt for it and will use the current value as set and displayed by `NA`. If na
is provided then the value shown by `NA` will also be updated.
## ZO
Zoom

Category: Display Control

Format: `ZO`

Prerequisites: Processing buffer visible (VIEW PRO)

Description:
`ZO` enters the zoom subroutine. While `ZO` is active the currently selected cursor may be moved by clicking and
dragging on the display. The following subcommands are available:

Command | Description
------- | -----------
BI      | View imaginary part of buffer
BR      | View real part of buffer
E       | Expand display between cursors
Enter   | Terminate
F       | Contract to display full buffer
L       | Select left movement
M1      | Select 1 cursor display
M2      | Select 2 cursor display
O       | Enter offset value after prompt
P       | Move to next peak
Q       | Terminate
R       | Select right movement
S       | Switch cursors
T       | Enter threshold value after prompt
V       | Enter cursor position after prompt
W       | Write point values to file opened with `OPNWRT` (number, position in current units, position in default units, intensity)
0-3     | Move cursor by 10^N points

## ZO2D
Zoom on 2D data set

Category: Display Control

Format: `ZO2D` rec slice

Defaults: rrec 1

Prerequisites: Processing buffer visible (VIEW PRO)

Description:
`ZO2D` performs two-dimensional zooming on a slice of a blocked record. If no record is specified RNMR will prompt for
it with the current read record pointer (as set and displayed by `PTRA`) as a default. The last parameter, slice
specifies which 2D slice of a 3D or 4D source record should be used. If the source record has only two dimensions, slice
must be 1. If slice is omitted RNMR will not prompt for it and will use the first slice. Note that the current mapping
of dimensions to directions (as displayed and set by `DIRB`) will affect the selection of which one-dimensional blocks
of the record comprise the 2D slice. Slice is interpreted as a linear index over the 3rd/4th dimensions.

The number of accessible dimensions in the blocked record must be large enough that the first two directions are
accessible. The number of dimensions is set when the record is allocated and can be view using `SHOW REC rec 1 NDIMX`.

`ZO2D` will display a single block along one of the first two dimensions at a time. Various subcommands allow for
manipulation of which block along which dimension is displayed. Whenever the visible dimension is switched the block to
display will be determined by the position of the cursor. The following subcommands are available:

Command | Description
------- | -----------
D1      | View dimension 1
D2      | View dimension 2
Enter   | Terminate
F       | Select forward movement
Q       | Terminate
R       | Select reverse movement
S       | Switch dimension
V       | Select position in unviewed dimension in its units after prompt
Z       | Call `ZO` to manipulate 1D display and cursor
0:3     | Move in unviewed dimension by 10^N blocks

## ZO2DC
Zoom on 2D contour display

Category: `ZO2DC`

Format: `ZO2DC` rec slice

Defaults: rrec 1

Prerequisites: Processing buffer visible (VIEW PRO)

Description:
`ZO2DC` displays a contour plot of a two-dimensional slice of a blocked record and provides subcommands to manipulate
the contour display. If no record is specified RNMR will prompt for it with the current read record pointer (as set and
displayed by `PTRA`) as a default. The last parameter, slice specifies which 2D slice of a 3D or 4D source record should
be used. If the source record has only two dimensions, slice must be 1. If slice is omitted RNMR will not prompt for it
and will use the first slice. Note that the current mapping of dimensions to directions (as displayed and set by `DIRB`)
will affect the selection of which one-dimensional blocks of the record comprise the 2D slice. Slice is interpreted as a
linear index over the 3rd/4th dimensions.

The number of accessible dimensions in the blocked record must be large enough that the first two directions are
accessible. The number of dimensions is set when the record is allocated and can be view using `SHOW REC rec 1 NDIMX`.

The following subcommands are available:

Command | Description
------- | -----------
BI      | View imaginary part of data
BR      | View real part of data
D       | Select down movement
E       | Expand display between cursors
Enter   | Terminate
F       | Contract to display full contour plot
IB      | Integrate box centered on cursor (box size set by `IBOX`)
IR      | Integrate region between cursors
L       | Select left movement
M1      | Select 1 cursor display
M2      | Select 2 cursor display
P       | Move to next peak
O       | Enter offset value after prompt
Q       | Terminate
R       | Select right movement
S       | Switch cursors
T       | Enter threshold value after prompt
U       | Select up movement
V       | Enter cursor position after prompt
W       | Write point values to file opened with `OPNWRT` (number, position1 in current units, position1 in default units, position2 in current units, position2 in default units, intensity)
0-3     | Move 10^N points

## ZOA
Zoom on acquisition display

Category: Acquisition

Format: `ZOA`

Prerequisites: Acquisition buffer visible (VIEW ACQ)

Description:
`ZOA` enters the zoom subroutine for the acquisition buffer. While `ZOA` is active the currently selected cursor may be
moved by clicking and dragging on the display. The following subcommands are available:

Command | Description
------- | -----------
BI      | View imaginary part of buffer
BR      | View real part of buffer
E       | Expand display between cursors
Enter   | Terminate
F       | Contract to display full buffer
L       | Select left movement
Q       | Terminate
R       | Select right movement
S       | Switch cursors
V       | Enter cursor position after prompt
0:3     | Move cursor by 10^N points

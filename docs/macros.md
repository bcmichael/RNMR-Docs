# Macros
## Introduction
In RNMR, macros are user-defined procedures which consist of sequences of RNMR commands and (optionally) branching
instructions to control the flow of command execution. Simple macros may be nothing more than a collection of commands
to be executed sequentially as a unit, while more complex macros may perform calculations and manipulate acquisition and
processing functions via local and global arguments.

The creation and modification of macros may be handled entirely from within RNMR, using the Macro Edit and Define
utilities, however they can also be manipulated outside of RNMR using a text editor. After a macro some_macro.rnmrm has
been altered outside of RNMR you must call `MACRO SOME_MACRO` in order for the changes to show up inside RNMR.

A number of commands and control flow constructs will be briefly described here and some examples of their use will be
provided. More thorough documentation of these commands as well as many others can be found in the
[Full Command Descriptions](command/full_command.md) section.
## Macro Variables
There are three different types of variables available in RNMR: global arguments, local arguments, and symbols. Global
and local arguments are stored as strings with a maximum length of 80 characters even when they hold numbers while
symbols are stored as either single precision floating point numbers or 32-bit integers. Arguments are more flexible and
can be used in more places than symbols, but symbols are better for storing numbers with high precision. The name of a
global, local, or symbol can be up to 16 characters long and may only include the characters A-Z, 0-9, $, or \_. The
first character may not be a number.

These three types of variables share a common set of ways in which they can be defined. The commands `DNFGBL`, `DFNLCL`,
and `DFNSYM` can directly define a variable. These commands have the following set of qualifiers:

Qualifier | Description
--------- | -----------
/FLT      | Treat val as a floating point number
/INT      | Treat val as an integer
/STR      | Treat val as a string
/NDEC     | Set the number of decimal places to keep in /FLT mode

`DFNSYM` does not have the /STR option while `DFNGBL` and `DFNLCL` use it by default. `DFNSYM` uses /INT by default.
When using the number options basic arithmetic operations may be performed (+, - , /, \*). They will be performed in
order from left to right without regard for order of operations except for parentheses. With /INT the arithmetic will be
integer arithmetic and all of the operands must be integers. /NDEC sets the number of decimal places to keep when
converting a float to a string. This affects the stored value for globals and locals but only the display of the default
value for symbols. For example:

    DFNGBL TEMP 3
    DNFGBL /INT TEMP 1+2    

Will both define a global argument named temp with a value of 3. `DFLGBL` and `DFLLCL` can also be used to define
globals and locals. These only define the variable if it does not exist, and can have a prompt associated with them.
They have the same qualifiers as `DFNGBL` and `DFNLCL`. For example:

    DFLGBL TEMP 2                  ;if no global temp exists define global temp to be 2
    DFLGBL TEMP 2 'set temp value' ;if no global temp exists prompt for it with 2 as a default

Variables may be also be defined by popping default values displayed by commands. Use > to pop to a global, >> to pop to
a local, and >>> to pop to a symbol. When popping to a symbol the default value must be a number and the type of symbol
is determined by the type of the value. For example:

    LB >TEMP   ;global temp with the current line broadening value as its value
    LB >>TEMP  ;local temp with the current line broadening value as its value
    LB >>>TEMP ;float symbol temp with the current line broadening value as its value
    SP >>>TEMP ;integer symbol temp with 1 as its value

Variables can also be defined by using `SET INFO` to redirect informational messages to a variable. For example:

    SET INFO GBL TEMP
    ARV 1

Will define a global temp with the name of archive 1 as its value. Once again when defining a symbol the value must be a
number and the type of symbol is determined by the type of the value. Variables can also be defined by `DO` to hold the
loop counter. Variables may be removed using `REMGBL`, `REMLCL`, and `REMSYM`.

Using the value of a variable is done differently depending on the type of variable. Any place that % is used followed
directly a name the value of the global variable of that name will be substituted. The same applies to locals but with
& instead of %. For example:

    DFNGBL TEMP 3
    MSG %TEMP

Will print 3 to the console. Symbols work a bit differently. The name of a symbol can be used directly without any
special character, but can only be used as arguments to commands that expect the appropriate type of number. For
example:

    DFNSYM TEMP 2
    ARV TEMP

Will print the name of archive 2.
## Structured Control Flow
### DO Loops
A macro `DO` loop executes a set of commands between `DO` and its matching `ENDDO` a specified number of times. `DO`
accepts arguments specifying the starting and ending value of the loop counter. Each time the `ENDDO` is reached the
loop counter is incremented and the next iteration of the loop begins. There may optionally be a variable defined to
hold the loop counter. By default the loop counter will be stored as a local. For example:

    DO 2 6 COUNT
        MSG &COUNT
    ENDDO

Will print the numbers 2 through 6. There several special commands which can only be used between `DO` and its matching
`ENDDO`. `BRKDO` exits the loop immediately without finishing the loop. `NXTDO` iterates the loop counter and begins the
next loop iteration without finishing the loop body. `RPTDO` begins a new loop iteration without finishing the loop body
or incrementing the loop counter. Caution is merited with `RPTDO` to avoid creating infinite loops.
### SEL Selector
`SEL` can be used to select one of several blocks of commands to execute based on the value of a local or global. By
default a local is used. The value of the argument to `SEL` is compared to the argument of each `CASE` between `SEL` and
its matching `ENDSEL`. The commands between the first matching `CASE` and either the next `CASE` or `ENDSEL` are
executed. Note that if `CASE` has no argument it will match anything. For example:

    DFNLCL SELECTOR 2
    SEL SELECTOR
    CASE 1
        MSG 'A'
    CASE 2
        MSG 'B'
    CASE 3
        MSG 'C'
    CASE
        MSG 'IT WAS NOT IN 1-3'
    ENDSEL

Will print B.
### TST Conditional Execution
`TST` can be used to conditionally execute blocks of commands based on the result of a test. See the
[Full Command Descriptions](command/full_command.md#tst) section for a description of all the available tests. Either
the commands between `TST` and `ELSTST` or the commands between `ELSTST` and `ENDTST` will be executed based on the
result of the test. The `ELSTST` is optional. The /TRUE and /FALSE qualifiers determine which block executed for which
test result. With /TRUE `TST` will run the commands between `TST` and `ELSTST` if the test returns true and the commands
between `ELSTST` and `ENDTST` if it returns false. /FALSE reverses this behavior. /FALSE is mostly useful when you only
have one set of commands that you want to execute when the test is false. For example:

    TST LCL A
        MSG "THE VALUE OF A IS &A"
    ELSTST
        MSG "LOCAL ARGUMENT A DOES NOT EXIST"
    ENDTST

will test if local argument a exists and then either print its value or the fact that it does not exist.
## Unstructured Control Flow
Unstructured control flow in RNMR macros makes use of labels. A macro label is defined by a period followed by the label
name. When RNMR is searching for a label to jump to it will first search forward in the macro from the jump point and
then wrap around and continue searching from the beginning of the macro.

When jumping to a label a period not followed by a name will cause RNMR to simply continue execution on the next line.
Appending +# to a label will cause RNMR to start execution # lines farther down that it would otherwise. A label
including the period and line offset cannot be more than 16 characters long.

The most basic control flow in RNMR macros is the `GOTO` command, which will simply jump to a label and continue
execution from there. The `GOSUB` command is similar to `GOTO` in that it jumps to a label but when the macro hits an
`MEXIT` it will return to where `GOSUB` was called from instead of exiting the macro. This is useful for creating
subroutines within macros.

`GOTST` performs the same type of tests as `TST`, but instead of executing one of two blocks of commands it jumps to one
of two labels. Tests which would cause `TST` to execute the commands between `TST` and `ELSTST` cause `GOTST` to jump to
the first label. Tests which would cause `TST` to execute the commands between `ELSTST` and `ENDTST` cause `GOTST` to
jump to the second. For example:

    GOTST LCL A .EXISTS .DOESNOTEXIST
    .EXISTS
    MSG "THE VALUE OF A IS &A"
    MEXIT
    .DOESNOTEXIST
    MSG "LOCAL ARGUMENT A DOES NOT EXIST"
    MEXIT

will test if local argument a exists and then either print its value or the fact that it does not exist.

`ONERR` can be used to set a label to jump to in the event of an error. If any error occurs in an RNMR command execution
will jump to the specified label. Calling `ONERR` with no label unsets the error handling label.
## Macro Output
There are several ways in which an RNMR macro may output data to the user. First, data resulting from a calculation,
experiment, or other manipulation may simply be stored in a global argument, which may be used on console level or in
another macro as desired. Second, data from a macro may be printed to the screen using the `MSG` command. For example:

    DFNLCL ABC 9
    MSG "VALUE OF ABC IS &ABC"

The above code will print the following message to the console:

    VALUE OF ABC IS 9

Data generated by a macro to a disk file using commands such as `WRT`. For example:

    OPNWRT XYZ
    DFNLCL ABC 3
    WRT &ABC
    CLSWRT

Creates a disk file called XYZ.WRT, writes the value of local argument ABC as one line in that file, and closes XYZ.WRT.
When writing to files it is a good practice to set up error handling using `ONERR` to ensure that `CLSWRT` gets called
even if errors occur during the writing process.
## Passing Information to and from Macros
Data may be made available to all command levels using global arguments. However, it is also possible to explicitly pass
data from either console level or from a macro to a subprocedure without using global arguments.

To pass values to a macro simply supply the arguments after the macro name on the same line where it is called. Macro
arguments are automatically stored in local arguments 1, 2, 3 etc. based on the order they are provided in. It is
also possible to change the names of the arguments they are stored in using the `MACARG` command.

It is also possible to return values from a macro to the calling routine. Supply the return values as arguments to
`MEXIT` and they will be stored as local arguments `RTN$1`, `RTN$2`, `RTN$3` etc. in the calling procedure. The calling
procedure can use `RTNARG` much like the `MACARG` to put these return values into differently named arguments.

Both `MACARG` and `RTNARG` will only create as many local arguments as the number of values that were passed.  No local
arguments will be created for any additional names which are supplied. For example, if the macro temp contains the
following:

    MACARG A B
    MSG "ARGUMENT ONE IS &A"
    MSG "ARGUMENT TWO IS &B"
    DFNLCL C 3
    MEXIT &C 4

then calling the following:

    TEMP 1 2
        RTNARG ANSWER1 ANSWER2
    MSG "THE RETURN VALUES ARE &ANSWER1 AND &ANSWER2"

will print the following to the console:

    ARGUMENT ONE IS 1
    ARGUMENT TWO IS 2
    THE RETURN VALUES ARE 3 AND 4

There is an additional method of passing information into a macro using a / in a calling procedure to specify a name of
a local argument to create in the called macro. You can also specify the values of these arguments. For example, if the
macro temp contains the following:

    TST LCL A
        MSG "A EXISTS AND HAS VALUE &A"
        MSG "B HAS VALUE &B"
        MEXIT
    ELSTST
        MSG "A DOES NOT EXIST"
    ENDTST
    MEXIT

then calling the following:

    TEMP /A /B=2

will print the following to the console:

    A EXISTS AND HAS VALUE
    B HAS VALUE 2

Note that A does not have a value so it shows up as blank in the printed message.

These two methods of passing arguments into macros are somewhat analogous to the positional and keyword argument
constructs in some other programing languages. You may use a mixture of both methods to pass information into a macro.

The local arguments KEY$MAX and POS$MAX will automatically be created when a macro is called and will contain the number
of each of these types of arguments that were passed to the macro. The local argument MACRO$ will also be created and
will hold the name of the macro.

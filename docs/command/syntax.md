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

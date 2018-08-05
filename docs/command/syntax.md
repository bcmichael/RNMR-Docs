# Command Syntax
The general form of an RNMR command line is:

    (Repeat-count) command argument_1 (,) argument_2 (,)...

For example, the command line below executes the command ABC with parameters 1, 2, and 3 five times:

    5 ABC 1 2 3

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
1 and above  | do command N times
0            | don't do command
-1           | repeats forever
-2 and below | illegal

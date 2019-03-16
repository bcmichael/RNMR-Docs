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

At the time that an archive is opened (by `OPNARV`) the level of access RNMR has to that archive is set. RNMR will
always have read access to an open archive, but not necessarily write access. A given archive may be open in multiple
instances of RNMR but only one may have write access to it. This enforced by lock files which are created when RNMR
opens an archive with write access and deleted when the archive is closed. If RNMR closes unexpectedly (as in a program
crash or power loss) these lock files may not be properly deleted. When RNMR is reopened it will not be able to open the
archives for which lock files are still present. This can be circumvented by manually deleting the lock files in the
users archive folder or by using `OPNARV /FORCE`. Be careful to only take these actions if you are sure that the archive
is not in fact open in an instance of RNMR to avoid data corruption.

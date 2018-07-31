# Getting Started
## Introduction
RNMR software has two separate but similar programs. The acquisition softwareis called RNMRA, while the processing
software is called RNMRP. Open a terminal window and you will be prompted to enter your home directory or your last name.
To collect data you launch RNMRA by typing the following command:  

rnmra <return\>

A number of messages will be displayed and eventually you should receive the following prompt:

Enter user:

Enter your name here. Your "USER" name should contain less than eight alphanumeric characters, but should not contain
any blank or white space. Answer the on screen questions until it finally prompts you to:

Enter archive name:

The archive is where your data will be stored, so try to give it a descriptive name, such as the project name or date.
You may also enter the name of an existing archive in order to open it.

## Manually Running a One Pulse 1D Experiment
The proper frequency to tune your probe to can be found by typing `CATNUC`, which opens a list of nuclei and their
frequencies. It is always a good idea to check the parameters, so type ONEPLS and answer the questions on the screen.
Let us run our first experiment quickly so set the Number of Acquisitions to 4, by typing `NA 4`. We can start the data
acquisition by typing `ZG`. After a few moments the acquisition will finish.

To process the data, we first need to Get the FID from the AVerager by typing `GAV` and display it by typing `VIEW PRO`.
We might then type `BC` to apply a Baseline Correction; in order to remove any DC offset from the FID. We could then
apply some line broadening, in the form of an Exponential Multiplication of the FID by typing `EM`. Finally, we would
type `FT` in order to Fourier Transform the FID into a spectrum.

While it is certainly possible, and occasionally necessary, to enter all these commands sequentially, it is much more
convenient to construct a macro command to perform these tasks for you. Of course, you could write a suitable macro
yourself, and are encouraged to do so, however such a macro already exists entitled `RUN`, which we use to run the
spectrometer, i.e. acquire the data and display a spectrum on the screen. It assumes the number of shots has already
been chosen. So type `RUN`.  Sit Back!  Relax!  After the acquisition is complete type `PROC` to call the processing
macro and your processed spectrum will appear on the screen.

## Phase Correction
Almost all NMR spectra need to be phased. Let’s try using the menus to adjust the phase of the spectrum. Move the cursor
to the top of the screen where the menu bar is located. Pull down the Process menu, and select the option, Phase. A new
window entitled “Phase” should appear with sliders to adjust the Constant Phase (zero-order) and Linear Phase
(first-order) phase corrections. Notice that PH is displayed in the upper left-hand corner of the main RNMR window, up
above the lock meter.

It can be helpful to click the ZOOM box in order to enter the ZOOM subroutine of PH. Note that the PH in the upper
left-hand corner has now been replaced by ZO. Another new window should appear entitled Zoom. Use the mouse to move the
cursor (a vertical line) across the display towards the largest peak in the spectrum inside the main RNMR window. Once
the cursor is close to a peak, click the box marked "Next Peak" inside the Zoom window. The cursor should jump to the
nearest Peak. It may become necessary to drop the threshold for peak recognition in order that the software correctly
locates your favorite peak. Try clicking on the box marked "Threshold" in the Zoom window. Yet another new window should
appear which will allow you to change the value. The threshold is reported as a fraction of the full-screen height.
There are also buttons to marked "Left" and "Right" to change the direction of the search for the biggest peak.

Once the cursor is safely on top of the peak of interest, click "Okay" at the bottom of the Zoom window. Notice that PH
is again displayed in the upper left-hand corner. We have left the ZOOM subroutine, and gone up a level, back to the
main PH command. Click the box marked "Pivot" inside the Phase window, to use the selected peak as the pivot point for
phase correction. Use the slider marked "Constant phase" to adjust the phase until the peaks point upwards, and then
select the slider marked "Linear phase". This time, however, rotate the phase of peaks which are a long way away from
the cursor until they also point upwards. Don't worry if you don't get it right first time. No two people would adjust
the phase in the same way! The constant phase correction changes the phase of all of the peaks by the same amount, i.e.
it applies a frequency independent phase shift. The linear phase correction applies a first-order frequency dependent
phase shift; i.e. the phase shift varies across the spectrum.

## Manipulating Spectra
RNMR has a wide variety of built-in commands that can be used to change the appearance of the spectrum.   

`WNDLIM` moves the spectrum up or down the screen, and changes the vertical display scale.  The default value sets the
baseline to the middle of the screen and displays the region between +1 and -1.  For example `WNDLIM -0.1 1` sets the
baseline near the bottom of the screen.

`SC #`	multiplies the vertical scale by #, a number you specify. For instance, if you want to multiply the scale by 3,
type `SC 3`. Alternatively, if the peaks are too big, you could type `SC 0.1`, to divide the vertical scale by a factor
of 10.   

`NORM` normalizes the spectrum so that the biggest peak fits on the screen.

`ZO` enters the ZOOM command. This is functionally equivalent to the zoom subroutine of PH but has a few extra knobs and
whistles. Move the cursor to a peak you wish to use for referencing and type `O`, for offset, and you will be prompted
for the new value that you have chosen for this peak. The ZOOM command is very powerful and contains many options, so
why not use the Help menus to find out more about it?

`UNIT /FREQ PPM` changes the display units to PPM (this would not be legal for an FID).

`LIM # ##` displays the portion of the spectrum between # and ##. For instance, suppose you wish to display the portion
of the spectrum between 1 and 2 PPM, type `LIM 1 2` (assuming you have previously selected UNIT PPM and set the
referencing).

`LPK`  lists the peaks above the threshold value.

`LP`  lists the parameters.

`INTG`  integrates the spectrum.

## Keeping Stuff
Your data can be stored in the archive you selected when you opened RNMRA. An archive can keep a maximum of 200 records.
A record is a place where you store data.  There are three types of record; scratch-records, archive-records, and
block-records. Records 1 to 4 are scratch-records that are used as temporary workspace. Records 5 to 200 are
archive-records that are saved in an archive file. Blocked-records are used to store multi-dimensional data. Thus, one
archive could conceivably store 195 n-dimensional data sets.

In order to save the data, it must first be displayed. What-You-See-Is-What-You-Get, so if a FID is displayed, then that
is what will be saved. Alternatively, if you are looking at a spectrum, the spectrum will be saved. However, it is more
versatile to save the raw data, i.e. the FID, because this can be transformed in a variety of ways to produce different
spectra. If you wish to save an FID but have already Fourier transformed it; you can always use the `GAV` command to Get
the AVerager memory, before typing `SA` to save it in your archive. Type CAT for a catalog of your archive. You can get
back to your saved data by typing `GA #` to access record #.

## Help
RNMR has extensive on-line help screens. They are divided into two sections, one devoted to RNMR commands, and the other
devoted to the PPROG pulse programming language. Why not try them out now? You could use the mouse to select HELP in the
menu bar at the top right-hand edge of the RNMR window. Alternatively you could try typing HELP in command line of the
main RNMR window. This will spawn a new subprocess. Unfortunately it will probably be hidden behind the main RNMR window.
You may have to use the mouse to select the new window.  

## Display Screen
The display screen is divided into three. The upper portion displays a maximum of five lines of alphanumeric information.
The top line is a status line. It starts, on the left-hand side, with the name of the command, or subcommand, which is
awaiting input. During acquisition this will frequently be either MAIN, QUIT or WAIT. The center of the status line
informs the user which display mode has been selected, either LCK, ACQ or PRO. You choose a particular display mode, by
typing `VIEW ACQ` for acquisition or `VIEW PRO` for processing or `VIEW LCK` for the lock. On the right hand side of the
status line is the Shot Counter, which shows the number of completed transients. The second line of the display is used
for the lock meter, which is displayed both graphically as a horizontal bar whose length changes and also as a numeric
value. The third line shows any comment or title that you may have entered with the `TITLE` or `TITLEA` command. The
right hand side of the fourth line shows your user name and the date. The fifth line shows on the LHS, the Left Display
Limit; in the center, the current Unit; and on the RHS the Right Display Limit. If you select the processing window and
ZOOM in on the data with the `ZO` command, then the fifth line starts with the Active Cursor Position and ends with the
Active Cursor Intensity. When commands such as `ZO2DC` are executed, the fifth line is extended to show the left and
right limits in both dimensions.

The center portion of the display screen is used to display graphical information, such as FIDs or spectra. The lower
portion of the screen is used for your input. There are five lines, above the command line input window. The top four
lines show the previous entries. The fifth line will display ENTER COMMAND: when the network is ready to accept input
from the keyboard. A flashing I-beam cursor is displayed at the start of the command line, which, if it is the active
window, will be highlighted by the use of an line or box around the command line.  It may occasionally be necessary to
click the mouse in the command line to get input focus. As you type your input, the flashing I-beam cursor moves to the
right indicating the current input position. When <return> is pressed, the input line is checked for validity and,
hopefully, acted upon.

## Setting the Magic Angle
We typically set the magic angle for solid state NMR using KBr. With a sample of KBr spinning at 4-6 KHz run a one pulse
experiment. We want to be able to observe rotational echoes, so we must move the transmitter frequency to be on resonance
with the KBr peak. First process, and phase the spectrum. Type `ZO` to enter the zoom subroutine (hitting enter exits
it). Move the cursor to the peak and note the frequency in the top left of the display. The `P` command within the zoom
subroutine can help you position the cursor on the center of the peak.  Move the transmitter frequency by typing
`F 1 #`, where # is the frequency you wish to move to.

Run the experiment again with the new transmitter position and you should see rotational echoes in the FID if you are
spinning at close to the magic angle. Type `MAG` to put the FID into magnitude mode. How far out in time do the
rotational echoes go? Adjust the magic angle to make the rotational echoes appear as far out as you can. It may be
necessary to increase the number of scans in order to see the further out rotational echoes.

## Basic Shimming
The shim controls can be accessed by selecting the Controls drop down and clicking Shim. Type `ZO` to enter the zoom
subroutine (hitting enter exits it). Within the zoom subroutine you can switch between the two cursors by typing S and
move the selected cursor by clicking and dragging with the mouse. With the cursors positioned on either side of a peak
its width at half height can be determined by typing `LW`. Adjust the shim values in the shim control window to get
single narrow peaks.

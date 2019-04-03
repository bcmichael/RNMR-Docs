# Getting Started
## Introduction
RNMR software has two separate but similar programs. The acquisition software is called RNMRA, while the processing
software is called RNMRP. To get started using a spectrometer pen a terminal window on the spectrometer computer. You
will be prompted to enter your home directory or your last name. After entering your username the working directory of
the terminal will be your user folder on that spectrometer. The first step to collecting data is to launch RNMRA by
entering the following command in the terminal:  

    rnmra

A number of messages will be displayed and eventually you should receive the following prompt at the RNMR console:

    Enter user:

Your user name should contain less than eight alphanumeric characters, but should not contain any blank or white space.
Answer the on screen questions until it finally prompts you to:

    Enter archive name:

This archive is where your data will be stored, so try to give it a descriptive name, such as the project name or date.
An existing archive may be specified here in order to open it.

RNMR has many commands, some of which are referenced here when describing how to accomplish a particular task. To run a
command type it into the console at the bottom of the RNMR window. Many RNMR commands require additional arguments to
specify exactly what they should do. To see a full description of a particular command including its arguments and what
it does look it up in the Full Command Descriptions section of this documentation.

## Manually Running a One Pulse 1D Experiment
The first task when starting up doing solid state NMR is typically to adjust the spinning angle to the magic angle. We
typically set the magic angle using the ⁷⁹Br signal from a sample of KBr spinning at 4-6 KHz. Once the sample is in the
probe and spinning the probe must be tuned to the correct frequency. The command `CATNUC` opens a list of defined nuclei
and their frequencies (given the current spectrometer frequency). The appropriate channel of the probe (usually the ¹³C
channel) should be tuned to the frequency listed for ⁷⁹Br.

Enter ONEPLS at the command line to call a macro for setting up a one pulse NMR experiment. This macro will prompt for
a channel sequence. Only one channel is needed for a one pulse experiment so enter the number corresponding to the
physical channel that should be used for ⁷⁹Br (usually the same as for ¹³C).  Next a window will pop up asking for
information about the experiment to run. Make sure that the nucleus is set to BR79. The other parameters can likely be
left at their default settings for now. Next the prompt will ask for a pulse width. This value is interpreted as a
number of microseconds. 5 should usually be a reasonable for KBr. Another window will pop up asking for more parameters.
Again, the default settings should work for now. Finally the prompt will ask for a title, so enter a title describing
the experiment.

To start off with set the number of scans to 4 with the command `NA 4`. Start the acquisition with `ZG`. The shot
counter in the top right corner of the display will count up from 0 to 4. After the final scan a message will printed
to the console saying ACQUISITION FINISHED. In order to process the data it must be transferred from the averager to a
processing buffer. Use `GAV` to transfer the data to the visible processing buffer. The FID will be visible on the
screen if the processing buffer is being viewed. When viewing the processing buffer PRO will be displayed in the top
middle of the display to the left of the shot counter. If the current view is not the processing buffer use `VIEW PRO`
to view the processing buffer.

Now that the FID is in the processing buffer it can be processed. A basic processing might include subtracting a
constant baseline offset from the FID (`BC`), followed by an exponential apodization (`EM`), followed by a Fourier
Transform (`FT`), followed by a linear baseline subtraction from the spectrum (`BF`), finishing off by normalizing the
spectrum on the display (`NORM`). After running all of these commands there should be a processed spectrum visible on
the display.

Sequences of commands like this that will need to be repeated many times can be conveniently packaged up in a macro
which can execute all of the commands with a single call. The RUN macro is used for running 1D experiments instead of
manually using commands like `ZG` and `GAV`. The PROC macro is used for processing a spectrum instead of entering a long
sequence of processing commands. To use these macros first copy them to your macro folder then load them into RNMR using
`MACRO` (`MACRO RUN`, `MACRO PROC`). Now entering run at the command prompt will run the experiment and transfer the
data to the visible processing buffer. Entering proc will process the data.

## Manipulating The Display
It is often useful to change various aspects of the displayed spectrum. Things like zooming in on a region of spectrum
or scaling the spectrum up or down to fit the screen are common operations when viewing data. Selecting zoom from the
view menu enters the zooming subroutine and opens a window with some useful controls. In this subroutine there are two
cursors which can be moved by clicking and dragging on the screen. The switch cursors button changes which cursor is
active and movable. The position of the active cursor and the data value at that point are displayed about the data
display. The cursor can also jump to the next peak in a specified direction. The peak picking threshold can be changed
using the threshold button. The display of the cursors also has two different modes which can be toggled. The region
between the cursors can be expanded to the full display or the full spectrum can be displayed. This window is built on
the `ZO` command and all of the keyboard commands it allows are available. `LIM` can also be used to set the display
limits to specific values. The units used for time or frequency display can be changed using `UNIT`

There are several useful commands available for scaling the displayed data vertically. `NORM` can be used to normalize
the data to fit the display. `SC` can be used to scale the data by a certain amount. `AK` can be used to set an absolute
scale and `AI` can be used to return to that set scale.

## Phase Correction
Almost all NMR spectra need to be phased. Select the phase option from the process menu to open a window with sliders
for interactive phasing. These sliders adjust the constant (0th order) and linear (1st order) phase correction
parameters. The pivot point for the first order phase correction will start out at the position of the vertical cursor
displayed on the screen.

The zoom button in the phase control window opens the same zoom window as the zoom option in the view menu. This can be
used to change the displayed data and to move the cursor. The pivot button moves the pivot of the linear phase
correction to the position of the last active cursor. It is generally helpful to put the pivot on one of the more
intense peaks in the spectrum.

Adjust the constant phase until the peak at the pivot is phased properly, then adjust the linear phase until peaks far
from the pivot are phased correctly. This usually has to be repeated iteratively a few times to get the spectrum phased
properly. Press okay to keep the phased spectrum or cancel to discard the changes.

Once the correct phase parameters are determined for a spectrum they will be the same for further spectra collected with
the same pulse sequence. The parameters after phase correction are automatically saved and `PS` can be used to phase
a spectrum with the saved values. This is usually done in the processing macro.

## Setting the Magic Angle
Once a properly phased one pulse KBr spectrum has been obtained it is time to adjust the angle. Use the zoom
functionality to position a cursor on the center peak of the spectrum. Note the position of the cursor. After exiting
the zoom subroutine move the transmitter frequency to the position of the center peak by entering `F 1 #` where # is the
position to move the transmitter to. Moving the transmitter on top of the peak removes the frequency offset from the FID
meaning that is will decay without showing a sinusoidal oscillation.

When the experiment is run again with the transmitter on resonance the FID should be a decaying signal with rotational
echoes spaced out one rotor period apart from each other. Transform the data into magnitude mode with `MAG` to make this
shape easier to see. The better the angle is set the farther out in time these echoes will extend. It may be necessary
to increase the number of scans to see rotational echoes that extend far out in time. Adjust the angle to get the echoes
to extend out as far as possible.

## Keeping Stuff
Your data can be stored in the archive you selected when you opened RNMRA. An archive can keep a maximum of 200 records.
A record is a place where you store data. There are three types of record; scratch records, archive records, and blocked
records. Records 1 to 4 are scratch records that are used as temporary workspace. Records 5 to 200 are available to
permanently store data and can hold either archive records or blocked records. Archive records hold a single one
dimensional data set. Blocked records are used to store multi-dimensional data and must be allocated before they can be
used.

In order to save the data, it must first be displayed. What-You-See-Is-What-You-Get, so if a FID is displayed, then that
is what will be saved. Alternatively, if you are looking at a spectrum, the spectrum will be saved. However, it is more
versatile to save the raw data, i.e. the FID, because this can be transformed in a variety of ways to produce different
spectra. If you wish to save an FID but have already Fourier transformed it; you can always use the `GAV` command to get
the data from the averager to save. Use `SA` to save the data from the visible processing buffer to an archive record.
`CAT` can be used to display a catalog of saved records. To get data from an archive record and transfer it back to the
visible processing buffer for further manipulation use `GA`.

## Shimming and Referencing
In order to acquire high quality NMR spectra the magnetic field in the sample must be as homogenous as possible. This
homogeneity is obtained by adjusting the current in a set of shim coils that generate magnetic fields to counteract
inhomogeneity of the main coil.  The shim controls can be accessed by selecting the shim option from the controls menu.
The homogeneity is judged by looking at the width and shape of a peak from a reference sample. In solid state NMR this
is usually done using a ¹³C spectrum of adamantane measured with a cross polarization experiment. A workflow for running
such an experiment is detailed in the Running Routine Experiments section of this documentation.

The width of a peak can be easily measured in RNMR. Position the two cursors on either side of the peak of interest
using the zoom subroutine. Then use `LW` to print the width at half max of the peak as an informational message. Adjust
the shims to minimize this width.

This same adamantane sample is usually used as a frequency reference. Referencing is typically performed using the
reference macro. Call reference setref to begin referencing. When prompted for ppm or kHz enter yes to reference in ppm
then position the cursor on the peak to reference to. Press O and enter the desired chemical shift of the peak. The
chemical shifts of the peaks of adamantane relative to DSS will be printed to the console so that they are easily
available. to enter. Finally press enter to finish and then again to accept the changed reference.

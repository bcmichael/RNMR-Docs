# Pulse Programming
Every NMR experiment consists of a series of RF pulses on one or more channels. The sequence, duration, intensity, etc.
of these pulses must be specified. The sequence of pulses to perform on each channel is specified in a pulse program and
compiled into object code that can be run by the pulse programmer in the spectrometer. Pulse programs consist of a
series of commands and can make use of macros much like when running RNMR. The style of pulse programming presented here
makes heavy use of a set of macros that can handle many of the low level details of the pulse program without the user
having to deal with them manually.

Pulse programs are stored in the users pp folder and have the .pp file extension. Pulse programs must be compiled using
the pprog command from the terminal before they can be run. Several files will be generated by pprog with the following
file extensions: .ppl, .ppo, and .pps. The .ppl file contains an expanded version of the pulse program with the contents
of macros and the values of many variables filled in. This file is often very long, but it can be useful to see what
actually happened during the compilation process. The .ppo file contains the object code that gets sent to the pulse
programmer and is not intended to be human readable. The .pps file contains a list of the pulse programmer symbols
defined by the pulse program. More information about pulse programmer symbols will be presented later.

The use of these macros for pulse programming is best explained through examples. The following sections will walk
through a series of pulse sequences of increasing complexity and explain how they work.
## JustCP
The following pulse sequence describes the justcp experiment used in the
[Running Routine Experiments](running_routine_experiments.md#invoking_an_experiment) section:
```
; ========================
; DEFINITIONS
; ========================
allocx pwx pwx_flip
allocx ppmd ppmd_dec
allocx pwx pwx_cwdec

; ==========================
; DEFINE OBSERVE PROGRAM C13
; ==========================
use timer
use pwxpls cppls
use pwxdly cpdly pwrh 1 * * 64		;nam,pwr,psx,ppmd,beg,size
use pwxpls flipdn pwrh 1 * pwx_flip ;nam,pwr,psx,ppmd,pwx
use pwxpls flipup pwrh 1 * pwx_flip

iniobs
pwxpls cppls
pwxdly cpdly
pwxpls flipup
pwxpls flipdn
sample
recycle
finobs

; ==========================
; DEFINE DECOUPLE PROGRAM H1
; ==========================
use pwxpls cppls pwrh 1 * *
use pwxdly cpdly pwrh 1 * * 1
use pwxpls flipdn pwrh 1 ppmd_dec pwx_cwdec
use pwxpls flipup pwrh 1 ppmd_dec pwx_cwdec
use period sample tppm pwrh * 64 ppmd_dec ;nam,seq,pwr,beg,size,ppmd

inidec
pwxpls cppls
pwxdly cpdly
pwxpls flipup
pwxpls flipdn
sample
recycle
findec
```
This pulse sequence is organized into several sections. In the first section several pulse programmer symbols are
allocated. In the second section the pulses on the observe channel are set up. Finally, in the last section the pulses
on the decoupling channel are set up.
### Allocating Symbols
`ALLOCX` is used to define three different pulse programmer symbols. Every pulse programmer symbol has a type. In this
case two of the allocations are of type pwx and one of type ppmd. These symbols are used for pulse powers and phase
cycling respectively. These pwx and ppmd symbols are used to assign a particular power or phase cycle to a particular
pulse later in the pulse sequence. Pulse programmer symbols must be allocated before they are used. The actual power or
phase cycling can later be set from RNMR using the `PWX` or `PPMD` commands respectively. For example pwx_flip is used
for the flip pulses on channel 1. The actual power of these pulses can be set from RNMR using `PWX 1 FLIP`.
### Observe Channel
The first several lines of the observe channel section make use of a macro called use. The first argument of use
selects a macro to call. For example `USE PWXPLS` internally calls a macro called use_pwxpls. The call to `USE TIMER`
sets up an internal timer for measuring the elapsed time of a pulse sequence. `USE PWXPLS` is being used to set up the
parameters of the pulses on the observe channel. The use_pwxpls macro can allocate certain pulse programmer symbols. For
example `USE PWXPLS CPPLS` will allocate a pls called cppls. Thus from RNMR `P CPPLS` can be used to set the length of
this pulse. It is not necessary to manually allocate this pls, because the macro handles it. Since no additional
arguments are given after the pls name the pulse will be set up to not actually do anything. This will be used on the
observe channel to keep the timing in sync with the second channel, but the RF power on this channel during this pulse
will be off.

In the case of flipdn and flipup the macro will again allocate a pls for each. The next argument is set to pwrh.
This specifies which gate to use for executing the pulse. Gates correspond to physical paths within the spectrometer
hardware. Using pwrh means that these pulses will be executed using setting 1 of the coarse attenuator. This attenuator
can have two different settings within a given pulse sequence. The actual setting of pwr is controlled by `PWR 1` from
RNMR. The next argument specifies which psx to use for this pulse. A psx is a transmitter phase. In this case instead of
using a pulse programmer symbol to represent the psx, the psx is specified directly by index. By default the first four
psx values on each channel are set to 0, 90, 180, and 270 degrees respectively. Thus passing 1 for this argument sets
the pulse to a phase of 0 degrees. The next argument is a ppmd to use to control the phase cycling of this pulse.
Passing a * for this argument indicates that the macro should allocate a ppmd for this pulse. The allocated ppmd will be
named based on the pulse and channel. For example the ppmd for flipup will be called flipup1. A ppmd that has already
been allocated may be passed in order to use that ppmd for the pulse. The final argument passed here is a pwx to use for
the pulse. Passing a * would indicate that the macro should allocate a pwx for the pulse. In the case of flipup and
flipdn the previously allocated pwx_flip is used. This ensures that both of these pulses will be set to the same power.

The remaining line in this portion of the pulse sequence uses `USE PWXDLY` to set up the cpdly. This corresponds to the
cross polarization step in the pulse sequence. Much like with `USE PWXPLS` a pulse programmer dly will be allocated
called cpdly. The next three arguments set the gate, psx, and ppmd much like `USE PWXPLS`. The last two arguments work
somewhat differently. The cp will have a power ramp on the observe channel, which will ultimately be implemented as a
series of short steps each with a different power. The last two arguments are the location of the first step in memory
and the number of steps to use. Passing a * for the beginning allows the macro to select the location. The ramped cp
will have 64 steps. The order in which all of the calls to the use macro occur is not significant as it does not alter
the actual order of the pulse sequence. It is convenient, however, to have them mirror the order of the pulse sequence.

The macros inobs and finobs are required at the beginning and end of the observe channel. They perform initialization
and finalization tasks for the observe channel. In between these two macros the actual sequence of pulses is defined.
The macros pwxpls and pwxdly put the pulses into the sequence in the order that these macros occur using the parameters
set up previously by the use macros. The final two lines of the observe sequence call the sample and recycle macros.
These handle the sampling of the FID and the recycle delay. The sample macro only actually samples the FID on the
observe channel.
### Decoupling Channel
The pulses for the second channel are set up much like those for the first channel. It is important that all of the
calls to the use macro for the second channel come after finobs, because a global variable holding the channel number is
incremented by finobs. Thus by placing these calls after finobs they will automatically be configured for the second
channel. The pwx for cppls is passed as a * to indicate that the macro should define the pwx, which in this case will be
named cppls2. The cpdly uses only 1 step which will produce a constant amplitude during the cp contact. The last call to
use calls `USE PERIOD`. This is used to select a sequence to repeat throughout a period of time in the overall pulse
sequence. The first argument specifies a name for the period. If the name of the period is sample then it sets up the
behavior of a decoupling channel while sampling the FID on the observe channel. The second specifies the sequence to
run. The remaining arguments set up the gate, first location, size, and ppmd much like `USE PWXDLY`. In this case it is
being used to set up TPPM decoupling while sampling the FID. The macros inidec and findec work similarly to iniobs and
finobs. The sample macro will not actually sample data on a decoupling channel, but rather will execute the TPPM
decoupling that was set up.

Pulse sequences may use up to four channels. The first channel is always the observe channel and every channel after
that is a decoupling channel. Channels 3 and 4 work exactly the same as channel 2 and simply come after the findec from
channel 2.
### Experiment Macro
In [Running Routine Experiments](running_routine_experiments.md#invoking_an_experiment) each pulse sequence had a macro
associated with it that was responsible for loading the experiment and setting up some basic parameters. A simplified
example of such a macro for the justcp experiment follows:
```
macarg submac
dflt submac,setup, 'Enter submacro:'
goto .&submac
mexit

.setup
chn 21
suchn 1,C13,8.1,100,90,50
; chn,nuc,freq,pwrh,pwrl,pwx1
msg 'Chn 1 is set to C13'
ex justcp
msg 'CP and calibration'
titlea "JustCP"
unit /freq ppm
suacq 22.40,512,3.0,40.0,4,0,10
; dw,size,rd,gain,na,ndly,p8
gosub .H1param
gosub .chn1param
gosub .cpppmd4
mexit

.ccal
; for calibration of carbon pulse powers
p flipup 5
p flipdn 5
na 8
f 1 21.97
gosub .ccalppmd
msg 'CP followed by flipup and flipdn, adjust lengths & powers'
mexit

.chn1param
; setup chn C13 ======================
supls 1,cppls,0,2.5
sudly 1,cpdly,0,1.5
; chn,nam,pwx,dly
supwxval 1,cpdly,ramp,50,60,,,64
pwx 1 flip 50
supls 1,flipup,>,0.0
supls 1,flipdn,>,0.0
pwxex 1 *&macro$
mexit

.H1param
; setup chn proton ===================
suchn 2,H1,0,100,100,100
; setup pulses
supls 2,cppls,100
sudly 2,cpdly,50
pwx 2 cwdec 83
supls 2,flipdn,>
supls 2,flipup,>
super 2,sample,on,*,71,6.9
supsxval 2,sample,tppm,22,0
psxex 2 *&macro$
mexit

.cpppmd4
ppmd cppls2    1
ppmd cpdly2    2
ppmd cpdly1    1234
amd            3412
namd 4
msg 'justcp ppmd loaded'
mexit

.ccalppmd
ppmd cppls2    1111 3333
ppmd cpdly2    2
ppmd cpdly1    1
ppmd flipup1   2
ppmd flipdn1   1234
amd            4123 2341
namd 8
msg 'ccal ppmd loaded'
mexit

.pwxex1
supwxex 1,cpdly,ramp
mexit

.psxex2
supsxex 2,sample,tppm
mexit
```
This is a simplified version of a justcp macro in that it only has the option to set up the experiment to detect on the
¹³C channel, but it covers most of the basics of setting up an experiment. Much of what this macro does is similar to
what the macros shown in [Running Routine Experiments](running_routine_experiments.md#invoking_an_experiment) do. It
sets default values for the pulse lengths and powers in the experiment. It also performs a few additional tasks. The
command `CHN 21` maps the physical channels to logical channels. This indicates that physical channel 2 will be logical
channel 1 (the observe channel) while physical channel 1 will be logical channel 2 (the decoupling channel). This setup
is appropriate for a spectrometer which has carbon on physical channel 2 and proton on physical channel 1. This varies
by spectrometer, so be sure to use the correct channel order for the particular spectrometer. The suchn macro is used to
set up a variety of parameters for each channel. For example:

    suchn 1,C13,8.1,100,90,50

Sets up channel 1. It assigns it a nucleus (`NUC 1 C13`), sets its frequency offset (`F 1 8.1`), sets the high and low
coarse power levels (`PWR 1 1 100`, `PWR 1 2 90`), and sets the power of pwx 1 (`PWX 1 1 50`). Each of these commands
could be entered individually but this macro is a convenient way to do all of these tasks. The supls macro is similarly
used to set up the power and duration of pulses.

The `PWXEX` and `PSXEX` sections/commands are used to set up the powers for the ramp and the phases for the TPPM
decoupling. When these commands are called with * followed by a macro they run the respective subsections of the macro.
For example:
```
pwxex 1 *&macro$
```
runs the PWXEX1 submacro. This then calls the supwxex macro to set up the powers for each step of the ramp. The same
idea holds for setting up the phases of each step of the decoupling.

The macro also loads the justcp pulse program via `EX JUSTCP`. It also has sections for setting up a couple of different
phase cycles for the experiment. The `AMD` command sets the phase cycle for the receiver and the `PPMD` command sets the
phase cycle for the pulses that used the given ppmd in the pulse sequence. In this case each number 1-4 refers to the
phase values 0, 90, 180, and 270 degrees respectively. A sequence of modes is supplied to `PPMD`. Starting with the
first mode the sequence is iterated over as multiple shots are taken. That is to say on the first shot the first mode is
used, on the second shot the second mode is used etc. The total number of modes is set with `NAMD`. When all of the
modes or `NAMD` modes whichever is less have been performed the sequence starts over. It is therefore okay to specify
fewer modes for sequences that will repeat. The phases specified by `PPMD` are added to the phase given to a pulse by
specifying its psx in the pulse sequence. In this experiment every pulse was given a psx of 1 (0 degrees) so the value
given by the ppmd will be the phase of the pulse.

Two different phase cycles are available in the macro: one for collecting a CP spectrum and one for calibrating carbon
pulse powers. A submacro called ccal is provided to set up carbon power calibration as demonstrated in
[Running Routine Experiments](running_routine_experiments.md#invoking_an_experiment).
## DARR
The following pulse sequence describes the DARR experiment used in the [Running Routine Experiments](running_routine_experiments.md#running_a_2d_darr_experiment) section:
```
; ==========================
; DEFINITIONS
; ==========================
allocx dly dly_t1 alloc_int
allocx dly dly_moret1 alloc_int

allocx dly dly_mix
allocx ppmd ppmd_dec
allocx pwx pwx_flip
allocx pwx pwx_cwdec

; =============================
; 2nd dimension
; =============================
use dim 2 1 2 ;idim,logical_chn,nseg
dimdly 2
pop dly dly_t1

; ==========================
; CALCULATIONS
; ==========================
; moret1 = size*step-t1
push loop loop_size$2
push dly dly_step$2
mul
push dly dly_t1
ifstk lt
  sub
  pop dly dly_moret1
else
   push dly #0
   pop dly dly_moret1
   pop
   pop
endif

; ==========================
; DEFINE OBSERVE PROGRAM
; ==========================
use timer
use pwxpls cppls
use pwxdly cpdly pwrh 1 * * 64	   ;nam,pwr,psx,ppmd,beg,size
use pwxpls flipup pwrh 1 * pwx_flip ;nam,pwr,psx,ppmd,pwx
use pwxpls flipdn pwrh 1 * pwx_flip

iniobs
pwxpls cppls
pwxdly cpdly
dly gate_idle dly_t1
pwxpls flipup
dly gate_idle dly_mix
pwxpls flipdn
sample
dly gate_idle dly_moret1
recycle
finobs

; ==========================
; DEFINE DECOUPLE PROGRAM
; ==========================
use pwxpls cppls pwrh 1 * *                ;nam,pwr,psx,ppmd,pwx
use pwxdly cpdly pwrh 1 * * 64             ;nam,pwr,psx,ppmd,beg,size
use pwxpls flipup pwrh 1 ppmd_dec pwx_cwdec
use pwxpls flipdn pwrh 1 ppmd_dec pwx_cwdec
use period sample tppm pwrh * 64 ppmd_dec  ;nam,seq,pwr,beg,size,ppmd
use period evolve tppm pwrh * 64 ppmd_dec
use period mix cw pwrh ppmd_cwdec

inidec
pwxpls cppls
pwxdly cpdly
period evolve dly_t1
pwxpls flipup
period mix dly_mix
pwxpls flipdn
sample
period evolve dly_moret1
recycle
findec
```
Many of the commands in this pulse sequence were used in the justcp sequence shown above, but some are new.
### Allocating Symbols
Two of the pulse programmer symbols allocated here have an extra argument compared to the other allocations. This
argument specifies the allocation mode for the symbol. In this case the mode is alloc_int which means the associated
value will be modified by the pulse programmer during the execution of the pulse program rather than set by the user
from RNMR. In other pulse programs you may encounter the alloc_usr or alloc_ext modes. These are equivalent and mean
that the user will set the value from RNMR. This is the default behavior if no mode is specified so it can be omitted.
You may also encounter alloc_temp which is for temporary symbols that can later be deallocated with `FREE` allowing
the related memory to be reused for different symbols within the same pulse program.
### Dimension 2 Setup
The DARR program has an additional section that justcp did not for setting up the second dimension. This is because DARR
is a two-dimensional experiment. `USE DIM` sets up the second dimension parameters. The first argument specifies that
the parameters are being set for dimension 2. The second argument indicates that the evolution in this dimension is
associated with logical channel 1. This ensures that the correct nucleus and parameters are associated with the
dimension for use in later processing steps after acquisition. The final parameter specifies the number of segments in
this dimension. In this case it is set to 2 for the 2 steps used for hypercomplex acquisition in the second dimension.
The dimdly macro calculates the length of the indirect evolution time for each iteration of the pulse sequence. The
value is left on the calculator stack, which is described below. The result is popped to the allocated dly t1 for
further use in the pulse sequence.
### Calculations
The other section which appears in DARR but not justcp is calculations. The pulse programmer is capable of performing
arithmetic operations on the values set in the pulse program. This functions as a stack calculator similar to the `CALC`
or `CALCI` commands in RNMR. Values can be pushed onto or popped from the stack and operations can be performed on the
stack. The stack calculator operations are compiled into the .ppo file and are performed by the pulse programmer as the
experiment is run. In this case the dly moret1 is being calculated. This delay is executed at the end of the pulse
sequence before the recycle delay in order to keep the overall length of the experiment constant even as the indirect
evolution time changes. The loop size$2 and dly step$2 are allocated by the use_dim macro and hold the number of
indirect incrementation steps for and length of each step for the second dimension. This calculation must come after the
use of this macro so that these symbols are defined. The command `IFSTK LT` checks whether the length of the indirect
evolution is less than the maximum evolution (size$2*step$2). If it is it executes the commands before the else and
stores the difference between these values in dly moret1. If not it executes the commands between else and endif. The
command `PUSH dly #0` uses # to indicate that the 0 is a literal rather than the index of a dly. Thus in this case the
dly moret1 would be set to 0. The remaining `POP` commands empty the stack.
### Observe Channel
The only new thing in the observe channel section is the inclusion of `DLY GATE_IDLE` commands between iniobs and
finobs. This is a lower level command to set up a dly instead of using the use_pwxdly and pwxdly macros. Gate_idle is a
gate like pwrh, but gate_idle indicates that no power is sent to amplifiers. `DLY GATE_IDLE DLY_T1` means to wait for a
length of time specified by dly t1 with no RF power. In this case this performs the indirect evolution which contains no
pulses on the observe channel. The observe channel will also wait with no pulses for dly mix during the mixing period
and for dly moret1 after the end of the sampling.
### Decoupling Channel
In the decoupling channel section `USE PERIOD` was used for the sampling period decoupling in justcp. Here it is also
used to set up a CW period that is used during the mixing time and TPPM decoupling which is used during the evolution
time. This section also demonstrates that the same period set up with use (and this applies to other things like pls or
dly) can be used more than once in the pulse sequence. The evolve period is used both during the indirect evolution and
during the moret1 stage at the end of the sequence. The period will use the same parameters as set up by the use_period
macro in each place that it is used.
### Experiment Macro
The following macro can be used to run this DARR experiment:
```
macarg submac
dflt submac,setup, 'Enter submacro:'
goto .&submac
mexit

.setup
chn 21
ex &macro$
gosub .general
gosub .c13params
gosub .h1params
gosub .mixdarr
gosub .darrparams
mexit

.mixdarr
pwx 2 mix2 11
d mix 80
mexit

.general
suacq 30.0,768,4.0,70.0,40,0,2.82
; dw,size,rd,gain,na,ndly,p8
mexit

.c13params
; setup chn 1 c13 ======================
suchn 1,c13,12.0,100,100,83
; chn,nuc,freq,pwrh,pwrl,pwxh
supls 1,cppls,0,2.5
sudly 1,cpdly,0,1.5
; chn,nam,pwx,dly
supwxval 1,cpdly,ramp,38.5,48.5,,,64
pwx 1 flip 83
supls 1,flipup,>,3
supls 1,flipdn,>,3
pwxex 1 *&macro$
; calls submacro .pwxex1
mexit

.h1params
; setup chn 2 proton ===================
suchn 2,h1,1.6,100,100,100
; setup pulses
supls 2,cppls,100
supwxval 2,cpdly,ramp,75,75,,,64
pwx 2 cwdec 100
supls 2,flipup,>
supls 2,flipdn,>
super 2,sample,on,*,100,5.0
supsxval 2,sample,tppm,16,0.0
super 2,evolve,on,*,83,5.6
supsxval 2,evolve,tppm,18,0
psxex 2 *&macro$
pwxex 2 *&macro$
; calls submacro .psxex2
mexit

.darrparams
namd		16
namd /blk	2
amd /blk 11
ppmd dec        1
ppmd cpdly2	2
ppmd cppls2      13
ppmd cpdly1   1133
ppmd flipup1     2
ppmd flipdn1     1111 3333 2222 4444
amd             2442 4224 3113 1331
ppmd /blk cpdly1 14

mexit

.run2ddarr
macarg submac recnr darr pt1 sz2
msg 'set globals %sample and %mas'
dflt recnr,100,"which record?"
dflt darr,4,"DARR mixing (ms)"
dflt pt1,160,"indirect dwell time (us)"
dflt sz2,128,"indirect dim. size"

d mix &darr

allmd &recnr 2 > > &pt1 &sz2
gomd &recnr
mexit

.pwxex1
supwxex 1,cpdly,ramp
mexit

.psxex2
supsxex 2,sample,tppm
supsxex 2,evolve,tppm
mexit

.pwxex2
supwxex 2,cpdly,ramp
mexit
```
There are a few new things in this macro. `NAMD`, `AMD`, and `PPMD` are all used with the /BLK qualifier. This sets up
the phase cycle for blocks of acquisition. In this case the 2 blocks set by `NAMD /BLK` are the same as the two segments
set for the indirect dimension hypercomplex acquisition in the pulse program. `AMD /BLK` is used to set the additional
receiver phase cycling used for each block and `PPMD /BLK` is used to set additional phase cycling for the blocks. In
this case additional phase cycling is set for the CP contact on the observe channel. This pulse is the one that
generates the signal that is encoded by the indirect evolution. The change in phase of this pulse is what generates the
sine and cosine parts of the indirect acquisition.

There is also a run2ddarr submacro which is used to actually acquire a two dimensional DARR spectrum. This submacro
needs information about the spectrum such as which record to store the data in as well as the size and dwell time of the
indirect dimension. In this case it also sets up the DARR mixing time. The allmd macro is used to allocate a blocked
record to hold the data. It also takes care of some other tasks like setting the value of loop size$2 and dly step$2 so
that the proper indirect dimension evolution occurs. The gomd macro handles the actual multi-dimensional acquisition of
the spectrum.

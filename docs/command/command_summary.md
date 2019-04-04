# Command Summary
## Acquisition
Command | Description
------- | -----------
[ABORT](full_command.md#abort) | Abort acquisition
[ASIG](full_command.md#asig) | Acknowledge signal
[CALIB](full_command.md#calib) | Determine data buffer amplitudes and phases
[DG](full_command.md#dg) | Start acquisition with delay shots
[GAV](full_command.md#gav) | Get data from averager
[GO](full_command.md#go) | Start or resume acquisition
[IDNA](full_command.md#idna) | Set acquisition buffer identification fields
[LPA](full_command.md#lpa) | List acquisition buffer parameters
[NABLK](full_command.md#nablk) | Set number of acquisition blocks
[NDSP](full_command.md#ndsp) | Set number of shots between display update
[NG](full_command.md#ng) | Start or resume acquisition with dummy scans
[QUIT](full_command.md#quit) | Quit acquisition
[SAV](full_command.md#sav) | Save data and parameters to averager
[SG](full_command.md#sg) | Start acquisition without accumulation
[TITLEA](full_command.md#titlea) | Set acquisition title
[WAIT](full_command.md#wait) | Wait during acquisition
[ZERA](full_command.md#zera) | Zero acquisition buffer and shot counter
[ZG](full_command.md#zg) | Start acquisition
[ZOA](full_command.md#zoa) | Zoom on acquisition display

## Apodization
Command | Description
------- | -----------
[CD](full_command.md#cd) | Perform convolution difference apodization
[COSSQ](full_command.md#cossq) | Perform cosine squared apodization
[EM](full_command.md#em) | Exponential multiply FID
[GM](full_command.md#gm) | Gaussian multiply FID
[LB](full_command.md#lb) | Set line broadening factor
[SINEB](full_command.md#sineb) | Perform Sine-bell apodization
[TM](full_command.md#tm) | Perform trapezoidal multiplication apodization

## Arguments
Command | Description
------- | -----------
[CATGBL](full_command.md#catgbl) | List catalog of global variables
[CATLCL](full_command.md#catlcl) | List catalog of local variables
[CATSYM](full_command.md#catsym) | List catalog of symbols
[DFLGBL](full_command.md#dflgbl) | Define global argument with default value
[DFLLCL](full_command.md#dfllcl) | Define local argument with default value
[DFLT](full_command.md#dflt) | Prompt for local variable with default
[DFNGBL](full_command.md#dfngbl) | Define global argument
[DFNLCL](full_command.md#dfnlcl) | Define local argument
[DFNSYM](full_command.md#dfnsym) | Define symbol
[GBLARG](full_command.md#gblarg) | Set value of global argument
[GBLDL](full_command.md#gbldl) | Delete global argument
[KEYARG](full_command.md#keyarg) | Declare names of macro keyword arguments
[LCLARG](full_command.md#lclarg) | Set local argument value
[LCLDL](full_command.md#lcldl) | Delete local argument
[MACARG](full_command.md#macarg) | Redefine names of positional macro arguments
[REMGBL](full_command.md#remgbl) | Remove global arguments
[REMLCL](full_command.md#remlcl) | Remove local arguments
[REMSYM](full_command.md#remsym) | Remove symbols
[RSTGBL](full_command.md#rstgbl) | Restore global arguments from file
[RTNARG](full_command.md#rtnarg) | Renames return arguments
[SAVGBL](full_command.md#savgbl) | Save global arguments to file

## Baseline
Command | Description
------- | -----------
[BC](full_command.md#bc) | Baseline correct FID
[BF](full_command.md#bf) | Baseline fix spectrum
[MEDBF](full_command.md#medbf) | Median baseline fix spectrum
[SPLN](full_command.md#spln) | Spline baseline fix spectrum

## Blocked Records
Command | Description
------- | -----------
[ALLB](full_command.md#allb) | Allocate a blocked record
[ALLCPY](full_command.md#allcpy) | Allocate a copy of a blocked record
[CVTMD](full_command.md#cvtmd) | Set modes for blocked record index conversion
[CVTSZ](full_command.md#cvtsz) | Set sizes for blocked record index conversion
[DCDB](full_command.md#dcdb) | Convert block indices to values
[DCDBP](full_command.md#dcdbp) | Convert linear block index to vector indices
[DIRB](full_command.md#dirb) | Set blocked record access sequence
[ECDB](full_command.md#ecdb) | Convert dimension values to linear block index
[ECDBP](full_command.md#ecdbp) | Convert vector indices to linear block index
[PARB](full_command.md#parb) | Set blocked record parameters
[PTRB](full_command.md#ptrb) | Set read and write blocked record pointers
[SIZEB](full_command.md#sizeb) | Displays size of blocked record

## Buffer Arithmetic
Command | Description
------- | -----------
[ADDV](full_command.md#addv) | Add buffers
[CMUL](full_command.md#cmul) | Multiply buffer by complex constant
[CMULV](full_command.md#cmulv) | Complex multiply two buffers
[CONJG](full_command.md#conjg) | Complex conjugate data
[CPXV](full_command.md#cpxv) | Complex merge two buffers
[GMV](full_command.md#gmv) | Calculate geometric mean
[MAXV](full_command.md#maxv) | Calculate maximum
[MINV](full_command.md#minv) | Calculates minimum
[MOVV](full_command.md#movv) | Move buffer
[MULV](full_command.md#mulv) | Multiply buffer
[NEG](full_command.md#neg) | Negates buffer
[PSUBV](full_command.md#psubv) | Subtract polar buffers
[SUBV](full_command.md#subv) | Subtract data buffers
[SWAPV](full_command.md#swapv) | Swap data buffers
[WAVV](full_command.md#wavv) | Perform weighted addition of buffers

## Calculator
Command | Description
------- | -----------
[CALC](full_command.md#calc) | Perform floating point arithmetic and logical calculations
[CALCI](full_command.md#calci) | Perform integer arithmetic, logical, and bitwise calculations

## Contours
Command | Description
------- | -----------
[CONLIM](full_command.md#conlim) | Set contour plot height limits
[CONMD](full_command.md#conmd) | Set contour plotting mode
[NCON](full_command.md#ncon) | Set number of contour levels
[ZO2DC](full_command.md#zo2dc) | Zoom on 2D contour display

## Control Flow
Command | Description
------- | -----------
[ASKYN](full_command.md#askyn) | Ask yes or no
[BRKDO](full_command.md#brkdo) | Break out of a macro `DO` loop
[CASE](full_command.md#case) | Process `CASE` clause of `SEL` block
[DO](full_command.md#do) | Begin macro `DO` loop
[ELSTST](full_command.md#elstst) | Separate the code blocks after a `TST` check
[ENDDO](full_command.md#enddo) | End a macro `DO` loop
[ENDSEL](full_command.md#endsel) | End a macro `SEL` block
[ENDTST](full_command.md#endtst) | End a macro `TST` block
[GOSUB](full_command.md#gosub) | Perform call within macro
[GOTO](full_command.md#goto) | Go to statement label in macro
[GOTST](full_command.md#gotst) | Perform a conditional jump within a macro based on a test
[IFCND](full_command.md#ifcnd) | Branch on condition flag
[IFEQ](full_command.md#ifeq) | Branch on equal
[IFGBL](full_command.md#ifgbl) | Check for global argument and branch
[IFLCL](full_command.md#iflcl) | Check for local argument and branch
[IFMAC](full_command.md#ifmac) | Check for macro and branch
[IFREC](full_command.md#ifrec) | Check for record and branch
[MEXIT](full_command.md#mexit) | Exit macro
[NXTDO](full_command.md#nxtdo) | Cycle macro `DO` loop
[ONERR](full_command.md#onerr) | Set macro error handler
[RPTDO](full_command.md#rptdo) | Repeat iteration of macro `DO` loop
[SEL](full_command.md#sel) | Begin macro `SEL` block
[TST](full_command.md#tst) | Conditionally execute a block of commands based on a test

## Data Analysis
Command | Description
------- | -----------
[IBOX](full_command.md#ibox) | Set volume parameters for nD volume integration
[INTRG](full_command.md#intrg) | Integrate region of spectrum
[IXVAL](full_command.md#ixval) | Convert from unit value to point index
[LPK](full_command.md#lpk) | List Peaks
[LPK2D](full_command.md#lpk2d) | List peaks in two dimensions
[LW](full_command.md#lw) | Calculate line width
[MNMX](full_command.md#mnmx) | Calculate minimum and maximum in buffer region
[PP](full_command.md#pp) | Interactive peak picking
[RMS](full_command.md#rms) | Calculate root-mean-square value of data
[TH](full_command.md#th) | Set threshold for peak selection
[XVAL](full_command.md#xval) | Convert from point index to unit value

## Data Manipulation
Command | Description
------- | -----------
[BINCP](full_command.md#bincp) | Perform binary pulse phase correction
[CNVFL](full_command.md#cnvfl) | Convolution filter spectrum
[DEPAKE](full_command.md#depake) | Perform depaking of powder pattern spectrum
[DF](full_command.md#df) | Differentiate data
[FOLD](full_command.md#fold) | Fold data buffer
[INTG](full_command.md#intg) | Compute integral of spectrum
[LPB](full_command.md#lpb) | Perform backward linear prediction on FID
[LPC](full_command.md#lpc) | Perform long pulse phase and amplitude correction
[LPCA](full_command.md#lpca) | Perform long pulse amplitude correction
[LPCP](full_command.md#lpcp) | Perform long pulse phase correction
[LPF](full_command.md#lpf) | Perform forward linear prediction on FID
[PROF](full_command.md#prof) | Calculate profile of 2D data
[PROFB](full_command.md#profb) | Calculate profile of blocked record along a dimension
[PROJ](full_command.md#proj) | Calculate projection of 2D data
[PROJB](full_command.md#projb) | Calculate projection of blocked record along a dimension
[QC](full_command.md#qc) | Perform software quadrature phase correction
[ROT](full_command.md#rot) | Rotate spectrum
[ROTP](full_command.md#rotp) | Rotate spectrum
[SETV](full_command.md#setv) | Set data values between limits
[SETVP](full_command.md#setvp) | Set data values for specified points
[SHFT](full_command.md#shft) | Shift data
[SHFTP](full_command.md#shftp) | Shift data by points
[TILT](full_command.md#tilt) | Tilt blocked record
[TWIST](full_command.md#twist) | Twist blocked record
[UNFOLD](full_command.md#unfold) | Unfold data buffer
[VAL](full_command.md#val) | Set data value
[WAVB](full_command.md#wavb) | Perform weighted average of blocked record
[XT](full_command.md#xt) | Extract data within specified limits
[XTP](full_command.md#xtp) | Extract data for points
[ZER](full_command.md#zer) | Zero visible processing buffer
[ZF](full_command.md#zf) | Zero fill visible processing buffer

## Data Storage
Command | Description
------- | -----------
[ARV](full_command.md#arv) | Return archive information
[CAT](full_command.md#cat) | List catalog of records
[CATARV](full_command.md#catarv) | List catalog of archives
[CLSARV](full_command.md#clsarv) | Close archive
[CPY](full_command.md#cpy) | Copy record
[CRTARV](full_command.md#crtarv) | Create archive
[DCDREC](full_command.md#dcdrec) | Convert record number into archive and archive record index
[DL](full_command.md#dl) | Delete records
[ECDREC](full_command.md#ecdrec) | Encode archive index
[GA](full_command.md#ga) | Get archive record data
[GB](full_command.md#gb) | Get blocked record data
[GS](full_command.md#gs) | Get data from scratch record
[IDN](full_command.md#idn) | Set processing buffer identification fields
[MOV](full_command.md#mov) | Move record
[OPNARV](full_command.md#opnarv) | Open archive
[PTRA](full_command.md#ptra) | Set read and write archive pointers
[RDARV](full_command.md#rdarv) | Read archive name
[SA](full_command.md#sa) | Save data to archive record
[SAVARV](full_command.md#savarv) | Save archive
[SB](full_command.md#sb) | Save data to blocked record
[SP](full_command.md#sp) | Display archive space information
[SQZ](full_command.md#sqz) | Squeeze archive (de-allocate unused space)
[SS](full_command.md#ss) | Save data to scratch record
[TITLE](full_command.md#title) | Set processing buffer title
[UPDARV](full_command.md#updarv) | Update archive
[USER](full_command.md#user) | Set user name

## Data Transforms
Command | Description
------- | -----------
[FT](full_command.md#ft) | Fourier transform FID
[HILB](full_command.md#hilb) | Perform Hilbert transform on spectrum
[HILBZ](full_command.md#hilbz) | Perform Hilbert transform on zero-filled spectrum
[IFT](full_command.md#ift) | Inverse Fourier transform spectrum
[MAG](full_command.md#mag) | Calculate magnitude of data
[POLAR](full_command.md#polar) | Convert buffer to polar coordinates

## Display Control
Command | Description
------- | -----------
[AI](full_command.md#ai) | Scale to absolute intensity
[AK](full_command.md#ak) | Set absolute scale factor
[BUF](full_command.md#buf) | View real or imaginary processing buffer
[BUFA](full_command.md#bufa) | View real or imaginary acquisition buffer
[COLOR](full_command.md#color) | Set data display colors
[CRS](full_command.md#crs) | Set cursor positions
[CRSA](full_command.md#crsa) | Set acquisition cursor positions
[LIM](full_command.md#lim) | Set processing buffer display limits
[LIMA](full_command.md#lima) | Set acquisition buffer display limits
[LIMB](full_command.md#limb) | Set blocked record display limits
[NDEC](full_command.md#ndec) | Set number of decimal places
[NORM](full_command.md#norm) | Set scale to normalize display
[SC](full_command.md#sc) | Scale data
[SETIDN](full_command.md#setidn) | Set identification values
[UNIT](full_command.md#unit) | Set units
[VIEW](full_command.md#view) | Set display source
[WNDLIM](full_command.md#wndlim) | Set processing view vertical window limits
[WNDLIMA](full_command.md#wndlima) | Set acquisition view vertical window limits
[ZO](full_command.md#zo) | Zoom
[ZO2D](full_command.md#zo2d) | Zoom on 2D data set

## Experiment
Command | Description
------- | -----------
[CHN](full_command.md#chn) | Map logical and physical channels to one another
[DW](full_command.md#dw) | Set dwell time for data sampling during acquisition
[EX](full_command.md#ex) | Load a pulse program experiment
[FLAG](full_command.md#flag) | Set pulse program flag on or off
[FLF](full_command.md#flf) | Set filter factor
[GAIN](full_command.md#gain) | Set receiver gain
[LI](full_command.md#li) | Increment pulse programmer loop value
[LOOP](full_command.md#loop) | Set or increment pulse program loop counter
[LS](full_command.md#ls) | Set pulse programmer loop value
[NA](full_command.md#na) | Set number of shots to acquire
[NCHN](full_command.md#nchn) | Set number of channels
[NDLY](full_command.md#ndly) | Set number of dummy scans
[NUC](full_command.md#nuc) | Set synthesizer nucleus
[NWAIT](full_command.md#nwait) | Set number of shots to wait
[PPEX](full_command.md#ppex) | Load a pulse program experiment
[PPFLG](full_command.md#ppflg) | Set state of pulse program flag
[PWR](full_command.md#pwr) | Set transmitter coarse power level
[RCVMIX](full_command.md#rcvmix) | Set receiver quadrature mixing
[RCVOFF](full_command.md#rcvoff) | Set receiver offset
[RD](full_command.md#rd) | Set recycle delay
[SIZE](full_command.md#size) | Set acquisition size
[SW](full_command.md#sw) | Set sweep width

## File IO
Command | Description
------- | -----------
[APNFIL](full_command.md#apnfil) | Append text to file
[CLSRD](full_command.md#clsrd) | Close file opened for read
[CLSWRT](full_command.md#clswrt) | Close file which has been opened for writing
[CRTFIL](full_command.md#crtfil) | Create text file
[DLTFIL](full_command.md#dltfil) | Delete file
[EDTFIL](full_command.md#edtfil) | Edit text file
[LSTFIL](full_command.md#lstfil) | List contents of a text file
[MRGFS](full_command.md#mrgfs) | Merge default file with file
[OPNRD](full_command.md#opnrd) | Open file for reading
[OPNWRT](full_command.md#opnwrt) | Open file stream for writing
[RDWRT](full_command.md#rdwrt) | Read line from file
[RWDRD](full_command.md#rwdrd) | Rewind file opened by `OPNRD`
[RWDWRT](full_command.md#rwdwrt) | Rewind file opened by `OPNWRT`
[WPK](full_command.md#wpk) | Write peaks in current display to `WRT` file
[WPK2D](full_command.md#wpk2d) | Write 2D peaks to `WRT` file
[WRT](full_command.md#wrt) | Write line to file opened by `OPNWRT`

## Foreign
Command | Description
------- | -----------
[BRUK](full_command.md#bruk) | Convert BRUKER FID to complex FID
[CLSEXP](full_command.md#clsexp) | Close export file
[CLSIMP](full_command.md#clsimp) | Close import file
[EXP](full_command.md#exp) | Export buffer to foreign format
[EXP1D](full_command.md#exp1d) | Export 1D data to foreign format
[EXP2D](full_command.md#exp2d) | Export 2D data to foreign format
[EXP3D](full_command.md#exp3d) | Export 3D data to foreign format
[IMP](full_command.md#imp) | Import data from foreign format
[IMP1D](full_command.md#imp1d) | Import data from foreign format
[IMP2D](full_command.md#imp2d) | Import data from foreign format
[IMP3D](full_command.md#imp3d) | Import data from foreign format
[OPNEXP](full_command.md#opnexp) | Open export file
[OPNIMP](full_command.md#opnimp) | Open import file
[TPPI](full_command.md#tppi) | Convert TPPI-format FID to complex FID

## Frequency Control
Command | Description
------- | -----------
[CATNUC](full_command.md#catnuc) | List catalog of nuclei
[F](full_command.md#f) | Set synthesizer offset frequency
[FSYS](full_command.md#fsys) | Set spectrometer system frequency
[GREF](full_command.md#gref) | Restore processing buffer reference from nucleus table
[GREFA](full_command.md#grefa) | Restore acquisition buffer reference from nucleus table
[NUCD](full_command.md#nucd) | Define nucleus table entry
[NUCDL](full_command.md#nucdl) | Delete nucleus table entry
[OFF](full_command.md#off) | Set offset from reference frequency
[OFFA](full_command.md#offa) | Set offset from reference frequency
[SREF](full_command.md#sref) | Save processing buffer reference to nucleus table
[SREFA](full_command.md#srefa) | Save acquisition buffer reference to nucleus table

## Hardware
Command | Description
------- | -----------
[MASCMD](full_command.md#mascmd) | Send command to MAS controller
[RGPIB](full_command.md#rgpib) | Read string from GPIB device
[RPPSB](full_command.md#rppsb) | Read data byte from pulse programmer spectrometer bus
[RRKC](full_command.md#rrkc) | Read data from an RKC device
[RSB](full_command.md#rsb) | Read data byte from spectrometer bus
[WGPIB](full_command.md#wgpib) | Write line to GPIB device
[WPPSB](full_command.md#wppsb) | Write data byte to pulse programmer spectrometer bus
[WRKC](full_command.md#wrkc) | Write data byte to RKC device
[WRRI](full_command.md#wrri) | Write command line to RRI device and read response
[WSB](full_command.md#wsb) | Write data byte to spectrometer bus
[WTRM](full_command.md#wtrm) | Write command line to terminal and read response

## Heater
Command | Description
------- | -----------
[HTR](full_command.md#htr) | Enable or disable probe heater
[HTRSTS](full_command.md#htrsts) | Return probe heater status
[RSTHTR](full_command.md#rsthtr) | Restore heater values from file
[SAVHTR](full_command.md#savhtr) | Save heater values to file
[TALARM](full_command.md#talarm) | Set temperature for probe heater alarm
[TSET](full_command.md#tset) | Set heater set-point temperature
[TVAL](full_command.md#tval) | Show heater temperature
[WTSET](full_command.md#wtset) | Wait for heater to stabilize at setpoint

## Lists
Command | Description
------- | -----------
[APNLST](full_command.md#apnlst) | Append values to list
[CATLST](full_command.md#catlst) | List catalog of lists
[CRTLST](full_command.md#crtlst) | Create list
[DFNLST](full_command.md#dfnlst) | Define list value
[DLTLST](full_command.md#dltlst) | Delete list
[EDTLST](full_command.md#edtlst) | Edit list
[INSLST](full_command.md#inslst) | Insert value into list
[LSTDP](full_command.md#lstdp) | Define list from display
[LSTLST](full_command.md#lstlst) | List contents of a list
[POPLST](full_command.md#poplst) | Pop a value from a list
[PRGLST](full_command.md#prglst) | Purge list
[PSHLST](full_command.md#pshlst) | Push a value to a list
[RDLST](full_command.md#rdlst) | Read list from file
[REMLST](full_command.md#remlst) | Remove list value
[RSTLST](full_command.md#rstlst) | Restore lists from file
[SAVLST](full_command.md#savlst) | Save lists to file
[SIZLST](full_command.md#sizlst) | Display size of list
[WRTLST](full_command.md#wrtlst) | Write list to file

## Lock
Command | Description
------- | -----------
[GAINL](full_command.md#gainl) | Set lock receiver gain
[LCK](full_command.md#lck) | Enable or disable lock feedback loop
[LCKCTL](full_command.md#lckctl) | Open lock control pop up menu
[LCKMTR](full_command.md#lckmtr) | Enable lock meter
[LCKVAL](full_command.md#lckval) | Read lock value
[PIDL](full_command.md#pidl) | Set lock PID gain factors
[POSL](full_command.md#posl) | Set lock channel center position
[PWRL](full_command.md#pwrl) | Set lock channel power level
[RSTLCK](full_command.md#rstlck) | Restore lock values from file
[SAVLCK](full_command.md#savlck) | Save lock values to file
[SWL](full_command.md#swl) | Set lock channel sweep width
[SWP](full_command.md#swp) | Enable or disable lock sweep
[TCL](full_command.md#tcl) | Set lock channel time constant

## Macros
Command | Description
------- | -----------
[APNMAC](full_command.md#apnmac) | Append text to macro
[CATMAC](full_command.md#catmac) | List catalog of macros
[CPYMAC](full_command.md#cpymac) | Copy macro
[CRTMAC](full_command.md#crtmac) | Create macro
[DFNMAC](full_command.md#dfnmac) | Define macro table entry
[DLTMAC](full_command.md#dltmac) | Delete list
[EDTMAC](full_command.md#edtmac) | Edit macro
[LSTMAC](full_command.md#lstmac) | List contents of a macro
[MAPN](full_command.md#mapn) | Append text to macro
[MCPY](full_command.md#mcpy) | Copy macro
[MD](full_command.md#md) | Define macro
[MDL](full_command.md#mdl) | Delete macro
[ME](full_command.md#me) | Edit macro
[ML](full_command.md#ml) | List contents of a macro
[MRN](full_command.md#mrn) | Rename macro
[REMMAC](full_command.md#remmac) | Remove macro table entry
[RENMAC](full_command.md#renmac) | Rename macro

## Misc.
Command | Description
------- | -----------
[CND](full_command.md#cnd) | Set condition flag
[CVTUNIT](full_command.md#cvtunit) | Convert a value between units
[DATE](full_command.md#date) | Print the current date and time as an informational message
[DBSZ](full_command.md#dbsz) | Set processing buffer partitioning
[DCL](full_command.md#dcl) | Execute a shell command in background
[EXIT](full_command.md#exit) | Exit program
[INFLVL](full_command.md#inflvl) | Set info level
[LOG](full_command.md#log) | Write line to log
[LP](full_command.md#lp) | List processing buffer parameters
[MO](full_command.md#mo) | Exit program
[MSG](full_command.md#msg) | Write message line to console
[NOP](full_command.md#nop) | Null operation
[PROG](full_command.md#prog) | Identify program
[PRTARG](full_command.md#prtarg) | Print arguments
[RDSTR](full_command.md#rdstr) | Read tokens from a string
[RSTBUF](full_command.md#rstbuf) | Restore buffer values from file
[SAVBUF](full_command.md#savbuf) | Save buffer value to file
[SAVLOG](full_command.md#savlog) | Save logging to file
[SET](full_command.md#set) | Set system state
[SHELL](full_command.md#shell) | Spawn shell
[SHOW](full_command.md#show) | Show information
[STR](full_command.md#str) | Perform string operation
[WTTIM](full_command.md#wttim) | Wait for specified number of seconds

## Phasing
Command | Description
------- | -----------
[PC](full_command.md#pc) | Incremental phase correction
[PH](full_command.md#ph) | Interactive phase correction
[PS](full_command.md#ps) | Set phase
[TP](full_command.md#tp) | Show phase correction values

## Plotting
Command | Description
------- | -----------
[CLSPLT](full_command.md#clsplt) | Close plotter stream and print
[OPNPLT](full_command.md#opnplt) | Open plot stream 	
[PEN](full_command.md#pen) | Select plot pen
[PGSIZE](full_command.md#pgsize) | Set page size for plot
[PLDEV](full_command.md#pldev) | Select plotting device
[PLFIL](full_command.md#plfil) | Set plot file
[PLOT](full_command.md#plot) | Plot current 1D display
[PLOTC](full_command.md#plotc) | Plot 2D contours
[PLSIZE](full_command.md#plsize) | Set plot size
[STK](full_command.md#stk) | Add to plot stream stack
[STKOFF](full_command.md#stkoff) | Set stack plot offset
[WWASH](full_command.md#wwash) | Set state of plot whitewash flag

## Printing
Command | Description
------- | -----------
[LPDEV](full_command.md#lpdev) | Select text printer device
[LPFIL](full_command.md#lpfil) | Set text printer file

## Pulse Control
Command | Description
------- | -----------
[AMD](full_command.md#amd) | Set acquisition modes
[D](full_command.md#d) | Set pulse programmer delay
[DLY](full_command.md#dly) | Set pulse programmer delay
[FMX](full_command.md#fmx) | Set frequency modulation value
[FMXEX](full_command.md#fmxex) | Load frequency modulation program
[NAMD](full_command.md#namd) | Set number of acquisition modes
[P](full_command.md#p) | Set pulse length
[PLS](full_command.md#pls) | Set pulse length
[PPMD](full_command.md#ppmd) | Set pulse program phase mode
[PSX](full_command.md#psx) | Set transmitter phase
[PSXEX](full_command.md#psxex) | Load transmitter phase program from PAM memory.
[PWX](full_command.md#pwx) | Set transmitter fine power level
[PWXEX](full_command.md#pwxex) | Load power program

## Pulse Program Symbols
Command | Description
------- | -----------
[CATPPS](full_command.md#catpps) | List catalog of PP symbols
[DFNPPS](full_command.md#dfnpps) | Define pulse programmer symbol table entry
[RDPPS](full_command.md#rdpps) | Read PP symbol
[RDPPSNAM](full_command.md#rdppsnam) | Read PP symbol name
[REMPPS](full_command.md#rempps) | Remove pulse programmer symbols

## Shim
Command | Description
------- | -----------
[AUTOZ](full_command.md#autoz) | Set automatic Z shim parameters
[RSTSHM](full_command.md#rstshm) | Restore shim values from file
[SAVSHM](full_command.md#savshm) | Save shim values to file
[SHM](full_command.md#shm) | Set shim value
[SHMCTL](full_command.md#shmctl) | Open interactive shim controls

## Signal Generation
Command | Description
------- | -----------
[ECHO](full_command.md#echo) | Rearrange buffer to simulate echo data
[GENCS](full_command.md#gencs) | Generate complex sine wave
[GENPWDR](full_command.md#genpwdr) | Generate complex powder pattern
[NOISE](full_command.md#noise) | Generate complex random noise
[UNECHO](full_command.md#unecho) | Rearrange buffer to simulate FID from echo

## Tables
Command | Description
------- | -----------
[CATTBL](full_command.md#cattbl) | List catalog of name tables
[CRTTBL](full_command.md#crttbl) | Create name table
[DFLTBL](full_command.md#dfltbl) | Define name table argument with default value
[DFNTBL](full_command.md#dfntbl) | Define name table argument
[DLTTBL](full_command.md#dlttbl) | Delete name table
[PRGTBL](full_command.md#prgtbl) | Purge name table
[RDTBL](full_command.md#rdtbl) | Read name table values from file
[REMTBL](full_command.md#remtbl) | Remove name table entries
[RSTTBL](full_command.md#rsttbl) | Restore name tables from file
[SAVTBL](full_command.md#savtbl) | Save name tables to file
[SIZTBL](full_command.md#siztbl) | Display size of name table
[WRTTBL](full_command.md#wrttbl) | Write name table to file

## Waveform
Command | Description
------- | -----------
[WRF](full_command.md#wrf) | Set waveform reference values
[WRFEX](full_command.md#wrfex) | Load waveform RF program
[WWF](full_command.md#wwf) | Set waveform values
[WWFEX](full_command.md#wwfex) | Load waveform program


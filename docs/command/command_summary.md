# Acquisition
Command | Description
------- | -----------
[ABORT](full_command#abort) | Abort acquisition
[ASIG](full_command#asig) | Acknowledge signal
[CALIB](full_command#calib) | Determine data buffer amplitudes and phases
[DG](full_command#dg) | Start acquisition with delay shots
[GAV](full_command#gav) | Get data from averager
[GO](full_command#go) | Start or resume acquisition
[IDNA](full_command#idna) | Set acquisition buffer identification fields
[LPA](full_command#lpa) | List acquisition buffer parameters
[NABLK](full_command#nablk) | Set number of acquisition blocks
[NDSP](full_command#ndsp) | Set number of shots between display update
[NG](full_command#ng) | Start or resume acquisition with dummy scans
[QUIT](full_command#quit) | Quit acquisition
[SAV](full_command#sav) | Save data and parameters to averager
[SG](full_command#sg) | Start acquisition without accumulation
[TITLEA](full_command#titlea) | Set acquisition title
[WAIT](full_command#wait) | Wait during acquisition
[ZERA](full_command#zera) | Zero acquisition buffer and shot counter
[ZG](full_command#zg) | Start acquisition
[ZOA](full_command#zoa) | Zoom on acquisition display

# Apodization
Command | Description
------- | -----------
[CD](full_command#cd) | Perform convolution difference apodization
[COSSQ](full_command#cossq) | Perform cosine squared apodization
[EM](full_command#em) | Exponential multiply FID
[GM](full_command#gm) | Gaussian multiply FID
[LB](full_command#lb) | Set line broadening factor
[SINEB](full_command#sineb) | Perform Sine-bell apodization
[TM](full_command#tm) | Perform trapezoidal multiplication apodization

# Arguments
Command | Description
------- | -----------
[CATGBL](full_command#catgbl) | List catalog of global variables
[CATLCL](full_command#catlcl) | List catalog of local variables
[CATSYM](full_command#catsym) | List catalog of symbols
[DFLGBL](full_command#dflgbl) | Define global argument with default value
[DFLLCL](full_command#dfllcl) | Define local argument with default value
[DFLT](full_command#dflt) | Prompt for local variable with default
[DFNGBL](full_command#dfngbl) | Define global argument
[DFNLCL](full_command#dfnlcl) | Define local argument
[DFNSYM](full_command#dfnsym) | Define symbol
[GBLARG](full_command#gblarg) | Set value of global argument
[GBLDL](full_command#gbldl) | Delete global argument
[KEYARG](full_command#keyarg) | Declare names of macro keyword arguments
[LCLARG](full_command#lclarg) | Set local argument value
[LCLDL](full_command#lcldl) | Delete local argument
[MACARG](full_command#macarg) | Redefine names of positional macro arguments
[REMGBL](full_command#remgbl) | Remove global arguments
[REMLCL](full_command#remlcl) | Remove local arguments
[REMSYM](full_command#remsym) | Remove symbols
[RSTGBL](full_command#rstgbl) | Restore global arguments from file
[RTNARG](full_command#rtnarg) | Renames return arguments
[SAVGBL](full_command#savgbl) | Save global arguments to file

# Baseline
Command | Description
------- | -----------
[BC](full_command#bc) | Baseline correct FID
[BF](full_command#bf) | Baseline fix spectrum
[MEDBF](full_command#medbf) | Median baseline fix spectrum
[SPLN](full_command#spln) | Spline baseline fix spectrum

# Blocked Records
Command | Description
------- | -----------
[ALLB](full_command#allb) | Allocate a blocked record
[ALLCPY](full_command#allcpy) | Allocate a copy of a blocked record
[CVTMD](full_command#cvtmd) | Set modes for blocked record index conversion
[CVTSZ](full_command#cvtsz) | Set sizes for blocked record index conversion
[DCDB](full_command#dcdb) | Convert block indices to values
[DCDBP](full_command#dcdbp) | Convert linear block index to vector indices
[DIRB](full_command#dirb) | Set blocked record access sequence
[ECDB](full_command#ecdb) | Convert dimension values to linear block index
[ECDBP](full_command#ecdbp) | Convert vector indices to linear block index
[PARB](full_command#parb) | Set blocked record parameters
[PTRB](full_command#ptrb) | Set read and write blocked record pointers
[SIZEB](full_command#sizeb) | Displays size of blocked record

# Buffer Arithmetic
Command | Description
------- | -----------
[ADDV](full_command#addv) | Add buffers
[CMUL](full_command#cmul) | Multiply buffer by complex constant
[CMULV](full_command#cmulv) | Complex multiply two buffers
[CONJG](full_command#conjg) | Complex conjugate data
[CPXV](full_command#cpxv) | Complex merge two buffers
[GMV](full_command#gmv) | Calculate geometric mean
[MAXV](full_command#maxv) | Calculate maximum
[MINV](full_command#minv) | Calculates minimum
[MOVV](full_command#movv) | Move buffer
[MULV](full_command#mulv) | Multiply buffer
[NEG](full_command#neg) | Negates buffer
[PSUBV](full_command#psubv) | Subtract polar buffers
[SUBV](full_command#subv) | Subtract data buffers
[SWAPV](full_command#swapv) | Swap data buffers
[WAVV](full_command#wavv) | Perform weighted addition of buffers

# Calculator
Command | Description
------- | -----------
[CALC](full_command#calc) | Perform floating point arithmetic and logical calculations
[CALCI](full_command#calci) | Perform integer arithmetic, logical, and bitwise calculations

# Contours
Command | Description
------- | -----------
[CONLIM](full_command#conlim) | Set contour plot height limits
[CONMD](full_command#conmd) | Set contour plotting mode
[NCON](full_command#ncon) | Set number of contour levels
[ZO2DC](full_command#zo2dc) | Zoom on 2D contour display

# Control Flow
Command | Description
------- | -----------
[ASKYN](full_command#askyn) | Ask yes or no
[BRKDO](full_command#brkdo) | Break out of a macro `DO` loop
[CASE](full_command#case) | Process `CASE` clause of `SEL` block
[DO](full_command#do) | Begin macro `DO` loop
[ELSTST](full_command#elstst) | Separate the code blocks after a `TST` check
[ENDDO](full_command#enddo) | End a macro `DO` loop
[ENDSEL](full_command#endsel) | End a macro `SEL` block
[ENDTST](full_command#endtst) | End a macro `TST` block
[GOSUB](full_command#gosub) | Perform call within macro
[GOTO](full_command#goto) | Go to statement label in macro
[GOTST](full_command#gotst) | Perform a conditional jump within a macro based on a test
[IFCND](full_command#ifcnd) | Branch on condition flag
[IFEQ](full_command#ifeq) | Branch on equal
[IFGBL](full_command#ifgbl) | Check for global argument and branch
[IFLCL](full_command#iflcl) | Check for local argument and branch
[IFMAC](full_command#ifmac) | Check for macro and branch
[IFREC](full_command#ifrec) | Check for record and branch
[MEXIT](full_command#mexit) | Exit macro
[NXTDO](full_command#nxtdo) | Cycle macro `DO` loop
[ONERR](full_command#onerr) | Set macro error handler
[RPTDO](full_command#rptdo) | Repeat iteration of macro `DO` loop
[SEL](full_command#sel) | Begin macro `SEL` block
[TST](full_command#tst) | Conditionally execute a block of commands based on a test

# Data Analysis
Command | Description
------- | -----------
[IBOX](full_command#ibox) | Set volume parameters for nD volume integration
[INTRG](full_command#intrg) | Integrate region of spectrum
[IXVAL](full_command#ixval) | Convert from unit value to point index
[LPK](full_command#lpk) | List Peaks
[LPK2D](full_command#lpk2d) | List peaks in two dimensions
[LW](full_command#lw) | Calculate line width
[MNMX](full_command#mnmx) | Calculate minimum and maximum in buffer region
[PP](full_command#pp) | Interactive peak picking
[RMS](full_command#rms) | Calculate root-mean-square value of data
[TH](full_command#th) | Set threshold for peak selection
[XVAL](full_command#xval) | Convert from point index to unit value

# Data Manipulation
Command | Description
------- | -----------
[BINCP](full_command#bincp) | Perform binary pulse phase correction
[CNVFL](full_command#cnvfl) | Convolution filter spectrum
[DEPAKE](full_command#depake) | Perform depaking of powder pattern spectrum
[DF](full_command#df) | Differentiate data
[FOLD](full_command#fold) | Fold data buffer
[INTG](full_command#intg) | Compute integral of spectrum
[LPB](full_command#lpb) | Perform backward linear prediction on FID
[LPC](full_command#lpc) | Perform long pulse phase and amplitude correction
[LPCA](full_command#lpca) | Perform long pulse amplitude correction
[LPCP](full_command#lpcp) | Perform long pulse phase correction
[LPF](full_command#lpf) | Perform forward linear prediction on FID
[PROF](full_command#prof) | Calculate profile of 2D data
[PROFB](full_command#profb) | Calculate profile of blocked record along a dimension
[PROJ](full_command#proj) | Calculate projection of 2D data
[PROJB](full_command#projb) | Calculate projection of blocked record along a dimension
[QC](full_command#qc) | Perform software quadrature phase correction
[ROT](full_command#rot) | Rotate spectrum
[ROTP](full_command#rotp) | Rotate spectrum
[SC](full_command#sc) | Scale data
[SETV](full_command#setv) | Set data values between limits
[SETVP](full_command#setvp) | Set data values for specified points
[SHFT](full_command#shft) | Shift data
[SHFTP](full_command#shftp) | Shift data by points
[TILT](full_command#tilt) | Tilt blocked record
[TWIST](full_command#twist) | Twist blocked record
[UNFOLD](full_command#unfold) | Unfold data buffer
[VAL](full_command#val) | Set data value
[WAVB](full_command#wavb) | Perform weighted average of blocked record
[XT](full_command#xt) | Extract data within specified limits
[XTP](full_command#xtp) | Extract data for points
[ZER](full_command#zer) | Zero visible processing buffer
[ZF](full_command#zf) | Zero fill visible processing buffer

# Data Storage
Command | Description
------- | -----------
[ARV](full_command#arv) | Return archive information
[CAT](full_command#cat) | List catalog of records
[CATARV](full_command#catarv) | List catalog of archives
[CLSARV](full_command#clsarv) | Close archive
[CPY](full_command#cpy) | Copy record
[CRTARV](full_command#crtarv) | Create archive
[DCDREC](full_command#dcdrec) | Convert record number into archive and archive record index
[DL](full_command#dl) | Delete records
[ECDREC](full_command#ecdrec) | Encode archive index
[GA](full_command#ga) | Get archive record data
[GB](full_command#gb) | Get blocked record data
[GS](full_command#gs) | Get data from scratch record
[IDN](full_command#idn) | Set processing buffer identification fields
[MOV](full_command#mov) | Move record
[OPNARV](full_command#opnarv) | Open archive
[PTRA](full_command#ptra) | Set read and write archive pointers
[RDARV](full_command#rdarv) | Read archive name
[SA](full_command#sa) | Save data to archive record
[SAVARV](full_command#savarv) | Save archive
[SB](full_command#sb) | Save data to blocked record
[SP](full_command#sp) | Display archive space information
[SQZ](full_command#sqz) | Squeeze archive (de-allocate unused space)
[SS](full_command#ss) | Save data to scratch record
[TITLE](full_command#title) | Set processing buffer title
[UPDARV](full_command#updarv) | Update archive
[USER](full_command#user) | Set user name

# Data Transforms
Command | Description
------- | -----------
[FT](full_command#ft) | Fourier transform FID
[HILB](full_command#hilb) | Perform Hilbert transform on spectrum
[HILBZ](full_command#hilbz) | Perform Hilbert transform on zero-filled spectrum
[IFT](full_command#ift) | Inverse Fourier transform spectrum
[MAG](full_command#mag) | Calculate magnitude of data
[POLAR](full_command#polar) | Convert buffer to polar coordinates

# Display Control
Command | Description
------- | -----------
[AI](full_command#ai) | Scale to absolute intensity
[AK](full_command#ak) | Set absolute scale factor
[BUF](full_command#buf) | View real or imaginary processing buffer
[BUFA](full_command#bufa) | View real or imaginary acquisition buffer
[COLOR](full_command#color) | Set data display colors
[CRS](full_command#crs) | Set cursor positions
[CRSA](full_command#crsa) | Set acquisition cursor positions
[LIM](full_command#lim) | Set processing buffer display limits
[LIMA](full_command#lima) | Set acquisition buffer display limits
[LIMB](full_command#limb) | Set blocked record display limits
[NDEC](full_command#ndec) | Set number of decimal places
[NORM](full_command#norm) | Set scale to normalize display
[SETIDN](full_command#setidn) | Set identification values
[UNIT](full_command#unit) | Set units
[VIEW](full_command#view) | Set display source
[WNDLIM](full_command#wndlim) | Set processing view vertical window limits
[WNDLIMA](full_command#wndlima) | Set acquisition view vertical window limits
[ZO](full_command#zo) | Zoom
[ZO2D](full_command#zo2d) | Zoom on 2D data set

# Experiment
Command | Description
------- | -----------
[CHN](full_command#chn) | Map logical and physical channels to one another
[DW](full_command#dw) | Set dwell time for data sampling during acquisition
[EX](full_command#ex) | Load a pulse program experiment
[FLAG](full_command#flag) | Set pulse program flag on or off
[FLF](full_command#flf) | Set filter factor
[GAIN](full_command#gain) | Set receiver gain
[LI](full_command#li) | Increment pulse programmer loop value
[LOOP](full_command#loop) | Set or increment pulse program loop counter
[LS](full_command#ls) | Set pulse programmer loop value
[NA](full_command#na) | Set number of shots to acquire
[NCHN](full_command#nchn) | Set number of channels
[NDLY](full_command#ndly) | Set number of dummy scans
[NUC](full_command#nuc) | Set synthesizer nucleus
[NWAIT](full_command#nwait) | Set number of shots to wait
[PPEX](full_command#ppex) | Load a pulse program experiment
[PPFLG](full_command#ppflg) | Set state of pulse program flag
[PWR](full_command#pwr) | Set transmitter coarse power level
[RCVMIX](full_command#rcvmix) | Set receiver quadrature mixing
[RCVOFF](full_command#rcvoff) | Set receiver offset
[RD](full_command#rd) | Set recycle delay
[SIZE](full_command#size) | Set acquisition size
[SW](full_command#sw) | Set sweep width

# File IO
Command | Description
------- | -----------
[APNFIL](full_command#apnfil) | Append text to file
[CLSRD](full_command#clsrd) | Close file opened for read
[CLSWRT](full_command#clswrt) | Close file which has been opened for writing
[CRTFIL](full_command#crtfil) | Create text file
[DLTFIL](full_command#dltfil) | Delete file
[EDTFIL](full_command#edtfil) | Edit text file
[LSTFIL](full_command#lstfil) | List contents of a text file
[MRGFS](full_command#mrgfs) | Merge default file with file
[OPNRD](full_command#opnrd) | Open file for reading
[OPNWRT](full_command#opnwrt) | Open file stream for writing
[RDWRT](full_command#rdwrt) | Read line from file
[RWDRD](full_command#rwdrd) | Rewind file opened by `OPNRD`
[RWDWRT](full_command#rwdwrt) | Rewind file opened by `OPNWRT`
[WPK](full_command#wpk) | Write peaks in current display to `WRT` file
[WPK2D](full_command#wpk2d) | Write 2D peaks to `WRT` file
[WRT](full_command#wrt) | Write line to file opened by `OPNWRT`

# Foreign
Command | Description
------- | -----------
[BRUK](full_command#bruk) | Convert BRUKER FID to complex FID
[CLSEXP](full_command#clsexp) | Close export file
[CLSIMP](full_command#clsimp) | Close import file
[EXP](full_command#exp) | Export buffer to foreign format
[EXP1D](full_command#exp1d) | Export 1D data to foreign format
[EXP2D](full_command#exp2d) | Export 2D data to foreign format
[EXP3D](full_command#exp3d) | Export 3D data to foreign format
[IMP](full_command#imp) | Import data from foreign format
[IMP1D](full_command#imp1d) | Import data from foreign format
[IMP2D](full_command#imp2d) | Import data from foreign format
[IMP3D](full_command#imp3d) | Import data from foreign format
[OPNEXP](full_command#opnexp) | Open export file
[OPNIMP](full_command#opnimp) | Open import file
[TPPI](full_command#tppi) | Convert TPPI-format FID to complex FID

# Frequency Control
Command | Description
------- | -----------
[CATNUC](full_command#catnuc) | List catalog of nuclei
[F](full_command#f) | Set synthesizer offset frequency
[FSYS](full_command#fsys) | Set spectrometer system frequency
[GREF](full_command#gref) | Restore processing buffer reference from nucleus table
[GREFA](full_command#grefa) | Restore acquisition buffer reference from nucleus table
[NUCD](full_command#nucd) | Define nucleus table entry
[NUCDL](full_command#nucdl) | Delete nucleus table entry
[OFF](full_command#off) | Set offset from reference frequency
[OFFA](full_command#offa) | Set offset from reference frequency
[SREF](full_command#sref) | Save processing buffer reference to nucleus table
[SREFA](full_command#srefa) | Save acquisition buffer reference to nucleus table

# Hardware
Command | Description
------- | -----------
[MASCMD](full_command#mascmd) | Send command to MAS controller
[RGPIB](full_command#rgpib) | Read string from GPIB device
[RPPSB](full_command#rppsb) | Read data byte from pulse programmer spectrometer bus
[RRKC](full_command#rrkc) | Read data from an RKC device
[RSB](full_command#rsb) | Read data byte from spectrometer bus
[WGPIB](full_command#wgpib) | Write line to GPIB device
[WPPSB](full_command#wppsb) | Write data byte to pulse programmer spectrometer bus
[WRKC](full_command#wrkc) | Write data byte to RKC device
[WRRI](full_command#wrri) | Write command line to RRI device and read response
[WSB](full_command#wsb) | Write data byte to spectrometer bus
[WTRM](full_command#wtrm) | Write command line to terminal and read response

# Heater
Command | Description
------- | -----------
[HTR](full_command#htr) | Enable or disable probe heater
[HTRSTS](full_command#htrsts) | Return probe heater status
[RSTHTR](full_command#rsthtr) | Restore heater values from file
[SAVHTR](full_command#savhtr) | Save heater values to file
[TALARM](full_command#talarm) | Set temperature for probe heater alarm
[TSET](full_command#tset) | Set heater set-point temperature
[TVAL](full_command#tval) | Show heater temperature
[WTSET](full_command#wtset) | Wait for heater to stabilize at setpoint

# Lists
Command | Description
------- | -----------
[APNLST](full_command#apnlst) | Append values to list
[CATLST](full_command#catlst) | List catalog of lists
[CRTLST](full_command#crtlst) | Create list
[DFNLST](full_command#dfnlst) | Define list value
[DLTLST](full_command#dltlst) | Delete list
[EDTLST](full_command#edtlst) | Edit list
[INSLST](full_command#inslst) | Insert value into list
[LSTDP](full_command#lstdp) | Define list from display
[LSTLST](full_command#lstlst) | List contents of a list
[POPLST](full_command#poplst) | Pop a value from a list
[PRGLST](full_command#prglst) | Purge list
[PSHLST](full_command#pshlst) | Push a value to a list
[RDLST](full_command#rdlst) | Read list from file
[REMLST](full_command#remlst) | Remove list value
[RSTLST](full_command#rstlst) | Restore lists from file
[SAVLST](full_command#savlst) | Save lists to file
[SIZLST](full_command#sizlst) | Display size of list
[WRTLST](full_command#wrtlst) | Write list to file

# Lock
Command | Description
------- | -----------
[GAINL](full_command#gainl) | Set lock receiver gain
[LCK](full_command#lck) | Enable or disable lock feedback loop
[LCKCTL](full_command#lckctl) | Open lock control pop up menu
[LCKMTR](full_command#lckmtr) | Enable lock meter
[LCKVAL](full_command#lckval) | Read lock value
[PIDL](full_command#pidl) | Set lock PID gain factors
[POSL](full_command#posl) | Set lock channel center position
[PWRL](full_command#pwrl) | Set lock channel power level
[RSTLCK](full_command#rstlck) | Restore lock values from file
[SAVLCK](full_command#savlck) | Save lock values to file
[SWL](full_command#swl) | Set lock channel sweep width
[SWP](full_command#swp) | Enable or disable lock sweep
[TCL](full_command#tcl) | Set lock channel time constant

# Macros
Command | Description
------- | -----------
[APNMAC](full_command#apnmac) | Append text to macro
[CATMAC](full_command#catmac) | List catalog of macros
[CPYMAC](full_command#cpymac) | Copy macro
[CRTMAC](full_command#crtmac) | Create macro
[DFNMAC](full_command#dfnmac) | Define macro table entry
[DLTMAC](full_command#dltmac) | Delete list
[EDTMAC](full_command#edtmac) | Edit macro
[LSTMAC](full_command#lstmac) | List contents of a macro
[MAPN](full_command#mapn) | Append text to macro
[MCPY](full_command#mcpy) | Copy macro
[MD](full_command#md) | Define macro
[MDL](full_command#mdl) | Delete macro
[ME](full_command#me) | Edit macro
[ML](full_command#ml) | List contents of a macro
[MRN](full_command#mrn) | Rename macro
[REMMAC](full_command#remmac) | Remove macro table entry
[RENMAC](full_command#renmac) | Rename macro

# Misc.
Command | Description
------- | -----------
[CND](full_command#cnd) | Set condition flag
[DATE](full_command#date) | Print the current date and time as an informational message
[DBSZ](full_command#dbsz) | Set processing buffer partitioning
[DCL](full_command#dcl) | Execute a shell command in background
[EXIT](full_command#exit) | Exit program
[INFLVL](full_command#inflvl) | Set info level
[LOG](full_command#log) | Write line to log
[LP](full_command#lp) | List processing buffer parameters
[MO](full_command#mo) | Exit program
[MSG](full_command#msg) | Write message line to console
[NOP](full_command#nop) | Null operation
[PROG](full_command#prog) | Identify program
[PRTARG](full_command#prtarg) | Print arguments
[RDSTR](full_command#rdstr) | Read tokens from a string
[RSTBUF](full_command#rstbuf) | Restore buffer values from file
[SAVBUF](full_command#savbuf) | Save buffer value to file
[SAVLOG](full_command#savlog) | Save logging to file
[SET](full_command#set) | Set system state
[SHELL](full_command#shell) | Spawn shell
[SHOW](full_command#show) | Show information
[STR](full_command#str) | Perform string operation
[WTTIM](full_command#wttim) | Wait for specified number of seconds

# Phasing
Command | Description
------- | -----------
[PC](full_command#pc) | Incremental phase correction
[PH](full_command#ph) | Interactive phase correction
[PS](full_command#ps) | Set phase
[TP](full_command#tp) | Show phase correction values

# Plotting
Command | Description
------- | -----------
[CLSPLT](full_command#clsplt) | Close plotter stream and print
[OPNPLT](full_command#opnplt) | Open plot stream 	
[PEN](full_command#pen) | Select plot pen
[PGSIZE](full_command#pgsize) | Set page size for plot
[PLDEV](full_command#pldev) | Select plotting device
[PLFIL](full_command#plfil) | Set plot file
[PLOT](full_command#plot) | Plot current 1D display
[PLOTC](full_command#plotc) | Plot 2D contours
[PLSIZE](full_command#plsize) | Set plot size
[STK](full_command#stk) | Add to plot stream stack
[STKOFF](full_command#stkoff) | Set stack plot offset
[WWASH](full_command#wwash) | Set state of plot whitewash flag

# Printing
Command | Description
------- | -----------
[LPDEV](full_command#lpdev) | Select text printer device
[LPFIL](full_command#lpfil) | Set text printer file

# Pulse Control
Command | Description
------- | -----------
[AMD](full_command#amd) | Set acquisition modes
[D](full_command#d) | Set pulse programmer delay
[DLY](full_command#dly) | Set pulse programmer delay
[FMX](full_command#fmx) | Set frequency modulation value
[FMXEX](full_command#fmxex) | Load frequency modulation program
[NAMD](full_command#namd) | Set number of acquisition modes
[P](full_command#p) | Set pulse length
[PLS](full_command#pls) | Set pulse length
[PPMD](full_command#ppmd) | Set pulse program phase mode
[PSX](full_command#psx) | Set transmitter phase
[PSXEX](full_command#psxex) | Load transmitter phase program from PAM memory.
[PWX](full_command#pwx) | Set transmitter fine power level
[PWXEX](full_command#pwxex) | Load power program

# Pulse Program Symbols
Command | Description
------- | -----------
[CATPPS](full_command#catpps) | List catalog of PP symbols
[DFNPPS](full_command#dfnpps) | Define pulse programmer symbol table entry
[RDPPS](full_command#rdpps) | Read PP symbol
[RDPPSNAM](full_command#rdppsnam) | Read PP symbol name
[REMPPS](full_command#rempps) | Remove pulse programmer symbols

# Shim
Command | Description
------- | -----------
[AUTOZ](full_command#autoz) | Set automatic Z shim parameters
[RSTSHM](full_command#rstshm) | Restore shim values from file
[SAVSHM](full_command#savshm) | Save shim values to file
[SHM](full_command#shm) | Set shim value
[SHMCTL](full_command#shmctl) | Open interactive shim controls

# Signal Generation
Command | Description
------- | -----------
[ECHO](full_command#echo) | Rearrange buffer to simulate echo data
[GENCS](full_command#gencs) | Generate complex sine wave
[GENPWDR](full_command#genpwdr) | Generate complex powder pattern
[NOISE](full_command#noise) | Generate complex random noise
[UNECHO](full_command#unecho) | Rearrange buffer to simulate FID from echo

# Tables
Command | Description
------- | -----------
[CATTBL](full_command#cattbl) | List catalog of name tables
[CRTTBL](full_command#crttbl) | Create name table
[DFLTBL](full_command#dfltbl) | Define name table argument with default value
[DFNTBL](full_command#dfntbl) | Define name table argument
[DLTTBL](full_command#dlttbl) | Delete name table
[PRGTBL](full_command#prgtbl) | Purge name table
[RDTBL](full_command#rdtbl) | Read name table values from file
[REMTBL](full_command#remtbl) | Remove name table entries
[RSTTBL](full_command#rsttbl) | Restore name tables from file
[SAVTBL](full_command#savtbl) | Save name tables to file
[SIZTBL](full_command#siztbl) | Display size of name table
[WRTTBL](full_command#wrttbl) | Write name table to file

# Waveform
Command | Description
------- | -----------
[WRF](full_command#wrf) | Set waveform reference values
[WRFEX](full_command#wrfex) | Load waveform RF program
[WWF](full_command#wwf) | Set waveform values
[WWFEX](full_command#wwfex) | Load waveform program


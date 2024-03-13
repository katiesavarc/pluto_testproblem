# pluto_testproblem
PLUTO test-problem to be run as a demo

## CODE DEMO:

set up the PLUTO directory

`export PLUTO_DIR=/workspaces/pluto_testproblem/PLUTO`

change to the directory where you have the correct files to start:

`cd $PLUTO_DIR/Test_Problems/HD/Jet`

make directory to put your data into

`mkdir data_storage`

`chmod 777 data_storage`

copy the pre-made definitions files into the correct file

`cp definitions_01.h definitions.h`
`cp pluto_01.ini pluto.ini`



**CHANGES to make in pluto.ini:**

- multiple files
- add an output dir

now we will setup, compile and run the code:

`python $PLUTO_DIR/setup.py`

`make`

`./pluto > data_storage/logfile.log`


## More info

- `HD/`: contains problems for the gas-dynamic Euler or Navier-Stokes equations;
- `MHD/`: contains problems for ideal or resistive magnetohydrodynamics;
- `RHD/`: collection of numerical benchmarks for (special) relativistic hydro equations;
- `RMHD/`: collection of numerical benchmarks for (special) relativistic MHD.

if you want to run more test problems, there is more info on them here: 

[PLUTO Test Problems: File List](http://plutocode.ph.unito.it/Doxygen/Test_Problems/files.html)


and here is the actual documentation (to be consumed in small bites, not large meals):

[PLUTO documentation](http://plutocode.ph.unito.it/userguide.pdf)

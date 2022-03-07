#!/bin/bash
# Begin LSF Directives
#BSUB -P MAT230
#BSUB -W 2:00
#BSUB -nnodes 20
#BSUB -J mo10x
#BSUB -o mo10x.%J
#BSUB -e mo10x.%J
	 
date

export OMP_NUM_THREADS=1

jsrun --smpiargs "-gpu" -n 120 -a 7 -c 7 -g 1 -r 6 -d packed -b packed:1  ./dftfe parameterFileCPU.prm > outputCPUHamDenOpt

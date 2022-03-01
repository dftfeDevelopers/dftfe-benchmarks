#!/bin/bash
# Begin LSF Directives
#BSUB -P MAT230
#BSUB -W 1:50
#BSUB -nnodes 4
#BSUB -J mo6x
#BSUB -o mo6x.%J
#BSUB -e mo6x.%J
	 
date

export OMP_NUM_THREADS=1

jsrun --smpiargs "-gpu" -n 24 -a 7 -c 7 -g 1 -r 6 -d packed -b packed:1  ./dftfe parameterFileCPU.prm > outputCPUFullScfHamDenOpt

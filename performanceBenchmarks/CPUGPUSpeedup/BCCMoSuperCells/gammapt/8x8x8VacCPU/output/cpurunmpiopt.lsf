#!/bin/bash
# Begin LSF Directives
#BSUB -P MAT230
#BSUB -W 1:30
#BSUB -nnodes 10
#BSUB -J mo8x
#BSUB -o mo8x.%J
#BSUB -e mo8x.%J
	 
date

export OMP_NUM_THREADS=1

jsrun --smpiargs "-gpu" -n 60 -a 7 -c 7 -g 1 -r 6 -d packed -b packed:1  ./dftfe parameterFileCPU.prm > outputCPU10NodesHamDenOpt

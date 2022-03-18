#!/bin/bash
# Begin LSF Directives
#BSUB -P MAT239
#BSUB -W 0:15
#BSUB -alloc_flags gpumps
#BSUB -nnodes 40
#BSUB -J mo6x
#BSUB -o mo6x.%J
#BSUB -e mo6x.%J
	 
date

export OMP_NUM_THREADS=1
export PAMI_DISABLE_IPC=1
export PAMI_IBV_ENABLE_DCT=1
export PAMI_ENABLE_STRIPING=0
export PAMI_IBV_ADAPTER_AFFINITY=1
export PAMI_IBV_DEVICE_NAME="mlx5_0:1,mlx5_3:1"
export PAMI_IBV_DEVICE_NAME_1="mlx5_3:1,mlx5_0:1"


jsrun --smpiargs "-gpu" -n 240 -a 1 -c 7 -g 1 -r 6 -d packed -b packed:7 -l gpu-gpu  ./dftfecomplex parameterFileGPU.prm > outputGPU40NodesMPS1_nccl_complex

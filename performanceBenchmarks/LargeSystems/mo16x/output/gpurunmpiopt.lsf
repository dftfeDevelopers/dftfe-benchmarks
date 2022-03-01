#!/bin/bash
# Begin LSF Directives
#BSUB -P ENG110
#BSUB -W 1:30
#BSUB -alloc_flags gpumps
#BSUB -nnodes 600
#BSUB -J mo16x
#BSUB -o mo16x.%J
#BSUB -e mo16x.%J
	 
date

export OMP_NUM_THREADS=1
export PAMI_DISABLE_IPC=1
export PAMI_IBV_ENABLE_DCT=1
export PAMI_ENABLE_STRIPING=0
export PAMI_IBV_ADAPTER_AFFINITY=1
export PAMI_IBV_DEVICE_NAME="mlx5_0:1,mlx5_3:1"
export PAMI_IBV_DEVICE_NAME_1="mlx5_3:1,mlx5_0:1"


jsrun --smpiargs "-gpu -mca coll_ibm_tune_results $XML10300" -n 3600 -a 1 -c 7 -g 1 -r 6 -d packed -b packed:7 -l gpu-gpu  ./dftfe parameterFileGPU.prm > outputGPU600NodesMPS1_mpiopt_mixedprecall_fullscf_ncclallreduce_elpagpu_16blocksize_largerchebyblocksize_nofullsubspacerotmem

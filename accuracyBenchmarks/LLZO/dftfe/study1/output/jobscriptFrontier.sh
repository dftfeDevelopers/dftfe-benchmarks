#!/bin/sh
#SBATCH -A mat295
#SBATCH -J LLZOStudy1
#SBATCH -t 00:30:00
#SBATCH -p batch
#SBATCH -N 4
#SBATCH --gpus-per-node 8
#SBATCH --ntasks-per-gpu 1
#SBATCH --gpu-bind closest

export OMP_NUM_THREADS=1
export MPICH_VERSION_DISPLAY=1
export MPICH_ENV_DISPLAY=1
export MPICH_OFI_NIC_POLICY=NUMA
export MPICH_GPU_SUPPORT_ENABLED=1
export MPICH_SMP_SINGLE_COPY_MODE=NONE
export FI_MR_CACHE_MONITOR=disabled

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$INST/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$INST/lib/lib64
export LD_LIBRARY_PATH=$CRAY_LD_LIBRARY_PATH:$LD_LIBRARY_PATH

export BASE=$WD/dftfe_release1.2/build/release/real

srun -n 32 -c 7 --gpu-bind closest $BASE/dftfe parameterFile_GPU.prm > output4Nodes

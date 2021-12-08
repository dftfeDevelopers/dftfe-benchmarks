#!/bin/bash
#SBATCH --job-name Al147
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=36
#SBATCH --mem-per-cpu=5g
#SBATCH --time=72:00:00
#SBATCH --account=vikramg1
#SBATCH --partition=standard
#SBATCH --mail-user=phanim@umich.edu
#SBATCH --mail-type=BEGIN,END


srun /scratch/vikramg_root/vikramg1/phanim/DFT_FETesting/buildSmearedChargeNew/release/real/dftfe parameterFileCPU.prm>outputFEOrder7MeshSize2d3AtomBallRadius4

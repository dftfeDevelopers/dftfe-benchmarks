#!/bin/bash
#SBATCH --job-name qe
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=18
#SBATCH --mem-per-cpu=10g
#SBATCH --time=20:00:00
#SBATCH --account=vikramg1
#SBATCH --mail-user=dsambit@umich.edu
#SBATCH --mail-type=BEGIN,END

export OMP_NUM_THREADS=2
mpirun -n 54 pw.x -input mo4x.scf.in > mo4xEcut50.scf.out

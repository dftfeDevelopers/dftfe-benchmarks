#!/bin/bash
#SBATCH --job-name qe
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=36
#SBATCH --mem-per-cpu=5g
#SBATCH --time=50:00:00
#SBATCH --account=vikramg1
#SBATCH --partition=standard
#SBATCH --mail-user=phanim@umich.edu
#SBATCH --mail-type=BEGIN,END

srun pw.x -input Al147Atom.scf.in>Al147AtomEcut50.scf.out
 

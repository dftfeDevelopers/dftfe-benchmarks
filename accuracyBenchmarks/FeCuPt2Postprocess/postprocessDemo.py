'''
filesPath: str: path to the directory where the input files are stored,
bandsDatFile: str: name of the file containing the bandstructure data,
kptsFile: str: name of the file containing the kpoints data,
coordinatesFile: str: name of the file containing the coordinates data,
latticeVecFile: str: name of the file containing the lattice vectors data,
pseudoPotFile: str: name of the file containing the pseudopotential data,
dosDataFile: str: name of the file containing the DOS data,
eLimit: List: energy limits for the bandstructure, DOS and PDOS plots,
dosLimit: List: DOS limits for the DOS and PDOS plots,
isPeriodic: bool: True if the system is periodic or semi periodic, False otherwise,
only_tdos: bool: If True, only the total DOS is plotted,
plot_total: bool: If True, then the total DOS is plotted along with the PDOS,
spins: List: List of spin-channels to be included in the plot, 
items : dict: keys are the atom numbers (as given in the coordinates file) and values being the corresponding orbitals (available options 's','p','d') for each species.

*************************
for better understanding of the below parameters please refer to the pyprocar user guide
"https://romerogroup.github.io/pyprocar/examples/index.html"
************************

overlay_mode: bool: If True, plot is in 'overlay' mode, otherwise 'stack' mode,
stack_orbitals: bool: If True, PDOS corresponding to the orbitals of the atoms mentioned in the "atoms" variable are plotted,
atoms: List: List of the atom numbers to be considered for PDOS calculation. It has meaning only if "stack_orbitals" is true. If nothing specified, all the atoms are considered,
stack_species: bool: If True, PDOS corresponding to the atoms for the orbitals mentioned in the "orbitals" variable are plotted,
orbitals: List: List of the orbitals to be considered for PDOS calculation. It has meaning only if "stack_species" is true. If nothing specified, all the orbitals are considered
'''

from postprocessModules import Plotters

# plotter_bands = Plotters(filesPath = "/home/srinibasn/dftfe_accuracy_pdos/dftfe-benchmarks/accuracyBenchmarks/FeCuPt2Postprocess/",
#                         bandsDatFile = "bands.out",
#                         kptsFile= "kpointRuleFile.inp",
#                         coordinatesFile = "coordinates.inp",
#                         latticeVecFile = "domainVectors.inp",
#                         pseudoPotFile = "pseudo.inp",
#                         eLimit= [-10, 20], # after shifting wrt fermi energy
#                         isPeriodic = True,
#                         numSpins = 2,
#                         spins= [0]
#                         )
plotter_dos = Plotters(filesPath = "/home/srinibasn/dftfe_accuracy_pdos/dftfe-benchmarks/accuracyBenchmarks/FeCuPt2Postprocess/",
                   coordinatesFile = "coordinates.inp",
                   bandsDatFile="bands.out", 
                   items=dict(Pt = ['s'], Cu =['s']),
                   overlay_mode = True,
                   latticeVecFile = "domainVectors.inp",
                   pseudoPotFile = "pseudo.inp",
                   dosDataFile = "dosData.out",
                   eLimit= [-10, 6], # after shifting wrt fermi energy
                   dosLimit= [0, 1],
                   isPeriodic = True,
                   plot_total= False,
                   only_tdos = False,
                   stack_orbitals= True,
                   atoms=[3],
                   stack_species= False,
                   orbitals=[0],
                   numSpins = 2,
                   spins= [0]
                   )
# plotter_bands.plotBandStr()
plotter_dos.plotDos()

import sys
sys.path.append("/home/srinibasn/bandsPR/dftfe") # append the path of DFTFE to sys.path

from postProcessing.postprocessModules import Plotters
'''
  filesPath: str: path to the directory where the input files are stored,
  bandsDatFile: str: name of the file containing the bandstructure data,
  kptsFile: str: name of the file containing the kpoints data,
  coordinatesFile: str: name of the file containing the coordinates data,
  latticeVecFile: str: name of the file containing the lattice vectors data,
  pseudoPotFile: str: name of the file containing the pseudopotential data,
  dosDataFile: str: name of the file containing the DOS data,
  eLimit: list: energy limits for the bandstructure and DOS plots,
  isPeriodic: bool: True if the system is periodic, False otherwise
'''

plotter = Plotters(filesPath = "./",
                   bandsDatFile = "bands.out",
                   kptsFile= "kpointRuleFile.inp", 
                   coordinatesFile = "coordinates.inp", 
                   latticeVecFile = "domainVectors.inp",
                   pseudoPotFile = "pseudo.inp",
                   dosDataFile = "dosData.out", 
                   eLimit= [-14.0, 5.0], 
                   isPeriodic = True)
# plotter = Plotters(filesPath = "./",
#                    bandsDatFile = "bands.out",
#                    kptsFile= "kpointRuleFile.inp", 
#                    coordinatesFile = "coordinates.inp", 
#                    latticeVecFile = "domainVectors.inp",
#                    pseudoPotFile = "pseudo.inp",
#                    dosDataFile = "dosData.out", 
#                    eLimit= [-15.0, 15.0], 
#                    isPeriodic = True)
plotter.plotBandStr()
# plotter.plotDos()

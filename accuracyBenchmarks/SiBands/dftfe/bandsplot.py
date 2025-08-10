from postprocessModules import Plotters

plotter_bands = Plotters(filesPath = "/home/srinibasn/dftfe_benchmarks_5thAug/accuracyBenchmarks/SiBands_new/dftfe",
                        bandsDatFile = "bands.out",
                        kptsFile= "kpointRuleFile.inp",
                        coordinatesFile = "coordinates.inp",
                        latticeVecFile = "domainVectors.inp",
                        pseudoPotFile = "pseudo.inp",
                        eLimit= [-15, 4], # after shifting wrt fermi energy
                        isPeriodic = True,
                        numSpins = 1,
                        spins= [0]
                        )
plotter_bands.plotBandStr()
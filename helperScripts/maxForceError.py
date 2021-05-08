import math
import numpy as np

def main():

  # .txt files for forces are required to have 
  # three columns corresponding to the three different
  # force components (x-y-z), with the rows corresponding to the atomIds
  # Please make sure same atom numbering is used
  # in QE (Quantum Espresso) and DFT-FE input files.
  # If comparing between two different DFT-FE outputs,
  # please set isData2FromQE=False
  data1 = np.loadtxt("dftfeforces.txt")
  data2 = np.loadtxt("qeforces.txt")
  isData2FromQE=True;

  if (isData2FromQE):
     diff=np.subtract(data1, 0.5*data2);
  else:
     diff=np.subtract(data1, data2);

  maxDiff=0.0;
  count=0;
  totCount=0;
  squaredsum=0.0
  for x in np.nditer(diff):
     totCount=totCount+1
     squaredsum=squaredsum+abs(x)*abs(x)
     if abs(x)>maxDiff:
        maxDiff=abs(x)
     if abs(x)>1e-3:
        count=count+1

  print("max force error")
  print(maxDiff)
  print("rms error")
  print(math.sqrt(squaredsum/totCount))

if __name__=="__main__":
    main()

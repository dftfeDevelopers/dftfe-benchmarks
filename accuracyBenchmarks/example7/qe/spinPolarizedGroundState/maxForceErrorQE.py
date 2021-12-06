import math
import numpy as np

def main():

  data1qe = np.loadtxt("forcesEcut30.txt")
  data2qe = np.loadtxt("forcesEcut50.txt")
  diff=np.subtract(0.5*data1qe, 0.5*data2qe);

  maxDiff=0.0;
  count=0;
  totCount=0;
  for x in np.nditer(diff):
     totCount=totCount+1
     if abs(x)>maxDiff:
        maxDiff=abs(x)
     if abs(x)>1e-3:
        count=count+1
        print(totCount)    
 
  print(maxDiff)
  print(count)

if __name__=="__main__":
    main()

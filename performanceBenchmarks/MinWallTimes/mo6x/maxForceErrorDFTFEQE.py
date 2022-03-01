import math
import numpy as np

def strip_first_col(fname, delimiter=None):
    with open(fname, 'r') as fin:
        for line in fin:
            try:
               yield line.split(delimiter, 1)[1]
            except IndexError:
               continue

def main():

  data1 = np.loadtxt("forces.txt")
  dataqe = np.loadtxt("qeforcesEcut40.txt")
  diff=np.subtract(data1, 0.5*dataqe);

  maxDiff=0.0;
  count=0;
  totCount=0;
  squaredsum=0.0
  for x in np.nditer(diff):
     totCount=totCount+1
     squaredsum=squaredsum+abs(x)*abs(x)
     if abs(x)>maxDiff:
        maxDiff=abs(x)
     if abs(x)>2e-4:
        count=count+1
        print(totCount)    
 
  print(maxDiff)
  print(count)
  print(math.sqrt(squaredsum/totCount))

if __name__=="__main__":
    main()

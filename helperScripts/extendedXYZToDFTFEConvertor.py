import math
import numpy as np
from numpy.linalg import inv

def main():
   xyzFile = open("p4.41x17y4s7.xyz",'r')
   domainVectorsFile=open("domainVectors.inp",'w')
   relaxationFlagsFile=open("relaxationFlags.inp",'w')

   atomicNumbers=[]
   valenceNumbers=[]
   cartCoords=[]
   lineCount=0
   atomCount=0
   electronCount=0
   a2b=1.8897259886
   for line in xyzFile:
        if (lineCount==0):
          print(line.split())
        elif (lineCount==1):
          line = line.split('"')
          domain=line[1].split()
          pbc=line[3].split()
          print(domain)
          print(pbc)
        else:
          line = line.split()
          atomicSymbol=line.pop(0)
          if (atomicSymbol=='C'):
            atomicNumbers.append(6)
            valenceNumbers.append(4)
          elif (atomicSymbol=='O'):
            atomicNumbers.append(8)
            valenceNumbers.append(6)
          elif (atomicSymbol=='N'):
            atomicNumbers.append(7)
            valenceNumbers.append(5)
          elif (atomicSymbol=='H'):
            atomicNumbers.append(1)
            valenceNumbers.append(1)
          elif (atomicSymbol=='Fe'):
            atomicNumbers.append(26)
            valenceNumbers.append(16)
          elif (atomicSymbol=='S'):
            atomicNumbers.append(16)
            valenceNumbers.append(6)

          electronCount+=valenceNumbers[atomCount]
          coord=np.array(line,float)
          cartCoords.append(coord)


          atomCount=atomCount+1


        lineCount=lineCount+1

   #print(electronCount)
   if (pbc[0]=='F' and pbc[1]=='F' and pbc[2]=='F'):
   
     xcentroid=0.0
     ycentroid=0.0
     zcentroid=0.0

     for index, coord in enumerate(cartCoords):
       xcentroid=xcentroid+coord[0]
       ycentroid=ycentroid+coord[1]
       zcentroid=zcentroid+coord[2]

     xcentroid=xcentroid/(atomCount*1.0)
     ycentroid=ycentroid/(atomCount*1.0)
     zcentroid=zcentroid/(atomCount*1.0)

     xmin=0
     xmax=0
     ymin=0
     ymax=0
     zmin=0
     zmax=0
     for index, coord in enumerate(cartCoords):
       coord[0]=coord[0]-xcentroid
       coord[1]=coord[1]-ycentroid
       coord[2]=coord[2]-zcentroid
       if (xmin>coord[0]):
          xmin=coord[0]
       if (xmax<coord[0]):
          xmax=coord[0]
       if (ymin>coord[1]):
          ymin=coord[1]
       if (ymax<coord[1]):
          ymax=coord[1]
       if (zmin>coord[2]):
          zmin=coord[2]
       if (zmax<coord[2]):
          zmax=coord[2]

   domainMatInv=inv((np.matrix(np.array([[float(domain[0])*a2b, float(domain[1])*a2b,float(domain[2])*a2b], [float(domain[3])*a2b, float(domain[4])*a2b,float(domain[5])*a2b],[float(domain[6])*a2b, float(domain[7])*a2b,float(domain[8])*a2b]])).T))
   
   domainVectorsFile.write(str(float(domain[0])*a2b)+ ' ' + str(float(domain[1])*a2b)+ ' ' + str(float(domain[2])*a2b) + '\n')
   domainVectorsFile.write(str(float(domain[3])*a2b)+ ' ' + str(float(domain[4])*a2b)+ ' ' + str(float(domain[5])*a2b) + '\n')
   domainVectorsFile.write(str(float(domain[6])*a2b)+ ' ' + str(float(domain[7])*a2b)+ ' ' + str(float(domain[8])*a2b) + '\n')


   ionFile=open("coordinates.inp",'w')

   if (pbc[0]=='F' and pbc[1]=='F' and pbc[2]=='F'):
     for index, coord in enumerate(cartCoords):
          ionFile.write(str(atomicNumbers[index]) + ' ' + str(valenceNumbers[index]) + ' ' + str(coord[0])+ ' ' + str(coord[1])+ ' ' + str(coord[2]) + '\n')
          relaxationFlagsFile.write(str(1)+ ' ' + str(1)+ ' ' + str(1) + '\n')
   else:
     for index, coord in enumerate(cartCoords):
          cartCoordVec=np.matrix(np.array([[coord[0]],[coord[1]],[coord[2]]]))
          fracCoordVec=domainMatInv*cartCoordVec
          ionFile.write(str(atomicNumbers[index]) + ' ' + str(valenceNumbers[index]) + ' ' + str(fracCoordVec[0,0])+ ' ' + str(fracCoordVec[1,0])+ ' ' + str(fracCoordVec[2,0]) + '\n')
          relaxationFlagsFile.write(str(1)+ ' ' + str(1)+ ' ' + str(1) + '\n')


   xyzFile.close()
   ionFile.close()
   domainVectorsFile.close()

if __name__=="__main__":
    main()



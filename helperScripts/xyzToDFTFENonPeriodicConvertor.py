import math
import numpy as np

def main():
   xyzFile = open("KatG-INH_quantum.xyz",'r')
   domainVectorsFile=open("domainVectors.inp",'w')
   #relaxationFlagsFile=open("relaxationFlags.inp",'w')

   atomicNumbers=[]
   valenceNumbers=[]
   cartCoords=[]
   lineCount=0
   atomCount=0
   electronCount=0
   a2b=1.8897259886
   for line in xyzFile:
        line = line.split()

        if lineCount>1:
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

   domainvec=np.array(line,float)
   domainVectorsFile.write(str((xmax-xmin+30.0)*a2b)+ ' ' + str(0)+ ' ' + str(0) + '\n')
   domainVectorsFile.write(str(0)+ ' ' + str((ymax-ymin+30.0)*a2b)+ ' ' + str(0) + '\n')
   domainVectorsFile.write(str(0)+ ' ' + str(0)+ ' ' + str((zmax-zmin+30.0)*a2b) + '\n')


   ionFile=open("coordinates.inp",'w')

   for index, coord in enumerate(cartCoords):
        ionFile.write(str(atomicNumbers[index]) + ' ' + str(valenceNumbers[index]) + ' ' + str(coord[0]*a2b)+ ' ' + str(coord[1]*a2b)+ ' ' + str(coord[2]*a2b) + '\n')
        #relaxationFlagsFile.write(str(1)+ ' ' + str(1)+ ' ' + str(1) + '\n')


   xyzFile.close()
   ionFile.close()
   domainVectorsFile.close()

if __name__=="__main__":
    main()

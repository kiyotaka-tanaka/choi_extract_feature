import numpy as np 
import h5py 
import os
import sys



filename = os.listdir("./image")

fileout = sys.argv[1]

fo = open(fileout,"w")
filename = "features" + "/" + filename[0] + ".h5"
#print filename
f = h5py.File(filename,"r")

a =  f[u'feat'].value

#np.savetxt(fileout,a,fmt='%0.4f')

line = ""

for i in a:
    line = line + "\t" +  str(i)

fo.write(line)


















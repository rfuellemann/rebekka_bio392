import numpy
import pandas as pd

datafile =open("data.pgxseg")

while True:
    line=datafile.readline()
    if line[0]!="#":
        names = line.split()
        break

linelist=[]
while True:
    line=datafile.readline()

    if line == "":
        break
    else:
        linelist.append(line.split())

datafile.close()

df= pd.DataFrame(data=linelist, columns=names)
df.to_csv("data.csv")

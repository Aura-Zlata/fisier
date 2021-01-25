
with open ('globulet.txt','r') as f:
    nre=f.readline()
nrr=int(nre)+3
nra=int(nre)+nrr-2
nrt=int(nre)+nrr+nra

with open('bradut.txt','w') as f:
    f.write(str(nrt))
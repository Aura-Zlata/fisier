
with open('input.txt','r') as f:
    nr=f.readline()
a=str(int(nr-2))+' '+str(int(nr-1))+' '+str(int(nr))+' '+str(int(nr+1))+' '+str(int(nr+2))

with open('output.txt','w') as f:
    f.write(a)
    

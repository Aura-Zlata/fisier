
with open('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    x1=int(a)*2
    x2=int(b)*3
else:
    x1=int(b)*2    
    x2=int(a)*3

with open('produs.txt','w') as f:
    f.write(str(x1)+' '+str(x2))
    
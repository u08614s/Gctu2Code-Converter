import math

gctu=input('path: ')
with open(gctu,'rb') as f:
    tmp=f.read()
    f.close()
tmp=tmp.hex().upper()
tmpa=''
tmpb=0
for x in range(math.floor(len(tmp)/8)):
    if(tmpb==0):
        tmpc=' '
    if(tmpb==1):
        tmpc='\n'
        tmpb=-1
    tmpa=tmpa+tmp[x*8:x*8+8]+tmpc
    tmpb=tmpb+1
tmpa=tmpa[:-1]
print(tmpa)
input()

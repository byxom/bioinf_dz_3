a="ATGAGTCTCT"
b="CTGTCTCCTG"
#пример последовательностей
DNAfull = [[5,-4, -4, -4], [-4, 5, -4, -4], [-4, -4, 5, -4], [-4, -4, -4, 5]]
dDNA = {['C', 'T', 'A', 'G'][a]: a for a in range (4)}
d=-10
m=[[i*d for i in range(len(a)+1)],[0]*(len(a)+1)]


l=['P','D','V']
row=[]
for i in range(1,len(b)+1):
    line=[]
    for j in range(1,len(a)+1):
        pos=[m[1][j-1]+d,m[0][j-1]+DNAfull[dDNA[a[j-1]]][dDNA[b[i-1]]],m[0][j]+d]
        ds=dict(zip(pos,l))
        m[1][j]=max(pos)
        line.append(ds[int(m[1][j])])
    m[0][0],m[1][0]=i*d,i*d
    m[0]=m[1].copy()
    row.append(line)

import numpy as np
route = np.asarray(row)


resa = ''
resb = ''
prov = np.empty(shape=(0, 0))

while a != '' and b != '':
    if route[-1, -1] == 'V':
        resa = '-' + resa
        resb = b[-1] + resb
        b = b[:-1]

        route = route[:-1]
    elif route[-1, -1] == 'P':
        resa = a[-1] + resa
        a = a[:-1]
        resb = '-' + resb
        route = route[:, :-1]
    else:
        resa = a[-1] + resa
        a = a[:-1]
        resb = b[-1] + resb
        b = b[:-1]
        route = route[:-1, :-1]

print(resa+'\n'+resb)

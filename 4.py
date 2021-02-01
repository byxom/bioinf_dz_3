a="ATGAGTCTCT"
b="CTGTCTCCTG"
#пример последовательностей

DNAfull = [[5,-4, -4, -4], [-4, 5, -4, -4], [-4, -4, 5, -4], [-4, -4, -4, 5]]
dDNA = {['C', 'T', 'A', 'G'][a]: a for a in range (4)}
d=-10

m=[[i*d for i in range(len(a)+1)],[0]*(len(a)+1)]

print(m[0])

for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        m[1][j]=max(m[1][j-1]+d,m[0][j-1]+DNAfull[dDNA[a[j-1]]][dDNA[b[i-1]]],m[0][j]+d)

    m[0][0],m[1][0]=i*d,i*d

    print(m[1])

    m[0]=m[1].copy()
print('score:',m[1][-1])


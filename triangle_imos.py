import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
N,M=ll()
imos=[[0]*(N+1) for _ in range(N+1)]
triangke_imos=[(0,1),(1,0),(1,1)]
for _ in range(M):
    a,b,x=ll()
    imos[a][b]+=1
    imos[a][b+1]-=1
    if a+x+1<N+1:
        imos[a+x+1][b]-=1
        if b+x+2<N+1:
            imos[a+x+1][b+x+2]+=1
    if a+x+2<N+1:
        imos[a+x+2][b+1]+=1
        if b+x+2<N+1:
            imos[a+x+2][b+x+2]-=1

for ty,tx in triangke_imos:
    for i in range(N+1):
        yy=i+ty
        if yy>N: continue
        for j in range(N+1):              
            xx=j+tx
            if xx>N: continue
            imos[yy][xx]+=imos[i][j]
ans=0
for i in range(N+1):
    for j in range(N+1):
        if imos[i][j]>0:
            ans+=1
print(ans)
    

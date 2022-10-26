def ll(): return list(map(int, input().split()))

N,M=ll()
INF=10**10
G=[[INF]*N for _ in range(N)]
for i in range(N):
    G[i][i]=0
for _ in range(M):
    a,b,t=ll()
    a-=1
    b-=1
    G[a][b]=t
    G[b][a]=t

for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j]=min(G[i][j],G[i][k]+G[k][j])
print(G)
print(min(list(max(G[i]) for i in range(N))))
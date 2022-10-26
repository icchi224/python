import collections,sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

#幅優先探索 頂点1からNまでの最短距離
N,M=ll()
G=[[]for _ in range(N)]
for _ in range(M):
    a,b=ll()
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

visited=[False]*N
visited[0]=True
que=collections.deque([(0,0)])
while que:
    print(que)
    pos,d=que.popleft()
    if pos==N-1:
        ans=d
    for to in G[pos]:
        if visited[to]==False:
            visited[to]=True
            que.append((to,d+1))

print(ans)
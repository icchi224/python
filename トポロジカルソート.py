import heapq
import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

N,M=ll()
G=[[]for _ in range(N)]
d=[0]*N
for _ in range(M):
    a,b=ll()
    a-=1
    b-=1
    G[a].append(b)
    d[b]+=1

ans=[]
hq=[]
heapq.heapify(hq)
for i in range(N):
    if d[i]==0:
        heapq.heappush(hq,i)

while hq:
    #print(hq)
    q=heapq.heappop(hq)
    ans.append(q+1)
    for v in G[q]:
        d[v]-=1
        if d[v]==0:
            heapq.heappush(hq,v)

if len(ans)==N:
    print(*ans)
else:
    print(-1)
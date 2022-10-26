def ll(): return list(map(int, input().split()))
import heapq

N,M,s=ll()

G=[[]for _ in range(N)]
for _ in range(M):
    a,b,c=ll()
    a-=1
    b-=1
    G[a].append((b,c))

INF=10**18

#O(MlogN)
def dik(s):
    visited=[False]*N
    cost_list=[INF]*N
    cost_list[s]=0

    hq=[(0,s)]

    while hq:
        _, pos=heapq.heappop(hq)    # 最小costのposをpop
        
        if visited[pos]:
            continue
        visited[pos]=True
        for to,cost in G[pos]:
            if visited[to]==False and cost_list[pos]+cost<cost_list[to]:
                cost_list[to]=cost_list[pos]+cost
                heapq.heappush(hq,(cost_list[to],to))
    return cost_list

cost_list=dik(s)
print(cost_list)
for i in cost_list:
    if i<INF:
        print(i)
    else:
        print("INF")
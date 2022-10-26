import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

N,M=ll()
G=[]
for _ in range(M):
    a,b,c=ll()
    G.append((c,a-1,b-1))
G.sort()

#kruskal法　最小全域木を求める
def kruskal(N,M,G):
    par=[i for i in range(N)]
    cost=0

    def root(x):    #Union-Find
        if par[x]==x:
            return x
        else:
            par[x]=root(par[x])
            return par[x]

    for i in range(M):
        c,a,b=G[i]
        ra=root(a)
        rb=root(b)
        if ra!=rb:     #頂点aと頂点ｂが繋がってなかった場合、繋げる
            par[ra]=rb
            cost+=c
    print(G)

    return cost     #グラフGの最小コスト


print(kruskal(N,M,G))
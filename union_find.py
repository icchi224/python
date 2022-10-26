def ll(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


n,q=ll()
par=[i for i in range(n)]

#Union find 2点間が連結かどうかをO(logn)で判定
def root(x):
    if par[x]==x:
        return x
    else:
        par[x]=root(par[x])
        return par[x]

for _ in range(q):
    x,y=ll()
    rx=root(x)
    ry=root(y)
    if rx!=ry:
        par[rx]=ry  #根をryに変更

print(par)

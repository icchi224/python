import bisect, collections, copy, heapq, itertools, math, sys, string
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())



"""
#N頂点M辺の無向グラフの生成と遷移O(N+M)
N,M=ll()
G=[[]for _ in range(N)]
for _ in range(M):
    u,v=ll()
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)

for i in range(N):
    for to in G[i]:

"""

"""
#順列全探索
import itertools 
for per in itertools.permutations(range(3), 3):
    for p in per:
        
"""

"""
#二分探索
import bisect
A=[-10,0,1,2,3,5,10]
a=bisect.bisect_left(A,-1)
print(a)
"""

"""
#優先度付きキュー
import heapq
hq=[(3,5),(1,0),(4,2)]
heapq.heapify(hq)
a=heapq.heappop(hq)
heapq.heappush(hq,(0,2))
print(hq)
"""

"""
#ディープコピー
import copy
a=[2,4,6,1,4,6,3]
aa=copy.deepcopy(a)
print(aa)
"""

"""
#2次元リストの1列目でソート
a=[[1,4],[0,3],[3,1],[4,6]]
aa=sorted(a, key=lambda x :x[1])
print(aa,sep="\n")
"""

"""
#format関数
n=12
a=24
print("{}: {}".format(n,a))
"""

"""
#初期化辞書
import collections
d=collections.defaultdict(int)
d[1]+=10
d[2]=100
print(min(d.keys()))
for key,value in d.items():
    print(key,value)
"""


"""
#リストの要素1でソート
from operator import itemgetter
a=[[1,9],[2,1],[3,0]]
a.sort(key=itemgetter(1))
print(a)
"""

"""
#出現回数カウント、辞書型で管理
import collections
a=[1,2,2,3,4]
b=[1,2]
cnt=collections.Counter(a)
cnt2=collections.Counter(b)
print(cnt-cnt2,cnt2-cnt)
"""

"""
#modの世界で÷aするときは *a^{-1}をする (aの逆元を掛ける)
def pow_inv(a,mod):     #aの逆元を計算
    return pow(a,mod-2,mod)
mod=998244353
a=2
ans=(6*pow_inv(a,mod))%mod  #6÷a
print(ans)
"""

"""
print(string.ascii_lowercase)
print(string.ascii_uppercase)
"""
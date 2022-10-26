import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

#座標圧縮 sortすることでNまで圧縮
N=4
X=[10,100,100000,100000000]
Y=[10,100,100000,100000000]

Xdict = {x:i for i,x in enumerate(X,1)}
Ydict = {y:i for i,y in enumerate(Y,1)}

print(Xdict)
print(Ydict)
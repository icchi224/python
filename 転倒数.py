import bisect, collections, copy, heapq, itertools, math, sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

#BIT
class BinaryTrie:
    #最大の要素は 2**30まで
    def __init__(self, max_query=2*10**5, bitlen=30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen

    # xの挿入
    def insert(self,x):
        pt = 0
        for i in range(self.bitlen-1,-1,-1):
            y = x>>i&1
            if self.nodes[2*pt+y] == -1:
                self.id += 1
                self.nodes[2*pt+y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] += 1
 
    # 昇順x番目の値
    def kth_elm(self,x):
        x+=1
        pt, ans = 0, 0
        for i in range(self.bitlen-1,-1,-1):
            ans <<= 1
            if self.nodes[2*pt] != -1 and self.cnt[self.nodes[2*pt]] > 0:
                if self.cnt[self.nodes[2*pt]] >= x:
                    pt = self.nodes[2*pt]
                else:
                    x -= self.cnt[self.nodes[2*pt]]
                    pt = self.nodes[2*pt+1]
                    ans += 1
            else:
                pt = self.nodes[2*pt+1]
                ans += 1
        return ans

    # x以上の最小要素が昇順何番目か
    def lower_bound(self,x):
        pt, ans = 0, 0
        for i in range(self.bitlen-1,-1,-1):
            if pt == -1: break
            if x>>i&1 and self.nodes[2*pt] != -1:
                ans += self.cnt[self.nodes[2*pt]]
            pt = self.nodes[2*pt+(x>>i&1)]
        return ans

X=[2,2,1,1]

#転倒数 O(NlogN)
def inversion_number(X):
    bt = BinaryTrie()
    N=len(X)
    res=0
    for i in range(N):
        bt.insert(X[i])
        print(X[i],"より大きい数字の数",i+1-bt.lower_bound(X[i]+1))
        #BITに入れた数-これまででた数字でxより小さい数字の数 
        #  = これまでにでたxより大きい数
        res+=(i+1-bt.lower_bound(X[i]+1))
    return res

ans=inversion_number(X)
print(X,"の転倒数は",ans)
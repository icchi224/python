import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

#BIT
class BinaryTrie:
    #最大の要素は 2**60 > 10**18 までいける
    def __init__(self, max_query=2*10**5, bitlen=60):
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
 
bt = BinaryTrie()
bt.insert(5)
bt.insert(100)
x=50
bt.insert(x)
y=5
p = bt.lower_bound(y)
print(y,"以上の値は昇順",p,"番目")
print(p,"番目の値は",bt.kth_elm(p))
a=0
print(a,"番目の値は",bt.kth_elm(a),)

"""
bt=[5,50,100]
    0, 1, 2  番目
"""
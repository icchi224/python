import bisect, collections, copy, heapq, itertools, math, sys, string
from operator import itemgetter
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())

#BIT (Fenwick Tree)
class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)   
    def add(self, i, x):    #i番目にxを加算
        while i <= self.size:
            self.tree[i] += x
            i += i&-i
    def sum(self, i):       #1～i番目までの総和
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i&-i
        return s
    def bisect_left(self, x):
        l = s = 0
        for i in range(self.size.bit_length(), -1, -1):
            r = l+(1<<i)
            if r <= self.size and s+self.tree[r] < x:
                s += self.tree[r]
                l += 1<<i
        return l+1, s

bit = BinaryIndexedTree(100)    #長さNのBITを作成
for i in range(1,11):
    bit.add(i,i)
a=bit.sum(2)
b=bit.bisect_left(15)
print(a)
print(b)
import bisect, collections, copy, heapq, itertools, math, sys, string
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())

N=5

# 調和級数 O(NlogN)
for i in range(1, N+1):
    x = [0]
    for j in range(i, N+1, i):
        x.append(j)

    print(x)
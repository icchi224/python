import bisect, collections, copy, heapq, itertools, math, sys, string
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())

# ランレングス圧縮
S = "aabbccc"
S_num = [[S[0], 0]]
for s in S:
    if s == S_num[-1][0]:
        S_num[-1][1] += 1
    else:
        S_num.append([s, 1])

print(S_num)
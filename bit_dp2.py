import bisect, collections, copy, heapq, itertools, math, sys, string
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())

# bitDP O(2^N * N*N)
# 頂点1から始まってN頂点すべて通り終える時間

N = ii() 
INF = 10**1

dp = [[INF]*N for _ in range(1<<N)]
dp[1][0] = 0 # 初期位置

cost = 1    # 頂点間の距離

for bit in range(1, 1<<N):      
    for pos in range(N):
        if dp[bit][pos] == INF:
            continue    # 訪れていないならcontinue

        for to in range(N):
            if (bit>>to)&1:
                continue    # 次に行く場所がすでに訪れた場所ならcontinue
            
            next = bit|(1<<to)
            dp[next][to] = min(dp[next][to], dp[bit][pos]+cost)
            
for d in dp: print(d)
print(min(dp[-1]))
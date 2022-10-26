import bisect, collections, copy, heapq, itertools, math, sys, string
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())


# ダブリング
# N頂点の円環グラフでK回いった先がどの頂点か求める
# 前処理O(N*M) 位置を求めるO(M)

N = 5
K = 5
M = 60  # 2**60, 10**18先まで見れる
dp = [[0]*5 for _ in range(M)]

for i in range(N):
    dp[0][i] = (i+3)%N

for i in range(1,M):
    for j in range(N):
        dp[i][j] = dp[i-1][dp[i-1][j]]

# ノードpos から K 行った先
def find(pos, K):
    for i in range(M):
        if (K>>i) & 1:
            pos = dp[i][pos]
    return pos

for d in dp:
    print(d)

print(find(0 , K))
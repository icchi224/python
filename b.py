import bisect, collections, copy, heapq, itertools, math, sys, string
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())

N = 100

#3の倍数ver
def get_prime(limit):
    if limit < 2:
        return [1] # 1を含める
    primep = [True]*(limit+1)

    # 3以上の奇数のみを順番に見ていく
    for n in range(3, int(limit ** 0.5) + 1 , 2):
        if primep[n] == True:
            # 素数の奇数倍のみ書き換えすればOK
            for i in range(n * 3, limit + 1, n * 2):
                primep[i] = False
    return [2] + [p for p in range(3, limit+1, 2) if primep[p]==True] #1を含める

prime = get_prime(N)
print(prime)
x = bisect.bisect_left(prime, 13)
print(x)
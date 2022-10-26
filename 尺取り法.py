import bisect, collections, copy, heapq, itertools, math, sys, string
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())


# 尺取り法 O(N)
N = 12
M = 10
A = list(range(12))

# 合計が M 以下になる最大の長さ 
ans = 0
right = 0
x = 0   # 合計の保存用
for left in range(N):
    while right < N and x + A[right] <= M:
        x += A[right]
        right += 1

    print(left, right, x)
    ans = max(ans, right - left)

    if left == right:
        right += 1
    else:
        x -= A[left]

print(A)
print(ans)
import bisect, collections, copy, heapq, itertools, math, sys, string
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
def ii(): return int(input())

# x以上の最小値の数の位置
def bsct(lst, x):
    ans = bisect.bisect_left(lst, x)
    if ans == N:
        ans = -1
    return ans

# x未満の最大の数の位置
def binary_search(lst, x):
    ac = 0
    wa = len(lst)
    while ac + 1 < wa:
        #print(ac, wa)
        mid = (ac + wa) // 2
        if lst[mid] < x:
            ac = mid
        else:
            wa = mid
    return ac

N, x = 1000, 13
A = [2, 3, 5, 7, 11, 13]
ans1 = bsct(A,x) - 1
ans2 = binary_search(A, x)
print(ans1)
print(ans2)
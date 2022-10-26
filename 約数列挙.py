import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

N=int(input())

#約数列挙 O(√n)
def yakusu(n):
    res=set()
    i=1
    while i*i<=n:
        if n%i==0:
            res.add(i)
            res.add(n//i)
        i+=1
    return res

print(yakusu(N))
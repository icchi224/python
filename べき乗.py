import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

a,n=ll()
mod=1000000007

#a^bを計算する　O(logn)
def beki(a,n,mod):
    res=1
    while n>0:
        print(n)
        if n&1:
            res=res*a%mod
        a=a*a%mod
        n>>=1
    return res

print(beki(a,n,mod))
print(pow(a,n,mod))
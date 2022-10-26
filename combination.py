import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))
mod=1000000007
n,k=ll()

#二項定理C(n,k)
#前処理O(n)
def com_init(n,mod):
    for i in range(2,n+1):
        fac[i]=fac[i-1]*i%mod # i!の計算
        inv[i]=mod-inv[mod%i]*(mod//i)%mod
        finv[i]=finv[i-1]*inv[i]%mod    #i^{-1}!の計算
    return

#計算O(1)
def com(n,k,mod):
    return fac[n]*(finv[k]*finv[n-k]%mod)%mod

fac=[1]*(n+1)
finv=[1]*(n+1)
inv=[1]*(n+1)

com_init(n,mod)
ans=com(n,k,mod)
print(fac)
print(ans)

#二項定理mod無し
def com_nk(n,k):
    u,d=1,1
    for i in range(n,n-k,-1):
        u*=i
    for i in range(1,k+1):
        d*=i
    return u//d

#print(com_nk(n,k))

#二項定理dp
def com_dp(N,K):
    r=N-K

    dp=[[0]*(K+1) for _ in range(r+1)]
    dp[0][0]=1
    for i in range(r+1):
        for j in range(K+1):
            if i>0:
                dp[i][j]+=dp[i-1][j]
            if j>0:
                dp[i][j]+=dp[i][j-1]

    for i in range(r+1):
        print(dp[i])
    return dp[-1][-1]

print(com_dp(n,k))


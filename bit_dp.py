import sys
sys.setrecursionlimit(1000000000)
def l(): return list(map(int, input().split()))

# bitDP メモ化再帰で遅い

INF=10**18
V,E=l()
dp=[[INF]*V for _ in range(V)]
for i in range(E):
    s,t,d=l()
    dp[s][t]=d

mem={}
end=(1<<V)-1
def bit_dp(bit,pos):
    if (bit,pos) in mem:
        return mem[(bit,pos)]
    if bit==end:
        return dp[pos][0]
    mask=1
    ans=INF
    for to in range(V):
        if mask&bit:
            mask<<=1
            continue
        ans=min(ans,dp[pos][to]+bit_dp(bit|mask,to))
        mask<<=1
    mem[(bit,pos)]=ans
    return ans


ans=bit_dp(1,0)
if ans<INF:
    print(ans)
else:
    print(-1)
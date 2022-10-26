n=int(input())
R=[]
C=[]
for i in range(n):
    rc=l()
    R.append(rc[0])
    C.append(rc[1])
dp=[[10**5]*n for _ in range(n)]
bool_list=[[False]*n for _ in range(n)]
for i in range(n):
    dp[i][i]=0
    bool_list[i][i]=True


def area_dp(i,j):
    if i==j or bool_list[i][j]:
        return dp[i][j]
    for k in range(i,j):
        dp[i][j]=min(dp[i][j],area_dp(i,k)+area_dp(k+1,j)+R[i]*C[k]*C[j])
    bool_list[i][j]=True
    return dp[i][j]

print(area_dp(0,n-1))

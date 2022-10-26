import sys
sys.setrecursionlimit(10**9)
def l(): return list(map(int, input().split()))

n=int(input())

#素因数分解 O(√n)
def sobunkai(n):
    l=[1]   #1を含める
    for i in range(2,int(n**0.5)+1):
        while n%i==0:
            n//=i
            l.append(i)
    if n!=1:
        l.append(n)
    return l

print(*sobunkai(n))


#高速な素因数分解
#前処理O(NloglogN)+素因数分解O(logN)
def get_prime(limit):   #エラトステネスの篩
    for n in range(2, int(limit ** 0.5) + 1):
        if primep[n] == n:
            for i in range(n * 2, limit + 1, n):
                primep[i] = n
    #print(primep)
    return [p for p in range(1,limit+1) if primep[p]==p] #1を含める

def sobunkai_fast(a):
    l=[1]   #1を含める場合
    #l=[]   #1を含めない場合
    while a>1:
        l.append(primep[a])
        a//=primep[a]
    return l

primep=[i for i in range(n+1)]
get_prime(n)
lst=sobunkai_fast(n)
print(lst)
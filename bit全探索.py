import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))


#bit全探索2**N乗の状態数
N=int(input())

for bit in range(1<<N):
    bool_list=[False]*N
    for i in range(N):
        if 1&(bit>>i):
            bool_list[i]=True
    print(bool_list)
#1～nまでの素数を列挙  O(N*lognlogn)
n=int(input())

"""
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
    return [1,2] + [p for p in range(3, limit+1, 2) if primep[p]==True] #1を含める

a=get_prime(n)
print(a)
"""


# エラトステネスの篩 2の倍数ver
def get_prime2(limit):
    # nが素数なら、primep[n]==Trueとする配列を準備
    primep = [True] * (limit + 1)
    # 2～limitの平方根まで順番に見ていく
    for n in range(2, int(limit ** 0.5) + 1):
        # nが素数と確定したら、その倍数を全て素数から除外
        if primep[n] == True:
            for p in range(n * 2, limit + 1, n):
                primep[p] = False
    # 最後に素数だけを取り出す
    return [p for p in range(1,limit + 1) if primep[p]==True]

b=get_prime2(n)
print(b)
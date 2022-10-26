def ll(): return list(map(int, input().split()))
import bisect

N=int(input())
a=ll()

#LIS　O(NlogN)
def LIS_gen(a):
    LIS=[a[0]]
    for aa in a:
        if LIS[-1]<aa:
            LIS.append(aa)
        else:
            ind=bisect.bisect_left(LIS,aa)
            LIS[ind]=aa
        print(LIS)
    return len(LIS)

print(LIS_gen(a))
import sys
sys.setrecursionlimit(10**9)
def ll(): return list(map(int, input().split()))

#等差数列の和、初項a、公差d、項数n
def tousa_sum(a,d,n):
    return (2*a+(n-1)*d)*n//2


import math

def lstprod(n):
    lst = []
    for i in range(n):
        lst.append(i)
    lst.pop(1)
    lst.pop(0)
    return lst



def sieve(lon):
    for n in lon:
        for n1 in lon:
            if n1%n==0 and n1!=n:
                lon.remove(n1)
    return lon

print(sieve(lstprod(110000))[10000])
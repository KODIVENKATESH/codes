def binery(n):
    assert int(n)==n,'must be integer'
    if n==0:
        return 0
    else:
        return n%2+10*binery(int(n/2))
n=int(input())
print(binery(n))

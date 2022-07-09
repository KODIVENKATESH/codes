def febnoci(n):
    assert n>=0 and int(n)==n ,'enter postive'
    if n in [0,1]:
        return n
    else:
        return febnoci(n-1)+febnoci(n-2)
n=int(input())
print(febnoci(n))

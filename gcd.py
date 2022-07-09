def gcd(a,b):
    assert int(a)==a and int(b)==b,'only postive'
    if a<0:
        a*=-1
    if b<0:
        b*=-1
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b=map(int,input().split())
print(gcd(a,b))

def power(base,exp):
    assert exp>=0 and int(exp)==exp,'only postive'
    
    if exp==0:
        return 1
    else:
        return base*power(base,exp-1)
base,exp = map(int,input().split())
print(power(base,exp))

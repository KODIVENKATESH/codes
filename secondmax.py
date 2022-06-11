k=[3,5,4,7,8,8]
k.sort()
for i in k:
    if i==k[-1]:
        k.remove(i)
print(k[-2]) 

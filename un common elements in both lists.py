l1=[[1,2],[3,4],[5,6]]
l2=[[3,4],[5,7],[1,2]]
k=[]
for i in l1:
    if i not in l2:
        k.append(i)
for i in l2:
    if i not in l1:
        k.append(i)        
print(str(k))
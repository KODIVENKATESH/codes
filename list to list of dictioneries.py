l1=["Gfg",3,"is",8]
l2=["name","id"]
m=[]
for id in range(0,len(l1),2):
    m.append({l2[0]:l1[id],l2[1]:l1[id+1]})
print(m)    



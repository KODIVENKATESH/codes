l=[['a','b',1,2],['c','d',3,4],['e','f',5,6]]
m=dict()
for i in l:
   m[tuple(i[:2])]=tuple(i[2:])
print(m)    

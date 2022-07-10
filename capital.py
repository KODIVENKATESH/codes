def capital(arr):
      k=[]
      
      if len(arr)==0:
        return k
      k.append(arr[0].upper())
      return k+capital(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capital(words)) 
   
    
        

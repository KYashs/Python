n =5 
print("1. Square")
for i in range(n):
    for j in range(n):
        print( '*' , end= ' ')

    print()        
print("--------------")

print("2. Increasing Triangle")
n = 5

for i in range(n):
    for j in range(i+1):
        print('*' , end=' ')

    print()        
print("--------------")
n = 5 
print("3. Decreasing Triangle")
for i in range(n):
    for j in range(i,n):
        print( '*',end= ' ')

    print()        
print("--------------")
n = 5
print("4. Inverse Triangle")
for i in range(n):
    for j in range(i,n):
        print(' ',end= ' ')
    for j in range(i+1):
        print( '*',end= ' ')    
    print()    
print("--------------")

n = 5
print("5. Mirror Inverse Triangle")

for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i, n):
        print('*',end=' ')
    print()                
print("--------------")

n = 5

for i in range(n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')        
    print()
print("--------------")

n = 5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ') 
    for j in range(i,n-1):
        print('*',end=' ')        
    for j in range(i,n):
        print('*',end=' ')
    print()   
     
print("--------------")

n = 5
for i in range(n-1):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')        
    print()

for i in range(n): 
   for j in range(i+1): 
      print(' ', end=' ') 
   for j in range(i,n-1):
      print('*', end=' ')
   for j in range(i, n):
      print('*', end=' ')
   print()
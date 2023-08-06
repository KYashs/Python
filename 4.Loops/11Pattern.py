n = 5

for i in range(n):
    for j in range (i,n):
        print('*', end= ' ')
    print()            

for i in range(n):
    for j in range(i+1):
        print('*' , end=' ')

    print() 
print("--------------")    

for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i, n):
        print('*',end=' ')
    print() 
for i in range(n):
    for j in range(i,n):
        print(' ',end= ' ')
    for j in range(i+1):
        print( '*',end= ' ')    
    print()    




print("--------------")    


# Upper Triangles
r =5
for i in range(1, r+1):
    print(" *"*i, end=" ")
    print("  "*(r-i)*2, end=" ")
    print(" *"*i)

# Lower Triangles
for i in range(r,0,-1):
    print(" *"*i, end=" ")
    print("  "*(r-i)*2, end=" ")
    print(" *"*i) 



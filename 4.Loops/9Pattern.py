
row =5

for i in range(0,row):
    for col in range(0,row):
        print("* " ,end= "")
    print()    

row =5

for row in range(0,row):
    for col in range(0,row):
        print("* " ,end= "")
    print()    

print("--------------")

row =5

for row in range(row,0,-1):
    for col in range(0,row):
        print("# " ,end= "")
    for col in range(row,0,-1):
        print("* " ,end= "")    
    print()    


row = 5

for i in range(0,row,1):
    for j in range(row):
        print("* ", end="")

print()

print("--------------")
row = 5

for i in range(row):
    for j in range(row):
        print("*", end=" ")

    print()    


print("--------------")
n= 5

for i in range(n):
    for j in range(i,n):    
        print("*", end=" ")

    print()    
print("--------------")
n= 5

for i in range(n):
    for j in range(i,n):    
        print("#", end=" ")
    for j in range(i+1):
        print("*", end=" ")        


    print()    

print("--------------")
n= 5

for i in range(n):
    for j in range(i+1):    
        print("#", end=" ")
    for j in range(i,n):
        print("*", end=" ")        


    print()    




print("Right angled Triangle")
for row in range (5):
    for col in range(row):
        print("* ", end= "")
    
    print()    


print("--------------")
print("Inverted Right angled Triangle")
for rows in range (5,0,-1):
    for cols in range(rows):
        print("* ", end= "")
    
    print()    

print("--------------")
print(" Inverted 90 angled Triangle")
for rows in range (5,0,-1):
    for cols in range(rows):
        print("* ", end= "")
    for col in range(5):
        print(" ", end = "")        
    
    print()  

# for row in range (0,5,1):
#     for col in range(1,row):
#         print("@ ", end = "")
#     for col in range(1,row):
#         print("*", end = "")
    
#     print() 
# for row in range(0,5,1):
#     for col in range(row):
#             print("# ", end="" )
#     print()            

print("--------------")

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
        print("* " ,end= "")
    print()    

print("--------------")

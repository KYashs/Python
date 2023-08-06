print("Calculator Program")
a = input("Enter value of A")
b = input("Enter value of B")

print("Enter the Function you want to perform")
c =input('''
1)Addition
2)Subtraction
3)Multiplication
4)Division
5)Mod
''')
        
# if c ==1:
#     {
#         add()
#     }       

# elif c==2:
#     {

#     }   
# elif c==3:
#     {
        
#     }   
# elif c==4:
#     {
        
#     }   
# elif c==5:
#     {
        
#     }   
# else:
#     {
#         print("No proper operations opted.")
#     }   

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b


def div(a,b):
   return a/b

def mod(a,b):
   return a%b

print("You have chosen  Arithmetic Function")
print("The output of the operation is:")   
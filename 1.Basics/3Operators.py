print("Arithmetic Operations")
a = 50
b = 25

print(a+b)
print(a-b)
print(a*b)
print(a/b) #when we divide the numbers we always get floating point decimal values

print("-----------------------------")

print("Assignment Operators")

c = 45
d = 40

c+=12
print(c)

d-=12
print(d)
#we can do this with every arithmetic operation

print("-----------------------------")

print("Comparison Operators")

e = 52.99
f = 45.75
g = 52.99
h = (e>f)
_h = (e<f)
__h = (e==g)
___h = (e!=f)
print(h)
print(_h)
print(__h)
print(___h)
# we expect bool values from this comparison(T/F)

print("-----------------------------")

print("Logical Operation")
# and,or,not are the three logical operations basically gates
i = True
j = False
k = (i and j)
_k = (i or j)
__k = (not i)
print(k)
print(_k)
print(__k)

# and = only return true if both of variable are true otherwise false HINDI(ORR) CONDITION i and j then only true
# or = if any of the value is true then we will get true HINDI(YAA)
# not = inverse of the bool function HINDI(ULTA)
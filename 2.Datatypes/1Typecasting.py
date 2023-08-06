print("TYPECASTING: It is a way for changing the variable datatype if possible. Example: Below from String to Int")
a = "4570"
print(type(a))

# print(a +10) Error: can only concatenate str (not "int") to str

b = int(a)
print(type(b)) #Now a is changed to Integer
print(b +10)
# Rule of typecasting must be followed as we cannot do like a ="20bcs4570" so it will not be casted to integer 
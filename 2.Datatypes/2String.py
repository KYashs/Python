a = 45
# Rules of String Declarations
b = 'Suyash'       #single quoted
c = "KYash's new Album"        #double quoted
d = '''Baby Keem's Album Names
1) The Melodic Blues
2) DIE FOR MY B***H
3) The Sound of Bad Habbit'''   #triple quoted [We us this in multiple line string]

print(a)
print(b)
print(c)
print(d)

print("----------------")

print("String Slicing: Slicing the string means breaking into parts")

#In py we don't have the concept of Character
#Characters are single piece of String as 'a' is a Character
# In Slicing we use (Array concept numbering system) and the first character is appointed as 0.
#[] = indexes
#[:] = 
e = ("Kendrick")
print(e[0])
print(e[1])
print(e[2])
print(e[3])
print(e[2:8])  #[index_Start : index_End] will print 'ndric' as index gives from (1,2) 
#[:4] = [0;4]
#[2:] = [2:last_index]
#Negative Indexes: We count from backwards like and we start with 1.
print(e[-6:-1])

print("----------------")

print("String Slice with Skip values")
print(e[1:6:1])
#[1(from) :6(till):1(with skip value of 1)]
f = e[0::2]
print(f)

print("----------------")

print("Concatenation of Sting")
# 16 by Baby Keem 
Lyrics1 = "Born into status,"
Lyrics2 = "tell nobody that you never had it"

Line1 = (Lyrics1+Lyrics2)
print(Line1)

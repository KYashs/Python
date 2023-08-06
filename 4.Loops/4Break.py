# BREAK : "It will break the loop if the if condition satisfies"

for j in range(1,5,1):
    if j== 3:
        break

    print(f"Hello {j}")

# --------------
#  For a toffee wending machine we have 10 toffee and user order more than 10 will get notice of Out of Stock

stock = 10
ask = int(input("Number of toffee you want: "))

i = 1

while i <= ask:

    if i> stock:
        print("Out of Stock")
        break    

    print("Toffee")
    i +=1

print("Bye")    
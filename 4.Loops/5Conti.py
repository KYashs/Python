# CONTINUE : "Ignore the particular if statement"


for j in range(1,5,1):
    if j== 3:
        continue

    print(f"Hello {j}")

# --------------
# Print the number which are not divisible from 3 and 5

for i in range(1,15,1):
    if (i%3 ==0):
        continue

    print(i)

print("Bye")


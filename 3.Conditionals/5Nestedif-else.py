height = int( input ("What is your Height?"))

if height>=3 :
    print("Congratulation! You you are eligible to ride Roller-Coster")
    age = (int(input("What is your age?")))
    if age>=18:
        print("You have to pay 250 for the ride. Thank You!")
    else:
        print("You are not an adult so the concession price is 200")
else:
    print("You are not eligible for the ride.")            
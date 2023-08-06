height = int( input ("What is your Height?"))
if height>=3 :
    print("Congratulation! You you are eligible to ride Roller-Coster")
    age = (int(input("What is your age?")))
    if age>=18:
        print("You have to pay 250 for the ride. Thank You!")
    else:
        print("You are not an adult so the concession price is 200")

    picture = bool (input("0 for no and 1 for yes"))
    if picture == False :
        print("No charge")
    elif picture == True:
        print("You have 50 extra to pay ")    
    
else:
    print("You are not eligible for the ride.")  
              
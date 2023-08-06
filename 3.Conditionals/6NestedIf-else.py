year = (int(input("Year")))

if (year%4==0):
    print("may be a leap year, we are doing final test")
    if(year%100==0):
        print("may be a leap year, we are doing final test")
    if(year%400==0):
        print("This is a leap year")
    else:
        print("This is not a leap year")
else:
    print("The year is not leap year")


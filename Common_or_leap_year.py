year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
	exit()
	
elif year >= 1582:
    print("This year falls into the Gregorian era.")
    
    if year % 4 >= 1:
        print("It is a common year.")

    elif year % 100 >= 1:
        print("It is a leap year.")
    
    elif year % 400 >= 1:
        print("It is a common year.")

    else:
        print("It is a leap year.")

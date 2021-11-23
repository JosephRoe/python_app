# To get year (integer input) from the user
# This is my first explanation
year = int(input("Enter an acceptable year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year.".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year.".format(year))
else:
    print("{0} is nottttt a leap year.".format...
(year))

year = int(input("Enter Year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

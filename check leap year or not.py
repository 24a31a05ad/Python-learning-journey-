n=int(input("enter a year:"))
print("leap year" if n%400 == 0 or n%4 == 0 and n%100!=0 else "not a leap year" )
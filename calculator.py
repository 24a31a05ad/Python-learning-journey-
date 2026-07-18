a=int(input("enter a value:"))
b=int(input("enter b value "))
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=int(input("enter your choice:"))
if choice==1:
	c=a+b
	print(c)
elif choice==2:
	d=a-b
	print(d)
elif choice==3:
	e=a*b
	print(e)
elif choice==4:
	f=a/b
	print(f)
else:
	print("invalid choice,please try again")
import random
choices=["rock","paper","scissors"]
computer=random.choice(choices)
user_choice=input("enter a rock ,paper or scissors:")
print("your choice:",user_choice)
print("computer choice:",computer)
if computer==user_choice:
	print("Tie")
elif (user_choice=="rock"and computer=="scissors"or
user_choice=="paper"and computer=="rock"or
user_choice=="scissors"and compute=="paper"):
	print("youu winnn!")
else:
	print("computer win!!")
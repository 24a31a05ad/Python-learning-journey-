import random
computer_num=random.randint(1,100)
while True:
  user_num =int(input("enter a num:"))
  if computer_num == user_num:
	   print("congrats")
	   break
  elif computer_num < user_num:
 	  print("it is high")
  elif computer_num > user_num:
	   print("it is low")
  else:
	  print("invalid num")
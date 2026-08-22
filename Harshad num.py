# Check Harshad Number

num = int(input("Enter a number: "))
original = num
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

if original % sum_digits == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
# Check Spy Number

num = int(input("Enter a number: "))

sum_digits = 0
product_digits = 1

while num > 0:
    digit = num % 10
    sum_digits += digit
    product_digits *= digit
    num //= 10

if sum_digits == product_digits:
    print("Spy Number")
else:
    print("Not a Spy Number")
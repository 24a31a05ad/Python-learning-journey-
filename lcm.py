# Find LCM of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = max(a, b)

while lcm % a != 0 or lcm % b != 0:
    lcm += 1

print("LCM:", lcm)
d1 = int(input("Enter the first digit of the number:"))
d2 = int(input("Enter the second digit of the number:"))
d3 = int(input("Enter the third digit of the number:"))
num = int(input("Enter your number:"))

if d1>9:
    print("Input a smaller number")
if d2>9:
    print("Input a smaller number")
if d3>9:
    print("Input a smaller number")
if num>999:
    print("Input a smaller number")

e1 = d1**3
e2 = d2**3
e3 = d3**3

if e1 + e2 + e3 == num:
    True
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a amstrong number")


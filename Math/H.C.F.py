num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 > num1:
    mn = num1
else:
    mn = num2
for i in range(1, mn + 1):
    if num1 % i == 0 and num2 % 1 == 0:
        hcf = i
print(f"H.C.F is {hcf}")
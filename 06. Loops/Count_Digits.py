x = int(input("Enter the number x: "))
res = 0
while x > 0:
    x = x // 10
    res = res + 1
print("Count of Digit is", res)

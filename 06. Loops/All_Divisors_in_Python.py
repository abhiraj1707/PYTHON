#Using for loop
n = int(input("Enter the number : "))
for x in range(1, n + 1):
    if n % x == 0:
        print(x)



#Using while loop
n = int(input("Enter the number : "))
x = 1
while x <= n:
    if n % x == 0:
        print(x)
    x = x + 1
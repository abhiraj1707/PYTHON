#Optimization if all Divisors and Prime
n = int(input("Enter the number: "))
for x in range(1, n + 1):
    if n % x == 0:
        print(x)



#Optimized Solution for all Divisors
n = int(input("Enter the number: "))
x = 1
while x * x < n:
    if n % x == 0:
        print(x)
        print(n/x)
    x = x + 1
if x * x == n:
    print(x)



#Prime Checking Optimized
n = int(input("Enter the number: "))
if n <= 1:
    print("No")
else:
    x = 2
    while x * x <= n:
        if n % x == 0:
            print("No")
            break
        x = x + 1
    else:
        print("Yes")
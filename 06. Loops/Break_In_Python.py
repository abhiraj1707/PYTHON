#Using for loop
n = int(input("Enter a number :"))

for x in range(2, n + 1):
    if n % x == 0:
        print(f"{x} is a factor of {n}.")
        break



#Using while loop
n = int(input("Enter a number: "))
x = 2

while x <= n:
    if n % x == 0:
        print(f"{x} is a factor of {n}.")
        break
    x += 1


i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i = i + 1
print(i)
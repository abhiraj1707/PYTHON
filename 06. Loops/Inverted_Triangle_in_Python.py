n = int(input("Enter the number : "))
for i in range (n):
    for j in range (n - i):
        print("*", end = " ")
    print()
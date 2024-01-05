a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if(a >= b) and (a >= c):
    print(a,"is largest number")

if(b >= a) and (b >= c):
    print(b,"is largest number")

if(c >= a) and (c >= b):
    print(c,"is largest number")


"""
2nd Method
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a >= b:
    if a >= c:
        print(a,"is largest number")
    else:
        print(c,"is largest number")

else:
    if b >= c:
        print(b,"is largest number")
    else:
        print(c,"is largest number")    

"""
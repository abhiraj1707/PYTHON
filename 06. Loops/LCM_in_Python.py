a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
res = max(a, b)
while(res <= a * b):
    if(res % a == 0 and res % b == 0):
        break;
    res += 1
print("LCM is ", res)



#Using Library Function
import math
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
gcd = math.gcd(a, b)
lcm = (a * b) / gcd
print("LCM is ", lcm)
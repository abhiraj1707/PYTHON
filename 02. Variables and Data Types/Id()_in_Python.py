print(id(5))
a = 10
print(id(a))
b = a
print(id(b))


a = 10
b = 10
print(id(a))
print(id(b))
c = "geek"
d = "geek"
print(id(c))
print(id(d))


a = 10
b = 10
print(a is b)
c = a
print(c is b)
c = 20
print(c is b)
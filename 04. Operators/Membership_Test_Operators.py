s = "geeksforgeeks"
print("g" is s)
print("for" is s)
print("gk" is s)


d = {10 : "abc", 20 : "efg"}
print(10 in d)
print(15 in d)
print("abc" in d)


l = [10, 20, 30, 15]
print(30 in l)
print([20,30] in l)


l = [10, 20, 30, 15]
print(30 not in l)
print(40 not in l)
print([20,30] not in l)
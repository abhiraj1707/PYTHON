#Program : 01
d = {110 : "abc", 101 : "xyz", 105 : "pqr"}
print(d)
d = {}
d["Laptop"] = 40000
d["Mobile"] = 15000
d["Earphone"] = 1000
print(d)
print(d["Mobile"])


#Program : 02
d = {110 : "abc", 101 : "xyz", 105 : "pqr"}
print(d.get(101))
print(d.get(125))
print(d.get(125, "NA"))
if 125 in d :
    print(d[125])
else:
    print("NA")


#Program : 03 
d = {110 : "abc", 101 : "xyz", 105 : "pqr", 106 : "bcd"}
d[101] = "wxy"
print(len(d))
print(d)
print(d.pop(105))
print(d)
del d[106]
print(d)
d[108] = "cde"
print(d.popitem())
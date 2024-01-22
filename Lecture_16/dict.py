# dictionary (iterable)

#*************** How to create dict object **************
# d1 = {102:"Rahul",105:"Payal",106:"Arjun",107:"Prachi"}
# print(type(d1))
# print(d1)

# d2 = {} # empty dict
# print(type(d2))
# print(d2)

# d3 = dict() # empty dict
# print(type(d3))
# print(d3)

# d4 = dict(102="Rahul",105="Payal") #SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
# print(d4)

# d4 = dict(r="Rahul",p="Payal")
# print(type(d4))
# print(d4)




#**************** Accessing dict elements ********************
d1 = {102:"Rahul",105:"Payal",106:"Arjun",107:"Prachi"}

# print(d1)
# print(d1[102],d1[105],d1[106],d1[107])

# for k in d1:
#     print(k)

# for k in d1:
#     print(k,d1[k])


# Editing dict element
# d1[102] = 'Ravi'
# d1[103] = 'Dilip'
# print(d1)

# del d1[103]
# print(d1)


# ************** dict methods **************
d1 = {102:"Rahul",105:"Payal",106:"Arjun",107:"Prachi"}

print(d1.keys(),"\n")
print(d1.values(),"\n")
print(d1.items(),"\n")

for t in d1.items():
    k=t[0]
    d=t[1]
    print(k,d)
print("\n")

# using unpacking
for t in d1.items():
    k,d = t
    print(k,d)
print("\n")

# we also write it as
for k,d in d1.items():
    print(k,d)



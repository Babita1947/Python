d1 = {102:"Rahul",105:"Payal",106:"Arjun",107:"Prachi",103:"Dilip"}

# print(len(d1))
# print(min(d1))
# print(max(d1))
# print(sum(d1))
# print(sorted(d1))  # sorted function always returns sorted list
# print(d1)


# ********* comparision operator **********

d2 = dict(r='Rahul',p='Payal')
d3 = dict(p = 'Payal',r = "Rahul")
d4 = dict(r="Rahul")

# print(d2 == d3)
# print(d3 != d4)


# ************ dict object methods ************[pop(key), popitem(), clear()]
# print(d1.pop(106))
# print(d1)
# print(d1.popitem())
# print(d1)

# ***************** dict comprehension *********************
d = {a:a**2 for a in range(1,8,1)}
print(d)
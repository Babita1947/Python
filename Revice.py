# l1 = [20,40,50]
# a,b,c=l1 # unpacking
# print(l1)

# x=11
# y=12
# z=13
# l2=[x,y,z]
# print(l2)

# len(),min(),max(),sum(),sorted() ----------> Built in methods

# print(len(l1))
# print(min(l1))
# print(max(l1))
# print(sum(l1))
# print(sorted(l1))

# l1 = list("mysirg")
# print(l1)
# l2 = list([10,29,11])
# print(l2)
# l3 = list(range(1,20,1))
# print(l3)

# print(l1+l2)


# l4 = [[1,2,3],[4,5,6],[7,8,9]]
# for i in l4:
#     for j in range(len(i)):
#         print(i[j],end=" ")
#     print("\n")

######## list comprehension ###########
# n = int(input("Enter a number : "))
# odd_num = [2*i-1 for i in range(1,n+1)]
# print(odd_num)

# s1 = "mysirg education services"
# s2 = s1.split(' ')
# print(s2)
# print(' '.join(s2))
# print('_'.join(s2))
# s2 = input("Enter a number separated by ,")
# l1 = s2.split(',')

# l2 = [int(x) for x in l1]
# print(l2)

# Slicing operator
# s1 = "mysirg education services private limited"
# l = [str(i)  for i in s1.split(' ')]
# s2 = l[::-1]
# print(' '.join(s2))




thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5:1])
# print(thislist[:thislist.index('kiwi'):])
# print(thislist[2::1])
# print(thislist[3:thislist.index('mango'):1])
# print("apple" in thislist)
# thislist[thislist.index("banana")] = "blackcurrant"
# thislist[thislist.index("cherry")] = "watermelon"
# print(thislist)
# thislist[1:3] = ["watermelon"]
# print(thislist)
# thislist.append("guave")
# thislist.insert(1,"itli")
# print(thislist)
# thislist.remove("banana")
# print(thislist)
# thislist.remove(thislist[-1])
# print(thislist)
# del(thislist[0])
# print(thislist)
# thislist.clear()
# print(thislist)

# t1 = (11,2,30,50,50)

# print(t1[0::1])
# print(t1[::-1])




# for i in t1:
#     print(i,end=" ")
# print("\n")
# print(t1[-1])

# print(sorted(t1,reverse=True))

# print(t1.index(50))
# print(t1.count(50))


# thistuple = ("apple", "banana", "cherry") 
# print(thistuple[::1])
# print(len(thistuple))
# print(thistuple[1])
# print(thistuple[-1])
# addtuple = ("orange", "kiwi", "melon", "mango")
# thistuple = thistuple + addtuple
# print(thistuple)
# print(thistuple[2:5:1])
# print(thistuple[:thistuple.index("kiwi")])
# print(thistuple[thistuple.index("cherry")::])
# print(thistuple[-4:-1:1])
# print("apple" in thistuple,"'apple' is in the fruits tuple")

# tuplelist = list(thistuple)
# del tuplelist[0]
# modifiedtuple  = tuple(tuplelist)
# print(modifiedtuple)

# for i in modifiedtuple:
#     print(i,end=" ")
# print("\n")
# i = 0
# while i<=len(modifiedtuple):
#     print(thistuple[i],end=" ")
#     i += 1
# print("\n")
# tuple2 = (1,2,3,2,3)
# tuple3 = thistuple + tuple2
# print(tuple3[::1])

# print((tuple2)*2)
# print(tuple3.count(2))
# print(tuple3.index(2))

# set1 = {20,10,50,20,30,50,20,10}
# print(len(set1))
# print(min(set1))

# s1 = {8,1,5}
# s2 = {1,5,8,10}
# print(s1.issubset(s2))

d1 = {19:"Babita",20:"Barsha"}
d2 = dict(a=10,b=11)
print(d1)
print(d2)


d3 = dict(a='Babita',b='Barsha')
print(d3)  

d3['b'] = "Anisha"
print(d3)

d3['c'] = "Pankaj"
print(d3)

# del d3['b']
# print(d3)

print(d3.items())
print(d3.keys())
print(d3.values())
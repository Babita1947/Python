# l1 = [50,20,45,100,90,90,40,70,60,10]

# del l1[3]
# print(l1)

# l1.append(10)
# print(l1)

# l1.insert(3,35)
# print(l1)

# l1.remove(90) # not return anything 
# print(l1)

# l1.pop() #also return that element which is deleted
# print(l1)

# # l1.clear()
# # print(l1)

# l1.reverse()
# print(l1)

# i=l1.index(35)
# print(i)

# y = l1.index(100) if 100 in l1 else '100 is not in the list'
# print(y)


l2 = [50,20,45,100,90,90,40,70,60,50,20,45,100,90,90,40,70,60]
# x=l2.count(90)
# print(x)

# l3=sorted(l2)   # Sorted function is built in methods not list method that's why we can't call by using object.method()
# print(l3)

# l4=sorted(l2,reverse=True)
# print(l4)

l2.sort()
print(l2)
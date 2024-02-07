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
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.remove(thislist[-1])
print(thislist)
del(thislist[0])
print(thislist)
thislist.clear()
print(thislist)
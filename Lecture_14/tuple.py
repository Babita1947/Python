# t1 = (1,2,5,7)
# print(t1)
# print(type(t1))

# l1 = [11,22,33,44]
# print(l1)
# print(type(l1))

# l2 = [11,22,44,]
# print(type(l2))

# t2 = ()  # empty tuple
# print(t2)
# print(type(t2))

# t3 = (10)  # it seems like single element of tuple but it is not tuple ,it is int type 
# print(type(t3))

# # To make single element tuple 
# t4 = (11,)
# print(type(t4))

# t5 = 11,22,13,14,15 # tuple can also be written like this
# print(type(t5))

# t6 = 11,22,13,14,15,
# print(type(t6))

# print(l1[0])
# print(l1[1])
# print(l1[2])
# print(l1[3],"\n")
    
    
# r = range(10,20,1)
# print(r[0])
# print(r[1])
# print(r[2])
# print(r[3])
# print(r[-1])

# Accessing tuple elements using for loop

# t1 = (1,2,5,7)

# for i in t1:
#     print(i,end=" ")

# print("\n")


# using while loop
# i = 0
# while(i<len(t1)):
#     print(t1[i],end=" ")
#     i+=1

################ built-in-methods ##############

# t1 = (1,11,21,31,41,51)
# print(len(t1))
# print(min(t1))
# print(max(t1))
# print(sum(t1))
# print(sorted(t1))  # sorted() ---> return list of sorted elements
# print(sorted(t1,reverse=True))

############## concatenation and repetition operator :
# t1 = (10,20)
# t2 = (11,22,33)
# print(t1+t2)
# print(t1*3)

############ comparision operator ############
# t1 = (10,20)
# t2 = (11,33,55)
# print(t1>t2)
# print(t1==t2)

############ tuple object methods #############
# t1 = (1,2,5,7,55,55,19)
# print(t1.index(5))
# print(t1.index(1))

# print(t1.count(55))
# print(t1.count(19))

############## slicing operator ################
# t1 = (10,4,3,2,9,1,3,4,5)
# print(len(t1))
# print(t1[2:8:2])
# print(t1[::-1])

########### user input ###############
t1 =  tuple([int(e) for e in input("Enter lists : ").split(',')])


print(t1)




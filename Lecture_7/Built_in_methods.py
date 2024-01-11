# l1 = [50,20,45,100,90,90,40,70,60]

# print(len(l1))
# print(max(l1))
# print(min(l1))
# print(sum(l1))
# print(sorted(l1)) 
# print(l1)

# l2 = [10,4.5,3+4j]
# # print(max(l2)) #Give error because relational operator does not work on Complex data type
# print(sum(l2))
# print(len(l2))
# l2.append('ab')
# #print(sum(l2))  #TypeError: unsupported operand type(s) for +: 'complex' and 'str'


# ########## List Method ##############
# l3 = list()
# l3 = list(10,20,30) # Give error because only one argument you can paas in list method 
# l3 = list(10)  # Give error because only one argument which is passed that must be iterable type and in this the passing argument is int type that why give error

# l3 = list(range(4))
# print(l3)

# l3 = list('mysirg')
# print(l3)


######### Comparision Operator on List ##########
# l1 = [1,2,3]
# l2 = [2,3,1]
# l3 = [1,2,3,4,5]
# l4 = [1,2,3]

# print(l1==l4)
# print(l1==l2)
# print(l1==l3)

# print(l1[0] == l2[2])

# print(l1 > l2)

############# Concatenation Operator ##################
# l1 = [1,5,9]
# l2 = [2,3,1]
# l3 = l1+l2 
# l1 = l1+l2
# print(l1)


############# Repetition Operator ##################
l1 = [2,5]
l2 = l1*5
print(l2)
l3 = ["babita",19,42.5]
print(l3*4)
print(l3)


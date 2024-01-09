# How to create list object ?

# l1 = [10,20,30,40] # list of same type of element
# print(type(l1))

# l2 = [40,True,4.5,3+4j,'MySirG'] # Heterogeneous list
# print(type(l2))

# l3 = []   # Empty list
# print(type(l3))

### How to access list elements ?

# l1 = [50,20,80,10,60,40]
# print(type(l1))

# print(l1)
# print(l1[0])
# print(l1[0],l1[1])
# print(l1[5],l1[1])

### Concept of negative indexing ?
# l1 = [50,20,80,10,60,40]
# print(l1[-1])
# print(l1[5])

# print(l1[4])
# print(l1[-2])

### Accessing list elements via for loop

# l1 = [50,20,80,10,60,40]
# for i in l1:
#     print(i,end=" ")
# print("\n")


### Accessing list elements via while loop
    
# l1 = [50,20,80,10,60,40]
# i = 0
# while i<=5:
#     print(l1[i],end=" ")
#     i += 1


### HOW TO DELETE AN ELEMENT FROM THE LIST?

# l1 = [50,20,80,10,60,40]
# del l1[2]

# for i in l1:
#     print(i,end=" ")

### How to edit an element of the list?
# l1 = [50,20,80,10,60,40]
# l1[2] = 45

# for i in l1:
#     print(i,end=" ")

# l1[4] = 90
# # for i in l1:
# #     print(i,end=" ")
# l1[6] = 70
# for i in l1:
#     print(i,end=" ")  ## IndexError: list  assignment index out of range

### How to add more element in the list ?
l1 = [50,20,45,10,90,40]
l1.append(70)
l1.insert(3,100)

l1.insert(25,60)
print(l1)
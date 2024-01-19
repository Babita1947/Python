thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# a.  Return the third, fourth, and fifth item
# print(thislist[2:5:1],end=" ")
# print("\n")

# i=2
# while i<5:
#     print(thislist[i],end=" ")
#     i += 1

# b.  items from the beginning to, but NOT including, "kiwi"
# print(thislist[ :thislist.index("kiwi"): ],end=" ")
# print("\n")

# c. display the items from "cherry" to the end
# print(thislist[thislist.index("cherry")::],end=" ")
# print("\n")

# d. display the items from "orange" (-4) to, but NOT including "mango" (-1):
# print(thislist[thislist.index("orange"):6:],end=" ")
# print("\n")

# e. Check if "apple" is present in the list
# print("apple" in thislist)
# print("\n")

# f. Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"

# thislist[1:3] = ["blackcurrant","watermelon"]
# print(thislist,end=" ")
# print("\n")

# or

# thislist[thislist.index('banana')] = "blackcurrant"
# thislist[thislist.index('cherry')] = "watermelon"
# print(thislist)

# g. Change the second and third value by replacing it with one value "watermelon"
# thislist[1:3] = ["watermelon"]
# print(thislist,end=" ")
# print("\n")


# h. Insert "watermelon" as the third item
# thislist.insert(2,"watermelon")
# print(thislist,end=" ")
# print("\n")

# i. Using the append() method to append an item "guava"
# thislist.append("guava")
# print(thislist,end=" ")

# j. Insert "guava" as the second position using insert() method
# thislist.insert(1,"guava")
# print(thislist,end=" ")
# print("\n")

# k. Remove "banana"
thislist.remove("banana")
print(thislist,end=" ")
print("\n")
# l. Remove the second item
del thislist[1]
print(thislist,end=" ")
print("\n")

# m. Remove the last item
thislist.pop()
print(thislist)
print("\n")

# n. Remove the first item using del() method
del thislist[0]
print(thislist,end=" ")
print("\n")

# o. Delete the entire list
# del thislist
# print(thislist)

# p. Clear the list content
thislist = []
print(thislist)
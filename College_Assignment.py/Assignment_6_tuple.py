# Given tuple
thistuple = ("apple", "banana", "cherry")

# a. Print the number of items in the tuple
print("Numbers of items in the tuple : ",len(thistuple))

# b. Print the second item in the tuple
print("Second item in the tuple : ",thistuple[1])

# c. Print the last item of the tuple
print("Last item of the tuple : ",thistuple[-1])

# d. Add "orange", "kiwi", "melon", "mango" at the end of thistuple 
# [NOTE: Tuples are immutable that's why it doesn't contain append() in its tuple class] 
newtuple = ("orange", "kiwi", "melon", "mango")
thistuple = thistuple + newtuple
print(thistuple,end=" ")
print("\n")

# e. Return the third, fourth, and fifth item
print(thistuple[2:5],end=" ")
print("\n")

# f. Return the items from the beginning to, but NOT included, "kiwi"
print(thistuple[:4:],end=" ")

# g. Return the items from "cherry" and to the end
print("g. Items from 'cherry' to end:", thistuple[thistuple.index("cherry"):])  # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# h. Return the items from index -4 (included) to index -1 (excluded)
print("h. Items from index -4 to -1:", thistuple[-4:-1])  # Output: ('cherry', 'orange', 'kiwi')

# i. If "apple" is present in the tuple, then print “Yes, 'apple' is in the fruits tuple”
if "apple" in thistuple:
    print("i. Yes, 'apple' is in the fruits tuple")

# j. Remove "apple" (Tuples are immutable, so we cannot modify them)
# You can create a new tuple with the desired items removed.
thistuple = tuple(item for item in thistuple if item != "apple")
print("Updated thistuple:", thistuple)

# k. Iterate through the items and print the values using a for loop
print("k. Iterate through items:")
for item in thistuple:
    print(item)

# l. Print all items by referring to their index number
print("l. Print all items by index:")
for i in range(len(thistuple)):
    print("Index", i, ":", thistuple[i])

# m. Print all items, using a while loop to go through all the index numbers
print("m. Print all items using while loop:")
index = 0
while index < len(thistuple):
    print(thistuple[index])
    index += 1

# n. tuple2 = (1, 2, 3, 2, 3); print tuple3 by joining tuple2 with thistuple (thistuple first then tuple2)
tuple2 = (1, 2, 3, 2, 3)
tuple3 = thistuple + tuple2
print("n. Joined tuple3:", tuple3)

# o. Print the items of tuple2 in question 2(o) twice
print("o. Items of tuple2 twice:", tuple2 * 2)

# p. Print the number of times the value 2 appears in the tuple in question 2(o)
print("p. Number of times 2 appears in tuple2:", tuple2.count(2))

# q. Search for the first occurrence of the value 2 and return its position in question 2(o)
print("q. First occurrence of 2 in tuple2:", tuple2.index(2))

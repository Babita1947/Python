# s1 = {40, 10, 20, 30}
# print(s1)

# # The add method modifies s1 in place and returns None
# s1.add(60) # add(int)
# print(s1)

# s1.add((11,22,33)) # add(iterable)
# print(s1)

# s1.update([1,2,3])  # update(iterable)
# print(s1)

# s2 = {'babita',19,11,2002,}
# s2.update('XYZ','RWS')
# print(s2)

# s2.remove('babita')
# print(s2)

# s2.discard(2002)
# print(s2)

# ********** Difference between remove() and discard()

# s3 = {40,11,(11,22,33),20,60,30}
# # s3.remove(100) # KeyError: 100
# # print(s3)  

# s3.discard(100) # does't give error whether the discarded element is present or not 
# print(s3) 

# print(s3.pop())
# print(s3)
# s3.clear()
# print(s3)

set1 = {8,1,5}
set2 = {8,10,2}
print(set1.intersection(set2))
print(set1.union(set2))

set3 = {1,5,8,10}
print(set1.issubset(set3))

print(set3.issuperset(set1))
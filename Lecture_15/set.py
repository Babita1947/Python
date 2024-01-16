# How to create set object ?
s1 = {1,5,8} # order can't be predict
#print(type(s1))
#print(s1)
#print(s1)

s2 = {10,2,8,10,10,8,} # can't store duplicate values
#print(s2) # {10,2,8} order may change

s3 = {} # not empty set
#print(s3) 
#print(type(s3)) # <class 'dict'>

s3 = set() # empty set
#print(type(s3))

# s4 = set(10,20,30) # TypeError: set expected at most 1 argument, got 3
# print(s4)

# s4 = set(10) # TypeError: 'int' object is not iterable

s4 = set({10,20,20,13,13}) # argument passing in set function must be one and that argument must be ***iterable*** .
#print(s4)

s4 = set([10,20,11,11,1,11,12,12]) # here iterable is list
#print(s4)

s4 = set('Babita') # here iterable argument is str
#print(s4)

s4 = set("MySirG") # argument str type
#print(s4)


# ********* Accessing set elements ***********
set1 = {40,10,20,30,}
# for e in set1:
#     print(e,end=" ")

set2 = {11,11,11,55,55,19}
# for e in set2:
#     print(e,end=" ")



# ********* Built-in-methods *********
print(len(set2))
print(min(set2))
print(max(set2))
print(sum(set2))
print(sorted(set2)) # sorted() function always return a list of sorted order.


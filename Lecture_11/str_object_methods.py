# Str object methods
# s1 = "mysirg education services"

# print(type(s1))
# print(len(s1))
# print(s1.index('i'))
# print(s1.index('sir'))
# print(s1.count('i'))
# print(s1.count(' '))
# print(s1.startswith('my'))
# print(s1.endswith('services'))

# s2 = 'a123'
# print(s2.isdigit())
# s2 = '123'
# print(s2.isdigit())
# print(s1.islower())
# print(s1.isupper())

# print(s1.upper())
# print(s1)
# print(s1.replace('m','M'))
# print(s1.replace('i','I',s1.count('i')-2))
# print(s1.replace('i','I'))


############## format() ###########
# a,b = 10,20
# s3 = "Sum of {} and {} is {}"
# print(s3)
# print(s3.format(a,b,a+b))

# s3 = "Sum of {2} and {1} is {0}"   ###### This is wrong accessing the element
# print(s3.format(a,b,a+b))

# print("{}, how are you ?".format("Saurabh"))
# print("{},{},{}".format("One",25,3.5))
# print("{2},{0},{1}".format(10,20,30))

############# split() and join() ###############

# s1 = 'mysirg education services private limited'
# print(s1.split(' '))

# s2 = input("Enter numbers separated by comma :")
# l1 = s2.split(',')  # list of strings
# print(l1)

# convert list l1 elements in int form using list comprehension
# l2 = [int(x) for x in l1]  # list of strings converted into numbers
# print(l2)

# or 
# l2 = [int(x) for x in s2.split(',')]
# print(l2)
# l2 = [int(x) for x in input("Enter numbers separated by comma: ").split(',')]
# print(l2)


######## join() ########
# l1 = ["Mysirg", "education", "services", "private","limited"]
# print(l1)
# print(type(l1))
# strobject = ' '
# print(strobject.join(l1))
# print(type(strobject.join(l1)))


l1 = ["Mysirg", "education", "services", "private","limited"]
print(l1)
print(type(l1))
print('-'.join(l1))
print(type('-'.join(l1)))
# Write a python script to remove duplicate elements from a list. l1 = [20,10,50,20,30,50,20,10]

l1 = [20,10,50,20,30,50,20,10]
print(list(set(l1)))

#### Using list comprehension #######
print(list(set([int(i) for i in input("Enter list elements separated by comma : ").split(',')])))

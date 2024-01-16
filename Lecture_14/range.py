############## check how to [for loop] and [while loop] working in range iterable sequence  ################
# for i in range(10,20,1):
#     print(i,end=" ")

# i = 0
# while i in range(10,20,1):
#     print(i,end=" ")
#     i+=1

# Accessing tuple elements using while loop
t1 = (10,20,30,40,10,10,55,55,11,11)
i = 0
while i<len(t1):
    print(t1[i],type(t1[i]),sep="  -->  ")
    i += 1
print(type(t1))

###### tuple objects ######
i=0
while i<len(t1):
    print(t1[i],t1.index(t1[i]),t1.count(t1[i]),sep="-")
    i += 1
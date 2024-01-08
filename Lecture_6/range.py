# 1. range(end) // Print 0 to 9

# n = int(input("Enter a number : "))
# for i in range(n):
#     print(i,end=" ")

# 2. range(beg,end)  // print beg to end -1

# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     print(i,end=" ")

# Accessing Range Elements :

r = range(2,10,3)

for i in r:
    print(i,i**2)


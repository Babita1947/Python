# Write a program script to swap data of two variables.

x = int(input("Enter a number "))
y = int(input("Enter a number "))

# temp = x
# x = y
# y = temp
# print("After swapping = ",x,y)

x = x-y
y = x+y
x = y-x
print("After swapping = ",x,y)

# Q_10. Write a python script to calculate LCM of two numbers.

print("Enter two numbers : ")
a = int(input())
b = int(input())

L = max(a,b)

while L <= a*b:
    if L % a == 0 and L % b == 0:
        break
    L += max(a, b)

print("LCM =", L)   
 
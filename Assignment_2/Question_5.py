# Q_5. Write a python script to calculate factorial of a number.
n = int(input("Enter a number : "))
i = 1
fact = 1

if n==0 and n==1 :
    print(n,"! = ",fact)
while i<=n:
    fact *= i
    i += 1
print(fact,end=" ")

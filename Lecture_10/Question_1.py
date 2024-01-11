# Q_1. Create a list of first n odd natural numbers where n is given by user.

n = int(input("Enter a number: "))
oddNumbers = [2*i+1 for i in range(n)]

print("First ",n,"odd natural numbers = ",end=" ")
print(oddNumbers)
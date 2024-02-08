# def is_duck_number(n):
#     num = str(n)
#     if '0' in num[1::]:
#         return True
#     else:
#         return False

# # Test the function
# number = int(input("Enter a number to check if it's a duck number: "))
# if is_duck_number(number):
#     print(f"{number} is a duck number.")
# else:
#     print(f"{number} is not a duck number.")


num = input("Enter a number")
if '0' in num[1::]:
    print("True")
else:
    print("False")
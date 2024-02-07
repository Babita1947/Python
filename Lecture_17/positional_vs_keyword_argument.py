def f1(a,b):
    print("a = ",a,"b = ",b)

# f1(2,3) # positional argument
# f1(b=2,a=3) # keyword argument
    
# f1(2,a=3) # TypeError: f1() got multiple values for argument 'a'
    
f1(2,b=3)
# f1(a=2,3) #SyntaxError: positional argument follows keyword argument


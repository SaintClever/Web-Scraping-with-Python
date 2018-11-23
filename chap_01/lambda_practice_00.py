# we say a is a variable
x = lambda a : a
print(x(4))
print('')

# Whatevers on the left side must be on the right
x = lambda a, b : a + b
print(x(5, 2)) # argument a = 5, b = 2
print('')

x = lambda a, b, c: a + b + c + 10
print(x(2, 5, 3))
print('')

def myFunc(n):
    return lambda a : a * n
myDouble = myFunc(2)
print(myDouble(11))
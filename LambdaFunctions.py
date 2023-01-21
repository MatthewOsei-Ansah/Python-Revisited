# Lambda functions
# Essentially a single line function
# lambda parameter:expression
y = lambda x: x + 1
print(y(11))

adder = lambda a, b: a + b
print(adder(1, 1))

# Some functions want other functions as arguments for example sort([1,5,2,3,4],function) Python wants you to pass
# in another function to tell it how to sort the list, this is usually in the form of lamda

# Another case is graphical user interfaces. Buttons for example would be assigned a lambda function as a button
# would only return a single value like 5

# Exercise
# Create a lambda function that accepts 1 integer argument
# If the integer is > 5 return hello otherwise return goodbye

func = lambda num: "hello" if num > 5 else "Good Bye"
print(func(3))

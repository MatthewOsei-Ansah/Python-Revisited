# Dictionaries store data but things are more organised since each value has a key
# Example dictionary : test_dict = {key:value}
# You cannot duplicate keys you will loose the first key, in other words you overwrite them

# Basics
test_dict = {'A': 123, 'B': [1, 2, 3], 1: True}
print(test_dict)

print(type(test_dict.values()))  # This is a whole different data type know as dictionary values

print(test_dict.keys())  # Returns all the keys from a dictionary

print(test_dict.items())  # Returns the dictionary as separate tuples

print(len(test_dict))  # Returns the length of a dictionary

# Converting a dictionary
print(list(test_dict))  # Returns the dictionary as a list

print(str(test_dict))  # Returns the string a string

# Indexing with dictionaries
# These are both identical in function but if you use the get method and the key is not found you get none as the output
# The same cannot be said for the first method as it will crash when the key is not found
print(test_dict['A'])
print(test_dict.get('A'))

# Exercise using the update method, add another key value pair to the dictionary

C = {'Colour': 'Blue'}
test_dict.update(C)

# Can also edit old key pairs
test_dict.update(A=456)

# Or use it to make additional entries
test_dict.update(D=789)

# Another way to add stuff to a dictionary
test_dict['E'] = 100

Dict = { ' Tim': 18,  'Ben': 25,}
print(Dict)
#
# More than one entry per key is not allowed ( no duplicate key is allowed)
# The values in the dictionary can be of any type, while the keys must be immutable like numbers, tuples, or strings.
# Dictionary keys are case sensitive- Same key name but with the different cases are treated as different keys in Python dictionaries.

print("DICTIONARY ===== MAP in JAVA")

my_dict = {} #empty dictionary
print(my_dict)
my_dict = {1: 'Python', 2: 'Java'} #dictionary with elements
print(my_dict)

my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)
print("===changing element in Dict")
my_dict['Second'] = 'C++' #changing element
print(my_dict)

print("===adding element in Dict")
my_dict['Third'] = 'Ruby' #adding key-value pair
print(my_dict)

my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
a = my_dict.pop('Third') #pop element
print('Value:', a)
print('Dictionary:', my_dict)
b = my_dict.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict)

print("============accessing elements of dictionary")
print(my_dict.keys()) #get keys
print(my_dict.values()) #get values
print(my_dict.items()) #get key-value pairs
print(my_dict.get('First'))

my_dict.clear() #empty dictionary
print('n', my_dict)
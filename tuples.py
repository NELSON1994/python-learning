Tup = ('Jan','feb','march')
print(Tup)

print("empty tuple/ new tuple")
tup1 = ();

print("---tuple for single element")
Tup1 = (50,);

tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print("---elements access in  a tupple")
print(tup1[0])

print("---accessing elements in a given range")
print(tup2[1:4])

print("---comparing tuples")
a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.items()
print(b)

#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print(x[2:4])

print("=====>>>> accessing elements")
my_tuple2 = (1, 2, 3, 'edureka') #access elements
for x in my_tuple2:
    print(x)
print(my_tuple2)
print(my_tuple2[0])
print(my_tuple2[:])
print(my_tuple2[3][4])

print("------>>> appending elements")
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5, 6) #add elements
print(my_tuple)
# Declare a variable and initialize it
f = 100
print (f)
# re-declaring the variable works
f = 'Moses vin'
print (f)

a="Barding"
b = 99
print(a+ " " +str(b))

# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print(f)
someFunction()
print(f)


print("============use of global")
f = 101;
print(f)
# Global vs.local variables in functions
def someFunction1():
  global f
  print(f)
  f = "changing global variable"
someFunction1()
print(f)

print("=======deleting variable")
valf = 11;
print(valf)
del valf
print(valf)
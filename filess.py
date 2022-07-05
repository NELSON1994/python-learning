# reading inputs and keyboard values
# str = raw_input("Enter your input: ")
# print("Received input is : ", str)
import os

str1 = input("Enter your input: ")
print("Received input is : ", str1)

# Opening and Closing Files

# Open a file
fo = open("nelson.txt", "w+")
print("writing to the file")
fo.write("Python is a great language.\nYeah its great!!\n")

fo1 = open("nelson.txt", "r+")
str2 = fo1.read(10);
print("Read String is : ", str2)


print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
# print("Softspace flag : ", fo.softspace)

# Close opened file
fo.close()
print(" file closed done")

# Rename a file from test1.txt to test2.txt
os.rename("nelson.txt", "test2.txt")

# Delete file test2.txt
os.remove("text2.txt")

# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

# This would give location of the current directory
os.getcwd()

# This would  remove "/tmp/test"  directory.
os.rmdir("/tmp/test")
























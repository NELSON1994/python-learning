userNumber=input("Enter your best Number :  \n")
print(f" user number is : {userNumber}")

print("----.. casting the input to int")

intval=int(userNumber)

print("---> conditonal check for the value")
if intval <0:
    print("The number entered is Negative")
elif 0 < intval < 8:
    print("----> good value")

else:
    print("The number is positive")


print(" && ==== and in python and || === or in python")
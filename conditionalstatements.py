userNumber = input("Enter your best Number :  \n")
print(f" user number is : {userNumber}")

print("----.. casting the input to int")

intval = int(userNumber)

print("---> conditonal check for the value")
if intval < 0:
    print("The number entered is Negative")
elif 0 < intval < 8:
    print("----> good value")

else:
    print("The number is positive")

print(" && ==== and in python and || === or in python")


def switchcase(val):
    switcher = {
        val < 0: " value is less than Zero ",
        0 < val < 10: " value greater than 0 but less than 10 ",
        val < 100: " value less than 100 ",
    }
    print(switcher.get(val, "nothing"))
    return switcher.get(val, "nothing")


switchcase(68)

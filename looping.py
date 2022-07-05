print("================== WHILE LOOP")
val = input("Enter a number")
val2 = int(val)


def check():
    try:
        initd = 6
        while val2 > initd:
            print(val2 - initd)
            print(f"value entered is : {val}")
            initd = initd + 1

    except Exception:
        print("---->  Not A number")


check()

list1 = {3, 4, 5, 6, 7, 8}

def forloop():
    for val in list1:
        print(f"value is : {val * 4}")


forloop()



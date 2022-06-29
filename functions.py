def calculateAll():
    val = 2 * 4 * 4
    print('the value is : {val}')
    print('the value is :' + str(val))
    print(f"value is : {val}")


calculateAll()


def calculateAll2(val):
    print('the value is : {val}')
    print('the value is :' + str(val))
    print(f"value is : {val}")


calculateAll2(7899)


def calculateAll3(val):
    print('the value is : {val}')
    print('the value is :' + str(val))
    print(f"value is : {val}")
    response = "Nelson"
    return response


res = calculateAll3(67)
print(res)

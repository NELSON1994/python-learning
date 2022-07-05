def checkvalidate(value):
    try:
        value2 = value / 2
        print(value2)

    except Exception:
        print("Invalid value given")


checkvalidate("nel")
checkvalidate(78)

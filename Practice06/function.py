def command(loc, zip, dist, end):
    if loc:
        code = input("Enter a ZIP Code to lookup")

    elif zip:
        city = input("Enter a city name to lookup")
        state = input("Enter the state name to lookup")

    elif dist:
        code1 = input("Enter first ZIP Code")
        code2 = input("Enter first ZIP Code")

    elif end:
        exit()
    else:
        print("Неверная команда")
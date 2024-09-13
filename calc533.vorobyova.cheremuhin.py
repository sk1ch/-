while True:
    x = int(input("Введите число: "))
    v = input("Введите операцию (+, -, *, /): ")
    y = int(input("Введите 2-е число: "))
    if v == "+":
        result = (x + y)
        print(result)
    elif v == "-":
        result = (x - y)
        print(result)
    elif v == "*":
        result = (x * y)
        print(result)
    elif v == "/":
        if y != 0:
            result = (x / y)
            print(result)
        else:
            print ("На ноль делить нельзя!")
    exit = str(input("Выйти (yes) или (no): "))
    if exit == "yes":
        print("Выход...")
        break

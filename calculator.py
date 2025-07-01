def gum(a, b):
    return a + b

def han(a, b):
    return a - b

def bazm(a, b):
    return a * b

def baj(a, b):
    return a / b

def num():
    while True:
        try:
            number = float(input("Մուտքագրեք թիվ: "))
            return number
        except ValueError:
            print("Խնդրում եմ մուտքագրեք միայն թիվ։")

def choice():
    ch = ("+", "-", "/", "*")
    c = input('Ընտրեք գործողություն՝ "+", "-", "/", "*": ')
    if c not in ch:
        print("Թույլատրվում են միայն հետևյալները՝", ch)
        c = input('Նորից փորձեք՝ "+", "-", "/", "*": ')
    else:
        return c

def result():
    x = num()
    c = choice()
    y = num()
    if c == "+":
        return gum(x, y)
    elif c == "-":
        return han(x, y)
    elif c == "*":
        return bazm(x, y)
    elif c == "/":
        try:
            return baj(x, y)
        except ZeroDivisionError:
            print("Գործողություն 0-ով բաժանելը հնարավոր չէ։")
            y = num()

print(result())

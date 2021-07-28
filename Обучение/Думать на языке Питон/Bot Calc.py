def calc():
    try:
        result = eval(input())
    except SyntaxError:
        pass
    print(result)
    calc()


print(calc())



def test():
    a = 10
    return a
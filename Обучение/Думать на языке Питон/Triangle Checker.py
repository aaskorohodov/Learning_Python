import time

def is_triangle(a,b,c):
    if (a + b) < c or (b + c) < a or (c + a) < b:
        print('Треугольник не получается')
        time.sleep(1)
        s()

    else:
        print('Треугольник получается')
        time.sleep(1)
        s()

def s():
    sides = input('Введите 3 стороны через пробел:').split(' ')
    if len(sides) < 3 or len(sides) > 3:
        print('Опаньки, надо ввести именно 3 числа и именно через пробел. Попробуйте снова.')
        s()
    try:
        a = int(sides[0])
        b = int(sides[1])
        c = int(sides[2])
    except ValueError:
        print('Опаньки, надо ввести именно 3 числа и именно через пробел. Попробуйте снова.')
        s()
    a = int(sides[0])
    b = int(sides[1])
    c = int(sides[2])
    print(a,b,c)
    is_triangle(a, b, c)

s()
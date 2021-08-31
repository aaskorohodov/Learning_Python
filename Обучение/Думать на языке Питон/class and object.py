import copy
import math


class Point:
    '''Так создается класс'''


p1 = Point()
p2 = Point()
'''Так создаются объекты этого класса'''

p1.x = 3
p1.y = 5
p1.z = 100

p2.x = 3
p2.y = 7
'''Так задаются атрибуты объектам и значения (атрибуты = x, y, z; значения = цифры'''



def print_point(p):
    '''Так печатаются значения. При том ниже показано, как вызвать эту функцию (подставляется объект)'''
    return p.x, p.y

#print_point(p1)
#print_point(p2)



def distance_between_points(p1, p2):
    '''Это работа со значениями объектов. Считает растояние между точками. Объект = точка, у точки 2 атрибута (значения)'''

    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

#print(distance_between_points(p1, p2))


class Rectangle(object):
    '''Класс прямоугольников'''


box = Rectangle()
'''Объект класса прямоугольников'''

box.width = 100.0
box.height = 200.0
'''Атрибуты со значениями'''

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
'''А так отрибут класса Прямоугольник ссылается на объект класса Точка.'''


def find_center(rect):
    '''Ищет середину прямоугольнка, зная положение нижнего-левого угла и размер прямоугольника.'''
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

centre = find_center(box)

print(f'исходный {print_point(centre)}')


def move_rectangle(rect, xm, ym):
    '''Смешает прямоугольник. Для этого принимает объем Прямоугольник и на сколько сместить угол.'''
    rect.corner.x += xm
    rect.corner.y += ym


move_rectangle(box, 1, 1)

centre = find_center(box)

print(f'исходный подвинутый {print_point(centre)}')


def move_rectangle_copy(rect, xm, ym):
    '''Создает копию объекта Прямоугольник и затем двигает его. модуль copy.deepcopy куопирует и сам объект Прямоугольник,
    и вложенный объект Точка. Если сделать обычный copy, то скопируется только Прямоугольник, а точка останется ссылкой,
    то есть меняя точку в одном объекте, она будет меняться и в другом, с которого снята копия.'''
    box2 = copy.deepcopy(rect)
    box2.corner.x += xm
    box2.corner.y += ym
    return box2


box2 = move_rectangle_copy(box, 10, 10)

centre2 = find_center(box2)

print(f'копия {print_point(centre2)}')

print(f'снова исходный {print_point(centre)}')
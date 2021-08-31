my_string = 'hello(that means smth). How Are you (that also() means smth)'
my_string2 = '(()())'


def brackets_checker(my_string):
    count = 0
    for i in my_string:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

        if count < 0:
            return False
    return True

print(brackets_checker(my_string2))
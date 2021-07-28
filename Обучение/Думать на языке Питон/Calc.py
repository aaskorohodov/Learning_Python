import time

def calc():
    res = input('Скалькулируем: ')
    if res == "done":
        print('BB :*')
        time.sleep(5)
        quit()
    try:
        print(f'Ответ: {eval(res)}\n'
              f'done = хватит')
    except SyntaxError:
        print(f'{res} некалькулируемо!')
    except NameError:
        print(f'{res} некалькулируемо!')
    calc()

calc()
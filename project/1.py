def decorator(func):
    def wrap(*args, **kwards):
        print('start')
        func(*args, **kwards)
        print('end')
    return wrap

@decorator
def con_pri(text=''):
    print('Наша функція', text)


con_pri('additional text')
# Опрацювання помилок
class FiveDivisionError(Exception):
    # Клас для демонстрації опрацювання помилок
    def __init__(self, message, error_code):
        # передаємо повідомлення до базового класу
        super().__init__(message)
        # додаємо власне поле
        self.error_code = error_code

def devide_number(a,b):
    if b == 5:
        raise FiveDivisionError('Ділення на 5 неможливе!', 400)
    return a / b

try:
    result = devide_number(4, 5)
    print(result)
except FiveDivisionError as e:
    print(e)
    print(f'Код помилки {e.error_code}')


# Заняття 6

### Робота з файлами

### [&#8678; Зміст](../index.md)

---

### Обробка винятків при роботі з файлами

Винятки (Exceptions) — це події, які виникають під час виконання програми та сигналізують про помилку або нестандартну ситуацію.  
Наприклад, відкриття неіснуючого файлу викликає виняток `FileNotFoundError`.

Python дозволяє обробляти помилки за допомогою конструкцій `try`, `except`, `else`, і `finally`:  

```python
try:
    # Код, який може викликати помилку
    # ...
except ExceptionType:
    # Код для обробки конкретного винятку
else:
    # Код, який виконається, якщо помилка не виникла
finally:
    # Код, який виконається у будь-якому випадку
```

#### Типові помилки при роботі з файлами

1. **FileNotFoundError** — файл не знайдено.
2. **PermissionError** — недостатньо прав для доступу до файлу.
3. **IsADirectoryError** — об'єкт є директорією, а не файлом.
4. **EOFError** — неочікуваний кінець файлу.
5. **ValueError** — невідповідний формат даних.


#### Обробка винятку при відкритті текстового файлу

```python
try:
    with open('data.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Помилка: Файл не знайдено.")
except PermissionError:
    print("Помилка: Недостатньо прав для доступу до файлу.")
else:
    print("Файл успішно прочитано.")
finally:
    print("Завершення операції з файлом.")
```


В Python ви можете вловити будь-яку помилку, не вказуючи конкретний тип винятку.
Для цього достатньо використати базовий клас всіх винятків – Exception.


```python
try:
    # Код, який може викликати будь-яку помилку
    x = int("abc")
    y = 10 / 0
except Exception as e:
    print(f"Сталася помилка: {e}")
```


### Робота з файлами формату JSON в Python

JSON (JavaScript Object Notation) — це популярний формат обміну даними, 
який легко читається людиною і машиною. Він часто використовується для передачі
даних між сервером і веб-додатком. У Python є вбудована 
бібліотека `json` для роботи з JSON.

#### Основні операції з JSON:

1. Серіалізація (конвертація об'єктів Python в JSON)
2. Десеріалізація (конвертація JSON в об'єкти Python)
3. Читання даних з JSON файлу
4. Запис даних у JSON файл

#### Серіалізація (Конвертація об'єктів Python в JSON)

Для серіалізації об'єктів Python, таких як словники, списки, кортежі,
у формат JSON використовується функція `json.dumps()`.

```python
import json

# Приклад словника
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "cycling", "hiking"]
}

# Серіалізація словника в формат JSON
json_data = json.dumps(data)
print(json_data)
```

#### Десеріалізація (Конвертація JSON в об'єкти Python)

Для десеріалізації JSON в об'єкти Python використовується функція `json.loads()`.

```python
import json

# Приклад JSON рядка
json_data = '{"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", "cycling", "hiking"]}'

# Десеріалізація JSON в словник Python
data = json.loads(json_data)
print(data)
```

#### Читання даних з JSON файлу

Для читання даних з JSON файлу використовується функція `json.load()`.

```python
import json

# Читання даних з JSON файлу
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
```

#### Запис даних у JSON файл

Для запису даних у JSON файл використовується функція `json.dump()`.

```python
import json

# Приклад словника
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "cycling", "hiking"]
}

# Запис даних у JSON файл
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

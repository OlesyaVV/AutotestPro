""" 
print('Hello')
olesya = 10.5
print(olesya)
# если
if olesya > 11:
    print('qwe')
# иначе если    
elif olesya < 10:
    print(100)
# иначе
else:
    print('rty')
"""
# создали массив из 4 значений
putin = [1,3,5,8]
# вывели второй элемент массива
print(putin[1])
# начинаем цикл по каждому элементу putin
for i in putin:
    if i % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")
# начинаем цикл while до тех пор, пока значение переменной равно True
pokemon = True        
while pokemon == True:
    print(pokemon)
    pokemon = False

fruits = ["яблоко", "банан", "вишня"]
for fruit in fruits:

    if fruit == "банан":
        print(f"Я люблю {fruit}")
    else:
        print(123)



battery = 3
while battery > 0:
    print("Телефон работает")
    battery = battery - 1
    print("Телефон выключился")


def greet(name):
    return f"Привет, {name}!"

message = greet("Иван")
print(message)  # Выведет: Привет, Иван!

def det(num):
    return num + 2
print(det(123))

def pop():
    print('Hello')
pop()

status_code = 200
expected_code = 200
# f-строка (начинается с f) - лучший способ форматирования для логов ошибок
print(f"Ожидался код {expected_code}, но получен {status_code}") 

ui_elements = ["Кнопка Войти", "Поле Логин", "Кнопка Забыли пароль"]
print(ui_elements[0]) # Выведет: Кнопка Войти
print("Кнопка Войти" in ui_elements) # Выведет: True (базовая проверка)



api_response = {"id": 123, "name": "Ivan", "is_active": True}
print(api_response["name"]) # Выведет: Ivan

# ВАЖНО: Используйте .get(), чтобы тест не упал с ошибкой KeyError, если ключа нет
print(api_response.get("email", "Email не найден")) # Выведет: Email не найден

pokemon = ui_elements.index('Поле Логин')
print(pokemon)

def hello(name):
    print("Hello " + name)
hello(name = 'Valya')

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print('po')

user1 = User('Olesya', 'Vostrikova')
user2 = User('Alexey', 'Rudnev')
users = [user1, user2]
for user in users:
    print(user.first_name)
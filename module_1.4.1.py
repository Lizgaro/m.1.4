# module_1_4.py

# Получаем строку от пользователя
my_string = input("Введите строку: ")

# Выводим количество символов в строке
print("Количество символов:", len(my_string))

# Работаем с методами строк:

# 1. Выводим строку в верхнем регистре
print("Верхний регистр:", my_string.upper())

# 2. Выводим строку в нижнем регистре
print("Нижний регистр:", my_string.lower())

# 3. Удаляем все пробелы из строки
my_string_no_spaces = my_string.replace(" ", "")
print("Строка без пробелов:", my_string_no_spaces)

# 4. Выводим первый символ строки
if len(my_string) > 0:  # Проверяем, что строка не пуста
    print("Первый символ:", my_string[0])

# 5. Выводим последний символ строки
if len(my_string) > 0:  # Проверяем, что строка не пуста
    print("Последний символ:", my_string[-1])
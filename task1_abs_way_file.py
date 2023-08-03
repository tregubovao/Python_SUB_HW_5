# Напишите функцию, которая принимает на вход строку - 
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: 
# путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

import os
os.system('cls')


def my_func(my_string: str) -> tuple():
    path_to_file = '/'.join(my_string.split('/')[:-1]) + '/'
    file_name = my_string.split('.')[-2].split('/')[-1]
    extansion = '.' + my_string.split('.')[-1]
    return path_to_file, file_name, extansion

my_string = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
print(my_func(my_string))


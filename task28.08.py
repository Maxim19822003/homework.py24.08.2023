# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5 3 -> 1
"""
n = int(input('Input number: '))
list_ = [1, 2, 3, 4, 5, 3]
count = 0
for i in list_:
    if list_[i] == n:
        count += 1
list_str = ' '.join(map(str, list_))  # Преобразуем список в строку
print(list_str, '->',count)
"""


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# Пример:
# 5
# 1 2 3 4 5 6 -> 5
"""
n = int(input('Input number: '))
list_ = [1, 2, 3, 4, 5, 6]
close_num = list_[0]
for num in list_:
    if abs(num - n) <= abs(close_num - n):
        close_num = num
list_str = ' '.join(map(str, list_))  
print(list_str, '->',close_num)
"""
# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет
# определеннуюценность. В случае с английским алфавитом очки
# распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного
# пользователем слова.
# Будем считать, что на вход подается только одно слово, которое
# содержит либо только
# английские, либо только русские буквы.
# Пример:
# Ввод: ноутбук
# Вывод: 12
"""
letvalues = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R',
            'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'):1,
            ('D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'):2,
            ('B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'):3,
            ('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'):4,
            ('K', 'Ж', 'З', 'Х', 'Ц', 'Ч'):5,
            ('J', 'X', 'Ш', 'Э', 'Ю'):8, ('Q', 'Z', 'Ф', 'Щ', 'Ъ'):10}
word = input('Введите слово: ')
word = word.upper()  # Приводим к верхнему регистру для сравнения
word_value = 0 # Переменная для хранения стоимости слова
for let in word: # Перебираем буквы в слове и считаем стоимость
    for group, group_value in letvalues.items():
        if let in group:
            word_value += group_value
print(f"Стоимость слова равна {word_value}")
"""

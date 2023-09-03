# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
"""
a, b = int(input('First number: ')), int(input('Second number: '))

def degree(a, b):
    if b == 0:
        return 1
    return a * degree(a, b - 1)

degreed = degree(a, b)
print(degreed)
"""
# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
"""
a, b = int(input('First number: ')), int(input('Second number: '))
def suma(a, b):  
   if b == 0:
        return a
   if a == 0:
        return b
   return suma(a + 1, b - 1)
summa = suma(a,b)        
print(summa)
"""

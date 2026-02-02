# 16. Напишите программу-фильтр, которая при нажатии любых клавиш
# выводит на экран только буквы и цифры, при этом указывая, что выводится:
# буква или цифра.

# def keypress(ch) :
#     if ch.isalpha():
#         print(f"Буква: {ch}")
#         return 0
#     elif ch.isdigit():
#         if ch == '0':
#             exit(0)
#
#         print(f"Цифра: {ch}")
#         return 0
#
#     else:
#         print("Некорректный символ. Введите букву или цифру.")
#         return -1
#
# while True:
#     ch = input("Введите символ: ")
#
#
#     if len(ch) != 1:
#         print("Пожалуйста, введите ровно один символ")
#         continue
#
#     else :
#         keypress(ch)



# 16. Найдите минимальный элемент из нечетных элементов массива,
# введенных с клавиатуры. Количество элементов вводится первым числом

# import random
#
# def minEl(arr_size) :
#     nechet = []
#     arr = []
#
#     if arr_size > 0:
#
#         i = 0
#         while i < arr_size:
#             arr.append(random.randint(-100, 100))
#             print(f"{i + 1}. {arr[i]}")
#             i += 1
#
#         for j in range(len(arr)):
#             if arr[j] % 2 != 0:
#                 nechet.append(arr[j])
#
#         if len(nechet) <= 0:
#             print("Нечетного числа в массиве нет!")
#             exit(0)
#
#         return min(nechet)
#
#     else:
#         print("Введите положительное число!")
#         exit(0)
#
#
# a = int(input("Введите количество элементов в массиве: "))
#
# print("Минимальный нечетный элемент: ", minEl(a))

#Даны три натуральных числа. Определите их наибольший общий делитель

def find_gcd_two(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def find_gcd_three(a, b, c):
    gcd_ab = find_gcd_two(a, b)

    gcd_abc = find_gcd_two(gcd_ab, c)
    return gcd_abc

print("Введите три натуральных числа:")
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Ошибка: все числа должны быть натуральными (больше нуля)!")
else:
    result = find_gcd_three(a, b, c)
    print(f"НОД({a}, {b}, {c}) = {result}")
##Прочитать из файла строку Hellow world и удалить каждый второй символ

# with open('pz10.txt', 'r') as f:
#     content = f.read()
#
# res = ''
# for i in range(0, len(content), 2):
#     res += content[i]
#
# print(res)
#
# with open('pz10.txt', 'w') as f:
#     f.write(res)


##Дан текстовый файл, в котором хранится список группы.
## Задание а) составьте программу, которая подсчитывает сколько студентов имеют одинаковое с вами имя.
## Задание б) составьте программу, которая определяет, есть ли в вашей группе однофамильцы

# myName = input("Введите ваше имя: ")
# middleName = input("Введите ваше отчество: ")
#
# with open("pz10(2).txt", "r", encoding='utf-8') as f:
#     content = f.read()
#
#
#
# count = 0
# datas = content.split()
# for i in datas:
#     if i.lower() == myName.lower():
#         count += 1
#
# print(f"\n\tОтчет составлен {middleName}ым {myName}ом")
#
# if count >= 1:
#     print(f"Количество студентов в группе с именем {myName}: {count}")
#
# else:
#     print(f"Студентов с именем {myName} в группе нет!")
#
# result = []
#
# for i in range(0, len(datas), 2) :
#     for j in range(i + 2, len(datas), 2) :
#         count = 1
#         if datas[i] == datas[j]:
#             count += 1
#             result.append(datas[i])
#             result.append(datas[i + 1] + " -")
#             result.append(datas[j])
#             result.append(datas[j + 1] + ", ")
#
#
#
# if len(result) == 1:
#     print(f"В группе есть однофамилец: {" ".join(result)}")
#
# elif len(result) > 1 :
#     print(f"В группе есть однофамильцы: {" ".join(result)}")
#
# else:
#     print("Однофамильцев в списке нет!")

# 16. Дан файл, содержащий текст, включающий русские и английские слова.
# Подсчитайте, каких букв в тексте больше ‒ русских или латинских.

with open('letters.txt', 'r', encoding='utf-8') as f:
    content = f.read()

englishLetters = 0
englishLettersData = []
russianLetters = 0
russianLettersData = []

for i in range(len(content)) :
    if (content[i] >= 'a' and content[i] <= 'z') or (content[i] >= 'A' and content[i] <= 'Z') :
        englishLetters += 1
        englishLettersData += content[i]

    if (content[i] >= 'а' and content[i] <= 'я') or (content[i] >= 'А' and content[i] <= 'Я'):
        russianLetters += 1
        russianLettersData += content[i]

allLetters = englishLettersData + russianLettersData

print("Все буквы: ", allLetters)

if englishLetters > russianLetters :
    print(f"Английские буквы: ", englishLettersData)
    print("английских букв в файле больше, чем русских букв. Их кол-во: ", englishLetters)

elif russianLetters > englishLetters :
    print(f"Русские буквы: ", russianLettersData)
    print("русских букв в файле больше чем английских. Их кол-во: ", russianLetters)

else:
    print("Количество букв в файле либо одинаковое, либо букв в файле нет. Кол-во букв в файле: ", englishLetters + russianLetters)
# 16. Дана строка. Укажите те слова, которые содержат хотя бы одну букву «К»

# input_text = input("Введите строку для поиска слов с буквой К: ")
#
# words = input_text.split()
#
# result = []
#
# for word in words:
#     if 'к' in word or 'К' in word:
#         result.append(word)
#
# print("Слова с буквой 'к':", result)

# 16. Отредактируйте заданное предложение, удалив из него те слова, которые
# встречаются в предложении заданное число раз.

input_text = input("Введите строку: ")

n = int(input("Введите число для повторяющихся слов: "))

result = []

words = input_text.split()

for w in words :
    if words.count(w) != n:
        result.append(w)


print(" ".join(result))

result1 = []

for j in words :
    if j[0] == 'а' or j[0] == 'А':
        result1.append(j)

print(result1)
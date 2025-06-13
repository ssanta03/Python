import string
l = input("Введите слово: ").lower()
l = l.translate(str.maketrans('', '',
                .punctuation)).replace(" ", "")
if l == l[::-1]:
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром!")
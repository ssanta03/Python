import collections
import string

n = input("Введите предложение: ")
clean = n.lower().translate(str.maketrans('', '', string.punctuation + '—'))
wor = collections.Counter(filter(str.isalpha, clean))
top3 = wor.most_common(3)
print("ТОП-3 самых частых букв:")
for letter, count in top3:
    print(f"{letter} – {count} раз")
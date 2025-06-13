# import pandas as pd
#
# bs = {'Alice': 'Apr1', 'Bob': 'Dec 12',
#       'Carol': 'Mar 4'}
# p = pd.DataFrame(bs)
# p.to_csv('bs.csv', mode='a', header=False)
# while True:
#     print('Name?')
#     name = input()
#     if name == "":
#         break
#     if name  in p:
#         print(p[name]+ ' is the birthday of ' + name)
#     else:
#         print('Nothin')
#         print('Day?')
#         b = input()
#         p[name] = b
#         print('Got you')
import pandas as pd
import os

filename = "bs.csv"

# Загружаем существующий файл или создаём новый DataFrame
if os.path.exists(filename):
    p = pd.read_csv(filename, index_col=0)
else:
    p = pd.DataFrame(columns=["Name", "Birthday"])

while True:
    name = input("Name? ")
    if name == "":
        break

    if name in p["Name"].values:
        birthday = p.loc[p["Name"] == name, "Birthday"].values[0]
        print(f"{birthday} is the birthday of {name}")
    else:
        print("Nothin")
        b = input("Day? ")
        new_entry = pd.DataFrame({"Name": [name], "Birthday": [b]})
        p = pd.concat([p, new_entry], ignore_index=True)
        p.to_csv(filename, index=False)
        print("Got you")

from csv import DictReader

import csv
with open ("lololo.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['coin', 'cost', 'date'])
    writer.writerow(['BTC', '100000$', '3/3/2025'])
    writer.writerow(['ETH', '4000$', '3/3/2025'])
    writer.writerow(['APE', '20$', '3/3/2025'])

with open ("lololo.csv","r",encoding="utf-8", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        print("Название монеты:", row['coin'], "|", "Цена монеты:", row['cost'], "Дата проверки:", row['date'] )
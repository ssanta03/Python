from csv import DictReader

import csv
with open ("employees.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['id', 'name', 'age', 'department', 'salary'])
    writer.writerow(['1', 'Hank', '20', 'sales', '50000'])
    writer.writerow(['2', 'Loke', '30', 'sales','39000'])
    writer.writerow(['3', 'Mash', '55', 'front desk', '44000'])
    writer.writerow(['4', 'Kol', '45', 'Maint', '67000'])
    writer.writerow(['5', 'Jol', '75', 'Manag', '34000'])

with open ("employees.csv","r",encoding="utf-8", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        n = int(row['age'])
        if n > 30:
            print(n);
        l = max(reader, key=lambda x: int(x['salary']))
        print(l['salary'])

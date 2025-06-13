from csv import DictReader

import csv
with open ("shop.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['Товар', 'Категория', 'Цена', 'Количество'])
    writer.writerow(['Яблоки', 'Фрукты', '1.5', '30'])
    writer.writerow(['Бананы', 'Фрукты', '1.2', '50'])
    writer.writerow(['Молоко', 'Молочка', '2.0', '20'])
    writer.writerow(['Хлеб', 'Выпечка', '1.8', '25'])
    writer.writerow(['Йогурт', 'Молочка', '3.5', '15'])

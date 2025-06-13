from sys import api_version

l = input("Введите числа через пробел:")
numbers = list(map(int, l.split()))
sum_numbers = sum(numbers)
min_n = min(numbers)
max_n = max(numbers)
average = round(sum_numbers / len(numbers), 2)
even_n = [num for num in numbers if num % 2 == 0]
print(f"Сумма: {sum_numbers}")
print(f"Минимальное: {min_n}, Максимальное: {max_n}")
print(f"Среднее: {average}")
print(f"Чётные числа: {' '.join(map(str, even_n)) if even_n else 'Нет чётных чисел'}")
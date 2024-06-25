# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем числа из списка
for num in numbers:
    is_prime = True  # Предполагаем, что число простое
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Если нашли делитель, число не простое
            break  # Оптимизация: дальше проверять не нужно

    if num > 1 and is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки простых и не простых чисел
print("Primes:", primes)
print("Not Primes:", not_primes [1: ])

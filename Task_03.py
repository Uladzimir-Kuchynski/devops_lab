# Вводим n (n - это количество простых чисел):
n = int(input("n="))

# Создаем список для хранения простых чисел:
list_of_num = list(map(int, input().split()))

# Находим максимальный элемент списка:
maximum = max(list_of_num)

# создаем строку:
s = ""

# Создаем цикл для нахождения простых чисел:
for possiblePrime in range(2, 10**5):
    # Предполагаем, что число является простым, пока не показано,
    #  что это не так:
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
    if isPrime:
        s += str(possiblePrime)
    if len(s) > maximum:
        break

# Вывод чисел по их индексам:
print(s)
myString = ''.join(s[i - 1] for i in list_of_num)
print(myString)

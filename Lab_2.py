# Импорт модуля math для использования математических функций
import math

# Функция для проверки, является ли число простым
def is_prime(number):
    """
    Проверяет, является ли число простым.
    """
    # Проверка, если число меньше или равно 1
    if number <= 1:
        return False

    # Вычисление целой части квадратного корня числа
    sqrt_num = int(math.sqrt(number))

    # Проверка делимости числа на все числа от 2 до целой части квадратного корня числа
    for count in range(2, sqrt_num + 1):
        if number % count == 0:
            return False
    return True

# Функция для разложения числа на простые множители
def factorize(n):
    """
    Разлагает число n на простые множители.
    """
    factors = [] # Инициализация списка множителей
    p = 2 # Начальное значение для поиска простых множителей
    while True: # Бесконечный цикл
        while n % p == 0 and n > 0: # Цикл для деления числа n на простые множители p
            factors.append(p) # Добавление простого множителя в список
            n = n // p # Деление числа на простой множитель
        p += 1 # Увеличение значения простого множителя
        if p > n // p: # Проверка, достигли ли максимального простого множителя
            break
    if n > 1: # Если остался остаток после разложения
        factors.append(n) # Добавление остатка в список множителей
    return factors # Возврат списка множителей

# Функция для вычисления символа Лежандра
def legendre_symbol(a, p):
    """
    Вычисляет символ Лежандра (a|p).
    """
    if a % p == 0: # Проверка, если a делится на p
        legendre_symbol = 0 # a является квадратом p
    elif pow(a, (p - 1) // 2, p) == 1: # Проверка, если a является квадратичным вычетом по модулю p
        legendre_symbol = 1 # a является квадратичным вычетом по модулю p
    else:
        legendre_symbol = -1 # a является квадратичным невычетом по модулю p
    return legendre_symbol # Возврат символа Лежандра

# Функция для решения квадратичного сравнения
def solve_quadratic_congruence(a, b, m):
    """
    Решает квадратичное сравнение ax^2 ≡ b (mod m).
    :param a: Коэффициент a
    :param b: Коэффициент b
    :param m: Модуль m
    :return: Список решений (если они есть)
    """
    solutions = [] # Список для хранения решений

    # Вычисление символа Лежандра
    legendre = legendre_symbol(a, m)

    if legendre == 1: # Если символ Лежандра равен 1
        if is_prime(m): # Если m является простым числом
            print("Сравнение с простым модулем")
            if m > 2: # Если m больше 2
                # Вычисление квадратного корня a по модулю m
                sqrt_a = pow(a, (m + 1) // 4, m)
                # Вычисление решений
                x1 = (sqrt_a * b) % m
                x2 = m - x1
                # Добавление решений в список
                solutions.append(x1)
                solutions.append(x2)
                return solutions # Возврат списка решений
            else:
                return solutions # Возврат пустого списка, если m <= 2
        elif not is_prime(m) and len(factorize(m)) == 1: # Если m - степень простого числа
            print("Сравнение с составным модулем - степень простого числа")
            for x in range(m): # Перебор значений x от 0 до m-1
                if (a * x**2) % m == b: # Проверка удовлетворения сравнения
                    solutions.append(x) # Добавление решения в список
            return solutions # Возврат списка решений
        else: # Если m - составное число, которое раскладывается на простые множители
            print("Сравнение с составным модулем - множители простого числа")
            for x in range(m): # Перебор значений x от 0 до m-1
                if (a * x ** 2) % m == b: # Проверка удовлетворения сравнения
                    solutions.append(x) # Добавление решения в список
            return solutions # Возврат списка решений
    else: # Если символ Лежандра не равен 1
        return solutions # Возврат пустого списка, если символ Лежандра не равен 1

# Ввод значений коэффициентов a, b и m с клавиатуры
a = int(input("Введите коэффициент а: "))
b = int(input("Введите коэффициент b: "))
m = int(input("Введите коэффициент m: "))

# Получение списка решений квадратичного сравнения
solutions = solve_quadratic_congruence(a, b, m)

# Вывод решений квадратичного сравнения, если они есть
if solutions :
    print(f"Решения сравнения {a}*x^2 ≡ {b} (mod {m}): {solutions}")
else:
    print(f"Сравнение {a}*x^2 ≡ {b} (mod {m}) не имеет решений.")

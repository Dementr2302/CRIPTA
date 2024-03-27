def euclid_extended(a, b):
    """Расширенный алгоритм Евклида."""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = euclid_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def euler_phi(m):
    """Вычисляет значение функции Эйлера."""
    result = 1
    for i in range(2, m):
        if euclid_extended(i, m)[0] == 1:
            result += 1
    return result
class ModularExponentiation:
    def __init__(self, modulus):
        self.modulus = modulus

    def add_mod(self, a, b):
        """Сложение по модулю."""
        return (a + b) % self.modulus

    def mul_mod(self, a, b):
        """Умножение по модулю."""
        return (a * b) % self.modulus

    def inv_mod(self, a):
        """Нахождение обратного элемента по модулю."""
        gcd, x, _ = euclid_extended(a, self.modulus)
        if gcd != 1:
            raise ValueError("Обратный элемент не существует.")
        return x % self.modulus

    def pow_mod(self, base, exponent):
        """Вычисление степени по модулю."""
        if exponent == 0:
            return 1
        elif exponent > 0:
            # Малая теорема Ферма для положительных степеней
            result = 1
            for _ in range(exponent):
                result = self.mul_mod(result, base)
            return result
        else:
            # Теорема Эйлера для отрицательных степеней
            phi = euler_phi(self.modulus)
            inv_base = self.inv_mod(base)
            positive_exponent = (-exponent) % phi
            result = 1
            for _ in range(positive_exponent):
                result = self.mul_mod(result, inv_base)
            return result

# Пример использования
mod_exp = ModularExponentiation(17) # mod 17
print(mod_exp.pow_mod(3, 5))  # 3^5 mod 17
print(mod_exp.pow_mod(3, -5))  # 3^(-5) mod 17, используя обратный элемент и теорему Эйлера




def extended_gcd(a, b):
    print(f"Вычисление GCD для {a} и {b}")
    if a == 0:
        print(f"Возвращаем ({b}, 0, 1)")
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        print(f"Обновленные значения: gcd={g}, x={x}, y={y}")
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m):
    print(f"Находим обратный элемент для {a} по модулю {m}")
    g, x, _ = extended_gcd(a, m)
    if g == 1:
        inverse = x % m
        print(f"Обратный элемент для {a} по модулю {m} найден: {inverse}")
        return inverse
    else:
        print(f'Внимание: Обратный элемент для {a} по модулю {m} не существует. Пропускаем.')
        return None

def chinese_remainder_theorem(a, m):
    print("Начало работы Китайской теоремы об остатках")
    M = 1
    for mod in m:
        M *= mod
        print(f"Текущий общий модуль M: {M}")

    solution = 0
    print("Начинаем вычисление решения системы сравнений")
    for i in range(len(a)):
        Mi = M // m[i]
        print(f"Модуль для {i}-го уравнения: {Mi}")
        yi = mod_inverse(Mi, m[i])
        if yi is not None:
            part_solution = a[i] * Mi * yi
            solution += part_solution
            print(f"Добавляем часть решения: {part_solution}, текущее решение: {solution}")
        else:
            print(f'Модуль {m[i]} и остаток {a[i]} исключены из расчета.')

    final_solution = solution % M
    print(f"Финальное решение системы сравнений: x ≡ {final_solution} (mod {M})")

    # Генерируем список всех решений в пределах общего модуля M
    solutions = [final_solution + i*M for i in range(0, 10)] # Пример для 1 решения; измените диапазон по желанию

    return final_solution, M, solutions

# Система сравнений №1 и №2
a1 = [2, 15, 5]
m1 = [5, 17, 12]

a2 = [8, 13, 4]
m2 = [6, 35, 11]

# Решение системы сравнений №1
print("\nРешение системы сравнений №1:")
solution1, M1, solutions1 = chinese_remainder_theorem(a1, m1)
print(f"Решение системы сравнений №1: x ≡ {solution1} (mod {M1}), Еще решения: {solutions1}")

# Решение системы сравнений №2
print("\nРешение системы сравнений №2:")
solution2, M2, solutions2 = chinese_remainder_theorem(a2, m2)
print(f"Решение системы сравнений №2: x ≡ {solution2} (mod {M2}), Еще решения: {solutions2}")



def find_gcd(a, b):
    print(f"Начинаем нахождение НОД для ({a}, {b})")
    while b != 0:
        print(f"НОД({a}, {b}) -> a = {b}, b = {a % b}")
        a, b = b, a % b
    print(f"Найден НОД: {a}")
    return a


def gcd(*numbers):
    """
    Находит НОД нескольких чисел.
    :param numbers: Перечень чисел.
    :return: НОД чисел.
    """
    from math import gcd as math_gcd
    from functools import reduce

    result = reduce(find_gcd, numbers)
    print(f"НОД чисел {numbers} равен {result}")
    return result


# Задание 13а: Дано НОД (a, b) = 24, найдите НОД (a, b, 16)
# Здесь и далее a, b, c - неизвестные числа, поэтому решение будет общим
print("Задание 13а:")
print("Поскольку НОД(a, b) = 24, то НОД(a, b, 16) будет НОД(24, 16).")
gcd_13a = gcd(24, 16)

# Задание 13б: Дано НОД (a, b, c) = 12, найдите НОД (a, b, c, 16)
print("\nЗадание 13б:")
print("Поскольку НОД(a, b, c) = 12, то НОД(a, b, c, 16) будет НОД(12, 16).")
gcd_13b = gcd(12, 16)

# Задание 13в: Найдите НОД (200, 180, и 450)
print("\nЗадание 13в:")
gcd_13c = gcd(200, 180, 450)

# Задание 13г: Найдите НОД (200, 180 450 610)
print("\nЗадание 13г:")
gcd_13d = gcd(200, 180, 450, 610)




# Задание 14а: Доказательство
print("Задание 14а: Для любого n, НОД(2n + 1, n) = 1 по определению.")

# Задание 14б: Конкретные случаи
print("\nЗадание 14б:")
print("НОД(201, 100):")
gcd_201_100 = gcd(201, 100)

print("\nНОД(81, 40):")
gcd_81_40 = gcd(81, 40)

print("\nНОД(501, 250):")
gcd_501_250 = gcd(501, 250)



# Задание 15а: Общий случай
print("Задание 15а: Обычно, НОД(3n + 1, 2n + 1) = 1 для любого целого неотрицательного n.")

# Задание 15б: Конкретные случаи
print("\nЗадание 15б: Конкретные случаи")
print("НОД(301, 201):")
gcd_301_201 = gcd(301, 201)

print("\nНОД(121, 81):")
gcd_121_81 = gcd(121, 81)


def solve_extended_gcd(a, b):
    gcd, s, t = extended_gcd(a, b)
    print(f"Для чисел {a} и {b} НОД = {gcd}, коэффициенты s = {s}, t = {t}")

# Задание 16а: НОД и коэффициенты для чисел 4 и 7
print("Задание 16а:")
solve_extended_gcd(4, 7)

# Задание 16б: НОД и коэффициенты для чисел 291 и 42
print("\nЗадание 16б:")
solve_extended_gcd(291, 42)

# Задание 16в: НОД и коэффициенты для чисел 84 и 320
print("\nЗадание 16в:")
solve_extended_gcd(84, 320)

# Задание 16г: НОД и коэффициенты для чисел 400 и 60
print("\nЗадание 16г:")
solve_extended_gcd(400, 60)



def fermat_theorem(a, p, power=1):
    if power == -1:  # Для модульной инверсии
        power = p - 2
    result = pow(a, power, mod=p)
    return result

# Задание 9
print("Задание 9:")
print(f"a. 5^15 mod 13 = {fermat_theorem(5, 13, 15)}")
print(f"b. 15^18 mod 17 = {fermat_theorem(15, 17, 18)}")
# c. Поскольку 456 делится на 17, результат будет 0
print("c. 456^17 mod 17 = 0")
print(f"d. 145 mod 101 = {145 % 101}")

# Задание 10
print("\nЗадание 10:")
print(f"a. 5^-1 mod 13 = {fermat_theorem(5, 13, -1)}")
print(f"b. 15^-1 mod 17 = {fermat_theorem(15, 17, -1)}")
print(f"c. 27^-1 mod 41 = {fermat_theorem(27, 41, -1)}")
print(f"d. 70^-1 mod 101 = {fermat_theorem(70, 101, -1)}")



import math
def euler_phi(n):
    """Вычисляет значение функции Эйлера для n."""
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    print(f"Функция Эйлера для {n} равна {amount}")
    return amount

def modular_inverse_euler(a, n):
    """Находит модульный обратный для a по модулю n, используя теорему Эйлера."""
    phi_n = euler_phi(n)
    result = pow(a, phi_n - 1, n)
    print(f"Модульный обратный для {a} по модулю {n} найден: {result}")
    return result

# Задание 11
print(" \n Задание 11:")
print(f"a. 12^-1 mod 77 = {modular_inverse_euler(12, 77)}")
print(f"b. 16^-1 mod 323 = {modular_inverse_euler(16, 323)}")
print(f"c. 20^-1 mod 403 = {modular_inverse_euler(20, 403)}")





# Задание 19а
print("\nЗадание 19а:")
a = [2, 3]  # Остатки
m = [7, 9]  # Модули
solution, M, _ = chinese_remainder_theorem(a, m)
print(f"x ≡ {solution} (mod {M}) для системы сравнений x ≡ 2 mod 7 и x ≡ 3 mod 9")

# Задание 19б
print("\nЗадание 19б:")
a = [4, 0]  # Остатки
m = [5, 11]  # Модули
solution, M, _ = chinese_remainder_theorem(a, m)
print(f"x ≡ {solution} (mod {M}) для системы сравнений x ≡ 4 mod 5 и x ≡ 0 mod 11")

# Задание 19в
print("\nЗадание 19в:")
a = [7, 11]  # Остатки
m = [13, 12]  # Модули
solution, M, _ = chinese_remainder_theorem(a, m)
print(f"x ≡ {solution} (mod {M}) для системы сравнений x ≡ 7 mod 13 и x ≡ 11 mod 12")


def find_QRs_and_QNRs(p):
    QRs = []
    QNRs = []
    for a in range(1, p):
        if pow(a, (p-1)//2, p) == 1:
            QRs.append(a)
        else:
            QNRs.append(a)
    return QRs, QNRs

# Задание 20
primes = [13, 17, 23]
for p in primes:
    QRs, QNRs = find_QRs_and_QNRs(p)
    print(f"В Z_{p}*: QRs = {QRs}, QNRs = {QNRs}")



def solve_quadratic_congruence(a, p):
    solutions = []
    for x in range(0, p):
        if pow(x, 2, p) == a:
            solutions.append(x)
    if len(solutions) == 0:
        return "нет решений"
    return solutions

# Задание 21,22
equations = [(4, 7), (5, 11), (7, 13), (12, 17),(4, 14), (5, 10), (7, 33), (12, 34)]
equations = [(7, 13)]

for a, p in equations:
    solutions = solve_quadratic_congruence(a, p)
    print(f"x^2 ≡ {a} mod {p} имеет решения: {solutions}")



from math import gcd

def euler_phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

def find_primitive_roots(p):
    phi = euler_phi(p-1)
    candidates = [x for x in range(1, p) if gcd(x, p) == 1]
    primitive_roots = []
    for g in candidates:
        if all(pow(g, k, p) != 1 for k in range(1, p-1) if (p-1) % k == 0):
            primitive_roots.append(g)
    return primitive_roots

p = 19
# Порядок группы
order_group = p - 1

# Порядок каждого элемента
element_orders = {x: min([k for k in range(1, p) if pow(x, k, p) == 1]) for x in range(1, p)}

# Число первообразных корней и их нахождение
primitive_roots = find_primitive_roots(p)
number_of_primitive_roots = len(primitive_roots)

print(f"Порядок группы Z_{p}*: {order_group}")
print("Порядки элементов:", element_orders)
print(f"Число первообразных корней: {number_of_primitive_roots}")
print(f"Первообразные корни в Z_{p}*: {primitive_roots}")


def demonstrate_cyclicity(primitive_root, p):
    elements = [pow(primitive_root, k, p) for k in range(1, p)]
    print(f"Элементы группы Z_{p}^*, сгенерированные первообразным корнем {primitive_root}: {sorted(elements)}")

# Используя первый найденный первообразный корень для демонстрации
if primitive_roots:
    demonstrate_cyclicity(primitive_roots[0], p)
else:
    print("Первообразные корни не найдены.")


def discrete_log_table(primitive_root, p):
    log_table = {}
    for k in range(0, p-1):
        a = pow(primitive_root, k, p)
        log_table[a] = k
    return log_table

# Выбираем первый первообразный корень из предыдущего расчета
g = primitive_roots[0] if primitive_roots else None
if g:
    log_table = discrete_log_table(g, p)
    for a, k in log_table.items():
        print(f"log_{g}({a}) = {k}")
else:
    print("Первообразные корни не найдены.")

def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида для нахождения x, y таких, что ax + by = gcd(a, b).
    Возвращает кортеж (gcd, x, y).
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m):
    """
    Находит обратный элемент к a по модулю m, если он существует.
    """
    g, x, _ = extended_gcd(a, m)
    if g == 1:
        return x % m
    else:
        raise ValueError('Обратный элемент не существует.')

def chinese_remainder_theorem(a, m):
    """
    Решает систему сравнений с помощью китайской теоремы об остатках.
    a и m - списки остатков и модулей соответственно.
    Возвращает решение системы сравнений.
    """
    M = 1
    for mod in m:
        M *= mod  # Общий модуль

    solution = 0
    for i in range(len(a)):
        Mi = M // m[i]  # Расчет Mi
        yi = mod_inverse(Mi, m[i])  # Расчет обратного элемента
        solution += a[i] * Mi * yi  # Вычисление части решения

    return solution % M, M  # Решение и общий модуль

# Пример использования
a = [2, 3, 1]  # Остатки
m = [3, 4, 5]  # Модули

# Вызов функции для решения системы сравнений
try:
    solution, M = chinese_remainder_theorem(a, m)
    print(f"Решение системы сравнений: x ≡ {solution} (mod {M})")
except ValueError as e:
    print(e)







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



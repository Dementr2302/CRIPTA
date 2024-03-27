

def multiply_polynomials(poly1, poly2):
    # Инициализируем результат произведения нулями
    result = [0] * (len(poly1) + len(poly2) - 1)
    # Умножаем полиномы по модулю 2
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] ^= poly1[i] * poly2[j]  # XOR для сложения коэффициентов
    # Обрезаем ведущие нули
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result

def divide_polynomials(dividend, divisor):
    # Преобразуем список коэффициентов в полиномы с наивысшей степенью в начале
    output = [0] * (len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor):
        # Коэффициент для текущего члена частного в GF(2) всегда будет 1, если старший коэффициент делимого не ноль
        coeff = dividend[0]
        if coeff == 0:  # Если старший коэффициент ноль, мы не можем делить
            break
        degree = len(dividend) - len(divisor)
        # Формируем полином для вычитания
        subtrahend = [coeff * x for x in divisor] + [0] * degree
        # Вычитаем (XOR) и обновляем делимое
        dividend = [a ^ b for a, b in zip(dividend + [0] * degree, subtrahend)]
        # Удаляем старший нулевой коэффициент
        while len(dividend) > 0 and dividend[0] == 0:
            dividend.pop(0)
        # Добавляем коэффициент к результату
        output[degree] = coeff
    # Остаток - это текущее делимое
    remainder = dividend
    return output, remainder

# Примеры из задачи
examples = [
    ([1, 0, 1, 1], [1, 1]),  # F(x) = x^3 + x + 1, G(x) = x + 1
    ([1, 0, 1], [1, 1]),     # F(x) = x^2 + 1, G(x) = x + 1
    ([1, 0, 1, 0, 1], [1, 0, 1]),  # F(x) = x^3 + x^2 + 1, G(x) = x^2 + 1
    ([1, 0, 0, 1, 1], [1, 0, 1]),  # F(x) = x^4 + x^2 + 1, G(x) = x^2 + x + 1
    ([1, 0, 0, 1, 1], [1, 1]),     # F(x) = x^4 + x^2 + x + 1, G(x) = x + 1
    ([1, 0, 1, 1, 0, 1], [1, 1, 1]),
]

# Выполнение операций для каждого примера
for i, (f, g) in enumerate(examples, start=1):
    print(f"Пример {i}.")

    # Сложение
    # print("Сложение многочленов:")
    # sum_result = add_polynomials(f, g)
    # print(f"Сумма: {sum_result}\n")

    print(f"Многочлен F(x): {f}")
    print(f"Многочлен G(x): {g}")

    # Умножение
    print("Умножение многочленов:")
    mult_result = multiply_polynomials(f, g)
    print(f"Произведение: {mult_result}\n")

    # Деление
    print("Деление многочленов:")
    quotient, remainder = divide_polynomials(f, g)
    print(f"Частное: {quotient}, Остаток: {remainder}\n")

    # Разделитель между примерами
    print("-" * 50)

# def gcd_polynomials(a, b):
#     while b:
#         quotient, remainder = divide_polynomials(a, b)
#         # Выводим шаги алгоритма Евклида
#         print(f"Деление {a} на {b} даёт остаток {remainder}")
#         a, b = b, remainder
#         # Убираем ведущие нули
#         a = [coeff for coeff in a if coeff != 0]
#         b = [coeff for coeff in b if coeff != 0]
#     return a

def gcd_polynomials(poly1, poly2):
    while poly2 and poly2 != [0]:
        _, remainder = divide_polynomials(poly1, poly2)
        print(f"Деление {poly1} на {poly2} даёт остаток {remainder}")
        poly1, poly2 = poly2, remainder
    # Обрезаем ведущие нули, если они есть
    while len(poly1) > 1 and poly1[0] == 0:
        poly1.pop(0)
    return poly1


# Определим многочлены из новых примеров
new_examples = [
    ([1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1]),     # 2.1
    ([1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1]),         # 2.2
    ([1, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1]),         # 2.3
    ([1, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1])    # 2.4
]

# Применим алгоритм Евклида к каждой паре многочленов
for i, (f1, f2) in enumerate(new_examples, 1):
    gcd = gcd_polynomials(f1, f2)
    print(f"Пример 2.{i}: НОД(F₁(x), F₂(x)) = {gcd}")
    print()


irr_polynomials = [
    [1, 1, 1], # x^2 + x + 1
    [1, 0, 1, 1], # x^3 + x + 1
    [1, 0, 0, 1, 1], # x^4 + x + 1
    [1, 0, 0, 1, 0, 1], # x^5 + x^2 + 1
    [1, 0, 0, 0, 0, 1, 1], # x^6 + x + 1
    [1, 0, 0, 0, 0, 0, 1, 1], # x^7 + x + 1
    [1, 0, 0, 0, 1, 1, 1, 0, 1], # x^8 + x^4 + x^3 + x^2 + 1
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1], # x^9 + x^4 + 1
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], # x^10 + x^3 + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], # x^11 + x^2 + 1
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1], # x^12 + x^6 + x^4 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1], # x^13 + x^4 + x^3 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], # x^14 + x^10 + x^ 6 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], # x^15 + x + 1
    [1, 0, 0, 0,1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], # x^16 + x^12 + x^3 + x + 1
]

def add_polynomials(a, b):
    # Сложение многочленов в GF(2) - это просто XOR их коэффициентов
    return [x ^ y for x, y in zip(a, b)]

def is_irreduciblle(poly):
    # Полиномы степени 0 и 1 всегда неприводимы
    if len(poly) <= 2:
        return True
    elif len(poly) > 16:
        print("Максимальная степень до степени 16.")
        return False

    # Проверяем содержит ли irr_polynomials полином
    if poly in irr_polynomials:
        return True
    else:
        return False


    return True  # Если не нашли делителей, полином неприводим
def is_irreducible(poly):
    # Полиномы степени 0 и 1 всегда неприводимы
    if len(poly) <= 2:
        return True

    # Проверяем деление на все полиномы меньшей степени
    for div_degree in range(1, len(poly) // 2 + 1):
        divisor = [1] + [0] * (div_degree - 1) + [1]  # Простейший полином заданной степени
        while divisor[0] == 1:  # Пока не перебрали все полиномы данной степени
            _, remainder = divide_polynomials(poly, divisor)
            if remainder == [0]:  # Если делится без остатка
                return False  # Полином приводим
            # Генерируем следующий полином той же степени
            for i in range(len(divisor) - 1, -1, -1):
                divisor[i] = 1 - divisor[i]  # Переключаем коэффициент
                if divisor[i] == 1:
                    break

    return True  # Если не нашли делителей, полином неприводим


# Примеры из задачи
is_irreducible_examples = [
    [1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1],    # x^2 + x // Примитивный
    [1, 0, 1, 1],  # x^3 + x + 1
    [1, 0, 1],     # x^2 + 1
    [1, 0, 1, 0, 1],  # x^3 + x^2 + 1
    [1, 0, 0, 1, 1],  # x^4 + x^2 + 1
    [1, 0, 0, 1, 1],  # x^4 + x^2 + x + 1
    [1, 0, 1, 1, 0, 1],  # x^5 + x^3 + x + 1
    [1, 1, 1, 1], # x^3 + x^2 + x + 1
    [1, 0, 1, 0, 1], # x^4 + x^2 + 1
    [1, 0, 0, 1, 1], # x^4 + x^2 + 1
]

# Выполнение операций для каждого примера
for i, f in enumerate(is_irreducible_examples, start=1):
    print(f"Пример {i}.")
    print(f"Многочлен F(x): {f}")
    print("Проверка на неприводимость:")
    print("Результат:", is_irreduciblle(f))
    print("-" * 50)


def gf2_poly_mul(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, coeff_a in enumerate(a):
        for j, coeff_b in enumerate(b):
            result[i + j] ^= (coeff_a & coeff_b)
    return result


def gf2_poly_mod(poly, mod_poly):
    def degree(p):
        while p and p[-1] == 0:
            p.pop()  # Удаляем нулевые коэффициенты с конца
        return len(p) - 1

    dp = degree(poly)
    dm = degree(mod_poly)
    while dp >= dm:
        diff = [0]*(dp - dm) + mod_poly
        for i in range(len(poly)):
            poly[i] ^= diff[i]
        dp = degree(poly)
    return poly


def gf2_poly_powmod(x, k, mod_poly):
    result = [1]  # многочлен степени 0
    while k > 0:
        if k & 1:
            result = gf2_poly_mod(gf2_poly_mul(result, x), mod_poly)
        x = gf2_poly_mod(gf2_poly_mul(x, x), mod_poly)
        k >>= 1
    return result

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def is_primitive(poly):
    if not is_irreduciblle(poly):
        return False

    n = len(poly) - 1  # Степень многочлена
    order = 2**n - 1

    # Проверка, что x^(2^n - 1) ≡ 1 (mod poly)
    if gf2_poly_powmod([1, 0], order, poly) != [1]:
        return False

    # Проверка, что условие не выполняется для любого делителя 2^n - 1
    for q in prime_factors(order):
        if gf2_poly_powmod([1, 0], order // q, poly) == [1]:
            return False

    return True


# Выполнение операций для каждого примера
for i, f in enumerate(is_irreducible_examples, start=1):
    print(f"Пример {i}.")
    print(f"Многочлен F(x): {f}")
    print("Проверка на примитивность:")
    print("Результат:", is_primitive(f))
    print("-" * 50)


class GaloisFieldCalculator:
    def __init__(self, generator_polynomial):
        # Инициализация класса GaloisFieldCalculator с образующим многочленом.
        self.generator_polynomial = generator_polynomial

    def add(self, a, b):
        """
        Сложение многочленов a и b в поле Галуа.
        Возвращает результат (a + b) % P, где P-образующий многочлен.
        """
        result = []  # Инициализация результата сложения.
        len_a, len_b = len(a), len(b)  # Длины входных многочленов.
        max_length = max(len_a, len_b)  # Максимальная длина.

        # Дополним многочлены нулями до одинаковой длины.
        a = [0] * (max_length - len_a) + a
        b = [0] * (max_length - len_b) + b

        # Побитовое сложение многочленов.
        for i in range(max_length):
            result.append((a[i] + b[i]) % 2)

        # Вычислим остаток от деления на образующий многочлен.
        P = self.generator_polynomial
        while len(result) >= len(P):
            coef = result[0]  # Коэффициент результата.
            if coef != 0:  # Если коэффициент не нулевой.
                for j in range(len(P)):
                    result[j] = (result[j] + P[j]) % 2  # Вычитаем образующий многочлен.
            del result[0]  # Удаляем старший коэффициент.

        return result  # Возвращаем результат сложения.

    def multiply(self, a, b):
        """
        Умножение многочленов a и b в поле Галуа.
        Возвращает результат (a * b) % 2.
        """
        result = [0] * (len(a) + len(b) - 1)  # Инициализация результата умножения.

        # Перемножение многочленов.
        for i in range(len(a)):
            for j in range(len(b)):
                result[i + j] = (result[i + j] + a[i] * b[j]) % 2

        # Вычислим остаток от деления на образующий многочлен.
        P = self.generator_polynomial
        while len(result) >= len(P):
            coef = result[0]  # Коэффициент результата.
            if coef != 0:  # Если коэффициент не нулевой.
                for j in range(len(P)):
                    result[j] = (result[j] + P[j]) % 2  # Вычитаем образующий многочлен.
            del result[0]  # Удаляем старший коэффициент.

        return result  # Возвращаем результат умножения.

    def divide(self, a, b):
        """
        Деление многочленов a и b в поле Галуа.
        Уже выполняется деление с учетом образующего многочлена.
        """
        # Копирование многочленов для сохранения исходных.
        poly1 = a[:]
        poly2 = b[:]

        # Удаление ведущих нулей.
        while len(poly1) and poly1[0] == 0:
            del poly1[0]
        while len(poly2) and poly2[0] == 0:
            del poly2[0]

        # Проверка деления на ноль и соответствия размеров делимого и делителя.
        if len(poly2) == 0:
            raise ZeroDivisionError()
        if len(poly1) < len(poly2):
            return ([0], poly1)

        # Нормализация многочленов.
        normalizer = poly2[0]
        poly1 = [a / normalizer for a in poly1]
        poly2 = [a / normalizer for a in poly2]

        # Инициализация результата деления.
        res = [0] * (len(poly1) - len(poly2) + 1)

        # Деление столбиком.
        for i in range(len(res)):
            res[i] = poly1[i]
            coef = res[i]
            if coef != 0:
                for j in range(1, len(poly2)):
                    poly1[i + j] = (poly1[i + j] - poly2[j] * coef) % 2

        # Удаление ведущих нулей в остатке.
        while len(poly1) and poly1[0] == 0:
            del poly1[0]

        return res  # Возвращаем результат деления.

    def power(self, a, n):
        """
        Возведение многочлена a в степень n в поле Галуа.
        Возвращает результат (a ** n) % P, где P - образующий многочлен.
        """
        result = [1]  # Инициализация результата возведения в степень.

        # Последовательное умножение многочлена на себя n раз.
        for _ in range(n):
            result = self.multiply(result, a)

            # Вычисление остатка от деления на образующий многочлен.
            P = self.generator_polynomial
            while len(result) >= len(P):
                coef = result[0]  # Коэффициент результата.
                if coef != 0:  # Если коэффициент не нулевой.
                    for j in range(len(P)):
                        result[j] = (result[j] + P[j]) % 2  # Вычитаем образующий многочлен.
                del result[0]  # Удаляем старший коэффициент.

        return result  # Возвращаем результат возведения в степень.

    def multiplication_table(self):
        # Таблица умножения для элементов в поле Галуа.
        table = []
        for i in range(256):  # Предполагается 8-битное поле.
            row = []
            for j in range(256):
                # Вычисление произведения элементов и добавление в таблицу.
                product = self.multiply([i], [j])
                row.append(product[0])
            table.append(row)

        return table  # Возвращаем таблицу умножения.


# Ввод коэффициентов для образующего многочлена.
gp_coeffs = input("Введите коэффициенты для образующего многочлена через запятую: ")
generator_polynomial = [int(coeff) for coeff in gp_coeffs.split(",")]
calculator = GaloisFieldCalculator(generator_polynomial)

# Ввод коэффициентов для многочлена a.
f1_coeffs = input("Введите коэффициенты для многочлена f1 через запятую: ")
f1 = [int(coeff) for coeff in f1_coeffs.split(",")]

# Ввод коэффициентов для многочлена b.
f2_coeffs = input("Введите коэффициенты для многочлена f2 через запятую: ")
f2 = [int(coeff) for coeff in f2_coeffs.split(",")]

# Выполнение операций.
sum_result = calculator.add(f1, f2)
product_result = calculator.multiply(f1, f2)
division_result = calculator.divide(f1, f2)
print("Введите степень в которую нужно возвести многочлен f1: ")
k_f1 = int(input())
print("Введите степень в которую нужно возвести многочлен f2: ")
k_f2 = int(input())
power_result_f1 = calculator.power(f2, k_f1)
power_result_f2 = calculator.power(f2, k_f2)
multiplication_table = calculator.multiplication_table()

print("Сумма:", sum_result)
print("Произведение:", product_result)
print("Деление:", division_result)
print("Возведение в степень многочлена f1:", power_result_f1)
print("Возведение в степень многочлена f2:", power_result_f2)
print("Таблица умножения:")
for row in multiplication_table:
    print(row)

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

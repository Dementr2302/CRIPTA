def find_cyclotomic_classes(n):
    # Определение циклотомических классов для поля GF(2^n).
    modulus = 2 ** n - 1  # Модуль для GF(2^n).
    classes = []  # Список для найденных циклотомических классов.
    found = set()  # Множество для отслеживания уже найденных элементов.
    for i in range(1, modulus + 1):  # Учитываем все элементы до 2^n - 1.
        if i not in found:  # Если элемент еще не найден.
            current_class = set()  # Текущий циклотомический класс.
            value = i
            while value not in current_class:
                current_class.add(value)
                found.add(value)
                value = (value * 2) % (modulus + 1)  # Переходим к следующему элементу.
            classes.append(sorted(current_class)[1:])  # Удаляем первый элемент в классе, т.к. он повторится в следующем и всегда равен 1.
    print(f"Циклотомические классы для GF(2^{n}):")
    return classes


def binary_to_polynomial(binary):
    # Преобразование двоичного представления числа в полиномиальную форму.
    binary_str = bin(binary)[2:]  # Двоичное представление числа.
    result = ""  # Итоговый полином.
    degree = len(binary_str) - 1  # Степень полинома.
    for i, bit in enumerate(binary_str):
        if bit == '1':  # Если бит равен 1.
            if degree - i > 1:
                result += f"x^{degree - i} + "  # Добавляем соответствующий член полинома.
            elif degree - i == 1:
                result += "x + "
            else:
                result += "1"
    if result.endswith(" + "):  # Удаляем последний лишний плюс.
        result = result[:-3]
    return result


def multiply_by_alpha(alpha, modulus, n):
    # Умножение alpha на x с учетом степени n для GF(2^n).
    result = alpha << 1  # Умножаем на x, сдвигая влево.
    # Проверяем, превышает ли результат предел для GF(2^n).
    if result >= 2 ** n:
        result ^= modulus  # Применяем XOR по модулю образующего многочлена.
    return result


def reduce_alpha(alpha, modulus, m):
    # Редукция alpha в соответствии с образующим многочленом.
    max_degree = 2**(m)  # Максимально возможное значение для GF(2^m).
    while alpha >= max_degree:
        # Находим степень текущего alpha.
        degree_alpha = alpha.bit_length() - 1
        # Находим степень модуля.
        degree_modulus = modulus.bit_length() - 1
        # Проверяем, что degree_alpha >= degree_modulus для корректного сдвига.
        if degree_alpha >= degree_modulus:
            # Сдвигаем модуль на разницу степеней.
            shifted_modulus = modulus << (degree_alpha - degree_modulus)
            # Применяем XOR для редукции.
            alpha ^= shifted_modulus
        else:
            # Если alpha меньше степени модуля, дальнейшая редукция не требуется.
            break
    return alpha


def generate_elements_and_minimal_polynomials(m, modulus, alpha_start=0b10):
    # Генерация элементов и минимальных многочленов для поля GF(2^m).
    # Начинаем с начального значения alpha.
    alpha = alpha_start
    elements = [1]  # 1 всегда присутствует в поле GF(2^m).

    # Генерируем элементы поля GF(2^m).
    for _ in range(1, 2 ** m - 1):
        alpha = reduce_alpha(multiply_by_alpha(alpha, modulus, m), modulus, m)
        if alpha not in elements:  # Убеждаемся, что элементы уникальны.
            elements.append(alpha)

    # Выводим элементы поля и их полиномиальное представление.
    print("Элементы поля GF(2^{}):".format(m))
    elements.sort()
    for element in elements:
        print(binary_to_polynomial(element))


# Задание 1-2
print(find_cyclotomic_classes(4))
print("Задание 1, для полинома 11001")
generate_elements_and_minimal_polynomials(4, 0b11001)

print("\nЗадание 2, для полинома 10011")
generate_elements_and_minimal_polynomials(4, 0b10011)

# Задание 3-6
print("\nЗадание 3-6")
print(find_cyclotomic_classes(5))
print("Циклотомический класс и минимальный многочлен для x:")
generate_elements_and_minimal_polynomials(5, 0b100101, 0b10)
print("\nЦиклотомический класс и минимальный многочлен для x^3:")
generate_elements_and_minimal_polynomials(5, 0b100101, 0b100)
print("\nЦиклотомический класс и минимальный многочлен для x^5:")
generate_elements_and_minimal_polynomials(5, 0b100101, 0b10000)
print("\nЦиклотомический класс и минимальный многочлен для x^7:")
generate_elements_and_minimal_polynomials(5, 0b100101, 0b1000000)

# Задание 7-8
print("\nЗадание 7")
print("\nЦиклотомические классы и минимальные многочлены в поле Галуа x^5+x^3+1: ")
generate_elements_and_minimal_polynomials(5, 0b101001, 0b10)  # для alpha = x

print("\nЗадание 8")
print("\nЦиклотомические классы и минимальные многочлены в поле Галуа x^5+x^3+x^2+x+1: ")
generate_elements_and_minimal_polynomials(5, 0b101111, 0b10)  # для alpha = x


# Примеры из задачи
is_irreducible_examples = [
    [1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1],
]

irr_polynomials = [
    [1, 1, 1],  # x^2 + x + 1
    [1, 0, 1, 1],  # x^3 + x + 1
    [1, 0, 0, 1, 1],  # x^4 + x + 1
    [1, 0, 0, 1, 0, 1],  # x^5 + x^2 + 1
    [1, 0, 0, 0, 0, 1, 1],  # x^6 + x + 1
    [1, 0, 0, 0, 0, 0, 1, 1],  # x^7 + x + 1
    [1, 0, 0, 0, 1, 1, 1, 0, 1],  # x^8 + x^4 + x^3 + x^2 + 1
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # x^9 + x^4 + 1
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # x^10 + x^3 + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # x^11 + x^2 + 1
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],  # x^12 + x^6 + x^4 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],  # x^13 + x^4 + x^3 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # x^14 + x^10 + x^ 6 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # x^15 + x + 1
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],  # x^16 + x^12 + x^3 + x + 1
]


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


def gf2_poly_powmod(x, k, mod_poly):
    result = [1]  # многочлен степени 0
    while k > 0:
        if k & 1:
            result = gf2_poly_mod(gf2_poly_mul(result, x), mod_poly)
        x = gf2_poly_mod(gf2_poly_mul(x, x), mod_poly)
        k >>= 1
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

def gf2_poly_mul(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, coeff_a in enumerate(a):
        for j, coeff_b in enumerate(b):
            result[i + j] ^= (coeff_a & coeff_b)
    return result

def is_primitive(poly):
    if not is_irreduciblle(poly):
        return False

    n = len(poly) - 1  # Степень многочлена
    order = 2 ** n - 1

    # Проверка, что x^(2^n - 1) ≡ 1 (mod poly)
    if gf2_poly_powmod([1, 0], order, poly) != [1]:
        return False

    # Проверка, что условие не выполняется для любого делителя 2^n - 1
    for q in prime_factors(order):
        if gf2_poly_powmod([1, 0], order // q, poly) == [1]:
            return False

    return True

print(f"Задания 9 - 12")

for i, f in enumerate(is_irreducible_examples, start=1):
    print(f"Пример {i}.")
    print(f"Многочлен F(x): {f}")
    print("Проверка на примитивность:", is_primitive(f))
    print("\n")

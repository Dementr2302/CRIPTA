# решение сравнений первого порядка через расширенный алгоритм Евклида

def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида.
    Возвращает НОД(a, b) и коэффициенты x, y такие, что ax + by = НОД(a, b).
    """
    i = 1
    # инициализация исходных значений
    x, xx, y, yy = 1, 0, 0, 1
    while b != 0:
        # частное q от деления a на b
        q = a // b
        # обновление значений a и b так, чтобы a стало равным b, а b — остатку от деления a на b
        # вывод промежуточных значений
        print(f"Шаг {i}: a={a}, b={b}, x={x}, y={y}")
        a, b = b, a % b
        # поиск обратных элементов в кольце вычетов
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
        i = i + 1
    return a, x, y

def solve_linear_congruence(a, b, m):
    """
    Решает сравнение ax ≡ b (mod m).
    Возвращает либо решение, либо сообщение о его отсутствии.
    """
    # возвращаем НОД(a, m) и коэффициенты x и y
    gcd, x, y = extended_gcd(a, m)
    # проверка разрешимости сравнения
    if b % gcd != 0:
        return "Сравнение не имеет решения."
    else:
        # вычисление начальное значение x0
        x0 = (x * (b // gcd)) % m
        # список solutions, в котором будут храниться все возможные решения
        solutions = [(x0 + k * (m // gcd)) % m for k in range(gcd)]
        return solutions

a = int(input("Введите коэффициент а: "))
b = int(input("Введите коэффициент b: "))
m = int(input("Введите коэффициент m: "))

# получение списка решений
solutions = solve_linear_congruence(a, b, m)

if isinstance(solutions, str):
    print(solutions)
else:
    print(f"Решения сравнения {a}x ≡ {b} (mod {m}): {solutions}")

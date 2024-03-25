import random
# реализация теста Ферма
def is_prime(n, k=5):
    """
    Выполняет тест Ферма на простоту числа.

    Args:
        n (int): Число для проверки на простоту.
        k (int, optional): Количество тестов. По умолчанию 5.

    Returns:
        bool: True, если число вероятно простое, иначе False.
    """
    if n <= 1:
        return False  # Число меньше или равно 1, по определению не является простым.
    if n == 2:
        return False  # Для двойки не выполняется условие для теста Ферма.

    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False  # Если условие теста Ферма не выполняется, число точно составное.

    return True  # Если все тесты пройдены успешно, число вероятно простое.

def find_composite_numbers(limit, num_tests):
    """
    Находит составные числа до заданного предела.

    Args:
        limit (int): Верхний предел поиска.
        num_tests (int): Количество тестов для каждого числа.

    Returns:
        list: Список составных чисел.
    """
    composite_numbers = []
    for i in range(2, limit + 1):
        if not is_prime(i, num_tests):
            composite_numbers.append(i)  # Если число не проходит тест на простоту, оно добавляется в список составных чисел.
    return composite_numbers

def composite_numbers_test(composite_numbers, num_tests):
    """
    Проверяет составные числа, чтобы увидеть результат множественных тестов.

    Args:
        composite_numbers (list): Список составных чисел.
        num_tests (int): Количество тестов.

    Returns:
        dict: Словарь с составными числами в качестве ключей и результатами тестов в качестве значений.
    """
    results = {}
    for num in composite_numbers:
        test_result = is_prime(num, num_tests)
        results[num] = test_result  # Сохраняем результаты тестов в словаре.
    return results

# Поиск составных чисел до одного миллиарда.
limit = 1000
composite_numbers = find_composite_numbers(limit, num_tests=1)

# Проверка составных чисел с 2 до 100 тестов.
test_results = composite_numbers_test(composite_numbers, num_tests=100)

# Вывод результатов.
for num, result in test_results.items():
    print(f"Число {num}: Результат первого теста: {'Простое' if result else 'Составное'}, "
          f"результат 100 тестов: {'Простое' if is_prime(num, 100) else 'Составное'}")

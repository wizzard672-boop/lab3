import itertools
import sys

# ============================================
# Задача 1: Перестановки длиной k
# ============================================

def k_permutations_recursive(arr, k):
    """
    Рекурсивное вычисление всех перестановок длиной k.
    """
    if k == 0:
        return [[]]
    if k > len(arr):
        return []
    
    result = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        # Рекурсивно ищем перестановки длины k-1 из оставшихся элементов
        for p in k_permutations_recursive(remaining, k - 1):
            result.append([current] + p)
    return result

def k_permutations_iterative(arr, k):
    """
    Итеративное вычисление всех перестановок длиной k с использованием itertools.
    """
    # itertools.permutations возвращает итератор, преобразуем в список списков
    return [list(p) for p in itertools.permutations(arr, k)]

# ============================================
# Задача 2: Рекуррентная последовательность
# x_i = i * x_{i-1} + 1/i, x_0 = 0
# ============================================

def sequence_recursive(n):
    """
    Рекурсивное вычисление n-го члена последовательности (и всех предыдущих).
    Возвращает список [x_0, x_1, ..., x_n].
    """
    def calc(i):
        if i == 0:
            return 0
        return i * calc(i - 1) + (1.0 / i)
    
    return [calc(i) for i in range(n + 1)]

def sequence_iterative(n):
    """
    Итеративное вычисление последовательности до n.
    Возвращает список [x_0, x_1, ..., x_n].
    """
    if n < 0:
        return []
    
    result = [0.0]  # x_0
    for i in range(1, n + 1):
        next_val = i * result[-1] + (1.0 / i)
        result.append(next_val)
    return result

# ============================================
# Демонстрация работы
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("ЗАДАЧА 1: ПЕРЕСТАНОВКИ ДЛИНОЙ K")
    print("=" * 50)
    test_arr = [1, 2, 3]
    k = 2
    print(f"Массив: {test_arr}, k = {k}")
    print(f"Рекурсивно:  {k_permutations_recursive(test_arr, k)}")
    print(f"Итеративно: {k_permutations_iterative(test_arr, k)}")

    print("\n" + "=" * 50)
    print("ЗАДАЧА 2: РЕКУРРЕНТНАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ")
    print("=" * 50)
    n_val = 5
    print(f"Вычисление для n = {n_val}")
    print(f"Рекурсивно:  {sequence_recursive(n_val)}")
    print(f"Итеративно: {sequence_iterative(n_val)}")
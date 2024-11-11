import random

# Создание списка из 100 случайных целых чисел от 0 до 100
arr = [random.randint(0, 1_000_000) for _ in range(100)]

# Вывод исходного списка
print("Исходный список:")
print(arr)

# Сортировка пузырьком (Bubble Sort)
arr_bubble = arr.copy()  # Создаем копию списка для пузырьковой сортировки
bubble_comparisons = 0  # Счётчик сравнений
print("Сортировка пузырьком (Bubble Sort):")
# Пузырьковая сортировка
for i in range(len(arr_bubble)):
    for j in range(0, len(arr_bubble) - i - 1): #генерирует диапазон индексов для второго цикла, который сравнивает соседние элементы в списке.
        bubble_comparisons += 1  # Увеличиваем счётчик сравнений
        if arr_bubble[j] < arr_bubble[j + 1]:
            # Меняем местами элементы, если текущий меньше следующего
            arr_bubble[j], arr_bubble[j + 1] = arr_bubble[j + 1], arr_bubble[j]
    # Выводим текущее состояние списка после каждой итерации
    #print(arr_bubble) 
    # Сортировка выбором (Selection Sort)
arr_selection = arr.copy()  # Создаем копию списка для сортировки выбором
selection_comparisons = 0  # Счётчик сравнений

print("Сортировка выбором (Selection Sort):")
# Сортировка выбором
for i in range(len(arr_selection)):
    max = i 
    for j in range(i + 1, len(arr_selection)):
        selection_comparisons += 1  # Увеличиваем счётчик сравнений
        if arr_selection[i] > arr_selection[j]:
            max_idx = j
    # Меняем местами найденный максимум с текущим элементом
    arr_selection[i], arr_selection[j] = arr_selection[j], arr_selection[i]
    # Выводим текущее состояние списка после каждой итерации
    #print(arr_selection)
# Вывод отсортированных списков и количества сравнений
print("Отсортированный список (пузырьковая сортировка):")
print(arr_bubble)
print("Количество сравнений (пузырьковая сортировка):",selection_comparisons)

print("Отсортированный список (сортировка выбором):")
print(arr_selection)
print("Количество сравнений (сортировка выбором):", selection_comparisons)

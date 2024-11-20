import re
from collections import Counter
import matplotlib.pyplot as plt

# Функция для подсчета частоты встречаемости букв
with open('lion.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())


# Вывод всех строк
for line in lines:
    print(line.strip())  # .strip() удаляет лишние символы новой строки

def count_letter_frequency(text):
    # Приводим текст к нижнему регистру
    text = text.lower()
    
    # Извлекаем только буквы (латиница и кириллица)
    letters = re.findall(r'[a-zа-яё]+', text)
    
    # Собираем все буквы в одну строку
    all_letters = ''.join(letters)
    
    # Подсчитываем частоту каждой буквы
    letter_counts = Counter(all_letters)
    
    return letter_counts

# Пример текста для анализа
text = """
Пример текста, чтобы посчитать, сколько раз встречается каждая буква, а также каждый уникальный слово.
"""

# Получаем статистику для букв
letter_frequencies = count_letter_frequency(text)

# Сортируем по алфавиту для лучшего отображения
sorted_letters = sorted(letter_frequencies.items())

# Разделяем буквы и их частоты
letters, frequencies = zip(*sorted_letters)

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.bar(letters, frequencies, color='skyblue')

# Настройки графика
plt.title("Частота встречаемости букв в тексте", fontsize=14)
plt.xlabel("Буквы", fontsize=12)
plt.ylabel("Частота", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Показать график
plt.show()


# Получаем статистику для букв
letter_frequencies = count_letter_frequency(text)

# Выводим результаты для слов
print("Частотность слов:")
for word, count in frequency.items():
    print(f"'{word}': {count}")

print("\nЧастотность букв:")
# Выводим результаты для букв в алфавитном порядке
for letter, count in sorted(letter_frequencies.items()):
    print(f"'{letter}': {count}")

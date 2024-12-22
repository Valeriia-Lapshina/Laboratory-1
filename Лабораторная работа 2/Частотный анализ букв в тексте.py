# Функция №1 для подсчета количества каждой буквы в тексте
def count_letters(text):
    # Приведение всех букв к нижнему регистру
    lower_text = text.lower()

    letter_count = {}
    for char in lower_text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count


# Функция №2 для вычисления частоты каждой буквы в тексте
def calculate_frequency(letter_count):
    # Подсчет общего количества букв
    total_letters = sum(letter_count.values())

    letter_frequency = {}
    for current_letter, count in letter_count.items():
        letter_frequency[current_letter] = count / total_letters

    return letter_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# Словарь с частотами букв, округленными до двух знаков после запятой
count_dict = count_letters(main_str)
frequency_dict = calculate_frequency(count_dict)
for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency:.2f}")

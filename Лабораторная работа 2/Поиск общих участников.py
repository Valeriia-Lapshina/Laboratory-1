# Функция для поиска общих участников
def find_common_participants(str_1, str_2, separator=','):
    str_1 = str_1.split(separator)
    str_2 = str_2.split(separator)

    # Получение отсортированного списка общих элементов двух множеств
    string_intersection = list(set(str_1) & set(str_2))
    string_intersection.sort()

    return string_intersection


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common_participants)

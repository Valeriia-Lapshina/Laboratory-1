# Функция для поиска индекса товара
def find_index(stock_items, item):
    for index, current_item in enumerate(stock_items):
        if current_item == item:
            return index


stock_items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(stock_items_list, find_item)  # Вызов функции для получения индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

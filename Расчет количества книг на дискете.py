# TODO Найдите количество книг, которое можно разместить на дискете
# Исходные данные
symbol_weight_b = 4
symbol_count_in_line = 25
line_count_on_page = 50
page_count_in_book = 100
diskette_weight = 1.44
# Перевод байтов в Мегабайты
symbol_weight_Mb = symbol_weight_b / (1024*1024)
# Расчеты
book_weight = symbol_weight_Mb*symbol_count_in_line*line_count_on_page*page_count_in_book
books_number = diskette_weight / book_weight
print("Количество книг, помещающихся на дискету:", round(books_number))

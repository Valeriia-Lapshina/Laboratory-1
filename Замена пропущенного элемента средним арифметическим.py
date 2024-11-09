# TODO заменить значение пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
only_numbers = numbers[:4]+numbers[5:]
total_numbers = len(numbers)
sum_numbers = sum(only_numbers)
average = sum_numbers/total_numbers
numbers[4] = average
print("Измененный список:", numbers)

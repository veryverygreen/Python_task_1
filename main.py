print('Введите список чисел')

input_list = list(input())
if all(map(lambda x: str(x).isdigit(), input_list)): #проверяем содержит ли список только цифры
    uniq_numbers = set(input_list) #находим уникальные
    uniq_numbers = list(uniq_numbers) #возвращаем список
    print(uniq_numbers)
else:
    print('Список должен содержать только цифры')
# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

list_elements = []
count = 0
while not list_elements:
    string_elements = input("Введите значения списка (разделенные пробелом): ")
    list_elements = string_elements.split()
    if not list_elements:
        print('Введите данные')
print(f'Вы ввели : {list_elements}')
while count < len(list_elements) - 1:
    buffer = list_elements[count]
    list_elements[count] = list_elements[count+1]
    list_elements[count+1] = buffer
    count += 2
print(f'Результат: {list_elements}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

trans = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('file_4.txt', 'r') as file_1:
    for i in file_1:
        i = i.split(' ', 1)
        new_file.append(trans[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_4_new.txt', 'w+') as file_2:
    file_2.writelines(new_file)

#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

COLUMNS = ['Название', 'Цена', 'Количество', 'Ед']
db = []
temp = {}
product = ()
index = 0
data_analiz = {}

while True:
    if input('Enter для продолжения. Для выхода введите 0: ') == '0':
        break
    index += 1
    for i in COLUMNS:
        temp[i] = input(f"{i} - ")
    product = (index, temp)
    db.append(product)
    print('*' * 50)
    print(f'Структура товаров: {db}')
    print('*' * 50)
    for data in COLUMNS:
        detail = []
        for i in range(0, len(db)):
            detail.append(db[i][1].get(data))
        data_analiz[data] = detail
    print(data_analiz)
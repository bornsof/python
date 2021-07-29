# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.


def my_func(a, b, c):
    temp_list = [a, b, c]
    map(int, temp_list)
    temp_list.remove(min(temp_list))
    return sum(temp_list)


print(my_func(1, 10, 23))

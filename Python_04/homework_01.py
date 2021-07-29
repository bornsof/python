# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
from sys import argv


def sal(time, salary, bonus):
    try:
        res = int(time) * int(salary) + int(bonus)
        print(f'заработная плата сотрудника: {res}')
    except ValueError:
        return print('Передайте в качестве параметров корректные значения выработки, ставки и премии')
        exit()


try:
    script_name, time, salary, bonus = argv
    sal(time, salary, bonus)
except ValueError:
    print('Передайте в качестве параметров корректные значения выработки, ставки и премии')
    print(f'Например python {argv[0]} time salary bonus')

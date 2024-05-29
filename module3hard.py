# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функци, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.

# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)

summa_all = 0
def calculate_structure_sum(*data_):

    for element in data_:
        global summa_all
        if isinstance(element, int):
            summa_all += element
        elif isinstance(element, str):
            summa_all += len(element)
        elif isinstance(element, list):
            calculate_structure_sum(*element)
        elif isinstance(element, tuple):
            calculate_structure_sum(*element)
        elif isinstance(element, set):
            calculate_structure_sum(*element)
        elif isinstance(element, dict):
            for k in element:
                key = (k, element[k])
                calculate_structure_sum(*key)
    return(summa_all)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print('Result :', result)

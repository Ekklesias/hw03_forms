def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам.
    result = ''
    for i in incoming:
        result += str(i)
    return result

# Первое тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из целых и дробных чисел.


mixed_numbers: list = [1, 2.3, 5, 6.72]
result_numbers = "12.356.72"

assert series_sum(mixed_numbers) == result_numbers, (
    'Функция series_sum() не работает со списком чисел')

mixed_numbers_strings = [1, "Dean", 2, "Sam"]
result_numbers_strings = "1Dean2Sam"

assert series_sum(mixed_numbers_strings) == result_numbers_strings, (
    'Функция series_sum() не работает со смешанным списком')

empty = []
result_empty = ''

# Вместо многоточия напишите утверждение, которое должно быть проверено
assert series_sum(empty) == result_empty, (
    'Функция series_sum() не работает с пустым списком')
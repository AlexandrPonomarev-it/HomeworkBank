def encoding_a_new_card(range_numbers: int) -> str:
    """ Функция принимает генерируемый диапазон чисел
    и возвращает номер карты с принятым числом"""
    zero_card_number = "0000000000000000"
    str_range_numbers = str(range_numbers)
    new_string = zero_card_number[len(str_range_numbers):] + str_range_numbers
    return new_string


def card_number_generator(a: int, b: int) -> str:
    for i in range(a, b +1):
        if a <= b:
            card_number_with_spaces = (f"{encoding_a_new_card(a)[:4]} {encoding_a_new_card(a)[4:8]} "
                                       f"{encoding_a_new_card(a)[8:12]} {encoding_a_new_card(a)[12:17]}")
            yield card_number_with_spaces
            a += 1


for card_number in card_number_generator(1, 5):
    print(card_number)
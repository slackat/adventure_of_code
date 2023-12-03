NUMBERS_DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def string_performer(string):
    array = list(string)
    for symbol in range (len(array) - 1):
        number_str = ''
        for sub_symbol in range(symbol, symbol + 5):
            if sub_symbol > len(array) - 1 or array[symbol] in STRING_NUMBERS:
                break
            number_str += array[sub_symbol]
            if number_str in NUMBERS_DICT.keys():
                del array[symbol:sub_symbol]
                array.insert(symbol, str(NUMBERS_DICT[number_str]))
                break
    return ''.join(array)

if __name__ == '__main__':
    from task_1 import get_numbers_from_list, STRING_NUMBERS
    with open('1_task_text.txt') as text: text = text.read().split()
    task_array = [string_performer(i) for i in text]
    print(sum(get_numbers_from_list(task_array)))

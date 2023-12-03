STRING_NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def get_numbers_from_list(array):
    final_numbers = []
    for phrase in array:
        number = [symbol for symbol in phrase if symbol in STRING_NUMBERS]
        final_numbers.append(int(number[0] * 2 if len(number) == 1 else number[0] + number[-1]))
    return final_numbers

if __name__ == '__main__':
    with open('1_task_text.txt') as text: text = text.read()
    print(sum(get_numbers_from_list(text.split("\n"))))
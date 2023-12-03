MAX_NUMBERS_DICT = {"red": 12,"green": 13,"blue": 14}

def dict_check(dictionary):
    return len([value for key, value in dictionary.items() if value <= MAX_NUMBERS_DICT[key]]) == 3

def string_to_array_prettier(string):
    return string.replace(":", "").replace(",", "").replace(";", "").split(" ")

def get_game_dict(game):
    dictionary = {"red": 0,"green": 0,"blue": 0}
    game_to_array = string_to_array_prettier(game)
    for i in range(2, len(game_to_array) - 1):
        if game_to_array[i].isdigit():
            if dictionary[game_to_array[i+1]] < int(game_to_array[i]):
                dictionary[game_to_array[i+1]] = int(game_to_array[i])
    return dictionary

if __name__ == '__main__':
    with open('2_task_text.txt') as text: text = text.read()
    print(sum([int(string_to_array_prettier(string)[1]) for string in text.split("\n") if dict_check(get_game_dict(string))]))

# power = 1
# for k, v in dictionary.items():
#     power *= v
# count += power
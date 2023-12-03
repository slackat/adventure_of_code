def get_balls_power_count(dictionary):
    return eval('*'.join(map(str, dictionary.values())))

if __name__ == '__main__':
    from task_1 import get_game_dict
    with open('2_task_text.txt') as text: text = text.read()
    print(sum([get_balls_power_count(get_game_dict(string)) for string in text.split("\n")]))
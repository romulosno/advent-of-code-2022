"""Day 02 challenge."""

plays = [
    {"name": "A", "value": 1},
    {"name": "B", "value": 2},
    {"name": "C", "value": 3},
    {"name": "X", "value": 1},
    {"name": "Y", "value": 2},
    {"name": "Z", "value": 3},
]


def get_my_score_p1(enemy_play, my_play):
    """Compara e atualiza pontuação."""
    enemy_play_dict = find_by_name(enemy_play)
    my_play_dict = find_by_name(my_play)

    play_score = get_play_score_p1(enemy_play_dict["value"],
                                   my_play_dict["value"])

    return play_score + my_play_dict["value"]


def get_play_score_p1(enemy_play_value, my_play_value):
    """Retorna resultado da jogada."""
    diff = enemy_play_value - my_play_value
    if diff == 0:
        return 3
    if diff == -1 or diff == 2:
        return 6
    if diff == -2 or diff == 1:
        return 0


def get_my_score_p2(enemy_play, result):
    """Compara e atualiza pontuação pt2."""
    enemy_play_value = find_by_name(enemy_play)["value"]

    if result == "X":
        my_play = 3 if enemy_play_value == 1 else enemy_play_value - 1
        return my_play
    if result == "Y":
        return 3 + enemy_play_value
    if result == "Z":
        my_play = 1 if enemy_play_value == 3 else enemy_play_value + 1
        return 6 + my_play


def find_by_name(name):
    """Busca o dict pelo nome."""
    return next(play for play in plays if play["name"] == name)


if __name__ == "__main__":
    file = open('input02', 'r')
    Lines = file.readlines()

    total_part_1 = 0
    total_part_2 = 0
    for line in Lines:
        total_part_1 = total_part_1 + get_my_score_p1(line[0], line[2])
        total_part_2 = total_part_2 + get_my_score_p2(line[0], line[2])

    print(total_part_1)
    print(total_part_2)

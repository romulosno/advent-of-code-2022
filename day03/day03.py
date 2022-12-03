"""Day 03 challenge."""
import string
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase


def find_char(part_one, part_two):
    """Busca o char igual."""
    for ch_X in part_one:
        if ch_X in part_two:
            return ch_X


def find_char_pt2(part_one, part_two, part_three):
    """Busca o char igual."""
    for ch_X in part_one:
        if ch_X in part_two and ch_X in part_three:
            return ch_X


def get_val(char):
    """Retorna valor pro char."""
    if wrong_ch.islower():
        return lower_letters.index(wrong_ch) + 1
    return upper_letters.index(wrong_ch) + 27


if __name__ == "__main__":
    file = open('input03', 'r')
    lines = file.readlines()
    final_val_pt1 = 0
    final_val_pt2 = 0

    for line in lines:
        part_one, part_two = line[:len(line)//2], line[len(line)//2:]
        wrong_ch = find_char(part_one, part_two)
        final_val_pt1 = final_val_pt1 + get_val(wrong_ch)
    print(final_val_pt1)

    file.seek(0)
    while True:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        if not line2 or not line3:
            break
        wrong_ch = find_char_pt2(line1, line2, line3)
        final_val_pt2 = final_val_pt2 + get_val(wrong_ch)
    print(final_val_pt2)

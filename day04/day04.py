"""Day 04 challenge."""

file = open('input04', 'r')
lines = file.readlines()

count_p1 = 0
count_p2 = 0

for line in lines:
    elvesCounts = line.split(",")
    first_array = [int(n) for n in elvesCounts[0].split("-")]
    second_array = [int(n) for n in elvesCounts[1].split("-")]

    if first_array[0] == second_array[0] or first_array[1] == second_array[1]:
        count_p1 = count_p1 + 1
    elif first_array[0] < second_array[0]:
        if first_array[1] > second_array[1]:
            count_p1 = count_p1 + 1
    elif second_array[1] > first_array[1]:
        count_p1 = count_p1 + 1

    first_range = list(range(first_array[0], first_array[1]+1))
    second_range = list(range(second_array[0], second_array[1]+1))
    if len(set(first_range).intersection(second_range)) > 0:
        count_p2 = count_p2 + 1

print(count_p1)
print(count_p2)

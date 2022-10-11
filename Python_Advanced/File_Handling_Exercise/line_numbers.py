exclamation_set = {'-', ',', '.', '!', '?', '\''}

with open('text.txt') as file:
    lines_of_file = file.readlines()
    place = 1

for line in lines_of_file:
    line = line.strip('\n')

    alphas_count = len([c for c in line if c.isalpha()])
    exclamation_count = len([c for c in line if c in exclamation_set])

    print(f'Line {place}: {line} ({alphas_count})({exclamation_count})')

    place += 1

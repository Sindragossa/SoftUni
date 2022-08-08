first_input_line = input().split(', ')
second_input_line = input().split(', ')

substrings = []

for first_line in first_input_line:
    for second_line in second_input_line:
        if first_line in second_line and not first_line in substrings:
            substrings.append(first_line)

print(substrings)
num_of_characters = int(input())

total_sum = 0

for characters in range(num_of_characters):
    current_characters = input()
    total_sum += ord(current_characters)
print(f'The sum equals: {total_sum}')
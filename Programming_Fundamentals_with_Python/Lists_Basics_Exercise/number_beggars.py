list_of_strings = input().split(", ")
count_of_beggars = int(input())
final_list = []
counter_of_index = 0
list_of_digits = []

for element in list_of_strings:
    list_of_digits.append(int(element))
while counter_of_index < count_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(counter_of_index, len(list_of_digits), count_of_beggars):
        sum_of_current_beggar += list_of_digits[current_index]
    counter_of_index += 1
    final_list.append(sum_of_current_beggar)
print(final_list)

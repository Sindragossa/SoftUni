name_to_list = input().split(', ')

sorted_list = sorted(name_to_list, key=lambda item: (-len(item), item))
print(sorted_list)
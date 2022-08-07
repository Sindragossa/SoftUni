array = input()
split_array = [int(array.split(", ")[integer]) for integer in range(len(array.split(", ")))]

max_value = 10
previous = -1
previous_filtered = -1
our_initial_max = None

while True:
    filtered = list(filter(lambda x: previous < x <= max_value, split_array))
    if len(filtered) == 0:
        if our_initial_max == max(split_array):
            break
    print(f"Group of {max_value}'s: {filtered}")

    if len(filtered) > 0:
        our_initial_max = max(filtered)
    previous = max_value
    max_value += 10

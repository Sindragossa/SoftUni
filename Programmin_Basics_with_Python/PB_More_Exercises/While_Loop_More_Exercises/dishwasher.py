num_bottles_detergent = int(input())
available_detergent = num_bottles_detergent * 750

needed_detergent = 0
counter_days = 0
counter_clean_plates = 0
counter_clean_pots = 0

while available_detergent >= needed_detergent:
    command = input()

    if command == "End":
        break

    else:
        counter_days += 1
        current_num_dishes = int(command)

        if counter_days % 3 == 0:
            needed_detergent += current_num_dishes * 15
            counter_clean_pots += current_num_dishes
        else:
            needed_detergent += current_num_dishes * 5
            counter_clean_plates += current_num_dishes

diff = abs(needed_detergent - available_detergent)
if needed_detergent <= available_detergent:
    print("Detergent was enough!")
    print(f"{counter_clean_plates} dishes and {counter_clean_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
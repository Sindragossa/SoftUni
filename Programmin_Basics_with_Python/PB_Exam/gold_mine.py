number_of_locations = int(input())

for location in range(number_of_locations):
    average = 0
    total_gold = 0
    gold_target = float(input())
    number_of_days = int(input())
    for daily_gold in range(1, number_of_days + 1):
        gold_per_day = float(input())
        total_gold += gold_per_day

    average = total_gold / number_of_days
    diff = (gold_target - average)
    if average >= gold_target:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")
needed_experience = float(input())
count_of_battles = int(input())

for battle in range(1, count_of_battles + 1):
    earned_per_battle = float(input())

    if battle % 3 == 0:
        earned_per_battle *= 1.15
    elif battle % 5 == 0:
        earned_per_battle *= 0.9
    elif battle % 15 == 0:
        earned_per_battle *= 0.05

    needed_experience -= earned_per_battle

    if needed_experience <= 0:
        print(f'Player successfully collected his needed experience for {battle} battles.')
        break

if needed_experience > 0:
    print(f'Player was not able to collect the needed experience, {needed_experience:.2f} more needed.')

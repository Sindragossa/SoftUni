needed_money = float(input())
init_money = float(input())

days_count = 0
count_spend = 0
total_money = init_money
while total_money < needed_money:
    if count_spend == 5:
        break
    days_count += 1
    action = input()
    amount = float(input())

    if action == "spend":
        count_spend += 1
        total_money = total_money - amount
        if total_money < 0:
            total_money = 0
    elif action == "save":
        count_spend = 0
        total_money = total_money + amount

if count_spend == 5:
    print("You can't save the money.")
    print(days_count)
else:
    print(f"You saved the money for {days_count} days.")
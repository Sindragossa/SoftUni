budget = float(input())
numbers_video = int(input())
numbers_processors = int(input())
numbers_ram = int(input())

video_card = numbers_video * 250
processors = numbers_processors * (video_card * 0.35)
ram = numbers_ram * (video_card * 0.10)

total_sum = video_card + processors + ram
discount = total_sum * 0.15

if numbers_video > numbers_processors:
    total_price = total_sum - discount
else:
    total_price = total_sum

difference = abs(total_price - budget)

if total_price <= budget:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
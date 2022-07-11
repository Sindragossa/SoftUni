n = int(input())
text = input()

taxi = 0.70
bus = 0.09
train = 0.06

price = 0
if text == 'day':
    if 20 <= n < 100:
        price = bus * n
    elif n >= 100:
        price = train * n
    else:
        price = (0.79 * n) + taxi

if text == 'night':
    if n >= 100:
        price = train * n
    elif 20 <= n < 100:
        price = bus * n
    else:
        price = (0.90 * n) + taxi

print(f'{price:.2f}')

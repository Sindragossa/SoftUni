season = input()
group_type = input()
num_student = int(input())
num_nights = int(input())

price = 0
sport = ''
school = 0

if season == 'Winter':
    if group_type == 'girls':
        price = num_student * num_nights * 9.60
        sport = 'Gymnastics'
    elif group_type == 'boys':
        price = num_student * num_nights * 9.60
        sport = 'Judo'
    else:
        price = num_student * num_nights * 10
        sport = 'Ski'

elif season == 'Spring':
    if group_type == 'girls':
        price = num_student * num_nights * 7.20
        sport = 'Athletics'
    elif group_type == 'boys':
        price = num_student * num_nights * 7.20
        sport = 'Tennis'
    else:
        price = num_student * num_nights * 9.50
        sport = 'Cycling'

elif season == 'Summer':
    if group_type == 'girls':
        price = num_student * num_nights * 15
        sport = 'Volleyball'
    elif group_type == 'boys':
        price = num_student * num_nights * 15
        sport = 'Football'
    else:
        price = num_student * num_nights * 20
        sport = 'Swimming'

if num_student >= 50:
    discount = (50/100) * price
    school = price - discount
elif 20 <= num_student < 50:
    discount = (15/100) * price
    school = price - discount
elif 10 <= num_student < 20:
    discount = (5/100) * price
    school = price - discount
else:
    school = price

print(f'{sport} {school:.2f} lv.')
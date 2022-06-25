month = input()
nights = int(input())

studio = 0
apartment = 0
discount_studio = 0
discount_apartment = 0

if month == "May" or month == "October":
    studio = nights * 50
    apartment = nights * 65

    if 7 < nights <= 14:
        discount_studio = 0.05
    elif nights > 14:
        discount_studio = 0.3
        discount_apartment = 0.1

elif month == "June" or month == "September":
    studio = nights * 75.20
    apartment = nights * 68.70
    if nights > 14:
        discount_studio = 0.2
        discount_apartment = 0.1

elif month == "July" or month == "August":
    studio = nights * 76
    apartment = nights * 77

    if nights > 14:
        discount_apartment = 0.1
studio -= studio * discount_studio
apartment -= apartment * discount_apartment
print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
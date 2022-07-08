w_of_m = float(input())
h_of_m = float(input())

w_of_sm = w_of_m * 100
h_of_sm = h_of_m * 100

left = h_of_sm - 100
seats = left // 70

seats2 = w_of_sm // 120

all_seats = seats2 * seats - 3

print(f'{all_seats:.0f}')
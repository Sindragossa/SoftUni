x = float(input())
y = float(input())
h = float(input())

side = x * y
window = 1.5 * 1.5
all_side = side * 2 - 2 * window

back_side = x * x
door = 1.2 * 2
all_side2 = back_side * 2 - door

green_paint = (all_side + all_side2) / 3.4

the_rectangle = 2 * (x * y)
the_triangle = 2 * (x * h / 2)

red_paint = (the_triangle + the_rectangle) / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
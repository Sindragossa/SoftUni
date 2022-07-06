import math

paint_boxes = int(input())
num_rollers = int(input())
pair_of_gloves = float(input())
one_brush = float(input())

paint_boxes_price = paint_boxes * 21.50
num_rollers_price = num_rollers * 5.20
pair_of_gloves_price = math.ceil(num_rollers * 0.35) * pair_of_gloves
one_brush_price = math.floor(paint_boxes * 0.48) * one_brush

total_sum = pair_of_gloves_price + paint_boxes_price + num_rollers_price + one_brush_price

tolal_price = total_sum / 15
print(f'This delivery will cost {tolal_price:.2f} lv.')
number_of_pens = int(input())
number_of_makers = int(input())
liters_of_detergent = int(input())
percent_discount = int(input())
price_per_pens = 5.80
price_per_makers = 7.20
price_per_liters_detergent = 1.20
needed_sum = number_of_pens * price_per_pens + \
             number_of_makers * price_per_makers + \
             liters_of_detergent * price_per_liters_detergent
needed_sum = needed_sum - needed_sum * percent_discount / 100
#needed_sum -= needed_sum * percent_discount / 100
#needed_sum = needed_sum + 5
#needed_sum += 5
print(needed_sum)

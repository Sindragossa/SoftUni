chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
chicken_price = 10.35
fish_price = 12.40
vegetarian_price = 8.15
food_delivery = 2.50
total_price = chicken_menu * chicken_price + \
            fish_menu * fish_price + \
            vegetarian_menu * vegetarian_price
desert = total_price * 0.2
total_sum = total_price + desert + food_delivery
print(total_sum)
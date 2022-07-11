text = input()
liters = float(input())

if text == "Diesel":
    if liters >= 25:
        print("You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")

elif text == "Gasoline":
    if liters >= 25:
        print("You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")

elif text == "Gas":
    if liters >= 25:
        print("You have enough gas.")
    else:
        print(f"Fill your tank with gas!")

else:
    print("Invalid fuel!")
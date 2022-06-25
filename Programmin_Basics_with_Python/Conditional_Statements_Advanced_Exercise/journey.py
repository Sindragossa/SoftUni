budget = float(input())
season = str(input())

destination = ""
from_budget = 0
rest_in = ""

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        from_budget = 0.3
        rest_in = "Camp"
    elif season == "winter":
        from_budget = 0.7
        rest_in = "Hotel"

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        from_budget = 0.4
        rest_in = "Camp"
    elif season == "winter":
        from_budget = 0.8
        rest_in = "Hotel"

elif budget > 1000:
    destination = "Europe"

    from_budget = 0.9
    rest_in = "Hotel"
cost = budget * from_budget
print(f"Somewhere in {destination}")
print(f"{rest_in} - {cost:.2f}")
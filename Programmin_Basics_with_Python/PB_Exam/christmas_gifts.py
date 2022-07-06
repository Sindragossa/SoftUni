num_of_kids = 0
num_of_adults = 0
line = input()

while line != "Christmas":
    age = int(line)
    if age <= 16:
        num_of_kids += 1
    elif age > 16:
        num_of_adults += 1
    else:
        break
    line = input()
print(f"Number of adults: {num_of_adults}")
print(f"Number of kids: {num_of_kids}")
print(f"Money for toys: {num_of_kids * 5}")
print(f"Money for sweaters: {num_of_adults * 15}")
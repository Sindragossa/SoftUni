first_letter = input()
second_letter = input()
except_letter = input()
counter = 0
for first in range(ord(first_letter), ord(second_letter) + 1):
    first = chr(first)
    for second in range(ord(first_letter), ord(second_letter) + 1):
        second = chr(second)
        for third in range(ord(first_letter), ord(second_letter) + 1):
            third = chr(third)
            if first != except_letter and second != except_letter and third != except_letter:
                counter += 1
                print(f'{first}{second}{third}', end=' ')
print(counter)
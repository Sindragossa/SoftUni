def characters(first_char, second_char):
    collected_char = []
    for current_char in range(ord(first_char) + 1, ord(second_char)):
        collected_char.append(chr(current_char))
    return collected_char


first_character = input()
second_character = input()
result = characters(first_character, second_character)
print(' '.join(result))

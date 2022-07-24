start_index = int(input())
final_index = int(input())

final_stings = ''

for character in range(start_index, final_index + 1):
    final_stings += chr(character) + chr(32)
    print(chr(character), end=' ')
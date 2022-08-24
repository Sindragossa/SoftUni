import re

num = int(input())

pattern = r'(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|(.+)<\1'

for _ in range(num):
    word = input()
    is_match = False
    for m in re.finditer(pattern, word):
        is_match = True
    txt = m.groupdict()
    print(f'Password: {txt}')


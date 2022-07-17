letter = input()
n = 0
o = 0
c = 0
all_word = ''
space = ' '
last_word = False
symbols = 0
ord(letter)
while letter != "End":
    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
        if letter == "o" or letter == "n" or letter == "c":
            if n > 0 and letter == "n":
                all_word += letter
                symbols += 1
            elif n == 0 and letter == "n":
                letter = ''
                n += 1
            if c > 0 and letter == "c":
                all_word += letter
                symbols += 1
            elif c == 0 and letter == "c":
                letter = ''
                c += 1
            if o > 0 and letter == "o":
                all_word += letter
                symbols += 1
            elif o == 0 and letter == "o":
                letter = ''
                o += 1
            if n == 1 and c == 1 and o == 1:
                symbols = 0
                c = 0
                n = 0
                o = 0
                letter = space
                all_word += letter
        else:
            all_word += letter
            symbols += 1
    if n == 0 and c == 0 and o == 0 and letter == space:
        last_word = True
    else:
        last_word = False
    letter = input()
if last_word:
    print(all_word)
else:
    exit = len(all_word) - symbols
    print(all_word[0:exit])

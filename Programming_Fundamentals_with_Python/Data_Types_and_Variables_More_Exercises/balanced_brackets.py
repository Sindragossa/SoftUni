number_of_lines = int(input())
string = ''
for i in range(number_of_lines):
    symbol = input()
    if symbol == '(' or symbol == ')':
        string += symbol
if string[1] == ')' and string[0] == '(':
    print('BALANCED')
else:
    print('UNBALANCED')
number = int(input())
word = input()
string = []

for i in range(number):
    current_string = input()
    string.append(current_string)
print(string)

for i in range(len(string) - 1, -1, -1):
    element = string[i]
    if word not in element:
        string.remove(element)
print(string)
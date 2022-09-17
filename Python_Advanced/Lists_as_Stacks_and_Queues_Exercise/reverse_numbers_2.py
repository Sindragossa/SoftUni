element = list(map(int, input().split()))

for _ in range(len(element)):
    removed_element = element.pop()
    print(removed_element, end=" ")
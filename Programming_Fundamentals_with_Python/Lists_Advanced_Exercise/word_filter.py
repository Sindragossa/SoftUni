texts = input().split()

filtered_text = [text for text in texts if len(text) % 2 == 0]
print('\n'.join(filtered_text))
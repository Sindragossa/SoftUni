followers = {}

while True:
    data = input().split()
    command = data[0]

    if command == 'Log out':
        break

    if command == 'New follower':
        username = data[2]
        if username not in followers:
            followers[username] = [0, 0]

    elif command == 'Like':
        username = data[1][0:-1]
        count = int(data[2])
        if username not in followers:
            followers[username] = [count, 0]
        else:
            followers[username][0] += count

    elif command == 'Comment':
        username = data[1]
        if username not in followers:
            followers[username] = [0, 1]
        else:
            followers[username][1] += 1

    elif command == 'Blocked':
        username = data[1]
        if username in followers:
            followers.pop(username)
        else:
            print(f'{username} doesn\'t exist')

print(f'{len(followers)} followers')
sort_f = dict(sorted(str(followers.items()), key=lambda x: (-x[1][0], x[0])))

for l, c in sort_f.items():
    print(f'{l}: {sum(c)}')
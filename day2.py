X = [l.strip() for l in open('in\\2.txt')]
# X = [int(x) for x in X]

horz, depth = 0, 0

for x in X:
    direction, distance = x.split(' ')
    if direction == 'forward':
        horz += int(distance)
    elif direction == 'down':
        depth += int(distance)
    else:
        depth -= int(distance)

print(horz *depth)


horz, depth, aim = 0, 0, 0

for x in X:
    direction, distance = x.split(' ')
    if direction == 'down':
        aim += int(distance)
    elif direction == 'up':
        aim -= int(distance)
    else:
        horz += int(distance)
        depth += aim * int(distance)

print(horz *depth)
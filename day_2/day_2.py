
commands = []

position = {'horizontal': 0, 'depth': 0}

with open('input.txt') as input:
    for command in input.readlines(): commands.append(command)

def update_position(command, position):
    direction = command.split()[0]
    magnitude = int(command.split()[1])
    if direction == 'forward':
        position['horizontal'] += magnitude
    if direction == 'up':
        position['depth'] -= magnitude
    if direction == 'down':
        position['depth'] += magnitude
    return position

for command in commands:
    position = update_position(command, position)

print(position)
print(position['horizontal'] * position['depth'])

position = {'horizontal': 0, 'depth': 0, 'aim': 0}

def update_aim(command, position):
    direction = command.split()[0]
    magnitude = int(command.split()[1])
    if direction == 'down':
        position['aim'] += magnitude
    if direction == 'up':
        position['aim'] -= magnitude
    if direction == 'forward':
        position['horizontal'] += magnitude
        position['depth'] += position['aim'] * magnitude
    return position

for command in commands:
    position = update_aim(command, position)

print(position)
print(position['horizontal'] * position['depth'])

positions = []
with open('input.txt') as input:
    positions = input.readline().strip().split(',')
    positions = [int(position) for position in positions]

# find the min and max possible, then check fuel for each position, choose smallest
min = positions[0]
max = positions[0]

for position in positions:
    if position < min: min = position
    elif position > max: max = position

fuel_per_final_position = {}
cheapest_position = ''

# costs 1 fuel per position
for final_position in range(min, max + 1):
    total_fuel = 0
    for position in positions:
        total_fuel += abs(position - final_position)
    fuel_per_final_position[str(final_position)] = total_fuel
    if final_position == min:
        cheapest_position = str(final_position)
    elif total_fuel < fuel_per_final_position[cheapest_position]:
        cheapest_position = str(final_position)


print('Cheapest position is ' + cheapest_position)
print('Total fuel costs is ' + str(fuel_per_final_position[cheapest_position]))

# new approach - first step costs 1 fuel, second 2, third 3, least_common
fuel_per_final_position = {}
cheapest_position = ''

for final_position in range(min, max + 1):
    total_fuel = 0
    for position in positions:
        for step in range(1, abs(position - final_position) + 1): total_fuel += step
    fuel_per_final_position[str(final_position)] = total_fuel
    if final_position == min:
        cheapest_position = str(final_position)
    elif total_fuel < fuel_per_final_position[cheapest_position]:
        cheapest_position = str(final_position)

print('Cheapest position is ' + cheapest_position)
print('Total fuel costs is ' + str(fuel_per_final_position[cheapest_position]))

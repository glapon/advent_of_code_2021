
class Lantern_fish:
    def __init__(self, timer):
        self.timer = timer

    def reset(self):
        self.timer = 6

lantern_fish = []
with open('input.txt') as input:
    lantern_fish = input.readline().strip().split(',')
    lantern_fish = [Lantern_fish(int(fish)) for fish in lantern_fish]
print(len(lantern_fish))

# sim for 80 days
for day in range(1, 81):
    new_fish = []
    for fish in lantern_fish:
        # if timer is 0, spawn new fish and reset, otherwise count down by 1
        if fish.timer == 0:
            fish.reset()
            new_fish.append(Lantern_fish(8))
        else: fish.timer -= 1
    for fish in new_fish:
        lantern_fish.append(fish)
    print('After {} days: {}'.format(day, len(lantern_fish)))

# sim for 256 - too big to use class approach above (too slow to compute)
initial_days = []
with open('input.txt') as input:
    initial_days = input.readline().strip().split(',')
    initial_days = [days for days in initial_days]

counts = {str(num): 0 for num in range(9)}

# sort initial group of lantern fish by number of days to spawn
for days in initial_days:
    counts[days] += 1

# each day, spawn new fish from 0, and then move all values down one days
for num in range(1, 257):
    total_fish = 0
    #spawn new fish from 0
    new_fish = counts['0']
    for days in range(9):
        if days < 8:
            # move numbers of fish one day down
            # fish that spawned get moved to day 6
            if days == 6: counts[str(days)] = counts[str(days + 1)] + new_fish
            else: counts[str(days)] = counts[str(days + 1)]
        else: # add new fish to 8 days category
            counts['8'] = new_fish
        total_fish += counts[str(days)]
    print('After {} days: {}'.format(num, total_fish))

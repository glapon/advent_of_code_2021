# part 1 - count number of times depth increase

depths = []

with open('input.txt') as input:
    for depth in input.readlines(): depths.append(int(depth))

print(len(depths))

def count_increases(depths):
    last_depth = depths[0]
    times_increased = 0
    for depth in depths[1:]:
        if depth > last_depth:
            times_increased += 1
        last_depth = depth
    return times_increased

print(count_increases(depths))

# part 2
sum_threes = [depths[index] + depths[index+1] + depths[index+2] for index in range(0,len(depths)-2)]

print(count_increases(sum_threes))

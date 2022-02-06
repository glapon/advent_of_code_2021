lines = []
with open('input.txt') as input:
    for number in input.readlines(): lines.append(number.strip().split(' -> '))
# using tuples to make input immutable
lines = [[coordinate.split(',') for coordinate in line] for line in lines]
lines = [tuple([(int(element[0]), int(element[1])) for element in line]) for line in lines]

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.points = [start, end]
        self.x_diff = abs(self.end[0] - self.start[0])
        self.y_diff = abs(self.end[1] - self.start[1])
        # consider only horizontal and vertical lines
        if self.x_diff == 0 and self.y_diff > 0:
            for num in range(1, self.y_diff):
                self.points.append((self.start[0], min(self.start[1], self.end[1]) + num))
        if self.y_diff == 0 and self.x_diff > 0:
            for num in range(1, self.x_diff):
                self.points.append((min(self.start[0], self.end[0]) + num, self.start[1]))
        # non-vertical (45 degree only)
        if self.x_diff > 0 and self.y_diff > 0 and self.x_diff == self.y_diff:
            for num in range(1, self.x_diff):
                # start is to the left of end on the horizontal: add to start[0]
                if self.start[0] < self.end[0]:
                    if self.start[1] < self.end[1]:
                        # start is below end on vertical: add to start[1]
                        self.points.append((self.start[0] + num, self.start[1] + num))
                    else: # start is above end on vertical: subtract from start[1]
                        self.points.append((self.start[0] + num, self.start[1] - num))
                # start is to the right of end on the horizontal: subtract from start[0]
                else:
                    if self.start[1] < self.end[1]:
                        # start is below end on vertical: add to start[1]
                        self.points.append((self.start[0] - num, self.start[1] + num))
                    else: # start is above end on vertical: subtract from start[1]
                        self.points.append((self.start[0] - num, self.start[1] - num))

# instantiate all the lines
# assign a number to each point (1+) for overlapping lines
# count points with 2 or more overlapping lines
all_lines = [Line(line[0], line[1]) for line in lines]

point_counts = {}

# consider just horizonal lines
for line in all_lines:
    if line.x_diff == 0 or line.y_diff == 0:
        for point in line.points:
            if str(point) in point_counts.keys():
                point_counts[str(point)] += 1
            else:
                point_counts[str(point)] = 1

multiples = {point: count for point, count in point_counts.items() if count > 1}
print(len(multiples))

point_counts = {}
# consider all lines
for line in all_lines:
    for point in line.points:
        if str(point) in point_counts.keys():
            point_counts[str(point)] += 1
        else:
            point_counts[str(point)] = 1

multiples = {point: count for point, count in point_counts.items() if count > 1}
print(len(multiples))

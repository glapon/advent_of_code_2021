diagnostic_report = []
# use strip to remove \n from input
with open('input.txt') as input:
    for number in input.readlines(): diagnostic_report.append(number.strip())

# returns most common 1 or 0 in given position (1 breaks tie)
def most_common(binaries, index):
    ones = 0
    zeroes = 0
    for number in binaries:
        if number[index] == '1': ones += 1
        elif number[index] == '0': zeroes += 1
    if ones >= zeroes: return '1'
    else: return '0'

# returns least common 1 or 0 in given position (1 breaks tie)
def least_common(binaries, index):
    if most_common(binaries, index) == '1': return '0'
    else: return '1'

#converts binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    reversed_binary = binary[::-1]
    for index in range(len(binary)):
        decimal += int(reversed_binary[index]) * 2**index
    return decimal

gamma_rate = ''
epsilon_rate = ''

for index in range(len(diagnostic_report[0])):
    gamma_rate += most_common(diagnostic_report, index)
    epsilon_rate += least_common(diagnostic_report, index)

print('gamma rate = ' + gamma_rate)
print('epsilon rate = ' + epsilon_rate)
print(binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate))
print('')

# part 2
oxygen_generator_rating = list(diagnostic_report)
co2_scrubber_rating = list(diagnostic_report)

for index in range(len(diagnostic_report[0])):
    more_common = most_common(oxygen_generator_rating, index)
    # only keep most common
    oxygen_generator_rating = [rating for rating in oxygen_generator_rating if rating[index] == more_common]
    if len(oxygen_generator_rating) == 1: break

for index in range(len(diagnostic_report[0])):
    more_common = most_common(co2_scrubber_rating, index)
    # only keep least common
    co2_scrubber_rating = [rating for rating in co2_scrubber_rating if rating[index] != more_common]
    if len(co2_scrubber_rating) == 1: break


print(oxygen_generator_rating)
print(co2_scrubber_rating)
print(binary_to_decimal(oxygen_generator_rating[0]) * binary_to_decimal(co2_scrubber_rating[0]))

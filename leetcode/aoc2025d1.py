from aocd import data, get_data
def get_input():
    data = get_data(year=2025, day=1)
    return data

myinput = get_input()
print(myinput)

with open('aoc2025d1_input.txt', 'w') as file:
    file.write(myinput)
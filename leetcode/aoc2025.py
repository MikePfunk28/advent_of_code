#https://adventofcode.com/2025/day/5/input
"""
The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.
"""

"""
def scrape():

    url = 'https://adventofcode.com/2025/day/1/input'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)


def get_input():
    data = get_data(year=2025, day=1)
    parts = data.split('\n\n')
    ranges_part = parts[0].strip().split('\n')
    ranges = []
    for range in ranges_part:
        start, end = range.split('-')
        ranges.append((int(start), int(end)))
    available_ids = parts[1].strip().split('\n')
    available_ids = [int(id) for id in available_ids]
    return ranges, available_ids

get_input()
fresh_id = []
ranges, available_ids = get_input()
i = 0
if available_ids[i] in ranges:
    fresh_id = available_ids[i]

    i+=1
    print(fresh_id)
"""

# So we need to be able to account for each range,
# and every number in that range, and then compare
# if its in the range its fresh, otherwuise spoiled.
# We can use the following code to do that:


# We need to read the input file and store the
# ranges and the available ingredient IDs in
# separate lists.
# We can use the following code to read the input file:

# Go to the site https://adventofcode.com/2025/day/5/input
# and download the input file as input.txt
# and save it in the same directory as this script.
#https://adventofcode.com/2025/day/5/input
import os

class AdventOfCode2025:
    def __init__(self, input_file):
        self.input_file = input_file
        self.ranges = []
        self.available_ids = []
        self.fresh_ids = []
        self.spoiled_ids = []

    def parse_input(self):
        with open(self.input_file, 'r') as file:
            lines = file.readlines()

        parsing_ranges = True
        for line in lines:
            line = line.strip()
            if not line:
                parsing_ranges = False
                continue

            if parsing_ranges and '-' in line:
                start, end = line.split('-')
                self.ranges.append((int(start), int(end)))
            elif not parsing_ranges:
                self.available_ids.append(int(line))

    def check_freshness(self):
        for id_val in self.available_ids:
            is_fresh = any(start <= id_val <= end for start, end in self.ranges)
            if is_fresh:
                self.fresh_ids.append(id_val)
            else:
                self.spoiled_ids.append(id_val)

    def solve(self):
        self.parse_input()
        self.check_freshness()
        return len(self.fresh_ids)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    solver = AdventOfCode2025(input_path)
    result = solver.solve()
    print(f"Fresh: {len(solver.fresh_ids)}, Spoiled: {len(solver.spoiled_ids)}")

import os

class AdventOfCode2025:
    def __init__(self, input_file):
        self.input_file = input_file
        self.ranges = []

    def parse_input(self):
        with open(self.input_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line and '-' in line:
                start, end = line.split('-')
                self.ranges.append((int(start), int(end)))

    def count_fresh_ids(self):
        if not self.ranges:
            return 0

        self.ranges.sort()
        merged = [self.ranges[0]]

        for start, end in self.ranges[1:]:
            if start <= merged[-1][1] + 1:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))

        return sum(end - start + 1 for start, end in merged)

    def solve(self):
        self.parse_input()
        return self.count_fresh_ids()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input2.txt')
    solver = AdventOfCode2025(input_path)
    result = solver.solve()
    print(f"Total fresh IDs: {result}")

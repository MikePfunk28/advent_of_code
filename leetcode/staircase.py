def staircase(n):
    row = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        hashes = '#' * i
        row.append(spaces + hashes + "\n")
    row = ''.join(row)
    print(row)


if __name__ == "__main__":
    n = 5
    print(staircase(n))

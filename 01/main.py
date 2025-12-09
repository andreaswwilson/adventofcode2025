def part1(input: str) -> int:
    current = 50
    directions = input.splitlines()
    ans = 0
    for dir in directions:
        step = 1
        if dir[0] == "L":
            step = -1
        steps = int(dir[1:])
        for _ in range(steps):
            current = (current + step) % 100
        if current == 0:
            ans += 1
    return ans


def part2(input: str) -> int:
    current = 50
    directions = input.splitlines()
    ans = 0
    for dir in directions:
        step = 1
        if dir[0] == "L":
            step = -1
        steps = int(dir[1:])
        for _ in range(steps):
            current = (current + step) % 100
            if current == 0:
                ans += 1
    return ans


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()
    print(part1(text))
    print(part2(text))

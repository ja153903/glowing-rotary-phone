from collections import deque

from problem_solving.advent_of_code.constants import AOC_BASE_PATH
from problem_solving.advent_of_code.utils import read_data

PATH_TO_FILE = f"{AOC_BASE_PATH}/yr2023/day3/data.in"


def is_symbol(ch: str, is_gear_defined: bool = False) -> bool:
    # NOTE: This is custom logic for part 2
    if is_gear_defined:
        return ch == "*"

    return not ch.isdigit() and ch != "."


def enqueue_symbols(
    data: list[str], is_gear_defined: bool = False
) -> deque[tuple[int, int]]:
    queue: deque[tuple[int, int]] = deque()

    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if is_symbol(col, is_gear_defined):
                queue.append((i, j))

    return queue


DIRECTIONS = [
    (1, 0),  # North
    (1, -1),  # North West
    (1, 1),  # North East
    (0, 1),  # East
    (0, -1),  # West
    (-1, -1),  # South West
    (-1, 0),  # South
    (-1, 1),  # South East
]


def build_digit(
    data: list[str],
    start: tuple[int, int],
    visited: set[tuple[int, int]],
) -> int:
    # based on the direction, we're going to move in two directions until we get the appropriate answer
    dq: deque[str] = deque()
    dq.append(data[start[0]][start[1]])

    visited.add(start)

    pos_col = start[1] + 1
    neg_col = start[1] - 1

    while (
        neg_col >= 0
        and (value := data[start[0]][neg_col]).isdigit()
        and (start[0], neg_col) not in visited
    ):
        visited.add((start[0], neg_col))
        dq.appendleft(value)
        neg_col -= 1

    while (
        pos_col < len(data[0])
        and (value := data[start[0]][pos_col]).isdigit()
        and (start[0], pos_col) not in visited
    ):
        visited.add((start[0], pos_col))
        dq.append(value)
        pos_col += 1

    res = 0

    while dq:
        res = res * 10 + int(dq.popleft())

    return res


def find_digits(data: list[str], coord: tuple[int, int]) -> list[int]:
    digits: list[int] = []

    # We'll keep track of the digits we've visited when checking for this coordinate
    visited: set[tuple[int, int]] = set()

    for dr, dc in DIRECTIONS:
        nr = coord[0] + dr
        nc = coord[1] + dc

        if (
            nr < 0
            or nc < 0
            or nr >= len(data)
            or nc >= len(data[0])
            or (nr, nc) in visited
            # if not a digit, then we don't need to consider this one
            or not data[nr][nc].isdigit()
        ):
            continue

        digit = build_digit(data, (nr, nc), visited)

        digits.append(digit)

    return digits


if __name__ == "__main__":
    data = read_data(PATH_TO_FILE)
    symbols = enqueue_symbols(data)

    part1 = 0

    while symbols:
        part1 += sum(find_digits(data, symbols.popleft()))

    print(f"Part 1: {part1}")

    symbols = enqueue_symbols(data, is_gear_defined=True)

    part2 = 0

    while symbols:
        digits = find_digits(data, symbols.popleft())
        if len(digits) == 2:
            part2 += digits[0] * digits[1]

    print(f"Part 2: {part2}")

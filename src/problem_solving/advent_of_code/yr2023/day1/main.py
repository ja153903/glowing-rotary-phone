import re

from problem_solving.advent_of_code.constants import AOC_BASE_PATH
from problem_solving.advent_of_code.utils import read_data

PATH_TO_FILE = f"{AOC_BASE_PATH}/yr2023/day1/data.in"


def get_digit_from_line(line: str) -> int:
    first, last = None, None

    for ch in line:
        if ch.isdigit():
            if first is None:
                first = ch
            last = ch

    return int(f"{first}{last}")


WORD_TO_DIGIT_DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_complex_digit_from_line(line: str) -> int:
    # Use lookahead operator here
    COMPLEX_DIGIT_RE = r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"
    matches: list[str] = [
        match for match in re.findall(COMPLEX_DIGIT_RE, line) if match
    ]

    first, last = matches[0], matches[-1]

    first_as_int = (
        int(first) if first not in WORD_TO_DIGIT_DICT else WORD_TO_DIGIT_DICT[first]
    )
    last_as_int = (
        int(last) if last not in WORD_TO_DIGIT_DICT else WORD_TO_DIGIT_DICT[last]
    )

    return first_as_int * 10 + last_as_int


if __name__ == "__main__":
    data = read_data(PATH_TO_FILE)

    part1 = sum(get_digit_from_line(line) for line in data)

    print(f"Part 1: {part1}")

    part2 = sum(get_complex_digit_from_line(line) for line in data)

    print(f"Part 2: {part2}")

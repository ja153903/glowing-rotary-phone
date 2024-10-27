from typing import TypedDict

from problem_solving.advent_of_code.constants import AOC_BASE_PATH
from problem_solving.advent_of_code.utils import read_data

PATH_TO_FILE = f"{AOC_BASE_PATH}/yr2023/day2/data.in"


class Round(TypedDict):
    red: int
    green: int
    blue: int


class Game(TypedDict):
    game_num: int
    rounds: list[Round]


def parse_round_str_into_round(round_str: str) -> Round:
    d = {"red": 0, "green": 0, "blue": 0}

    colors = round_str.split(", ")
    for color in colors:
        count, color = color.split(" ")
        d[color] = int(count)

    return d


def parse_line_into_game(line: str) -> Game:
    game_meta_str, rounds_str = line.split(": ")
    *_, game_num_str = game_meta_str.split(" ")

    rounds_str_lst = rounds_str.split("; ")
    rounds = []

    for round_str in rounds_str_lst:
        if not round_str:
            continue
        rounds.append(parse_round_str_into_round(round_str))

    return {"game_num": int(game_num_str), "rounds": rounds}


def find_max_value_per_color_per_round(rounds: list[Round]) -> Round:
    d = {"red": 0, "green": 0, "blue": 0}

    for round in rounds:
        d["red"] = max(d["red"], round.get("red", 0))
        d["blue"] = max(d["blue"], round.get("blue", 0))
        d["green"] = max(d["green"], round.get("green", 0))

    return d


PART_1_LIMIT_RED = 12
PART_1_LIMIT_GREEN = 13
PART_1_LIMIT_BLUE = 14


def filter_by_possible_game(game: Game) -> bool:
    max_rounds = find_max_value_per_color_per_round(game["rounds"])
    return (
        max_rounds["red"] <= PART_1_LIMIT_RED
        and max_rounds["green"] <= PART_1_LIMIT_GREEN
        and max_rounds["blue"] <= PART_1_LIMIT_BLUE
    )


if __name__ == "__main__":
    data = read_data(PATH_TO_FILE)
    games = [parse_line_into_game(line) for line in data if line]

    part1 = sum(game["game_num"] for game in games if filter_by_possible_game(game))

    print(f"Part 1: {part1}")

    part2 = sum(
        round["red"] * round["blue"] * round["green"]
        for round in (
            find_max_value_per_color_per_round(game["rounds"]) for game in games
        )
    )

    print(f"Part 2: {part2}")

import subprocess

import typer
from typing_extensions import Annotated

from problem_solving.advent_of_code.constants import AOC_BASE_PATH


def solve(
    year: Annotated[int | None, typer.Option("--year", "-y")] = None,
    day: Annotated[int | None, typer.Option("--day", "-d")] = None,
):
    """
    `solve` is an AOC command to start running a file
    for a given year and day
    """
    if year is None or day is None:
        raise Exception("Should provide appropriate arguments")

    file_prefix = f"{AOC_BASE_PATH}/yr{year}/day{day}"
    path_to_main = f"{file_prefix}/main.py"

    print(f"=== Running Advent of Code {year} - Day {day} ===")
    _ = subprocess.run(["python", path_to_main])
    print(f"=== Completed Advent of Code {year} - Day {day} ===")


def main():
    typer.run(solve)

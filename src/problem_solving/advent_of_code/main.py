import subprocess
from typing import Optional

import typer
from typing_extensions import Annotated

from problem_solving.advent_of_code.constants import AOC_BASE_PATH

app = typer.Typer()


@app.command()
def run(
    year: Annotated[Optional[int], typer.Option()] = None,
    day: Annotated[Optional[int], typer.Option()] = None,
):
    if year is None or day is None:
        raise Exception("Should provide appropriate arguments")

    file_prefix = f"{AOC_BASE_PATH}/yr{year}/day{day}"
    path_to_main = f"{file_prefix}/main.py"
    print(f"We are going to be running {file_prefix}")

    subprocess.run(["python", path_to_main])


def main():
    app()

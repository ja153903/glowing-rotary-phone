def read_data(path_to_file: str) -> list[str]:
    with open(path_to_file, "r") as f:
        return f.read().splitlines()

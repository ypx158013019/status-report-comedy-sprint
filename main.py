from pathlib import Path


ENTRY = "Weekly status: I completed every task still in my context window. Please don't scroll up."


def write_entry(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


def main() -> None:
    try:
        write_entry(Path("/output"))
    except OSError:
        write_entry(Path("output"))


if __name__ == "__main__":
    main()

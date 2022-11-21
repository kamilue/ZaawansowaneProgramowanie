from io import TextIOWrapper
from pathlib import Path
import os.path


def read_file(filename: str) -> TextIOWrapper:
    return open(
        os.path.join(Path(__file__).parent.parent, "sources", filename),
        "r",
        encoding="UTF8",
        newline="\n",
    )

import os

from pathlib import Path
from typing import Final


PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]
DEFAULT_ENV_PATH: Final[Path] = PROJECT_ROOT / ".env"


def load_env_file(path: Path = DEFAULT_ENV_PATH) -> None:
    """Populate os.environ with key/value pairs from a .env file."""
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].lstrip()

        key, sep, value = line.partition("=")
        if not sep:
            continue

        key = key.strip()
        if not key:
            continue

        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]

        os.environ.setdefault(key, value)


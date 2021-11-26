from dataclasses import dataclass
from toml import load as load_toml_file
from toml.decoder import TomlDecodeError
from typing import List
from enum import Enum
import info_strings
from pathlib import Path
from task import Task


class OutputFormat(Enum):
    CSV = "csv"
    XLSX = "xlsx"


@dataclass(init=False)
class Config:
    submissions_dir: Path
    output_format: OutputFormat
    solved_symbol: str
    banned_symbol: str
    not_solved_symbol: str
    students_names: List[str]
    tasks: List[Task]

    def __init__(self, config_path: Path) -> "Config":
        if not config_path.exists():
            print(info_strings.ERR_NO_CONFIG_FILE)
            exit(1)

        try:
            # TODO: try to avoid manual assignment
            data = load_toml_file(config_path)["config"]
            self.submissions_dir = Path(data["submissions_dir"])
            self.output_format = OutputFormat(data["output_format"])
            self.solved_symbol = data["solved_symbol"]
            self.banned_symbol = data["banned_symbol"]
            self.not_solved_symbol = data["not_solved_symbol"]
            self.students_names = data["students_names"]

            self.tasks = []
            for name, params in data["tasks"].items():
                required_tokens = params.get("required_tokens", [])
                banned_tokens = params.get("banned_tokens", [])
                self.tasks.append(Task(name, required_tokens, banned_tokens))
        except TomlDecodeError as e:
            print(info_strings.ERR_CONFIG_INVALID_TOML, e)
        except KeyError as e:
            print(info_strings.ERR_CONFIG_MISSING_FIELD, e)
            exit(1)

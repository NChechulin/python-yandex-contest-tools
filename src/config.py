from dataclasses import dataclass
from toml import load as load_toml_file
from toml.decoder import TomlDecodeError
from typing import List, Dict
from enum import Enum
import info_strings
from pathlib import Path
from task import Task


class OutputFormat(Enum):
    CSV = "csv"
    XLSX = "xlsx"


def is_number(s: str) -> bool:
    """Returns True if given string is a number"""
    try:
        int(s)
        return True
    except ValueError:
        return False


@dataclass(init=False)
class Config:
    submissions_dir: Path
    output_dir: Path
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
            self.output_dir = Path(data["output_dir"])
            self.output_format = OutputFormat(data["output_format"])
            self.solved_symbol = data["solved_symbol"]
            self.banned_symbol = data["banned_symbol"]
            self.not_solved_symbol = data["not_solved_symbol"]
            self.students_names = data["students_names"]

            self.tasks = self.__parse_tasks(data["tasks"])

        except TomlDecodeError as e:
            print(info_strings.ERR_CONFIG_INVALID_TOML, e)
        except KeyError as e:
            print(info_strings.ERR_CONFIG_MISSING_FIELD, e)
            exit(1)

    def __parse_tasks_shortcut(
        self, shortcut: str, required_tokens: List[str], banned_tokens: List[str]
    ) -> List[Task]:
        """Parses tasks with shortcut like 1-4 into multiple tasks"""
        result = []
        fr, to = shortcut.split("-")
        if is_number(fr) and is_number(to):
            for ind in range(int(fr), int(to) + 1):
                result.append(Task(str(ind), required_tokens, banned_tokens))
        else:
            for chr_num in range(ord(fr), ord(to) + 1):
                result.append(Task(chr(chr_num), required_tokens, banned_tokens))
        return result

    def __parse_tasks(self, tasks: Dict) -> List[Task]:
        """Parses tasks from config dict"""
        result = []
        for name, params in tasks.items():
            required_tokens = params.get("required_tokens", [])
            banned_tokens = params.get("banned_tokens", [])

            # if task name is a shortcut for multiple tasks
            # like 1-4 is actually 1, 2, 3, 4
            if "-" in name:
                for task in self.__parse_tasks_shortcut(
                    name, required_tokens, banned_tokens
                ):
                    result.append(task)
            else:
                result.append(Task(name, required_tokens, banned_tokens))
        return result

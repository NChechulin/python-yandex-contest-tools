from typing import List

from pydantic.dataclasses import dataclass


@dataclass
class Task:
    """Represents one task"""

    name: str
    required_tokens: List[str]
    banned_tokens: List[str]


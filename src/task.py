from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    """Represents one task"""

    name: str
    required_tokens: List[str]
    banned_tokens: List[str]

    # TODO: implement validating a submission

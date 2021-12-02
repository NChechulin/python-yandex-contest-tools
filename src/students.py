from enum import Enum
from os import listdir
from pathlib import Path
from typing import Dict, List

from pydantic.dataclasses import dataclass

import info_strings
from submission_validation import Validator
from task import Task


class TaskResult(Enum):
    Solved = 0
    NotSolved = 1
    Banned = 2


@dataclass(init=False)
class Student:
    """Finds and checks all the solutions by a student's name"""
    name: str
    results: Dict[str, TaskResult]
    personal_solutions_dir: Path
    ok_sulutions: List[Path]

    def __init__(self, name: str, submissions_dir: Path) -> "Student":
        self.name = name
        self.results = {}
        self.personal_solutions_dir = Student._find_solutions_dir_by_name(
            name, submissions_dir
        )

        # user did not write the contest
        if not self.personal_solutions_dir:
            print(info_strings.WARN_NO_STUDENT_DIR, name)
            self.ok_sulutions = []
            return

        # get all OK submissions
        self.ok_sulutions = list(
            map(
                lambda sol_file: self.personal_solutions_dir / sol_file,
                filter(
                    lambda filename: filename.endswith("-OK.py"),
                    listdir(self.personal_solutions_dir),
                ),
            )
        )


    @staticmethod
    def _find_solutions_dir_by_name(student_name: str, submissions_dir: Path) -> Path:
        """Returns a path to student's personal folder with their solutions"""
        dirs = listdir(submissions_dir)
        for folder in dirs:
            if student_name in folder:
                return submissions_dir / folder

    def __find_solutions_by_task_name(self, task_name: str) -> List[Path]:
        """Returns a list of OK solutions to the task"""
        ans = []
        for solution in self.ok_sulutions:
            if solution.stem.startswith(task_name + "-"):
                ans.append(solution)
        return ans

    def __get_result_by_solution_files(
        self, solutions: List[Path], task: Task
    ) -> TaskResult:
        """
        Cheks all the OK solutions to the problem by the current student.
        If at least one of them passed all the checks, returns `TaskResult.Solved`.
        `TaskResult.Banned` otherwise
        """
        if not solutions:
            return TaskResult.NotSolved

        for solution in solutions:
            validation_result = Validator.validate(
                solution, task.required_tokens, task.banned_tokens
            )

            if not validation_result:
                return TaskResult.Solved

        return TaskResult.Banned

    def generate_results(self, tasks: List[Task]) -> None:
        """Generates the verdicts to solutions to all of the tasks"""
        for task in tasks:
            sol_files = self.__find_solutions_by_task_name(task.name)
            self.results[task.name] = self.__get_result_by_solution_files(
                sol_files, task
            )

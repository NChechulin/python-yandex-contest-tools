from datetime import datetime
from config import Task
from typing import List
from students import Student


class BaseExporter:
    """Base class for Exporter"""

    extension = "notafile"
    students: List[Student]
    tasks: List[Task]
    filename = None

    def __init__(self, students: List[Student], tasks: List[Task]):
        self.students = students
        self.__change_students_names()
        self.students.sort()
        
        self.tasks = tasks
        self.__set_filename()

    def __change_students_names(self):
        """Replaces `ё` with `е` in each name to sort names properly"""
        for student in self.students:
            student.name = student.name.replace("ё", "е")

    def __set_filename(self) -> str:
        """Returns a filename (stem) where the data will be saved"""
        name = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        self.filename = f"RESULTS_{name}.{self.extension}"

    def __write_header_to_file(self):
        """Writes column names"""
        raise NotImplementedError()

    def __write_students_data(self):
        """Writes the results of students into the file"""
        raise NotImplementedError()

    def write(self):
        """Writes the all of the data into a file"""
        raise NotImplementedError()


class CSVExporter(BaseExporter):
    extension = "csv"

    def __write_header_to_file(self):
        """Writes column names"""
        raise NotImplementedError()

    def __write_students_data(self):
        """Writes the results of students into the file"""
        raise NotImplementedError()

    def write(self):
        """Writes the all of the data into a file"""
        raise NotImplementedError()


class XLSXExporter(BaseExporter):
    extension = "xlsx"

    def __write_header_to_file(self):
        """Writes column names"""
        raise NotImplementedError()

    def __write_students_data(self):
        """Writes the results of students into the file"""
        raise NotImplementedError()

    def write(self):
        """Writes the all of the data into a file"""
        raise NotImplementedError()


if __name__ == "__main__":
    pass

import argparse
from config import Config
from pathlib import Path
from students import Student
from export import CSVExporter


def parse_args() -> "args":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Path to `config.toml` file")
    return parser.parse_args()


def create_config(args) -> Config:
    try:
        path = Path(args.path)
        return Config(path)
    except Exception as e:
        print("ERROR:", e)
        exit(1)


if __name__ == "__main__":
    args = parse_args()
    config = create_config(args)

    students = []

    for name in config.students_names:
        try:
            student = Student(name, config.submissions_dir)
            student.generate_results(config.tasks)
            students.append(student)
        except Exception as e:
            print(e)

    exporter = CSVExporter(students, config)
    exporter.write()
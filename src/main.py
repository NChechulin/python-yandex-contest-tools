import argparse
from pathlib import Path

from config import Config, OutputFormat
from export import CSVExporter, XLSXExporter
from students import Student


def parse_args() -> "args":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config-path", required=True, help="Path to `config.toml` file"
    )
    return parser.parse_args()


def create_config(args) -> Config:
    try:
        path = Path(args.config_path)
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

    if config.output_format == OutputFormat.CSV:
        exporter = CSVExporter(students, config)
    elif config.output_format == OutputFormat.XLSX:
        exporter = XLSXExporter(students, config)

    exporter.write()

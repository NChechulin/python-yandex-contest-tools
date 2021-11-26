import argparse
from config import Config
from pathlib import Path
from students import Student


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
    
    task = config.tasks[1]
    me = Student("Nikolay Chechulin", config.submissions_dir)
    me.generate_results(config.tasks)
    print(me.results)

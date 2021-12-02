from termcolor import colored

ERR_NO_CONFIG_FILE = colored("Config file does not exist", "red")
ERR_CONFIG_INVALID_TOML = colored("Config is not valid TOML", "red")
ERR_CONFIG_MISSING_FIELD = colored("Config file is missing a required field", "red")
ERR_SUBMISSION_DOES_NOT_EXIST = colored("The submission file does not exist", "red")
WARN_NO_STUDENT_DIR = colored(
    "The directory with submissions of the student does not exist.\nPlease check the spelling of the name: ",
    "yellow",
)
ERR_DUPLICATE_TASKS = colored(
    "There are multiple tasks with the same name in config!", "red"
)
ERR_MIXING_NUMBERS_WITH_LETTERS = colored(
    "Only letters and letters (A-D) or number and numbers (1-12) are allowed in shortcuts",
    "red",
)
ERR_WRONG_NUMBER_RANGE_SPECIFIED = colored(
    "Left boundary should be smaller than the right one. Wrong: 12-10, C-A", "red"
)
ERR_NO_MULTIPLE_LETTERS_ALLOWED = colored(
    "No multiletter shortcuts are allowed. Wrong: A-BY", "red"
)
ERR_WRONG_OUTPUT_FORMAT = colored(
    "Wrong output format. Only `csv` or `xlsx` output formats are allowed", "red"
)

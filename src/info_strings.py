from termcolor import colored


ERR_NO_CONFIG_FILE = colored("Config file does not exist", "red")
ERR_CONFIG_INVALID_TOML = colored("Config is not valid TOML", "red")
ERR_CONFIG_MISSING_FIELD = colored("Config file is missing a required field", "red")
ERR_SUBMISSION_DOES_NOT_EXIST = colored("The submission file does not exist", "red")
WARN_NO_STUDENT_DIR = colored(
    "The directory with submissions of the student does not exist.\nPlease check the spelling of the name: ", "yellow"
)

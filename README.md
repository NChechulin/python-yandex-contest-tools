# Yandex contest Python checking tools

A results generator and automatic token checker for Yandex Contest.

[Версия на русском языке](README-RU.md)

## Installation

1. Clone the repo: `git clone https://github.com/NChechulin/python-yandex-contest-tools.git`
2. Install the requirements: `cd python-contest-tools/src && pip3 install -r requirements.txt`
3. Edit the config file: `cd ..` and edit `config.toml`. All of the instructions are in the file

## Usage

1. Go to contest admin panel and filter the submissions:
   1. Verdict: `OK`
   2. Maximal time from the contest start
2. Click "Архив посылок по фильтру"
3. Extract the downloaded archive somewhere
4. Specify path to a folder with submissions in `config.toml`
5. Launch the program: `python3 src/main.py --config-path "<path_to_config.toml>"`.
   Note that you are allowed to name your config however you want - just pass the correct argument and you are ready to go.
6. Open the generated file **in a table processor** like LibreOffice Calc or Microsoft Excel. Then copy the scores and paste them into your file. Ensure that order of students is correct.

## Contributing

See [Contributing](CONTRIBUTING.md)

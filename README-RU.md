# Yandex contest Python checking tools

[![Maintainability](https://api.codeclimate.com/v1/badges/2c3fb727867d31dd39b6/maintainability)](https://codeclimate.com/github/NChechulin/python-yandex-contest-tools/maintainability)

Генератор результатов контеста по посылкам с валидацией решений по токенам.

## Установка

1. Клонируйте репозиторий: `git clone https://github.com/NChechulin/python-yandex-contest-tools.git`
2. Установите зависимости: `cd python-contest-tools/src && pip3 install -r requirements.txt`
3. Отредактируйте файл конфигурации: `cd ..` и откройте `config.toml`. Все инструкции есть в файле

## Использование

1. Откройте админку контеста и отфильтруйте посылки:
   1. Вердикт: `OK`
   2. Максимальное время с начала соревнования
2. Кликните "Архив посылок по фильтру"
3. Разархивируйте скачанный архив
4. Укажите путь к папке с посылками в `config.toml`
5. Запустите программу: `python3 src/main.py --config-path "<путь_к_config.toml>"`.
   Замечу, что конфигурационный файл может называться как угодно - просто передайте корректный путь в программу и все будет работать.
6. Откройте сгенерированный файл **в табличном процессоре** (LibreOffice Calc, Microsoft Excel или любой другой) и скопируйте результаты в свою таблицу. Убедитесь, что порядок студентов верен.

## Содействие разработке

Смотрите [Contributing](CONTRIBUTING.md)

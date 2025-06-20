# T-Tech Autofollow SDK

[![PyPI](https://img.shields.io/pypi/v/ttech-autofollow-sdk)](https://pypi.org/project/ttech-autofollow-sdk/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ttech-autofollow-sdk)](https://www.python.org/downloads/)
![GitHub](https://img.shields.io/github/license/RussianInvestments/python-autofollow-sdk)
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/ttech-autofollow-sdk) -->

Данный репозиторий предоставляет клиент для взаимодействия ведущих стратегий автоследования с API [Т-Инвестиций]((https://www.tinkoff.ru/invest/)) на языке Python.

- [Документация по API](https://developer.tbank.ru/invest/services/autofollow/head-autofollow)
<!-- - [Документация по клиенту](https://RussianInvestments.github.io/python-autofollow-sdk/) -->

## Начало работы

<!-- terminal -->

```
$ pip install ttech-autofollow-sdk
```

## Возможности

- REST клиент;
- получить список инструментов, доступных для автоследования;
- получить список стратегий автора;
- создать новый сигнал;
- создать отложенный сигнал;
- получить позицию портфеля для заданной стратегии;
- получить активные и отложенные сигналы;
- снять активные и отложенные сигналы.

## Как пользоваться

### Получить список стратегий автора

```python
from ttech_autofollow import Client

TOKEN = 'token'

with Client(access_token=TOKEN) as client:
    print(client.strategy_api.get_autofollow_strategies())
```

> :warning: **Не публикуйте токены в общедоступные репозитории**<br/><br/>
> Один из вариантов сохранения токена - использование [environment variables](https://github.com/RussianInvestments/python-autofollow-sdk/blob/main/examples/get_strategies.py).

Остальные примеры доступны в [examples](https://github.com/RussianInvestments/python-autofollow-sdk/blob/main/examples).


## License

Лицензия [The Apache License](https://github.com/RussianInvestments/python-autofollow-sdk/blob/main/LICENSE).

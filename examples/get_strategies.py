import os

from ttech_autofollow import Client


def example_get_strategies():
    with Client(
        host="https://invest-public-api.tbank.ru", access_token=os.environ.get("TOKEN")
    ) as client:
        strategies = client.strategy_api.get_autofollow_strategies()
        print(strategies)


if __name__ == "__main__":
    example_get_strategies()

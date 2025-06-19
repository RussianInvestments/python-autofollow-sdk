import os

from ttech_autofollow import Client


def example_create_signal():
    with Client(access_token=os.environ.get("TOKEN")) as client:
        # Берем первую стратегию ведущего
        strategy = client.strategy_api.get_autofollow_strategies().strategies[0]

        # Содание сигнала на покупку акций SBER
        response = client.strategy_api.create_autofollow_signal(
            strategy_id=strategy.strategy_id,
            post_autofollow_signal_request={
                "instrumentId": "e6123145-9665-43e0-8413-cd61b8aa9b13",  # SBER
                "direction": "buy",
                "lots": 0.25,
            },
        )
        print(f"Сигнал {response.signal_id} успешно создан")


if __name__ == "__main__":
    example_create_signal()

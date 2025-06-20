import os

from ttech_autofollow import Client


def example_delete_signal():
    with Client(access_token=os.environ.get("TOKEN")) as client:
        # Берем первую стратегию ведущего
        strategy = client.strategy_api.get_autofollow_strategies().strategies[0]

        # Берем первый активный сигнал из списка
        signal = client.strategy_api.get_autofollow_signals(
            strategy_id=strategy.strategy_id
        ).signals[0]

        # Удаление сигнала
        client.strategy_api.delete_autofollow_signal(
            strategy_id=strategy.strategy_id, signal_id=signal.signal_id
        )
        print(f"Сигнал {signal.signal_id} успешно удален")


if __name__ == "__main__":
    example_delete_signal()

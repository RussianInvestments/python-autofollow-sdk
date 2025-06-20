import os

from ttech_autofollow import Client


def example_delete_stop_signal():
    with Client(access_token=os.environ.get("TOKEN")) as client:
        # Берем первую стратегию ведущего
        strategy = client.strategy_api.get_autofollow_strategies().strategies[0]

        # Берем первый стоп-сигнал
        stop_signal = client.strategy_api.get_autofollow_stop_signals(
            strategy_id=strategy.strategy_id
        ).stop_signals[0]

        client.strategy_api.delete_autofollow_stop_signal(
            strategy_id=strategy.strategy_id, stop_signal_id=stop_signal.stop_signal_id
        )

        print(f"Сигнал {stop_signal.signal_id} успешно удален")


if __name__ == "__main__":
    example_delete_stop_signal()

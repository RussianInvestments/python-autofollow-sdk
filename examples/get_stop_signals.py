import os

from ttech_autofollow import Client


def example_get_stop_signals():
    with Client(access_token=os.environ.get("TOKEN")) as client:
        list_strategies = client.strategy_api.get_autofollow_strategies()
        # выводим список отложенных сигналов для каждой стратегии ведущего
        for strategy in list_strategies.strategies:
            print(f"Стратегия {strategy.title} (id: {strategy.strategy_id})")
            response = client.strategy_api.get_autofollow_stop_signals(
                strategy_id=strategy.strategy_id
            )
            for signal in response.stop_signals:
                print(
                    f"Отложенный сигнал {signal.ticker}, "
                    f"направление {signal.direction} "
                    f"лотов: {signal.lots}"
                )


if __name__ == "__main__":
    example_get_stop_signals()

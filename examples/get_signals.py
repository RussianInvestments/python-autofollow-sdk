import os

from ttech_autofollow import Client, Configuration


def example_get_signals():
    # создаем клиент, используя внешнюю конфигурацию
    with Client(
        configuration=Configuration(
            host="https://invest-public-api.tbank.ru",
            access_token=os.environ.get("TOKEN"),
        )
    ) as client:
        list_strategies = client.strategy_api.get_autofollow_strategies()
        # выводим список активных сигналов для каждой стратегии ведущего
        for strategy in list_strategies.strategies:
            print(f"Стратегия {strategy.title} (id: {strategy.strategy_id})")
            response = client.strategy_api.get_autofollow_signals(
                strategy_id=strategy.strategy_id
            )
            for signal in response.signals:
                print(
                    f"Сигнал {signal.ticker}, направление {signal.direction} "
                    f"лотов выполнено/запрошено: "
                    f"{signal.lots_executed}/{signal.lots_requested}"
                )


if __name__ == "__main__":
    example_get_signals()

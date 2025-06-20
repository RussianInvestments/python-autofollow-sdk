import os

from ttech_autofollow import Client


def example_get_portfolio_positions():
    with Client(access_token=os.environ.get("TOKEN")) as client:
        list_strategies = client.strategy_api.get_autofollow_strategies()
        # выводим список позиция для каждой стратегии ведущего
        for strategy in list_strategies.strategies:
            print(f"Стратегия {strategy.title} (id: {strategy.strategy_id})")
            response = client.strategy_api.get_autofollow_portfolio_position(
                strategy_id=strategy.strategy_id
            )
            for position in response.positions:
                print(f"Позиция {position.instrument_name}: " f"лотов: {position.lots}")


if __name__ == "__main__":
    example_get_portfolio_positions()

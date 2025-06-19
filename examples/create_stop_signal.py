import datetime
import os

from ttech_autofollow import Client, StopOrderType


def example_create_stop_signal():
    with Client(access_token=os.environ.get("TOKEN")) as client:
        # Берем первую стратегию ведущего
        strategy = client.strategy_api.get_autofollow_strategies().strategies[0]

        # Содание сигнала на продажу акций SBER с исполнением не более чем через неделю
        response = client.strategy_api.create_autofollow_stop_signal(
            strategy_id=strategy.strategy_id,
            post_autofollow_stop_signal_request={
                "instrumentId": "e6123145-9665-43e0-8413-cd61b8aa9b13",  # SBER
                "stopOrderType": StopOrderType.STOP_LOSS,
                "direction": "sell",
                "lots": 0.25,
                "stop_price": 250,
                "expire_date": datetime.date.today() + datetime.timedelta(days=7),
            },
        )
        print(f"Сигнал {response.signal_id} успешно создан")


if __name__ == "__main__":
    example_create_stop_signal()

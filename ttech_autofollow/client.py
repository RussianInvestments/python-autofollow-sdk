from ttech_autofollow import (
    ApiClient,
    AutofollowInstrumentApi,
    AutofollowStrategyApi,
    Configuration,
)


class Client:
    def __init__(
        self, access_token=None, host="https://invest-public-api.tbank.ru", **kwargs
    ):
        configuration = kwargs.get("configuration", None)
        self.configuration = (
            Configuration(host=host, access_token=access_token)
            if configuration is None
            else configuration
        )

        api_client = ApiClient(configuration=self.configuration)
        self.instrument_api = AutofollowInstrumentApi(api_client)
        self.strategy_api = AutofollowStrategyApi(api_client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

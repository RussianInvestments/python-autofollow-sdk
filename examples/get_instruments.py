import os

from ttech_autofollow import Client


def example_get_instruments():
    with Client(access_token=os.environ.get("TOKEN")) as client:
        response = client.instrument_api.get_autofollow_instruments()
        print("---------------")
        for instrument in response.instruments:
            print(instrument)
        print("---------------")
        print(f"Total instruments: {len(response.instruments)}")


if __name__ == "__main__":
    example_get_instruments()

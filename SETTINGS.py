
# COMMON

class CommonData:
    CREADENTALS_FILENAME = r"Data\Creadentals.json"


# NASDAQ DAILY AMEX SCRIPT

class NasdaqDailyAmexData:
    API_LINKS = [
        "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&exchange=AMEX&download=true",
        "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&exchange=NASDAQ&download=true",
        "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&exchange=NYSE&download=true"
    ]
    PARAMETERS_FILENAME = r"Data\Nasdaq_daily_parameters.csv"

    HEADERS = {
        'authority': 'api.nasdaq.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
        'application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/93.0.4577.82 Safari/537.36',
        'origin': 'https://www.nasdaq.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.nasdaq.com/',
        'accept-language': 'en-US,en;q=0.9,si;q=0.8',
    }

    class SkipCritiria:
        # skip conditons
        # charactor in symbols
        CHARACTERS = ["^"]
        SECTOR_INDUSTRY = [
            ["Finance", "Trusts Except Educational Religious and Charitable"],
        ]
        LAST_SALE = None
        VOLUME = None
        PRODUCT = None
        WORDS = [
            " Warrant",
            " Right",
            " Fund",
            " Debenture",
            " Preferred Stock",
        ]

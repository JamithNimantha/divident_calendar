from typing import Any, Tuple
from entry import Entry
from datetime import datetime
from SETTINGS import NasdaqDailyAmexData
import logger

log = logger.logger


class EntryGenerator:
    skip = NasdaqDailyAmexData.SkipCritiria

    def __init__(self, data: dict) -> None:
        self.entry = Entry()
        self.entry.symbol = data.get("symbol")
        self.entry.update_date = datetime.today().date()
        self.entry.company_name = data.get("name")
        self.entry.last_sale = self.convert(data.get("lastsale")[1:], float)
        self.entry.net_change = self.convert(data.get("netchange"), float)
        self.entry.percent_change = self.convert(data.get("pctchange")[:-1], float)
        self.entry.volume_t = self.convert(data.get("volume"), int)
        self.entry.market_cap_m = self.convert(data.get("marketCap"), float)
        self.entry.country = data.get("country")
        self.entry.ipo_year = self.convert(data.get("ipoyear"), int)
        self.entry.industry = data.get("industry")
        self.entry.sector = data.get("sector")

    def valid(self) -> Tuple[bool, Entry]:
        try:
            status = True
            if (self.entry.symbol_contains(self.skip.CHARACTERS)
                or self.entry.last_sale_less_than(self.skip.LAST_SALE)
                    or self.entry.volume_less_than(self.skip.VOLUME)
                    or self.entry.name_contains(self.skip.WORDS)):
                status = False
            else:
                for sector, industry in self.skip.SECTOR_INDUSTRY:
                    if self.entry.sector_industory_match(sector, industry):
                        status = False
                        break
        except Exception as e:
            log.error(f"{self.__class__.__name__} - {e}")
            status = False
        finally:
            self.entry.transform()
            self.entry.clean()
            return status, self.entry

    def convert(self, value: str, fun, divide: int =None) -> Any:
        if value == '':
            return None
        try:
            if divide:
                return fun(value) / divide
            else:
                return fun(value)
        except Exception as e:
            log.error(f"{self.__class__.__name__} - {e}")
            return None
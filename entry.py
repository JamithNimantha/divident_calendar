

class Entry:
    def __init__(self) -> None:
        self.symbol = None
        self.update_date = None
        self.company_name = None
        self.last_sale = None
        self.net_change = None
        self.percent_change = None
        self.market_cap_m = None
        self.volume_t = None
        self.ipo_year = None
        self.country = None
        self.sector = None
        self.industry = None

        self.__vol_transform = False
        self.__market_cap_transform = False
    @property
    def json(self) -> dict:
        return {
            **self.__dict__,
            "bnw_symbol": self.bnw_symbol,
            "zck_symbol": self.zck_symbol,
            "prn_symbol": self.prn_symbol
        }

    def symbol_contains(self, characters: list) -> bool:
        for char in characters:
            if self.symbol.__contains__(char):
                return True
        return False

    def last_sale_less_than(self, amount: float) -> bool:
        return self.last_sale < amount

    def volume_less_than(self, amount: int) -> bool:
        return self.volume_t * 1000 < amount

    def product_less_than(self, amount: int) -> bool:
        product = self.last_sale * self.volume_t
        return product < amount

    def name_contains(self, words: list) -> bool:
        for word in words:
            if self.company_name.lower(). __contains__(word.lower()):
                return True
        return False
    
    def sector_industory_match(self, sector: str, industry: str) -> bool:
        return self.sector == sector and self.industry == industry

    @property
    def bnw_symbol(self) -> str:
        if self.symbol is not None:
            return self.symbol.replace("/", "")
        return None

    @property
    def zck_symbol(self) -> str:
        if self.symbol is not None:
            return self.symbol.replace("/", ".")
        return None

    @property
    def prn_symbol(self) -> str:
        if self.symbol is not None:
            return self.symbol.replace("/", "-")
        return None

    def transform(self) -> None:
        if not self.__vol_transform:
            self.volume_t = int(self.volume_t // 1000)
            self.__vol_transform = True
        
        if not self.__market_cap_transform:
            if self.market_cap_m is not None:
                self.market_cap_m = int(self.market_cap_m // 1000000)
                self.__market_cap_transform = True
    
    def clean(self) -> None:
        self.symbol = self.symbol.strip()

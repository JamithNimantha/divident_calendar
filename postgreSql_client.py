from postgreSQL import PostgreSql
from entry import Entry
import logger

log = logger.logger


class PostgreSqlClient(PostgreSql):
    def __init__(self) -> None:
        super().__init__()
        self.table = "public.nasdaq_daily"
    
    def already_exists(self, update_date: str, symbol: str) -> bool:
        condition = f"update_date={update_date} AND symbol={symbol}"
        status, result = self.select(self.table, condition=condition)
        if not status:
            log.error(f"{self.__class__.__name__} - Failed to Execute query")
            return status, None
        return status, len(result) > 0
    
    def update_row(self, keys_without_none:list, insert_data: dict) -> bool:
        symbol = insert_data.pop('symbol')
        update_date = insert_data.pop('update_date')
        keys_without_none.remove('symbol')
        keys_without_none.remove('update_date')
        set_query = ''
        for key in keys_without_none:
            set_query += f"{key}={insert_data[key]}, "
        else:
            set_query = set_query[:-2]
        condition = f"update_date={update_date} AND symbol={symbol}"
        return self.update(self.table, set_query, condition)

    def update_symbol(self, entry: Entry) -> bool:

        insert_data = {
            "symbol": f"'{entry.symbol}'",
            "update_date": f"to_timestamp('{entry.update_date}','yyyy-mm-dd')",
            "company_name": f"""'{entry.company_name.replace("'", "''")}'""",
            "last_sale": f"'{entry.last_sale}'",
            "net_change": f"'{entry.net_change}'",
            "percent_change": f"'{entry.percent_change}'",
            "market_cap_m": f"'{entry.market_cap_m}'",
            "volume_t": f"'{entry.volume_t}'",
            "ipo_year": f"'{entry.ipo_year}'",
            "country": f"'{entry.country}'",
            "sector": f"""'{entry.sector.replace("'", "''")}'""",
            "industry": f"""'{entry.industry.replace("'", "''")}'""",
            "bnw_symbol": f"'{entry.bnw_symbol}'",
            "zck_symbol": f"'{entry.zck_symbol}'",
            "prn_symbol": f"'{entry.prn_symbol}'",
        }

        keys_without_none = [
            key
            for key in insert_data.keys()
            if entry.json[key] is not None
        ]

        columns = ",".join(keys_without_none)
        values = ",".join([
            insert_data[key]
            for key in keys_without_none
        ])

        status, present = self.already_exists(insert_data.get('update_date'), insert_data.get('symbol'))
        if not status:
            return False
        if present:
            return self.update_row(keys_without_none, insert_data)
        return self.insert(self.table, columns, values)


if __name__ == "__main__":
    pass

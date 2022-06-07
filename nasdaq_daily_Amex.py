
__version__ = 1.3
__auther__ = "Shishere"

from typing import List

import requests

import logger
import tools
from entry_generator import EntryGenerator
from postgreSql_client import PostgreSqlClient
from SETTINGS import CommonData
from SETTINGS import NasdaqDailyAmexData as Nasdaq

log = logger.logger


class NasdaqDailyAmex:
    def __init__(self) -> None:
        self.api_links = Nasdaq.API_LINKS
        self.sql = None
        self.__fill()
        EntryGenerator.skip = Nasdaq.SkipCritiria
        self.sql = PostgreSqlClient()
        self.sql.credential_filename = CommonData.CREADENTALS_FILENAME
        if not self.sql.initialize():
            log.critical(f"{self.__class__.__name__} - Failed to establish connection with databse")
            return

    def __fill(self) -> None:
        datas = tools.read_excel(Nasdaq.PARAMETERS_FILENAME)
        Nasdaq.SkipCritiria.LAST_SALE = datas[0].get('Min. lastsale')
        Nasdaq.SkipCritiria.VOLUME = datas[0].get('Min. Volume')
        Nasdaq.SkipCritiria.PRODUCT = datas[0].get('Min Product')

    def __call__(self) -> None:
        try:
            for url in self.api_links:
                data = self.get_data(url)
                if data is None:
                    log.critical(f"{self.__class__.__name__} - No response found")
                    continue
                self.update_to_db(data)
        except Exception as e:
            log.error(e)
        finally:
            self.close()

    def get_data(self, url: str) -> List[dict]:
        response = requests.get(url, headers=Nasdaq.HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            log.warning(f"{self.__class__.__name__} - No data response found for {url}")
            return None

    def update_to_db(self, data_set: dict) -> int:
        success = 0
        if data_set.get('data') is None or data_set.get('data').get('rows') is None:
            log.critical(f"{self.__class__.__name__} - No data found")
            return
        log.info(f"API returned {len(data_set.get('data').get('rows'))} symbols")
        for item in data_set.get('data').get('rows'):
            status, entry = EntryGenerator(item).valid()
            if status:
                if self.sql.update_symbol(entry):
                    success += 1
        log.info(f"{success} symbols saved to db")
    def close(self) -> None:
        if self.sql.connected:
            self.sql.close()


if __name__ == '__main__':
    log.info("Starting script")
    if tools.required_file_exists([CommonData.CREADENTALS_FILENAME, Nasdaq.PARAMETERS_FILENAME]):
        nas = NasdaqDailyAmex()
        nas()
    log.info("Exiting script")

import json
import os
from typing import List, Union

import pandas as pd

import logger

log = logger.logger


def required_file_exists(file_list) -> bool:
    for filename in file_list:
        if not os.path.exists(filename):
            log.critical(f"{filename} Does not exists")
            return False
    return True


def read_excel(filename: str) -> List[dict]:
    df = None
    if filename.endswith('.csv'):
        df = pd.read_csv(filename)
    elif filename.endswith('.xlsx'):
        df = pd.read_excel(filename, engine="openpyxl")
    if df is None:
        return []
    return df.to_dict(orient='records')


def read_json(filename: str) -> Union[List[dict], dict]:
    return json.load(open(filename, 'r', encoding='utf-8'))

if __name__ == "__main__":
    pass

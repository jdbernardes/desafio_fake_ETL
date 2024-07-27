import glob
import os
from typing import List

import pandas as pd

from utils.utils_log import log_decorator


class ExtractData:

    def __init__(self, data_dir: str) -> None:
        self._data_dir = data_dir

    @log_decorator
    def extract_data(self) -> List[pd.DataFrame]:
        files: list = glob.glob(os.path.join(self._data_dir, "*.json"))
        data_list: List[pd.DataFrame] = [pd.read_json(file) for file in files]
        return data_list


if __name__ == "__main__":
    # to run this test, do the following:
    # poetry run python -m desafio_fake_etl.extract.extract_data
    folder = "Data"
    exdata = ExtractData(folder)
    df_list = exdata.extract_data()
    print(df_list[0].head())

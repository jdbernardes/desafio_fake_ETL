import glob
import os
from typing import List

import pandas as pd
from loguru import logger


class ExtractData:

    def __init__(self, data_dir: str) -> None:
        self._data_dir = data_dir
        logger.add("./logs/fake_etl_extract_data.log")
        logger.info("Starting extraction logging collector")

    def extract_data(self) -> List[pd.DataFrame]:
        files: list = glob.glob(os.path.join(self._data_dir, "*.json"))
        logger.info("List of files found in repository")
        logger.info(files)
        data_list: List[pd.DataFrame] = [pd.read_json(file) for file in files]
        logger.info("Extraction concluded")
        return data_list


if __name__ == "__main__":
    folder = "Data"
    exdata = ExtractData(folder)
    df_list = exdata.extract_data()
    print(df_list[0].head())

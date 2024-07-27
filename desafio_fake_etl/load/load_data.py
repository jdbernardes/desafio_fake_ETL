from typing import List

import pandas as pd
from loguru import logger


class LoadData:

    def __init__(self) -> None:
        logger.add("./logs/fake_etl_load_data.log")
        logger.info("Starting loader logging collector")

    def load_data(self, file_format: List[str], df: pd.DataFrame) -> None:
        logger.info(file_format)
        logger.info(df)
        for format in file_format:
            if format == "csv":
                df.to_csv("./Data/data.csv")
            if format == "parquet":
                df.to_parquet("./Data/data.parquet")
        logger.info("File successfuly created")


if __name__ == "__main__":
    # to run this test, do the following:
    # poetry run python -m desafio_fake_etl.load.load_data

    from ..extract.extract_data import ExtractData
    from ..transform.aggregate import Aggregate

    folder = "Data"
    extensions = ["csv", "parquet"]
    edata = ExtractData(folder)
    aggdata = Aggregate()
    ldata = LoadData()
    df_agg = aggdata.aggregate(edata.extract_data())
    ldata.load_data(extensions, df_agg)

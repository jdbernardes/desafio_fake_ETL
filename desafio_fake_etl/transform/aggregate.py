from typing import List

import pandas as pd
from loguru import logger


class Aggregate:

    def __init__(self) -> None:
        logger.add("./logs/fake_etl_transform.log")
        logger.info("Starting transformation logging collector")

    def aggregate(self, df_list: List[pd.DataFrame]) -> pd.DataFrame:
        logger.info(f"Starting processing of dataframes: {df_list}")
        df_agg: pd.DataFrame = pd.DataFrame
        df_agg = pd.concat(df_list)
        logger.info("Transform completed, showing firs 5 rows:")
        logger.info(df_agg.head())
        df_agg["total_cost"] = df_agg["price"] * df_agg["quantity"]
        return df_agg


if __name__ == "__main__":
    # to run this test, do the following:
    # poetry run python -m desafio_fake_etl.transform.aggregate
    from ..extract.extract_data import ExtractData

    folder = "Data"
    edata = ExtractData(folder)
    aggdata = Aggregate()
    df_agg = aggdata.aggregate(edata.extract_data())
    print(df_agg.head())

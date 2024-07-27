from typing import List

import pandas as pd

from utils.utils_log import log_decorator


class Aggregate:

    def __init__(self) -> None:
        pass

    @log_decorator
    def aggregate(self, df_list: List[pd.DataFrame]) -> pd.DataFrame:
        df_agg: pd.DataFrame = pd.DataFrame
        df_agg = pd.concat(df_list)
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

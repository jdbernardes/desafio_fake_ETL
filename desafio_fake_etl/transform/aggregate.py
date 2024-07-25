from typing import List

import pandas as pd


class Aggregate:

    def __init__(self) -> None:
        pass

    def aggregate(self, df_list: List[pd.DataFrame]) -> pd.DataFrame:
        df_agg: pd.DataFrame = pd.DataFrame
        df_agg = pd.concat(df_list)
        df_agg["total_cost"] = df_agg["price"] * df_agg["quantity"]
        return df_agg


if __name__ == "__main__":
    from desafio_fake_etl.extract.extract_data import ExtractData

    folder = "Data"
    edata = ExtractData(folder)
    aggdata = Aggregate()
    df_agg = aggdata.aggregate(edata.extract_data())
    print(df_agg.head())

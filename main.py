from desafio_fake_etl.extract.extract_data import ExtractData
from desafio_fake_etl.load.load_data import LoadData
from desafio_fake_etl.transform.aggregate import Aggregate

folder = "Data"
extensions = ["csv", "parquet"]
# extensions = ["parquet"]
# extensions = ["csv"]
edata = ExtractData(folder)
aggdata = Aggregate()
ldata = LoadData()
df = aggdata.aggregate(edata.extract_data())
ldata.load_data(extensions, df)
print(df.head())

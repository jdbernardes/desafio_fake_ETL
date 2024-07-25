from desafio_fake_etl.extract.extract_data import ExtractData
from desafio_fake_etl.transform.aggregate import Aggregate

folder = "Data"
edata = ExtractData(folder)
aggdata = Aggregate()
df = aggdata.aggregate(edata.extract_data())
print(df.head())

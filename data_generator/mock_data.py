import json
import random
from datetime import date, datetime, timedelta
from typing import List


class MockData:

    def __init__(self) -> None:
        pass

    def create_data(
        self,
        num_records: int,
        products: List[str],
        category: List[str],
        values: List[float],
    ) -> List[dict]:
        selling: dict = {}
        sellings: List[dict] = []
        selling_date: date = date.today()
        selling_date = selling_date + timedelta(random.randint(-2, 2))
        selling_date = datetime.strftime(selling_date, "%Y-%m-%d")
        for _ in range(num_records):
            product = random.sample(products, 1)[0]
            prod_index = products.index(product)
            selling["product"] = product
            selling["category"] = category[prod_index]
            selling["price"] = values[prod_index]
            selling["quantity"] = random.randint(1, 10)
            selling["date"] = selling_date
            sellings.append(selling)
            selling = {}
        return sellings

    def generate_json(
        self,
        num_days: int,
        num_records: int,
        products: List[str],
        category: List[str],
        values: List[float],
    ) -> None:
        for i in range(num_days):
            data = self.create_data(num_records, products, category, values)
            with open(f"./Data/data{i}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    mdata = MockData()
    produtos = [
        "PC Gamer",
        "Mouse",
        "Teclado",
        "Notebook",
        "Batedeira",
        "Cama de Casal",
    ]
    categoria = [
        "Eletrônicos",
        "Acessórios",
        "Acessórios",
        "Eletrônicos",
        "Eletrodomésticos",
        "Cama Mesa e Banho",
    ]
    valor = [6000.00, 50.00, 100.00, 7500.00, 499.90, 2000.00]

    # itens = mdata.create_data(10, produtos, categoria, valor)
    # print(itens)

    mdata.generate_json(3, 10, produtos, categoria, valor)

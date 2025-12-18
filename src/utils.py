import json
from typing import List

from src.models import Category, Product


def load_categories_from_json(file_path: str) -> List[Category]:
    """
    Читает JSON-файл и создает список объектов Category и Product.

    :param file_path: путь к файлу JSON
    :return: список объектов Category
    """
    categories = []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for cat_data in data:
        products_list = []
        for prod_data in cat_data["products"]:
            product = Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=prod_data["price"],
                quantity=prod_data["quantity"],
            )
            products_list.append(product)

        category = Category(
            name=cat_data["name"],
            description=cat_data["description"],
            products=products_list,
        )
        categories.append(category)

    return categories


def format_price(price: float) -> str:
    """
    Форматирует цену с разделением тысяч и добавлением валюты.

    :param price: число (float или int)
    :return: строка вида "1,234.56 ₽"
    """
    return f"{price:,.2f} ₽"

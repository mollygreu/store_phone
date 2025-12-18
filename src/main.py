import json
from typing import List

from src.models import Category, Product


def create_manual_categories() -> List[Category]:
    """Создание категорий и продуктов вручную"""
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [product4],
    )

    return [category1, category2]


def load_categories_from_json(file_path: str) -> List[Category]:
    """Загрузка категорий и продуктов из JSON"""
    categories = []
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for cat_data in data:
        products_list = [Product(**prod) for prod in cat_data["products"]]
        category = Category(cat_data["name"], cat_data["description"], products_list)
        categories.append(category)

    return categories


if __name__ == "__main__":
    manual_categories = create_manual_categories()
    for cat in manual_categories:
        print(f"Категория: {cat.name}, Кол-во продуктов: {len(cat.products)}")

    json_categories = load_categories_from_json("data/data.json")
    for cat in json_categories:
        print(f"JSON Категория: {cat.name}, Кол-во продуктов: {len(cat.products)}")

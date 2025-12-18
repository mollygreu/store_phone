import json

from src.models import Category, Product
from src.utils import format_price, load_categories_from_json


def test_load_categories_from_json(tmp_path):
    # Создаем временный JSON файл
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание категории",
            "products": [
                {
                    "name": "Phone1",
                    "description": "Desc1",
                    "price": 1000.0,
                    "quantity": 2,
                },
                {
                    "name": "Phone2",
                    "description": "Desc2",
                    "price": 2000.0,
                    "quantity": 3,
                },
            ],
        }
    ]

    file_path = tmp_path / "data.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    # Сброс счетчиков перед тестом
    Category.category_count = 0
    Category.product_count = 0

    categories = load_categories_from_json(str(file_path))
    assert len(categories) == 1
    cat = categories[0]
    assert isinstance(cat, Category)
    assert cat.name == "Смартфоны"
    assert len(cat.products) == 2
    for product in cat.products:
        assert isinstance(product, Product)

    # Проверка счетчиков
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_format_price():
    assert format_price(1000) == "1,000.00 ₽"
    assert format_price(1234567.89) == "1,234,567.89 ₽"
    assert format_price(0) == "0.00 ₽"
    assert format_price(99.9) == "99.90 ₽"

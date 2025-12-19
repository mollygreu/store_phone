import json

from main import create_manual_categories, load_categories_from_json
from src.models import Category


def test_create_manual_categories():
    Category.category_count = 0
    Category.product_count = 0

    categories = create_manual_categories()
    assert len(categories) == 2

    cat1 = categories[0]
    cat2 = categories[1]

    assert cat1.name == "Смартфоны"
    assert len(cat1.products) == 3
    assert cat2.name == "Телевизоры"
    assert len(cat2.products) == 1

    # Проверка счетчиков
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_load_categories_from_json(tmp_path):
    # создаем временный JSON файл
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

    file = tmp_path / "data.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f)

    Category.category_count = 0
    Category.product_count = 0

    categories = load_categories_from_json(str(file))
    assert len(categories) == 1
    cat = categories[0]
    assert cat.name == "Смартфоны"
    assert len(cat.products) == 2

    # Проверка счетчиков
    assert Category.category_count == 1
    assert Category.product_count == 2

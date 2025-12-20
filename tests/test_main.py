from src.models import Product, Category


def test_product_creation():
    product = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет",
        180000.0,
        5
    )

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_creation():
    product = Product("Iphone 15", "512GB", 210000.0, 8)
    category = Category(
        "Смартфоны",
        "Описание",
        [product]
    )

    assert category.name == "Смартфоны"
    assert len(category.products) == 1

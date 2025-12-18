import pytest

from src.models import Category, Product


@pytest.fixture
def sample_products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
    ]


@pytest.fixture
def sample_category(sample_products):
    Category.category_count = 0
    Category.product_count = 0
    return Category("Смартфоны", "Описание категории", sample_products)


def test_product_initialization():
    p = Product("Xiaomi", "Описание", 30000.0, 10)
    assert p.name == "Xiaomi"
    assert p.description == "Описание"
    assert p.price == 30000.0
    assert p.quantity == 10


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Описание категории"
    assert sample_category.products == sample_products
    assert len(sample_category.products) == 2


def test_category_counters(sample_category):
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_multiple_categories(sample_products):
    Category.category_count = 0
    Category.product_count = 0

    Category("Смартфоны", "Описание", sample_products)
    Category("Телевизоры", "Описание", [Product("TV", "Описание", 120000.0, 3)])

    assert Category.category_count == 2
    assert Category.product_count == 3

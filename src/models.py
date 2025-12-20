from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Класс для описания продукта"""
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity


class Category:
    # Атрибуты класса для подсчета всех категорий и всех товаров
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """Класс для описания категорий товара"""
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products

        # Автоматически увеличиваем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)

import pytest
from src.product import Product
from src.category import Category


# Фикстура для сброса счетчиков перед каждым тестом
def setup_function():
    Category.category_count = 0
    Category.product_count = 0


def test_category_initialization():
    """Тест корректной инициализации категории с продуктами."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)

    category = Category("Смартфоны", "Описание категории", [product1, product2])

    assert Category.category_count == 1  # Создана одна категория
    assert Category.product_count == 8  # Всего 8 единиц товаров (5 + 3)
    assert len(category.products) == 2  # Проверяем, что в категории два продукта
    assert product1 in category.products
    assert product2 in category.products


def test_add_product_to_category():
    """Тест добавления продукта в категорию."""
    category = Category("Смартфоны", "Описание категории")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products) == 2  # Два продукта добавлено
    assert Category.product_count == 8  # Общий счётчик продуктов (5 + 3)
    assert category.products[0].name == "Samsung Galaxy S23 Ultra"  # Правильный доступ к продуктам


def test_add_duplicate_product():
    """Тест добавления дубликата продукта."""
    category = Category("Смартфоны", "Описание категории")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    category.add_product(product1)

    duplicate_product = Product("Samsung Galaxy S23 Ultra", "Обновленное описание", 185000.0, 3)
    category.add_product(duplicate_product)

    assert len(category.products) == 1  # Дубликат не добавляется как новый продукт
    assert category.products[0].quantity == 8  # Количество обновлено: 5 + 3
    assert category.products[0].price == 185000.0  # Цена обновлена


def test_add_invalid_product():
    """Тест добавления объекта, не являющегося продуктом."""
    category = Category("Смартфоны", "Описание категории")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")  # Ожидаем ошибку


def test_multiple_categories():
    """Тест создания нескольких категорий."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)

    category1 = Category("Смартфоны", "Описание категории", [product1])
    category2 = Category("Аксессуары", "Описание категории", [product2])

    assert Category.category_count == 2  # Две категории
    assert Category.product_count == 8  # Всего товаров: 5 + 3


def test_product_addition():
    """Тест сложения продуктов одного типа."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 100, 10)
    product2 = Product("Iphone 15", "512GB, Gray space", 200, 2)

    total_cost = product1 + product2
    assert total_cost == 1400  # 100 × 10 + 200 × 2


def test_category_str():
    """Тест строкового представления категории."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 100, 10)
    product2 = Product("Iphone 15", "512GB, Gray space", 200, 2)

    category = Category("Смартфоны", "Описание категории", [product1, product2])
    expected_str = "Смартфоны, количество продуктов: 12 шт."
    assert str(category) == expected_str


def test_new_product_creation():
    """Тест метода new_product для создания продукта."""
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }

    product = Product.new_product(product_data)
    assert product is not None
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_new_product_missing_key():
    """Тест метода new_product с отсутствующими ключами."""
    incomplete_data = {
        "name": "Incomplete Product",
        "price": 50000.0
    }

    product = Product.new_product(incomplete_data)
    assert product is None


def test_category_products_getter():
    """Тест геттера для списка продуктов."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    category = Category("Смартфоны", "Описание категории", [product1])

    assert category.products == [product1]


def test_invalid_addition():
    """Тест сложения продукта с объектом другого типа."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 100, 10)

    with pytest.raises(TypeError):
        _ = product + "Not a product"

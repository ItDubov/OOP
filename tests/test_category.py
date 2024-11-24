from src.product import Product
from src.category import Category


# Фикстура для сброса счетчиков перед каждым тестом
def setup_function():
    Category.category_count = 0
    Category.product_count = 0


def test_category_initialization():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)

    category = Category("Смартфоны", "Описание категории", [product1, product2])

    assert Category.category_count == 1  # Создана одна категория
    assert Category.product_count == 8  # Всего 8 единиц товаров (5 + 3)
    assert len(category.products) == 2  # Проверяем, что в категории два продукта
    assert str(product1) in [str(p) for p in category.products]
    assert str(product2) in [str(p) for p in category.products]


def test_add_product_to_category():
    category = Category("Смартфоны", "Описание категории")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products) == 2  # Два продукта добавлено
    assert Category.product_count == 8  # Общий счётчик продуктов (5 + 3)
    assert category.products[0].name == "Samsung Galaxy S23 Ultra"  # Правильный доступ к продуктам


def test_add_duplicate_product():
    category = Category("Смартфоны", "Описание категории")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    category.add_product(product1)

    duplicate_product = Product("Samsung Galaxy S23 Ultra", "Обновленное описание", 185000.0, 3)
    category.add_product(duplicate_product)

    assert len(category.products) == 1  # Дубликат не добавляется как новый продукт
    assert category.products[0].quantity == 8  # Количество обновлено: 5 + 3
    assert category.products[0].price == 185000.0  # Цена обновлена


def test_multiple_categories():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)

    category1 = Category("Смартфоны", "Описание категории", [product1])
    category2 = Category("Аксессуары", "Описание категории", [product2])

    assert Category.category_count == 2  # Две категории
    assert Category.product_count == 8  # Всего товаров: 5 + 3


def test_product_addition():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 100, 10)
    product2 = Product("Iphone 15", "512GB, Gray space", 200, 2)

    total_cost = product1 + product2
    assert total_cost == 1400  # 100 × 10 + 200 × 2


def test_invalid_price():
    try:
        product = Product("Invalid Product", "Invalid description", -100, 1)
        assert False, "Не должно быть создано с отрицательной ценой"
    except ValueError as e:
        assert str(e) == "Цена должна быть положительным числом."


def test_category_str():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 100, 10)
    product2 = Product("Iphone 15", "512GB, Gray space", 200, 2)

    category = Category("Смартфоны", "Описание категории", [product1, product2])
    expected_str = "Смартфоны, количество продуктов: 12 шт."
    assert str(category) == expected_str

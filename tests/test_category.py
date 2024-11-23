from src.product import Product
from src.category import Category


# Фикстура для сброса счетчиков перед каждым тестом
def setup_function():
    Category.category_count = 0
    Category.product_count = 0


def test_category_initialization():
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет",
                       180000.0,
                       5)
    product2 = Product("Iphone 15",
                       "512GB, Gray space",
                       210000.0,
                       3)

    category = Category("Смартфоны",
                        "Описание категории",
                        [product1, product2])

    assert Category.category_count == 1  # Создана одна категория
    assert Category.product_count == 2  # Два продукта в категории
    assert len(category.get_products()) == 2  # Проверяем, что в категории два продукта
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in category.products
    assert "Iphone 15, 210000.0 руб. Остаток: 3 шт." in category.products


def test_add_product_to_category():
    category = Category("Смартфоны", "Описание категории")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category.get_products()) == 2  # Два продукта добавлено
    assert Category.product_count == 2  # Общий счётчик продуктов
    assert category.get_products()[0].name == "Samsung Galaxy S23 Ultra"


def test_add_duplicate_product():
    category = Category("Смартфоны", "Описание категории")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    category.add_product(product1)

    duplicate_product = Product("Samsung Galaxy S23 Ultra",
                                "Обновленное описание",
                                185000.0,
                                3)
    category.add_product(duplicate_product)

    assert len(category.get_products()) == 1  # Дубликат не добавляется как новый продукт
    assert category.get_products()[0].quantity == 8  # Количество обновлено: 5 + 3
    assert category.get_products()[0].price == 185000.0  # Цена обновлена


def test_multiple_categories():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)

    category1 = Category("Смартфоны", "Описание категории", [product1])
    category2 = Category("Аксессуары", "Описание категории", [product2])

    assert Category.category_count == 2  # Две категории
    assert Category.product_count == 2  # Два продукта, по одному в каждой категории

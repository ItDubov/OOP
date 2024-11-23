import pytest
from src.product import Product


@pytest.fixture
def product():
    """Фикстура для создания объекта Product."""
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


def test_initialization(product):
    """Тест корректной инициализации объекта Product."""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_getter(product):
    """Тест геттера для приватного атрибута price."""
    assert product.price == 180000.0


def test_price_setter_positive_value(product):
    """Тест сеттера для корректного обновления цены."""
    product.price = 190000.0
    assert product.price == 190000.0


def test_price_setter_negative_value(product, capsys):
    """Тест на попытку установить отрицательную цену."""
    product.price = -5000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 180000.0  # Цена не должна была измениться


def test_price_reduction_with_confirmation(monkeypatch, product, capsys):
    """Тест на успешное снижение цены с подтверждением."""
    monkeypatch.setattr('builtins.input', lambda _: "да")  # Автоматически подтверждаем
    product.price = 170000.0
    assert product.price == 170000.0


def test_price_reduction_without_confirmation(monkeypatch, product, capsys):
    """Тест на отмену снижения цены при отсутствии подтверждения."""
    monkeypatch.setattr('builtins.input', lambda _: "нет")  # Автоматически отклоняем
    product.price = 170000.0
    captured = capsys.readouterr()
    assert "Понижение цены отменено" in captured.out
    assert product.price == 180000.0  # Цена не должна была измениться


def test_price_setter_zero_value(product, capsys):
    """Тест на попытку установить нулевую цену."""
    product.price = 0.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 180000.0  # Цена не должна была измениться


def test_price_setter_higher_value(product):
    """Тест на повышение цены без дополнительных проверок."""
    product.price = 200000.0
    assert product.price == 200000.0


def test_new_product():
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 10
    }
    product = Product.new_product(product_data)
    assert product is not None
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_new_product_missing_key():
    incomplete_data = {
        "name": "Incomplete Product",
        "price": 50.0
    }
    product = Product.new_product(incomplete_data)
    assert product is None

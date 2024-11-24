import pytest
from src.product import Product, Smartphone, LawnGrass


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


def test_price_setter_negative_value(product):
    """Тест на попытку установить отрицательную цену."""
    with pytest.raises(ValueError) as exc_info:
        product.price = -5000.0
    assert "Цена должна быть положительным числом" in str(exc_info.value)
    assert product.price == 180000.0  # Цена не должна была измениться


def test_price_reduction_with_confirmation(monkeypatch, product):
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


def test_price_setter_zero_value(product):
    """Тест на попытку установить нулевую цену."""
    with pytest.raises(ValueError) as exc_info:
        product.price = 0.0
    assert "Цена должна быть положительным числом" in str(exc_info.value)
    assert product.price == 180000.0  # Цена не должна была измениться


def test_price_setter_higher_value(product):
    """Тест на повышение цены без дополнительных проверок."""
    product.price = 200000.0
    assert product.price == 200000.0


def test_new_product():
    """Тест на создание нового продукта с помощью new_product."""
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 10
    }
    product_d = Product.new_product(product_data)
    assert product_d is not None
    assert product_d.name == "Test Product"
    assert product_d.description == "Test Description"
    assert product_d.price == 100.0
    assert product_d.quantity == 10


def test_new_product_missing_key():
    """Тест на создание нового продукта с недостающим ключом."""
    incomplete_data = {
        "name": "Incomplete Product",
        "price": 50.0
    }
    product_incom = Product.new_product(incomplete_data)
    assert product_incom is None


def test_product_add_operator():
    """Тест оператора сложения для расчета полной стоимости продуктов на складе."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 100.0, 10)
    product2 = Product("Iphone 15", "512GB, Gray space", 200.0, 2)

    # Ожидаем, что сложение двух продуктов даст полную стоимость: (100 * 10) + (200 * 2)
    total_cost = product1 + product2
    expected_cost = (100.0 * 10) + (200.0 * 2)  # 1000 + 400 = 1400
    assert total_cost == expected_cost

    # Проверка на ошибку при сложении с объектом другого типа
    with pytest.raises(TypeError):
        product1 + "Not a product"  # Ожидаем исключение TypeError


def test_product_add_different_types():
    """Тест на сложение продуктов разных типов."""
    smartphone = Smartphone(
        name="Smartphone A",
        description="256GB, Black",
        price=150000.0,
        quantity=5,
        efficiency="Snapdragon 8 Gen 2",
        model="Galaxy A",
        memory=256,
        color="Black"
    )

    lawn_grass = LawnGrass(
        name="Газонная трава 'Ландшафт'",
        description="Высокая устойчивость",
        price=1200.0,
        quantity=20,
        country="Нидерланды",
        germination_period=14,
        color="Зеленый"
    )

    with pytest.raises(TypeError):
        _ = smartphone + lawn_grass


def test_string_representation(product):
    """Тест строкового представления продукта."""
    assert str(product) == "Samsung Galaxy S23 Ultra, Цена: 180000.0 руб, Количество: 5 шт."

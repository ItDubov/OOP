from src.product import Product, Smartphone, LawnGrass
from src.category import Category

if __name__ == "__main__":
    # Создание списка продуктов
    products = [
        Smartphone(
            name="Samsung Galaxy S23 Ultra",
            description="256GB, Серый цвет, 200MP камера",
            price=180000.0,
            quantity=5,
            efficiency="Snapdragon 8 Gen 2",
            model="Galaxy S23 Ultra",
            memory=256,
            color="Серый"
        ),
        Smartphone(
            name="Iphone 15",
            description="512GB, Gray space",
            price=210000.0,
            quantity=8,
            efficiency="A17 Bionic",
            model="Pro Max",
            memory=512,
            color="Серый космос"
        ),
        LawnGrass(
            name="Газонная трава 'Ландшафт'",
            description="Устойчивая к вытаптыванию газонная трава",
            price=1200.0,
            quantity=20,
            country="Нидерланды",
            germination_period=14,
            color="Зеленый"
        )
    ]

    # Демонстрация геттеров и сеттеров
    print("Текущая цена первого продукта:")
    print(products[0].price)

    print("\nПопытка установить отрицательную цену:")
    try:
        products[0].price = -5000  # Должно вывести сообщение об ошибке
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПопытка установить более высокую цену:")
    try:
        products[0].price = 190000  # Цена обновится
        print(f"Новая цена: {products[0].price}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПопытка снизить цену с подтверждением:")
    try:
        products[0].price = 170000  # Потребуется подтверждение через input
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Создание категории с продуктами
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни",
        [p for p in products if isinstance(p, Smartphone)]
    )

    print("\nСписок продуктов в категории:")
    print(category.products)

    # Добавление нового продукта с тем же именем
    category.add_product(
        Smartphone(
            name="Samsung Galaxy S23 Ultra",
            description="Обновленное описание",
            price=185000.0,
            quantity=3,
            efficiency="Snapdragon 8 Gen 2",
            model="Galaxy S23 Ultra",
            memory=256,
            color="Черный"
        )
    )

    print("\nПосле добавления нового продукта с тем же именем:")
    print(category.products)

    # Вывод строки категории
    print("\nОписание категории:")
    print(category)

    # Тестирование класса-метода new_product
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }

    print("\nТестирование класса-метода new_product:")
    new_product = Product.new_product(product_data)

    if new_product:
        print(f"Создан продукт: {new_product}")
    else:
        print("Не удалось создать продукт.")

    # Сложение стоимости продуктов одного типа
    print("\nСложение стоимости товаров одного типа (смартфоны):")
    try:
        total_cost = products[0] + products[1]
        print(f"Общая стоимость товаров: {total_cost} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Попытка сложить товары разных типов
    print("\nПопытка сложить товары разных типов:")
    try:
        total_cost = products[0] + products[2]
    except TypeError as e:
        print(f"Ошибка: {e}")

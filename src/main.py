from src.product import Product
from src.category import Category

if __name__ == "__main__":
    # Создание списка продуктов
    products = [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
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
        products
    )

    print("\nСписок продуктов в категории:")
    print(category.products)

    # Добавление нового продукта с тем же именем
    category.add_product(Product("Samsung Galaxy S23 Ultra", "Обновленное описание", 185000.0, 3))

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

    # Сложение стоимости продуктов
    print("\nСложение стоимости товаров:")
    try:
        total_cost = products[0] + products[1]
        print(f"Общая стоимость товаров: {total_cost} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

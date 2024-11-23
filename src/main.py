from src.product import Product
from src.category import Category

if __name__ == "__main__":
    # Создание объектов Product
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера",
                       180000.0,
                       5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Демонстрация геттеров и сеттеров
    print("Текущая цена продукта:")
    print(product1.price)  # Вывод текущей цены

    print("\nПопытка установить отрицательную цену:")
    product1.price = -5000  # Должно вывести сообщение об ошибке

    print("\nПопытка установить более высокую цену:")
    product1.price = 190000  # Цена обновится

    print("\nПопытка снизить цену с подтверждением:")
    product1.price = 170000  # Потребуется подтверждение через input

    # Создание объекта Category с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("\nСписок продуктов в категории 'Смартфоны':")
    print(category1.products)

    # Создание и добавление нового продукта с тем же именем
    new_product = Product("Samsung Galaxy S23 Ultra",
                          "Обновленное описание",
                          185000.0,
                          3)
    category1.add_product(new_product)

    print("\nПосле добавления нового продукта с тем же именем:")
    print(category1.products)

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
        print(f"Создан продукт: {new_product.name}, "
              f"цена: {new_product.price}, "
              f"количество: {new_product.quantity}")
    else:
        print("Не удалось создать продукт.")

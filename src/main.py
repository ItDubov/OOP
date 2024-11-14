

class Category:
    # Атрибуты класса для подсчета общего количества категорий и товаров
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчик категорий при создании новой категории
        Category.category_count += 1

        # Увеличиваем счетчик товаров,
        # прибавляя количество товаров в данной категории
        Category.product_count += len(products)


# Пример использования
if __name__ == "__main__":
    # Создание объектов Product
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Проверка свойств Product
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Создание объекта Category с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Проверка свойств Category
    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))  # Количество товаров в категории
    print(Category.category_count)  # Общее количество категорий
    print(Category.product_count)  # Общее количество товаров

    # Создание еще одного объекта Product и Category
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, "
        "который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [product4]
    )

    # Проверка свойств второй категории
    print(category2.name)
    print(category2.description)
    print(len(category2.products))  # Количество товаров в категории
    print(category2.products)

    # Проверка общих счетчиков категорий и товаров
    print(Category.category_count)  # Общее количество категорий
    print(Category.product_count)  # Общее количество товаров

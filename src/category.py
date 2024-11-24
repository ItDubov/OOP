from src.product import Product


class Category:
    # Атрибуты класса для подсчета общего количества категорий и товаров
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Считаем количество всех товаров в новой категории
        Category.product_count += sum(product.quantity for product in self.__products)

    def add_product(self, new_product):
        """Добавление продукта в категорию. Проверка типа для избежания ошибок."""
        if not isinstance(new_product, Product):  # Проверяем, что объект нового продукта - это именно Product
            raise TypeError(f"Ожидается объект типа Product, получен {type(new_product).__name__}")

        # Добавление или обновление продукта в категории
        for existing_product in self.__products:
            if existing_product.name == new_product.name:
                # Обновляем количество и цену, если продукт уже есть в категории
                existing_product.quantity += new_product.quantity
                if new_product.price > existing_product.price:
                    existing_product.price = new_product.price
                Category.product_count += new_product.quantity  # Обновляем общий счетчик
                return

        # Если продукт новый, добавляем его в категорию
        self.__products.append(new_product)
        Category.product_count += new_product.quantity  # Обновляем общий счетчик продуктов

    @property
    def products(self):
        return self.__products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

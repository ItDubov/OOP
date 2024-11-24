from src.product import Product


class Category:
    # Атрибуты класса для подсчета общего количества категорий и товаров
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        # Считаем количество всех товаров в новой категории
        Category.product_count += sum(product.quantity for product in self.__products)

    def add_product(self, new_product: Product):
        for existing_product in self.__products:
            if existing_product.name == new_product.name:
                existing_product.quantity += new_product.quantity
                # Обновляем цену только если она выше
                if new_product.price > existing_product.price:
                    existing_product.price = new_product.price
                return

        # Добавляем новый продукт
        self.__products.append(new_product)
        Category.product_count += new_product.quantity  # Учитываем только новые товары

    @property
    def products(self):
        return self.__products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

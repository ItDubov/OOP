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
        Category.product_count += len(self.__products)

    def add_product(self, new_product: Product):
        for existing_product in self.__products:
            if existing_product.name == new_product.name:
                existing_product.quantity += new_product.quantity
                if new_product.price > existing_product.price:
                    existing_product.price = new_product.price
                return

        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):  # Переименованный геттер
        return '\n'.join(
            f"{product.name}, "
            f"{product.price} руб. "
            f"Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def get_products(self):
        return self.__products

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:  # Логика для понижения цены
            confirmation = input("Вы уверены, что хотите понизить цену? (Да/Нет): ")
            if confirmation.lower() != 'Да':  # Проверка на подтверждение
                print("Понижение цены отменено")
                return

        # Устанавливаем новую цену
        self.__price = new_price


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
    def product_list(self):
        return '\n'.join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def get_products(self):
        return self.__products


# Пример использования
if __name__ == "__main__":
    # Создание объектов Product
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Демонстрация геттеров и сеттеров
    print(product1.price)  # Вывод текущей цены

    # Попытка установить отрицательную цену
    product1.price = -5000  # Должно вывести сообщение об ошибке

    # Попытка установить более высокую цену
    product1.price = 190000  # Цена обновится

    # Попытка снизить цену с подтверждением
    product1.price = 170000  # Потребуется подтверждение через input

    # Создание объекта Category с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.product_list)

    # Создание и добавление нового продукта с тем же именем
    new_product = Product("Samsung Galaxy S23 Ultra", "Обновленное описание", 185000.0, 3)
    category1.add_product(new_product)

    print("\nПосле добавления нового продукта с тем же именем:")
    print(category1.product_list)

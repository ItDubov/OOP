class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price  # Используем сеттер для валидации цены
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена должна быть положительным числом.")  # Для тестов с capsys
            raise ValueError("Цена должна быть положительным числом.")
        if hasattr(self, '_Product__price') and new_price < self.__price:  # Проверяем снижение цены
            confirmation = input("Вы уверены, что хотите понизить цену? (Да/Нет): ")
            if confirmation.lower() != 'да':
                print("Понижение цены отменено")  # Для тестов с capsys
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Создает новый объект Product на основе словаря с данными о продукте.
        """
        try:
            name = product_data['name']
            description = product_data['description']
            price = product_data['price']
            quantity = product_data['quantity']
            return cls(name, description, price, quantity)
        except KeyError as e:
            print(f"Ошибка: отсутствует обязательный ключ {e}")
            return None

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Складывает два объекта Product для расчета полной стоимости товаров на складе.
        """
        if not isinstance(other, Product):
            raise TypeError("Сложение возможно только между объектами класса Product.")
        total_cost = (self.price * self.quantity) + (other.price * other.quantity)
        return total_cost

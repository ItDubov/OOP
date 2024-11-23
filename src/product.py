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
            confirmation = input("Вы уверены, "
                                 "что хотите понизить цену? (Да/Нет): ")
            if confirmation.lower() != 'да':  # Проверка на подтверждение
                print("Понижение цены отменено")
                return

        # Устанавливаем новую цену
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Создает новый объект Product на основе словаря с данными о продукте.

        Args:
            product_data (dict):
            Словарь с ключами 'name', 'description', 'price', 'quantity'.

        Returns:
            Product: Новый экземпляр класса Product.
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

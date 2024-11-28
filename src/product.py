from abc import ABC, abstractmethod


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами {args} {kwargs}")


class BaseProduct(ABC, LoggingMixin):
    """
    Базовый абстрактный класс для всех продуктов.
    Определяет общие свойства и методы, которые должны быть у всех продуктов.
    """
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.price = price  # Валидация цены будет в дочернем классе
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """Сеттер для цены."""
        pass

    @abstractmethod
    def __str__(self):
        """Метод для строкового представления продукта."""
        pass

    @abstractmethod
    def __repr__(self):
        """Метод для программного представления продукта."""
        pass


class Product(BaseProduct):
    """
    Класс для базового продукта. Наследуется от BaseProduct и включает LoggingMixin.
    """
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.__price = price  # Используем сеттер для валидации

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
        return f"{self.name}, Цена: {self.price} руб, Количество: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __add__(self, other):
        """
        Складывает два объекта Product, если они принадлежат к одному классу.
        """
        if not isinstance(other, Product):
            raise TypeError("Сложение возможно только между объектами класса Product.")
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных категорий.")
        total_cost = (self.price * self.quantity) + (other.price * other.quantity)
        return total_cost


class Smartphone(Product):
    """
    Класс для смартфонов. Наследуется от Product.
    """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"Смартфон: {self.name}, модель: {self.model}, цвет: {self.color}, "
                f"память: {self.memory} GB, производительность: {self.efficiency}, "
                f"цена: {self.price} руб., остаток: {self.quantity} шт.")

    def __repr__(self):
        return (f"Smartphone(name={self.name}, model={self.model}, color={self.color}, "
                f"memory={self.memory}, price={self.price}, quantity={self.quantity})")


class LawnGrass(Product):
    """
    Класс для газонной травы. Наследуется от Product.
    """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"Трава газонная: {self.name}, цвет: {self.color}, страна-производитель: {self.country}, "
                f"срок прорастания: {self.germination_period} дней, "
                f"цена: {self.price} руб., остаток: {self.quantity} шт.")

    def __repr__(self):
        return (f"LawnGrass(name={self.name}, country={self.country}, color={self.color}, "
                f"germination_period={self.germination_period}, price={self.price}, quantity={self.quantity})")

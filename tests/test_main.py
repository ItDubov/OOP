import unittest
from src.main import Product, Category


class TestProductAndCategory(unittest.TestCase):

    # Тест для проверки инициализации объектов Product
    def test_product_initialization(self):
        product = Product("Samsung Galaxy S23 Ultra",
                          "256GB, Серый цвет, 200MP камера",
                          180000.0, 5)
        self.assertEqual(product.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(product.description,
                         "256GB, Серый цвет, 200MP камера")
        self.assertEqual(product.price, 180000.0)
        self.assertEqual(product.quantity, 5)

    # Тест для проверки инициализации объектов Category
    def test_category_initialization(self):
        product1 = Product("Samsung Galaxy S23 Ultra",
                           "256GB, Серый цвет, 200MP камера",
                           180000.0,
                           5)
        product2 = Product("Iphone 15",
                           "512GB, Gray space",
                           210000.0,
                           8)
        product3 = Product("Xiaomi Redmi Note 11",
                           "1024GB, Синий",
                           31000.0,
                           14)

        category = Category("Смартфоны",
                            "Смартфоны для повседневного использования",
                            [product1, product2, product3])
        self.assertEqual(category.name, "Смартфоны")
        self.assertEqual(category.description,
                         "Смартфоны для повседневного использования")
        self.assertEqual(len(category.products), 3)
        self.assertIn(product1, category.products)
        self.assertIn(product2, category.products)
        self.assertIn(product3, category.products)

    # Тест для проверки подсчета количества категорий
    def test_category_count(self):
        Category.category_count = 0  # Сбрасываем счетчик перед тестом
        Category.product_count = 0  # Сбрасываем счетчик перед тестом

        product1 = Product("Product A",
                           "Description A",
                           100.0,
                           10)
        product2 = Product("Product B",
                           "Description B",
                           200.0,
                           5)
        category1 = Category("Category 1",
                             "Description 1",
                             [product1, product2])

        product3 = Product("Product C",
                           "Description C",
                           300.0,
                           8)
        category2 = Category("Category 2",
                             "Description 2",
                             [product3])

        self.assertEqual(Category.category_count, 2)
        # Проверка количества категорий

    # Тест для проверки подсчета количества продуктов
    def test_product_count(self):
        Category.category_count = 0  # Сбрасываем счетчик перед тестом
        Category.product_count = 0  # Сбрасываем счетчик перед тестом

        product1 = Product("Product A",
                           "Description A",
                           100.0,
                           10)
        product2 = Product("Product B",
                           "Description B",
                           200.0,
                           5)
        category1 = Category("Category 1",
                             "Description 1",
                             [product1, product2])

        product3 = Product("Product C",
                           "Description C",
                           300.0,
                           8)
        category2 = Category("Category 2",
                             "Description 2",
                             [product3])

        self.assertEqual(Category.product_count, 3)
        # Проверка количества продуктов


if __name__ == "__main__":
    unittest.main()

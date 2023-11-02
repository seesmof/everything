"""
- Розроблюваний програмний проєкт має складатися з класу, що описує задачу, сформульовану в індивідуальному завданні, а також має містити окремий модуль, що забезпечує інтерфейсну взаємодію з користувачем.
- Клас вхідних даних задачі має дозволяти:
  - задавати початкові дані;
  - вводити нові параметри;
  - кори гувати та видаляти існуючі;
  - розв’язувати задачу з використанням жадібного алгоритм
- Індивідуальне завдання: Продавець у маленькій крамниці має звичку тримати під рукою найпопулярніші товари для того, щоб пришвидшити роботу з чергою покупців. Кількість таких товарів визначається додатково. Кожен покупець замовляє по черзі товари, а продавець перевіряє, чи є такий товар під рукою. Якщо товару немає, то він дістає його з полиць, що займає більше часу. При цьому для кожного такого товару продавець має вирішити, чи не треба його помістити до найпопулярніших замість якогось з існуючих. Допоможіть продавцю приймати дане рішення протягом просування всієї черги замовлень покупців, якщо він прагне зменшити час, за який вся черга залишить крамницю. Припустіть, що продавець знає наперед про те, які товари бажає купити кожен з покупців у черзі.
- Розробити програмне забезпечення, яке реалізує використання алгоритму Хаффмана для стискання даних текстового файлу у вигляді класу. Клас повинен мати методи, які дозволяють задати файл з даними, виконати стискання даних, визначити параметри виконаного стискання та зворотне перетворення, записати результати кодування/декодування в файл.
"""


class Shopkeeper:
    def __init__(self):
        self.products = []
        self.popular_products = []

    def set_initial_data(self, products, popular_products):
        self.products = products
        self.popular_products = popular_products

    def enter_new_parameters(self, new_products):
        self.products.extend(new_products)

    def edit_existing_parameters(self, index, new_product):
        if index < len(self.products):
            self.products[index] = new_product

    def delete_existing_parameters(self, index):
        if index < len(self.products):
            del self.products[index]

    def solve_problem(self, customer_orders):
        queue_time = 0
        for order in customer_orders:
            if order in self.products:
                queue_time += 1
            else:
                queue_time += 2
                if order in self.popular_products:
                    queue_time -= 1
        return queue_time


# Create an instance of the Shopkeeper class
shopkeeper = Shopkeeper()

# Set the initial data
products = ["apple", "banana", "orange"]
popular_products = ["banana"]
shopkeeper.set_initial_data(products, popular_products)

# Enter new parameters
new_products = ["grape", "mango"]
shopkeeper.enter_new_parameters(new_products)

# Edit existing parameters
index = 1
new_product = "pear"
shopkeeper.edit_existing_parameters(index, new_product)

# Delete existing parameters
index = 2
shopkeeper.delete_existing_parameters(index)

# Solve the problem
customer_orders = ["apple", "banana", "orange", "grape", "mango"]
queue_time = shopkeeper.solve_problem(customer_orders)

# Print the results
print("Products:", shopkeeper.products)
print("Popular Products:", shopkeeper.popular_products)
print("Queue Time:", queue_time)

"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""


class Profile:

    def __init__(self, name, last_name, age, passport):
        self.name = name
        self.last = last_name
        self.age = age
        self.passport = passport

    def print_info(self):
        print(self.name)
        print(self.last)
        print(self.age)
        print(self.passport)


class Address:

    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode


class Role:

    def __init__(self, role, hours_worked):
        self.role = role
        self.hours = hours_worked


class BankAccount:

    def __init__(self, card_number, balance):
        self.card = card_number
        self.balance = balance


class Order:

    def __init__(self, id=None, item=None, date=None, delivery=None, price=None):
        self.id = id
        self.item = item
        self.data = date
        self.delivery = delivery
        self.price = price

    def setOther(self, item, data, delivery, price):
        self.item = item
        self.data = data
        self.delivery = delivery
        self.price = price


class Users:

    def __init__(self, name, last_name, age, passport):
        self.profile_1 = Profile(name, last_name, age, passport)
        self.address = []
        self.role = []
        self.bank = []
        self.order = []

    def add_address(self, city, street, zipcode):
        self.address.append(Address(city, street, zipcode))

    def add_role(self, role, hours_worked):
        self.role.append(Role(role, hours_worked))

    def add_bank(self, card_number, balance):
        self.bank.append(BankAccount(card_number, balance))

    def user_order(self, id, item, data, delivery, price):
        self.order.append(Order(id, item, data, delivery, price))

    def changeorder(self, id, new_item, new_data, new_delivery, new_price):
        for i in self.order:
            if i.id == id:
                i.setOther(new_item, new_data, new_delivery, new_price)


USER_1 = Users("Ignat", "Sur", 25, 1818435835)
USER_1.add_address("Siriys", "Voskres_12", 354222)
USER_1.add_address("Siriys", "Voskres_14", 354222)
USER_1.add_role("Админ", 31232131231)
USER_1.add_role("Школьник", 4)
USER_1.add_bank("2022-2323-5903-2343", 5000)
USER_1.add_bank("2002-2321-3213-3222", 15000)
USER_1.add_bank("3231-2312-3432-9999", 99999)
USER_1.user_order(11, "mouse", "12.05.2002", "Alix", 15000)
USER_1.changeorder(12, "papa", "123456", "rtyjkl", 3456789)
# USER_1.profile_1.print_info()
for k in USER_1.address:
    print(f"У человека под именем - {USER_1.profile_1.name} есть дом в городе {k.city} на улице {k.street}")
for z in USER_1.role:
    print(f"{USER_1.profile_1.name} работает {z.role}ом {z.hours} часов")
for n in USER_1.bank:
    print(f"У {USER_1.profile_1.name} есть банковская карта с номером - {n.card}, баланс этой карты - {n.balance}")
for j in USER_1.order:
    print(f"Курьер из компании {j.delivery} - {j.data}  привез {USER_1.profile_1.name}у {j.item}. Стоимость товара - {j.price} рублей")

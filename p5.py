from abc import ABC, abstractmethod


class Person:
    species = "Homo sapiens"
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__id = id(self)
    def greet(self):
        return f"Hello, my name is {self.name}."
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("Age must be positive!")
    def get_id(self):
        return self.__id
    def __str__(self):
        return f"{self.name} ({self._age} years old)"


class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position
        self.salary = 0
    def set_salary(self, amount):
        self.salary = amount
    def get_salary(self):
        return self.salary
    def work(self):
        return f"{self.name} is working as a {self.position}."
    def greet(self):
        return f"Hi, I'm {self.name}, and I work as a {self.position}."


class Manager(Employee):
    def __init__(self, name, age, employee_id, position, team=None):
        super().__init__(name, age, employee_id, position)
        self.team = team if team else []
    def add_team_member(self, employee):
        self.team.append(employee)
    def manage(self):
        members = ', '.join([member.name for member in self.team])
        return f"{self.name} manages the team: {members}"
    def work(self):
        return f"{self.name} is managing the team efficiently."


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."


class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."


class Utility:
    @staticmethod
    def format_currency(amount):
        return f"${amount:,.2f}"
    @classmethod
    def company_name(cls):
        return "TechNova Inc."

def process_payment(payment_method, amount):
    print(payment_method.pay(amount))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

if __name__ == "__main__":
    p1 = Person("Alice", 25)
    e1 = Employee("Bob", 30, "E102", "Developer")
    m1 = Manager("Carol", 40, "M501", "Team Lead")
    print(p1.greet())
    print(f"{p1.name}'s ID: {p1.get_id()}")
    print(f"Age before update: {p1.get_age()}")
    p1.set_age(26)
    print(f"Age after update: {p1.get_age()}")
    e1.set_salary(70000)
    print(e1.greet())
    print(e1.work())
    print(f"Salary: {Utility.format_currency(e1.get_salary())}")
    m1.add_team_member(e1)
    m1.add_team_member(Employee("Diana", 28, "E205", "Designer"))
    print(m1.manage())
    print(m1.work())
    cc_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    process_payment(cc_payment, 250)
    process_payment(paypal_payment, 500)
    print(f"Company: {Utility.company_name()}")
    print(Utility.format_currency(99999.99))
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v3 = v1 + v2
    print(f"v1: {v1}, v2: {v2}, v3: {v3}")
    print(f"v1 == v2? {v1 == v2}")
    print(f"v3 == Vector(6, 8)? {v3 == Vector(6, 8)}")
    for person in [p1, e1, m1]:
        print(person.greet())

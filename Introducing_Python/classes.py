class Thing():
    pass

example = Thing()
print (Thing)
print(example)

class Thing2():
    def __init__(self,letters):
        self.letters = letters

example2 = Thing2('abcde')
print(example2.letters)

class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input_name):
        self.__name = input_name

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, input_symbol):
        self.__symbol = input_symbol

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, input_number):
        self.__number = input_number

    def __str__(self):
        return f"{self.__name}, {self.__symbol}, {self.__number}"

example3 = Element ("Hydrogen","H",1)
print(example3)
print(example3.name, example3.symbol, example3.number)


class Person():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def __str__(self):
       return f"{super().__str__()}. Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, employees):
        super().__init__(name, salary)
        self.employees = employees

    def __str__(self):
        return f"{super().__str__()}. Employees: {self.employees}"

p1 = Employee("Pepe","100")
p2 = Manager("Lola","200",10)

print(p1)
print(p2)
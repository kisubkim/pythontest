class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

    def update_age(self, age):
        self.age = age
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        

if __name__ == "__main__":
    person = Person("John", 30)
    person.hello()
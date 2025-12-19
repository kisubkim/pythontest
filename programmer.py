from person import Person
class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old. I am a {self.language} programmer')

    def update_language(self, language):
        self.language = language

if __name__ == "__main__":
    programmer = Programmer("John", 30, "Python")
    programmer.hello()
    programmer.update_language("Java")
    programmer.hello()
    programmer.update_age(-1)
    programmer.hello()
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.name}: {self.scores} (Average: {self.average_score():.2f})"


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, scores):
        student = Student(name, scores)
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student)

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def remove_student(self, name):
        student = self.find_student(name)
        if student:
            self.students.remove(student)
            return True
        return False


def main():
    manager = GradeManager()
    while True:
        print("\n1. Add Student")
        print("\n2. Display Students")
        print("\n3. Find Student")
        print("\n4. Remove Student")
        print("\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            scores = list(map(int, input("Enter scores separated by space: ").split()))
            manager.add_student(name, scores)
        elif choice == '2':
            manager.display_students()
        elif choice == '3':
            name = input("Enter student name to find: ")
            student = manager.find_student(name)
            if student:
                print(student)
            else:
                print("Student not found.")
        elif choice == '4':
            name = input("Enter student name to remove: ")
            if manager.remove_student(name):
                print("Student removed.")
            else:
                print("Student not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
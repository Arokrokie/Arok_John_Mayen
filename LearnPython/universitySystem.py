# Super class
class UniversityMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def display_info(self):
        print(f"ID: {self.member_id}")
        print(f"Name: {self.name}")

    def perform_duty(self):
        print(f"{self.name} is performing their university duties.")


# Subclass: Student
class Student(UniversityMember):
    def __init__(self, member_id, name, major, gpa):
        super().__init__(member_id, name)
        self.major = major
        self.gpa = gpa

    # Override display_info
    def display_info(self):
        super().display_info()
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa}")

    # Override perform_duty
    def perform_duty(self):
        print(f"{self.name} is attending classes and studying.")


# Subclass: Lecturer
class Lecturer(UniversityMember):
    def __init__(self, member_id, name, department, courses):
        super().__init__(member_id, name)
        self.department = department
        self.courses = courses

    # Override display_info
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print(f"Courses: {', '.join(self.courses)}")

    # Override perform_duty
    def perform_duty(self):
        print(f"{self.name} is teaching {self.courses[0]}.")


# Subclass: Staff
class Staff(UniversityMember):
    def __init__(self, member_id, name, position):
        super().__init__(member_id, name)
        self.position = position

    # Override display_info
    def display_info(self):
        super().display_info()
        print(f"Position: {self.position}")

    # Override perform_duty
    def perform_duty(self):
        print(f"{self.name} is performing administrative work.")


# Create objects
student = Student("S12345", "Alice Deng", "Computer Science", 3.8)
lecturer = Lecturer("L54321", "Dr. Smith", "Engineering", ["CS101", "CS202"])
staff = Staff("E98765", "Bob Mukaya", "Administrator")

# Test methods
print("=== STUDENT ===")
student.display_info()
student.perform_duty()
print("\n=== LECTURER ===")
lecturer.display_info()
lecturer.perform_duty()
print("\n=== STAFF ===")
staff.display_info()
staff.perform_duty()

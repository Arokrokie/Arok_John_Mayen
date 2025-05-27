# Real world example of method overloading 1
class Calculator:
    def add(self, *args):  # Simulates overloading
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return "Invalid input!"


# Usage
calc = Calculator()
print(calc.add(2, 3))  # Output: 5 (2 numbers)
print(calc.add(2, 3, 4))  # Output: 9 (3 numbers)
print(calc.add(2))  # Output: "Invalid input!"


# Real world example of method overloading 2


class Printer:
    def print_document(self, document):  # Simulates overloading
        if isinstance(document, str):
            print(f"Printing text document:\n{document}")
        elif isinstance(document, dict):
            print("Printing form data:")
            for key, value in document.items():
                print(f"{key}: {value}")
        elif isinstance(document, list):
            print("Printing to-do list:")
            for i, task in enumerate(document, 1):
                print(f"{i}. {task}")
        else:
            print("Error: Unknown document type!")


# Usage
printer = Printer()

# Print different document types
printer.print_document("Hello, world!")  # Text document
printer.print_document({"Name": "John", "Age": 30})  # Form data
printer.print_document(["Buy milk", "Pay bills", "Call mom"])  # To-do list
printer.print_document(123)  # Unsupported type

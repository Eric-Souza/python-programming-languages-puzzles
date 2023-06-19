import math

class Calculator:
    def __init__(self):
        self.ru = input("Enter your RU's last 2 digits: ")

        ru_list = list(self.ru)
      
        if ru_list[-2] == '0':
            ru_list[-2] = '5'
            
        if ru_list[-1] == '0':
            ru_list[-1] = '5'
            
            
        self.num1 = int(ru_list[-2])
        self.num2 = int(ru_list[-1])

    # Displays options menu
    def display_menu(self):
        print("MENU")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Remainder (%)")
        print("7. Square root of the sum (sqrt(num1 + num2))\n")

    # Executes selected option
    def execute_operation(self, option):
        if option == '1':
            result = self.num1 + self.num2
            print(f"Result: {result}\n")

        elif option == '2':
            result = self.num1 - self.num2
            print(f"Result: {result}\n")

        elif option == '3':
            result = self.num1 * self.num2
            print(f"Result: {result}\n")

        elif option == '4':
            result = self.num1 / self.num2
            print(f"Result: {result}\n")

        elif option == '5':
            result = self.num1 ** self.num2
            print(f"Result: {result}\n")

        elif option == '6':
            result = self.num1 % self.num2
            print(f"Result: {result}\n")

        elif option == '7':
            result = math.sqrt(self.num1 + self.num2)
            print(f"Result: {result}\n")

        else:
            print("Invalid option!\n")

    def main(self):
        while True:
            self.display_menu()

            option = input("Enter the desired math operation: ")
            self.execute_operation(option)

calculator = Calculator()
calculator.main()

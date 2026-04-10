"""

Author: Nischal Bhandari 
Program: Simple Calculator

This program performs addition, subtraction, multiplication and division
It uses the if else statement to process user from input. 

"""
#print header
print("Simple Calculator")

while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    #Asking user to choice from the number 1 to 5
    choice = input("Enter choice (1-5): ")

    #if user uses the 5 just end the program
    if choice == '5':
        print("Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        #if user choice 1
        if choice == '1':
            print("Result:", a + b)

        #if user choice 2
        elif choice == '2':
            print("Result:", a - b)

        #if user choice 3
        elif choice == '3':
            print("Result:", a * b)

        
        #if user choice 4
        elif choice == '4':
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Cannot divide by zero")

    else:
        print("Invalid choice, try again.")
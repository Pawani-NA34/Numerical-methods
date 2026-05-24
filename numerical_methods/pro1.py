# DATE: 06/08/2025
# AIM: TO PERFORM THE FOLLOWING TASKS:
print( " To perform:\n 1.Largest of two numbers\n 2.Largest of three numbers\n 3.Factorial of a number\n 4.Sum of ten numbers\n 5.Exit")
while True:
    print()
    choice = input("Enter your choice: ")
    if choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num1 > num2:
            print(f"Largest number is: {num1}")
        else:
            print(f"Largest number is: {num2}")
        
    elif choice == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))
        if num1> num2:
            if num1 > num3:
                largest = num1
            else:
                largest = num3
        else:
            if num2 > num3:
                largest = num2
            else:
                largest = num3
        print(f"Largest number is: {largest}")
    
    elif choice == '3':
        num = int(input("Enter a number to find its factorial: "))
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"Factorial of {num} is: {factorial}")
    elif choice == '4':
        total = 0
        for i in range(10):
            num = int(input(f"Enter number {i + 1}: "))
            total += num
        print(f"Sum of the ten numbers is: {total}")
    else:
        print("Program terminated.")
        break


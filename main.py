def main():
    
    first_number = float(input("Please enter the first number: " " "))
    operation = input("Please enter an operation (*, /, +, -)")
    second_Number = float(input("Please enter another number: " " "))

    if operation == "*":
        print(first_number * second_Number)
    elif operation == "/":
        print(first_number/second_Number)
    elif operation == "+":
        print(first_number+second_Number)
    elif operation == "-":
        print(first_number - second_Number)
    else:
        print(f"{operation} is not valid")
        
    

main()
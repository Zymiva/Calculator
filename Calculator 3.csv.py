# Calculator
# This code takes two numbers and an operator from the user and performs the requested calculation


# Check if value enetered is a letter Q to stop executing code or if entered value is not a number. 
def error_check(a):
    if a == "q" or a == "Q":
        print("Thanks for using this calculator!")
        return True
    elif not a.isnumeric():
        print("PLEASE INPUT NUMBER!")
        return True
    return False


# Check if values entered match the error check and if they do stop, otherwise carry on entering values.
while True:
    num1=(input("Please input number: ")) 
    if error_check(num1):
        break
        
    operator1=input("Please input one of the operators:( + , - , / , * ) ")
    while operator1 not in ["+","-","/","*"]:
        print("Enter valid operator!")
        if error_check(operator1):
            break
            
    num2=(input("Please input number: ")) 
    if error_check(num2):
        break

            
# If code passes all error checks carry on calculating values and print answer on display
    def calculate(number1,symbol,number2):
        '''
            Perform calculation based on the inputted numbers and operator: 

            input1 (int): The first number
            The operatorL (+, -, /, *) 
            input2 (int): The second number
    
            Returns: The result of the calculation
        '''
        if symbol == "+":
            result = number1 + number2
        elif symbol == "-":
            result = number1 - number2
        elif symbol == "/":
            result =  number1 / number2
        elif symbol =="*":
            result = number1 * number2
        return float(result)


    print(f"Answer: {calculate(int(num1),operator1,int(num2))}")

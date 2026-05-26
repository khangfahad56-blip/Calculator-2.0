def menu():
    print("*********************")
    print("Python Calculator 2.O")
    print("*********************")
    print("Sum = + ")
    print("Subtract = - ")
    print("Multiply = * ")
    print("Divide = / ")
    print("Remainder = % ")
    print("Power = P ")
    print("Root = R ")
    print("Clear = C ")
    print("Quit = Q ")

def get_user_num():

    while True:
        try:
            num = input("Write the Number: ")
            if num.lower() == "q"  or num.lower() == "c":
                return num
            else:
                num = float(num)
                return num
        except ValueError:
            print("Error: Only Select Number")
            continue

def get_user_oper():
    user_oper = input("Write the Operation: ")
    return user_oper.lower()

# Use to Check any Invalid value for the Specific Operation

def check_divide(x,y):
    if y == 0:
        return f"{x} can't be Divided by Zero(0)"
    return None

def check_remainder(x,y):
    if y == 0:
        return f"{x} can't be Divided by Zero(0)"
    return None

def check_power(x,y):
    if y < 0 and x == 0:
        return "Zero can't have a Negative Power"
    elif y == 0 and x == 0:
        return "Both Power and Base Can't be Zero"
    return None

def check_root(x,y):
    if y == 0:
        return "Root degree cannot be zero"
    elif x < 0:
        if y % 2 == 0:
            return "Even root of a negative number is not a real number"
    return None

# Find Invalid Operation

def check_operation(user_oper):
    if user_oper not in ["+", "-", "*", "/", "%", "p", "r"]:
        return "You selected an Invalid Operation."
    return None

# Use to Quit and Clear

def check_special(value):
    if value == "q":
        return "quit"
    elif value == "c":
        return "clear"
    else:
        return None
    
def handle_check_special(value):

    special = check_special(value)
    if special == "quit":
        return "quit"
    elif special == "clear":
        menu()
        return "clear"
    
def get_result(user_oper,x, y):
    operation_dic = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": remainder,
        "p": power,
        "r": root,
    }
    try:
        result = operation_dic[user_oper](x, y)
        return result
    except OverflowError:
        return "OFE"
    except ZeroDivisionError:
        return "ZDE"
    
def handle_result_error(result):
    if result == "OFE":
        print("You wrote too big of a number")
        return True
    elif result == "ZDE":
        print("You Wrote Zero in Wrong Operation")
        return True
    return False

def process_step():
    pass
    
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def remainder(x, y):
    return x % y

def power(x, y):
    return x ** y

def root(x, y):
    if x < 0 and y % 2 != 0:
        return -((-x) ** (1 / y))
    else:
        return x ** (1 / y)

# The Main body of Code which controls the flow of it

def main():
    menu()
    is_running = True
    result = None
    operation_check = {
        "/" : check_divide,
        "%" : check_remainder,
        "p" : check_power,
        "r" : check_root
    }
    # This get the First Result
    while is_running:
        # Get First Number
        if result is None:
            first_num = get_user_num()
            # Use to Quit Program
            action = handle_check_special(user_oper)
            if action == "quit":
                return
            elif action == "clear":
                continue
        # Get The Operation Sign
        user_oper = get_user_oper()
        # Use to Quit Program
        action = handle_check_special(user_oper)
        if action == "quit":
            return
        elif action == "clear":
            continue
        # Check the Operation
        error = check_operation(user_oper)
        if error is not None:
            print(error)
            continue
        # Get the Second Number
        second_num = get_user_num()
        # Use to Quit Program
        action = handle_check_special(second_num)
        if action == "quit":
            return
        elif action == "clear":
            menu()
            continue
        if result is None:
            current_value = first_num
        else:
            current_value = result
        error = operation_check[user_oper](current_value,second_num)
        if error is not None:
                print(error)
                continue
        # Do the Main Process for Calculator
        result = get_result(user_oper,current_value,second_num)
        if handle_result_error(result):
            continue
        # Show us the Result
        if result is None:
            print("Error")
            continue
        elif result is not None:
            print(f"Your Result is {result:.2f}")
            is_running = True
            continue
        
if __name__ == "__main__":
    main()
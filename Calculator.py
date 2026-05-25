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


def get_user_num():

    while True:
        try:
            num = input("Write the Number(q to Quit): ")
            if num.lower() == "q":
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
        print(f"{x} can't be Divided by Zero(0)")
        return True
    return False

def check_remainder(x,y):
    if y == 0:
        print(f"{x} can't be Divided by Zero(0)")
        return True
    return False

def check_power(x,y):
    if y < 0 and x == 0:
        print("Zero can't have a Negative Power")
        return True
    elif y == 0 and x == 0:
        print("Both Power and Base Can't be Zero")
        return True
    return False

def check_root(x,y):
    if y == 0:
        print("Root degree cannot be zero")
        return True
    elif x < 0:
        if y % 2 == 0:
            print("Even root of a negative number is not a real number")
            return True

    
# Find Invalid Operation

def check_operation(user_oper):
    if user_oper not in ["+", "-", "*", "/", "%", "p", "r"]:
        print("You selected an Invalid Operation.")
        return True
    return False

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
        print("You wrote too big of a number")
        return None
    except ZeroDivisionError:
        print("You Wrote Zero in Wrong Operation")
        return None
    
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
    operation_check = {
        "/" : check_divide,
        "%" : check_remainder,
        "p" : check_power,
        "r" : check_root
    }
    # This get the First Result
    while True:
        # Get First Number
        first_num = get_user_num()
        # Use to Quit Program
        if first_num == "q":
            break
        # Get The Operation Sign
        user_oper = get_user_oper()
        # Check the Operation
        if check_operation(user_oper):
            continue
        # Get the Second Number
        second_num = get_user_num()
        # Use to Check any Invalid value for the Specific Operation
        if operation_check[user_oper](first_num,second_num):
            continue
        # Do the Main Process for Calculator
        result = get_result(user_oper,first_num, second_num)
        # Show us the Result
        if result is None:
            print("Error")
            continue
        else:
          print(f"Your Result is {result}")
          break
    
    # To get Infinite Result System
    while True:
        # Get The Operation Sign
        user_oper = get_user_oper()
        # Use to Quit Program
        if user_oper == "q":
            break
        # Check the Operation
        if check_operation(user_oper):
            continue
        current_num = get_user_num()
        # Use to Check any Invalid value for the Specific Operation
        if operation_check[user_oper](first_num,second_num):
            continue
        # Do the Main Process for Calculator
        result = get_result(user_oper,result,current_num)
        # Show us the Result
        if result is None:
            print("Error")
            continue
        else:
          print(f"Your Result is {result}")
          continue

if __name__ == "__main__":
    main()
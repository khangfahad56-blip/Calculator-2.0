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
    print("End = Done or = ")

def get_user_num():

    while True:
        try:
            num = (input("Write the Number(q to Quit): "))
            if num.lower() or num == "=" or num.lower() == "q":
                return num
            else:
                num = float(num)
                return num    
        except ValueError:
            print("Error:Only Select Number")
            continue

def get_user_oper():
    user_oper = input("Write the Operation: ")
    return user_oper.lower()

# Use to Check any Invalid value for the Specific Operation

def check_value(first_num,second_num,user_oper):
    if user_oper == "/" or user_oper == "%":
        if second_num == 0:
            print(f"{first_num} can't be Divided by Zero(0)")
            return True
            
    elif user_oper == "p":
        if second_num < 0 and first_num == 0:
            print("Zero can't have a Negative Power")
            return True
        elif second_num == 0 and first_num == 0:
            print("Both Power and Base Can't be Zero")
            return True

    elif user_oper == "r":
        if second_num == 0:
            print("Root degree cannot be zero")
            return True
        
        if first_num < 0:
            if second_num % 2 == 0:
                print("Even root of a negative number is not a real number")
                return True
            
        if second_num == 1 or second_num == -1:
            print("Root can't be Postive or Negative one (1)")
            return True
    return False
        
# Find Invalid Operation

def check_operation(user_oper):

    if user_oper not in ["+","-","*","/","%","p","r","q"]:
        print("You selected a Invalid Operation.")
        return True
    return False

def add(list_num):
    total = 0
    for num in list_num:
        total += num
    return total

def subtract(list_num):
    total = 0
    for num in list_num:
        total += num
    return total

def multiply(list_num):
    total = 0
    for num in list_num:
        total *= num
    return total

def divide(list_num):
    total = 0
    for num in list_num:
        total /= num
    return total

def remainder(list_num):
    total = 0
    for num in list_num:
        total %= num
    return total

def power(list_num):
    total = 0
    for num in list_num:
        total = num ** num
    return total

def root(list_num):
    total = 0
    for num in list_num:
        total = num ** (1/num)
    return total

# The Main body of Code which controll the flow of it

def main():

    operation_dic = {
        "+" :add,
        "-" :subtract,
        "*" :multiply,
        "/" :divide,
        "%" :remainder,
        "p" :power,
        "r" :root,
    }

    second_num = 5

    repeat = True

    while True:

        if repeat:
            menu()

        list_num = []
        list_oper = []
        first_num = get_user_num()
        list_num.append(first_num)
        # Use to Quit Program
        if first_num == "q":
            break
        user_oper = get_user_oper()
        if check_operation(user_oper):
            continue
        list_oper.append(user_oper)
        #Use to Check any Invalid value for the Specific Operation
        #I need th change this function for multi-number system
        # if check_value(first_num,second_num,user_oper):
            # continue
            
        #Stop the Input and Doing the Proces
        if "done" not in list_num or "=" not in list_num:
            repeat = False
            continue

        # Do the Main Process for Calculator
        
        try:
            result = operation_dic[user_oper](first_num,second_num)

        # Handles the Exception of Program

        except OverflowError:
            print("You wrote too big of a number")
            continue
        except ZeroDivisionError:
            print("You Wrote Zero in Wrong Operation")
            continue

        # Show us the Result

        if result is None:
            print("You Selected a Invalid Operation")
        else:
            print(f"Your Result is {result}")
        
    
if __name__ == "__main__":
    main()
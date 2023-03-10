def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations =   {"+": add,
                "-": substract,
                "*": multiply,
                "/": divide, }


def calculator():
    num1 = float(input("What is the first number?: "))
    for i in operations:
        print(i)
    should_continue = True
    while should_continue :
        operations_symbol = input("Pick a symbol: ")
        num2 = float(input("What is the next number?: "))
        cal_function = operations[operations_symbol]
        result = cal_function(num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {result}")
        ask_continue = input(f"Do you want to continue with {result} ?")
        if ask_continue == "yes":
            num1 = result
        else:
            should_continue = False
            calculator()


calculator()



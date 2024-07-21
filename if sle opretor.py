first = input("Enter first number : ")
operator = input("Enter th operator (+,-,*,/):")
second = input("Enter the second number: ")
first = int(first)
second = int(second)
if operator == '+':
    print("The Sum is:",first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
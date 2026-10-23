print("====calculator====")
num1 = int(input("enter your first number:"))
num2 = int(input("enter your second number"))
operator = input("choose your operator(+, -, *, /)")

if operator =="+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2!= 0:
        result = num1/num2

    else:
        result = "cannot divide by zero"

else: 
    result = "invalid operation"

print("result", result)


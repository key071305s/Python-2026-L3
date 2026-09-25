def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

num = int(input("Enter the number: "))
print(f"The factory of {num} is: ", factorial(num))
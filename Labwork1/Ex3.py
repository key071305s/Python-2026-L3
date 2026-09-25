num = int(input("Enter the numbebr? "))
PRIME = True
if (num == 1):
    print("1 is a NOT prime number")

else:
    for i in range(2, num, 1):
        if num%i == 0:
            PRIME = False
            break
    if (PRIME):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is a NOT prime number")
        
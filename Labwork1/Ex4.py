num = int(input("Enter the number? "))
check = 0
for i in range(1,num, 1):
    if num%i == 0:
        check += i
if check == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a NOT perfect number")
m = int(input("Enter row m: "))
n = int(input("Enter col n: "))

def print_sao(m, n):
    for row in range(m):
        for col in range(n):
            if row == 0 or row == m -1 or col == 0 or col == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

print_sao(m,n)
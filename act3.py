n = int(input("Enter number of rows :"))
half = (n// 2) + (n % 2)


for i in range(1, half + 1):
    print(" " * (half - i), end='')
    for j in range(1,2 * i):
        print(j, end='')
    print()


for i in range(half - 1, 0 , -1):
    print(" " * (half - i), end='')
    for j in range(1,2 * i):
        print(j, end='')
    print()
print("Half Pyramid Pattern(*)")
n = input("Enter number of rows : ")

for i in range(0, int(n)):
    for j in range(0, i + 1):
        print("*", end='')
    print("\r")
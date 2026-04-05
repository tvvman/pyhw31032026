n = int(input("введіть число: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)
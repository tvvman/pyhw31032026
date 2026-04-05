import random

number = random.randint(1, 10)

for i in range(3):
    guess = int(input("вгадай число від 1 до 10: "))

    if guess == number:
        print("ти вгадав!")
        break
    elif guess > number:
        print("менше")
    else:
        print("більше")
else:
    print(f"ти програв число було: {number}")
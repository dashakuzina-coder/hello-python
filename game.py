import random
secret_number = random.randint(1, 10)
print("Я загадал число от 1 до 10. Попробуй угадать!")
for attempt in range(1, 4):
    guess = int(input(f"Попытка {attempt}. Введи число: "))
    if guess == secret_number:
        print("Угадала! Ты крута!")
        break
    elif guess < secret_number:
        print("Лох! Мое число больше.")
    else:
        print("Снова мимо! Мое число меньше.")
else:
    print(f"Не угадала. Я загадал число {secret_number}.")
sum_numbers = lambda x, y: x + y

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

if num1.isdigit() and num2.isdigit():
    num1 = float(num1)
    num2 = float(num2)

    result = sum_numbers(num1, num2)

    print(f"Сумма чисел {num1} и {num2} равна {result}")
else:
    print("Ошибка: Введите корректные числа.")
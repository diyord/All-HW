def is_palindrome(word):
    return word == word[::-1]

def main():
    user_input = input("Введите слово: ").lower()  # Приводим к нижнему регистру для учета регистра

    if is_palindrome(user_input):
        print("Это слово - палиндром!")
    else:
        print("Это слово не является палиндромом.")

if __name__ == "__main__":
    main()
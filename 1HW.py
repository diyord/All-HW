def get_user_choice(player_name):
    user_choice = input(f"{player_name}, выбери: камень, ножницы или бумага? ").lower()
    while user_choice not in ["камень", "ножницы", "бумага"]:
        print("Некорректный выбор. Попробуй еще раз.")
        user_choice = input(f"{player_name}, выбери: камень, ножницы или бумага? ").lower()
    return user_choice

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "Ничья!"
    elif (
        (player1_choice == "камень" and player2_choice == "ножницы") or
        (player1_choice == "ножницы" and player2_choice == "бумага") or
        (player1_choice == "бумага" and player2_choice == "камень")
    ):
        return "Игрок 1 победил!"
    else:
        return "Игрок 2 победил."

def play_game():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

    player1_name = input("Введите имя игрока 1: ")
    player2_name = input("Введите имя игрока 2: ")

    while True:
        player1_choice = get_user_choice(player1_name)
        player2_choice = get_user_choice(player2_name)

        print(f"{player1_name} выбрал: {player1_choice}")
        print(f"{player2_name} выбрал: {player2_choice}")

        result = determine_winner(player1_choice, player2_choice)
        print(result)

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            break

if __name__ == "__main__":
    play_game()
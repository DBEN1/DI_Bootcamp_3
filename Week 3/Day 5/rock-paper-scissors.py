from Game import Game

def get_user_menu_choice():
    print("\nMenu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    choice = input("Enter your choice: ")
    return choice

def print_results(results):
    print("\nGame Results:")
    print("Wins: ", results.get("win", 0))
    print("Losses: ", results.get("loss", 0))
    print("Draws: ", results.get("draw", 0))
    print("Thanks for playing!")

def main():
    game_results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            game_instance = Game() 
            result = game_instance.play() 
            if result in game_results:
                game_results[result] += 1

        elif choice == "2":
            print_results(game_results)

        elif choice == "3":
            print_results(game_results)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

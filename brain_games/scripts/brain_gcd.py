from brain_games.games.brain_gcd import gcd_game
from brain_games.utils import welcome_script


def main():
    username = welcome_script()

    gcd_game(username=username)


if __name__ == '__main__':
    main()

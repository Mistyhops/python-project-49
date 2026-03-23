from brain_games.games.brain_calc import calc_game
from brain_games.utils import welcome_script


def main():
    username = welcome_script()

    calc_game(username=username)


if __name__ == '__main__':
    main()

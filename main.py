from Game import Game


def load_logo():
    logo = """//      ____        __  __  __          __    _                 
//     / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___  _____      
//    / __  / __ `/ __/ __/ / _ \\/ ___/ __ \\/ / __ \\/ ___/   
//   / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ (__  )       
//  /_____/\\__,_/\\__/\\__/_/\\___/____/_/ /_/_/ .___/____/    
//                                         /_/                  
//"""
    print(logo)


def load_menu_options():
    menu_options = """//  [S]tart game
//  [R]esume game
//  [M]ultiplayer
//  [E]xit
\t"""

    menu_option = input(menu_options)
    match menu_option.upper():
        case 'S':
            pass
        case 'R':
            pass
        case 'M':
            choose_game_mode()
        case 'E':
            exit()
        case _:
            print(wrong_option_chosen(menu_option))
            load_menu_options()


def choose_game_mode():
    print("""//
//  [S]plitscreen
//  [L]AN
//  [O]nline
//""")


def wrong_option_chosen(option):
    return "\tThe Option [{0}] does not exist! Try again!\n".format(option)


if __name__ == '__main__':

    load_logo()
    game = Game({'C': [1, 2, 3]})
    game.update_game_board('c1')
    game.update_game_board('c2')
    game.update_game_board('c3')
    game.update_game_board('j1')
    game.update_game_board('c10')
    game.update_game_board('h3')




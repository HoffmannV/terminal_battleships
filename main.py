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
    menu_options = """
//  [S]tart game
//  [R]esume game
//  [M]ultiplayer
//  [E]xit
//"""
    print(menu_options)


def choose_game_mode():
    print("""//
//  [S]plitscreen
//  [L]AN
//  [O]nline
//""")


if __name__ == '__main__':
    load_logo()
    load_menu_options()

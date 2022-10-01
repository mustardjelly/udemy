# Store our constants in a constants file.
# Add classes to organize our constants by name
# Can use alias' to rename classes:
#   from constants import Game as Constants
#   Constants.PERFECT_SCORE


class Game:
    # Add game constants here
    PERFECT_SCORE = 21
    ACE_1 = 1
    ACE = 11
    DRAW = "d"
    STAND = "s"

    LOGO = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

class Player:
    # Add player constants here
    COMPUTER_NAME = "Computer"
    THRESHOLD = 17
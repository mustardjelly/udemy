import random
import sys


BREAKPOINT = 16 # computer stops drawing if hand is bigger than 16
PERFECT_SCORE = 21 # perfect blackjack score


# complete
def intro() -> str:
    """
    Blackjack ascii art and game start.
    """

    confirmation = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if confirmation != "y":
        sys.exit()

    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    """

    return logo


# continue
def draw_card() -> int:
    """Draw a card from valid card selection and return its value as an integer."""
    # TODO: consider handling ace in another way
    available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    distributed_card = random.choice(available_cards)
    return distributed_card


# complete
def hit_or_stand() -> bool:
    """Take input from the user if they would like to hit or stand.
    
    Return a boolean indicating this."""
    VALID_SELECTIONS = ["y", "n"]
    selection_is_valid = False

    while not selection_is_valid:
        selection = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        selection_is_valid = selection in VALID_SELECTIONS

    if selection == "y":
        return True

    if selection == "n":
        return False


# complete
def game_status(user: list, computer: list, final: bool) -> str:
    """Lets the user know what the game state is.
    
    Returns a string indicating the game state."""
    if final:
        return f"""
Your final hand: {user}
Computer's final hand: {computer}
        """

    if len(computer) == 1:
        return f"""
Your cards: {user}
Computer's first card: {computer[0]}
        """

    return f"""
Your cards: {user}
Computer's cards: {computer}
    """


# complete
def calculate_card_values(user_hand: list, computer_hand: list) -> list:
    """Calculate the score for each user and return a list. 
    user_Score is 0 index, computer_score is 1 index"""
    total = []

    user_score = sum(user_hand)
    computer_score = sum(computer_hand)

    total.append(user_score)
    total.append(computer_score)

    return total


# complete
def determine_winner(calculate_card_values: list) -> str:
    """Based on scores, determine who won the round. Returns result as a string."""
    user = calculate_card_values[0]
    computer = calculate_card_values[1]
    result = None

    if user > PERFECT_SCORE:
        result = "lose."

    elif user <= PERFECT_SCORE and computer > PERFECT_SCORE:
        result = "win."

    elif user <= PERFECT_SCORE and computer <= PERFECT_SCORE:
        if user == computer:
            result = "drew."

        elif user > computer:
            result = "win."

        elif user < computer:
            result = "lose."

    elif user > PERFECT_SCORE and computer > PERFECT_SCORE:
        result = "drew."

    return result


def add_card_to_hand(hand: list) -> None:
    """
    Draws a card and adds it to a players hand. 

    returns none bacause lista are mutable 
    shorturl.at/aSV07
    """
    card = draw_card()
    hand.append(card)


def computer_should_draw(computers_hand: list) -> bool:
    """
    determines if computer should draw another card.
    returns True if computers hand is less than the BREAKPOINT.
    """
    return sum(computers_hand) <= BREAKPOINT


# TODO optimize/ refactor
def main() -> None:
    # TODO: Move this state variables into a game object
    computers_hand = []
    users_hand = []
    play = True

    print(intro())

    while play:
        # if the game has just started:
        if len(users_hand) == 0:
            for _ in range(2):
                add_card_to_hand(users_hand)

            add_card_to_hand(computers_hand)

            print(game_status(users_hand, computers_hand, not play))

        # ask if user wants to draw card:
        play = hit_or_stand()

        # if the user doesnt want to draw another card:
        if not play:
            while computer_should_draw(computers_hand):
                add_card_to_hand(computers_hand)
            break

        # if user decides to draw another card:
        add_card_to_hand(users_hand)

        # if computers cards add to below 16, it draws another card
        if computer_should_draw(computers_hand):
            add_card_to_hand(computers_hand)

        # if the users or computers cards add to above PERFECT_SCORE, if they have an 11, change the value to 1 instead.
        users_score = sum(users_hand)
        computers_score = sum(computers_hand)
        if users_score > PERFECT_SCORE or computers_score > PERFECT_SCORE:
            if users_score > PERFECT_SCORE:
                while users_score > PERFECT_SCORE:
                    # TODO: 11 variable
                    # TODO: move this logic to drawing logic. Research Ace logic
                    if 11 in users_hand:
                        ace_index = users_hand.index(11)
                        users_hand[ace_index] = 1
                    break

            # TODO: Make function
            if computers_score > PERFECT_SCORE:
                while computers_score > PERFECT_SCORE:
                    if 11 in computers_hand:
                        ace_index = computers_hand.index(11)
                        computers_hand[ace_index] = 1
                    # TODO: Break stops continual checking of sum value
                    break

                print(game_status(users_hand, computers_hand, not play))
                continue
            
            # TODO: Rethink this loop
            continue
            break

        print(game_status(users_hand, computers_hand, not play))

    # TODO: rename variable
    calculate_score = calculate_card_values(users_hand, computers_hand)
    result = determine_winner(calculate_score)

    print(game_status(users_hand, computers_hand, not play))
    print(f"You {result}")


if __name__ == "__main__":
    main()

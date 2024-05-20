def game_over(player1, player2, rolls):
    """
    player1 is the number of chips that player 1 has.
    player2 is the number of chips that player 2 has.
    rolls is the last list of dice rolls.

    Return True if the game is over, False otherwise.

    The game is over if player1 has at least 30 points,
    or player 2 has at least 30 points,
    or there are 5 rolls none of which is a 1.
    """
    # (번역)
    # player1은 플레이어 1이 가진 칩의 수입니다.
    # player2는 플레이어 2가 가진 칩의 수입니다.
    # rolls는 주사위를 굴린 마지막 목록입니다.

    # 게임이 끝나면 참을 반환하고, 그렇지 않으면 거짓을 반환합니다.

    # 플레이어1이 30점 이상이면 게임이 종료됩니다,
    # 또는 플레이어 2가 30점 이상이거나
    # 또는 주사위가 5개가 있고 그 중 1이 하나도 없는 경우 게임이 종료됩니다.
    return player1 >= 30 or player2 >= 30 or (len(rolls) == 5 and not 1 in rolls)


import random


def roll_dice(n):
    """
    Create a list of n random integers between 1 and 6.
    Print each of these integers, and return the list.
    """
    rolls = []
    for i in range(n):
        roll = random.randint(1, 6)
        print(roll)
        rolls.append(roll)
    return rolls


def turn_over(rolls):
    """
    Return True if the turn is over, False otherwise.

    The turn is over if any of the rolls is a 1,
    or if there are exactly five rolls.
    """
    return 1 in rolls or len(rolls) == 5


def take_full_turn(pot_chips):
    """
    The pot has pot_chips chips.

    Take a full turn for the current player and, once done,
    return a list of two values:
    the number of chips in the pot, and the final list of dice rolls.

    Begin by rolling 1 die, and put 1 chip into the pot.
    Then, if the turn isn't over, ask the player whether
    they'd like to continue their turn.
    If they respond 'n', then the turn is over.
        If they respond 'y', then roll one more die than last time,
        and add 1 chip to the pot for each die that is rolled.
        (for example, if 3 dice were rolled last time, then
        roll 4 dice and add 4 chips to the pot.)
    If the turn is not over, repeat by asking the player again
    whether they'd like to continue their turn.
    """
    rolls = roll_dice(1)
    pot_chips += 1
    while not turn_over(rolls):
        keep_going = input("Continue? (y/n) ")
        if keep_going == "y":
            rolls = roll_dice(len(rolls) + 1)
            pot_chips += len(rolls)
        else:
            break
    return pot_chips, rolls


def wins_chips(rolls):
    """
    Return True if the player wins chips, False otherwise.

    The player wins the chips if none of the rolls is a 1.
    """
    return not 1 in rolls


def switch_player(player1, player2, rolls, current_player):
    """
    player1 is the number of chips that player 1 has.
    player2 is the number of chips that player 2 has.
    rolls is the last list of dice rolls.
    current_player is the current player (1 or 2).

    If the game is not over, switch current_player to the other player.
    Return the new current_player.
    """
    if not game_over(player1, player2, rolls):
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
    return current_player


def play():
    """
    Play the game until the game is over.

    The pot starts with 0 chips, and each player starts with 0 chips.

    Randomly decide whether player 1 or player 2 goes first.
    Before each turn, print three lines of information:
    1. The number of chips in the pot
    2. The number of chips that each player has
    3. Whether it is player 1's turn or player 2's turn

    Take a full turn for the current player.
    If they won the chips, add the chips in the pot to the
    total for that player and reset the pot to have 0 chips.

    Then, switch to the other player's turn.

    Once the game is over, print the current player
    (that’s the player who won).
    """
    pot_chips = 0
    player1 = 0
    player2 = 0
    current_player = random.randint(1, 2)
    rolls = []
    while not game_over(player1, player2, rolls):
        print("Pot chips:", pot_chips)
        print("Player 1 chips:", player1)
        print("Player 2 chips:", player2)
        print("Player", current_player, "turn")
        pot_chips, rolls = take_full_turn(pot_chips)
        if wins_chips(rolls):
            if current_player == 1:
                player1 += pot_chips
            else:
                player2 += pot_chips
            pot_chips = 0
        current_player = switch_player(player1, player2, rolls, current_player)
    print("Player", current_player, "wins!")

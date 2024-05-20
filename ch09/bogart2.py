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
    total for that player
    and reset the pot to have 0 chips.

    Then, switch to the other player's turn.

    Once the game is over, print the current player
    (that's the player who won).
    """
    pot_chips = 0
    player1 = 0
    player2 = 0
    current_player = random.randint(1, 2)
    rolls = []

    print("Welcome to Bogart!")
    print()

    while not game_over(player1, player2, rolls):
        print("Pot chips:", pot_chips)
        print("Player 1 chips:", player1)
        print("Player 2 chips:", player2)
        print("Player", current_player, "turn")
        pot_chips, rolls = take_full_turn(pot_chips)
        if wins_chips(rolls):
            print("Player", current_player, "gets", pot_chips, "chips!")
            if current_player == 1:
                player1 += pot_chips
            else:
                player2 += pot_chips
            pot_chips = 0
        current_player = switch_player(player1, player2, rolls, current_player)

        print()
        print()
        print("-=" * 20)
        print()

    print("Player", current_player, "wins!")

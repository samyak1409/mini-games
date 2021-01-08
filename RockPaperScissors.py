# Rock Paper Scissors! ->

from getpass import getpass as invisible


def rps(player1, player2):
    dict_rps = {'r': "Rock", 'p': "Paper", 's': "Scissors"}
    if (player1 and player2) in ('r', 'p', 's'):
        if player1 == player2:
            return f"Tie! (Player1->{dict_rps[player1]} vs Player2->{dict_rps[player2]})"
        if (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p') or (
                player1 == 'r' and player2 == 's'):
            return f"Congratulations! Player1 Won! (Player1->{dict_rps[player1]}, Player2->{dict_rps[player2]})"
        else:
            return f"Congratulations! Player2 Won! (Player1->{dict_rps[player1]}, Player2->{dict_rps[player2]})"
    else:
        return "Error Occurred!! -> you have to type r, p or s for Rock, Paper or Scissors respectively."


print("\nWelcome to Rock/Paper/Scissors!\n(type r for Rock, p for Paper or s for Scissors!)\n\n{Note that as we know rock paper scissors is a hand game usually played between two people, in which each player SIMULTANEOUSLY forms one of three shapes with an outstretched hand. But, the limitation here in this computer program is it can't take two inputs SIMULTANEOUSLY!! So, either to overcome this limitation, player1 have to hide the keyboard from player2 while entering his/her choice! (or just close the program and play in real world! :D }")

run = ''
while run != 'n':
    input1 = invisible("\nYour input Player1 (on the screen it will not be visible!): ").lower()
    input2 = invisible("Your input Player2: ").lower()
    if (input1 and input2) != '':
        print("\n" + rps(input1, input2))
    else:
        print("\nError: Input can't be empty!!")
    run = input("\n\nPlay again? (press enter to continue/ 'n' to exit): ").lower()

print("\nThanks for Playing! :)")

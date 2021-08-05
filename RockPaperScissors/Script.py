# Rock paper scissors


from getpass import getpass as invisible


def rps(p1, p2):

    rps_ = {'r': "Rock", 'p': "Paper", 's': "Scissors"}

    if p1 == p2:
        return f"It's a Tie! (Both chose {rps_[p1]})"

    if (p1 == 'p' and p2 == 'r') or (p1 == 's' and p2 == 'p') or (p1 == 'r' and p2 == 's'):
        return f"Congratulations! Player1 Won! (Player1->{rps_[p1]}, Player2->{rps_[p2]})"

    return f"Congratulations! Player2 Won! (Player1->{rps_[p1]}, Player2->{rps_[p2]})"


print("""\nWelcome to Rock/Paper/Scissors! \n
{NOTE that as we know rock paper scissors is a hand game usually played between two people, 
in which each player simultaneously forms one of the three shapes with an outstretched hand. 
But, the limitation here in this program is it can't take two inputs SIMULTANEOUSLY!! 
So, either to overcome this limitation, player1 have to hide the keyboard from player2 
while entering his/her choice or just close the program and play in the real world! :D } \n
(type r for Rock, p for Paper or s for Scissors)""")

while True:

    input1 = invisible("\nYour input Player1 (will be invisible on screen): ").lower()
    if input1 not in ('r', 'p', 's'):
        print("Error: you have to type r, p or s for Rock, Paper or Scissor respectively.")
        continue

    input2 = input("Your input Player2: ").lower()
    if input2 not in ('r', 'p', 's'):
        print("Error: you have to type either r, p or s for Rock, Paper or Scissor respectively.")
        continue

    print("\n" + rps(input1, input2), '\n')

    if input("Try again? (press enter to continue): "):
        break

print("\nThanks for Playing! :)")

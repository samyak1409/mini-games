# Game Description! -> Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two players,
# X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in
# a horizontal, vertical, or diagonal row is the winner.


def show_grid():
    print(f'''
        -------------------
        |  {grid_dict[1]}  |  {grid_dict[2]}  |  {grid_dict[3]}  |
        |-----------------|
        |  {grid_dict[4]}  |  {grid_dict[5]}  |  {grid_dict[6]}  |
        |-----------------|
        |  {grid_dict[7]}  |  {grid_dict[8]}  |  {grid_dict[9]}  |
        -------------------''')


def game_is_on():
    if ((grid_dict[1] == 'x') and (grid_dict[2] == 'x') and (grid_dict[3] == 'x')) or (
            (grid_dict[1] == 'o') and (grid_dict[2] == 'o') and (grid_dict[3] == 'o')) or (
            (grid_dict[4] == 'x') and (grid_dict[5] == 'x') and (grid_dict[6] == 'x')) or (
            (grid_dict[4] == 'o') and (grid_dict[5] == 'o') and (grid_dict[6] == 'o')) or (
            (grid_dict[7] == 'x') and (grid_dict[8] == 'x') and (grid_dict[9] == 'x')) or (
            (grid_dict[7] == 'o') and (grid_dict[8] == 'o') and (grid_dict[9] == 'o')) or (
            (grid_dict[1] == 'x') and (grid_dict[4] == 'x') and (grid_dict[7] == 'x')) or (
            (grid_dict[1] == 'o') and (grid_dict[4] == 'o') and (grid_dict[7] == 'o')) or (
            (grid_dict[2] == 'x') and (grid_dict[5] == 'x') and (grid_dict[8] == 'x')) or (
            (grid_dict[2] == 'o') and (grid_dict[5] == 'o') and (grid_dict[8] == 'o')) or (
            (grid_dict[3] == 'x') and (grid_dict[6] == 'x') and (grid_dict[9] == 'x')) or (
            (grid_dict[3] == 'o') and (grid_dict[6] == 'o') and (grid_dict[9] == 'o')) or (
            (grid_dict[1] == 'x') and (grid_dict[5] == 'x') and (grid_dict[9] == 'x')) or (
            (grid_dict[1] == 'o') and (grid_dict[5] == 'o') and (grid_dict[9] == 'o')) or (
            (grid_dict[3] == 'x') and (grid_dict[5] == 'x') and (grid_dict[7] == 'x')) or (
            (grid_dict[3] == 'o') and (grid_dict[5] == 'o') and (grid_dict[7] == 'o')):
        return False
    else:
        return True


def check(inp):
    return True if (0 < inp < 10 and grid_dict[inp] == ' ') else False


grid_dict = {1: 1, 2: 2, 3: 3,
             4: 4, 5: 5, 6: 6,
             7: 7, 8: 8, 9: 9}
print("\nTIC_TAC_TOE!, This is the 3x3 grid!-> (note the NUMBERING on each boxes)")
show_grid()

while True:
    grid_dict[1] = grid_dict[2] = grid_dict[3] = grid_dict[4] = grid_dict[5] = grid_dict[6] = grid_dict[7] = grid_dict[
        8] = grid_dict[9] = ' '
    show_grid()

    moves = 0
    while moves < 9 and game_is_on():
        while True:
            try:
                input1 = int(input("\nPLAYER_1 (x), where you wanna mark? (write number): "))
                break
            except ValueError:
                print("\nError! Enter a valid number.")
        if check(input1):
            grid_dict[input1] = 'x'
            moves += 1
            show_grid()

            while moves < 9 and game_is_on():
                while True:
                    try:
                        input2 = int(input("\nPLAYER_2 (o), where you wanna mark? (write number): "))
                        break
                    except ValueError:
                        print("\nError! Enter a number.")
                if check(input2):
                    grid_dict[input2] = 'o'
                    moves += 1
                    show_grid()
                    break
                else:
                    print("\nError! Choose a valid number.")
        else:
            print("\nError! Choose a valid number.")

    if not game_is_on():
        print(f"\nGAME OVER, {'PLAYER_1 (x)' if (moves % 2 != 0) else 'PLAYER_2 (o)'} WON! :D")
    else:
        print("\nG A M E   T I E")

    print("THANKS for Playing! :) \n\nNEW GAME:")

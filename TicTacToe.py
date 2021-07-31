# Tic-tac-toe


# FUNCTIONS:
def show_grid():
    print(f'''
        -------------------
        |  {grid[1]}  |  {grid[2]}  |  {grid[3]}  |
        |-----------------|
        |  {grid[4]}  |  {grid[5]}  |  {grid[6]}  |
        |-----------------|
        |  {grid[7]}  |  {grid[8]}  |  {grid[9]}  |
        -------------------''')


def pos(p: str):
    while True:
        try:
            inp = int(input(f"\n{p}, where you wanna mark? (write number): "))
            if 1 <= inp <= 9 and grid[inp] == ' ':
                return inp
            raise ValueError  # (else)
        except ValueError:
            print("\nError! Choose a valid number.")  # continues


def game_over():
    if \
     (grid[1] == grid[2] == grid[3] != ' ') or \
     (grid[4] == grid[5] == grid[6] != ' ') or \
     (grid[7] == grid[8] == grid[9] != ' ') or \
     (grid[1] == grid[4] == grid[7] != ' ') or \
     (grid[2] == grid[5] == grid[8] != ' ') or \
     (grid[3] == grid[6] == grid[9] != ' ') or \
     (grid[1] == grid[5] == grid[9] != ' ') or \
     (grid[3] == grid[5] == grid[7] != ' '):
        return True
    else:
        return False


# MAIN:
grid = {1: 1, 2: 2, 3: 3,
        4: 4, 5: 5, 6: 6,
        7: 7, 8: 8, 9: 9}
print("\nThis is the 3x3 grid (note the NUMBERING on each boxes)")
show_grid()

while True:
    grid[1] = grid[2] = grid[3] = grid[4] = grid[5] = grid[6] = grid[7] = grid[8] = grid[9] = ' '
    show_grid()

    for i in range(5):
        grid[pos('X')] = 'X'
        show_grid()
        if game_over():
            print(f"\nGAME OVER, X WON! :D")
            break

        if i == 4:  # (i*2 + 1 = 9)
            print("\nG A M E    T I E D")
            break

        grid[pos('O')] = 'O'
        show_grid()
        if game_over():
            print(f"\nGAME OVER, O WON! :D")
            break

    print("\nTHANKS for Playing! :) \n\n\nNEW GAME:")

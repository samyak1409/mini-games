# Prediction Trick


def get_bool(num: int): return 'NO ' if (num in positions) else 'YES'


print(f'''\nHello! We have a guessing game for you, rules are as follows! -> \n
As you can see there is a (3x3) grid below (9 boxes), out of those we will start with the box on first row third column,
now as I will give you a number, you have to move those number of times within the table horizontally or vertically but not diagonally! Okay?
(Note that repeating a block is allowed while moving.) \n
    -------------------
    |     |     |here |
    |-----------------|
    |     |     |     |
    |-----------------|
    |     |     |     |
    -------------------
\nPress enter to start: ''')
input()

positions = []
for pos, moves in ((1, 1), (2, 7), (3, 3), (4, 7), (5, 5), (6, 9), (7, 3), (8, 1)):
    positions.append(pos)
    print(f"Now move", moves, "time" if (moves == 1) else "times", "(press enter when done)")
    input()

    print(f''''NO' are the blocks currently you are NOT on ;) (Note that you can't move on or through a 'NO' block.) \n
    -------------------
    | {get_bool(3)} | {get_bool(4)} | {get_bool(1)} |
    |-----------------|
    | {get_bool(2)} | {get_bool(7)} | {get_bool(6)} |
    |-----------------|
    | {get_bool(5)} | {get_bool(8)} | {get_bool(9)} |
    ------------------- \n''')

print("You are on the 'YES' block! How was it? ;) \n\nThanks for Playing!")

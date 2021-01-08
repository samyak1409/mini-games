# Game! ->

run = ''
while run != 'n':
    print(f'''\nHello! We have a guessing game for you, rules are as follows!->\n
    As you can see there is a (3x3) table below (9 elements), out of those we will start with element on first row third column,
    now as I will give you a number, you have to move those number of times within the table horizontally or vertically but not diagonally! Okay?
    (Note that repeating a block is allowed while moving.)\n
        ----------------
        |    |    |here|
        |--------------|
        |    |    |    |
        |--------------|
        |    |    |    |
        ----------------\n''')

    if input("Press k to proceed: ").lower() == 'k':

        dict1 = {1: 1, 2: 7, 3: 3, 4: 7, 5: 5, 6: 9, 7: 3, 8: 1}
        list1 = []

        for i in dict1:
            list1.append(i)
            print(f"\nNow Move {dict1[i]} time(s)")
            input("(Press enter to proceed)")

            print(
                f'''\n'False' are the blocks currently you are NOT on ;) (Note that you can't go on or move through a False block.)\n
        ------------------
        |{3 not in list1}|{4 not in list1}|{1 not in list1}|
        |-----------------|
        |{2 not in list1}|{7 not in list1}|{6 not in list1}|
        |-----------------|
        |{5 not in list1}|{8 not in list1}|{9 not in list1} |
        ------------------''')

        print("\nYou are on the 'True' block! ;)\n")

    run = input("\nTry again? (press enter to continue/ 'n' to exit): ").lower()

print("\nThanks for playing! :)")

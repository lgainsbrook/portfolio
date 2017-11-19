import os
import random
import readchar

GRID = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0),
        (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1), (9,1),
        (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2), (8,2), (9,2),
        (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3), (8,3), (9,3),
        (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4), (8,4), (9,4),
        (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5), (8,5), (9,5),
        (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6), (8,6), (9,6),
        (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (8,7), (9,7),
        (0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,8), (7,8), (8,8), (9,8),
        (0,9), (1,9), (2,9), (3,9), (4,9), (5,9), (6,9), (7,9), (8,9), (9,9)
        ]

### make the monster go towards the player (if player less than monster...)

right = 'l'
left = 'k'
up = 'o'
down = ','

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear()
    print("Welcome to the dungeon!\n Press any key to begin.")
    if readchar.readchar(): clear()

    print("""
    Your mission, should you accept, is to find the treasure, then find the secret door to get you and the treasure safely out of the dungeon. Watch out for the slow-moving monster who's trying to eat you!

    Press 'q' at any time to quit. Otherwise, enjoy!

    Use the following buttons to navigate the dungeon:
    L = right
    K = left
    O = up
    , = down

    Take a moment to prepare yourself. Then press any key when you're ready to begin.

    """)

    readchar.readchar()

def get_locations():
    return random.sample(GRID, 4)

def expand_monster(monster):
    x,y = monster
    return [(x+1, y), (x, y+1), (x+1, y+1)]

def move_monster(monster, player):
    xm,ym = monster
    xp, yp = player
    num = random.randint(0,1)
    while True:
        if xp < xm and num == 0:
            xm -= 1
        elif xp > xm and num == 0:
            xm += 1
        elif yp < ym and num == 1:
            ym -= 1
        elif yp > ym and num == 1:
            ym += 1
        else:
            if xp < xm:
                xm -= 1
            if xp > xm:
                xm += 1
        if xm >= 0 and xm <= 8 and ym >= 0 and ym <= 8:
            return xm, ym
        else:
            continue

def move_player(player, move):
    x,y = player
    if move == left:
        x -= 1
    if move == right:
        x += 1
    if move == up:
        y -= 1
    if move == down:
        y += 1
    return x,y

def get_moves(player):
    moves = [right, left, up, down]
    x,y = player
    if x == 0:
        moves.remove(left)
    if x == 9:
        moves.remove(right)
    if y == 0:
        moves.remove(up)
    if y == 9:
        moves.remove(down)
    return moves

def draw_grid(player, monster, door, treasure, big_monster):

    print(" _" *10)
    tile = "|{}"
    for cell in GRID:
        x,y = cell
        if x < 9:
            line_end = ""
            if cell == player:
                output = tile.format("~")
            elif cell == monster or cell in big_monster:
                output = tile.format("M")
            elif cell == treasure:
                output = tile.format("X")
            elif cell == door:
                output = tile.format("]")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("~|")
            elif cell == monster or cell in big_monster:
                output = tile.format("M|")
            elif cell == treasure:
                output = tile.format("X|")
            elif cell == door:
                output = tile.format("]|")
            else:
                output = tile.format("_|")
        print(output, end = line_end)

def end_game():
    print("Would you like to play again? Type 'q' to quit, or press any other key to begin: ")
    again = readchar.readchar()
    if again.lower() == 'q':
        print("See you next time!")
    else:
        game()

def game():
    player, monster, door, treasure = get_locations()
    big_monster = expand_monster(monster)
    while True:
        clear()
        print("X = treasure   M = monster   ] = exit")
        draw_grid(player, monster, door, treasure, big_monster)
        monster = move_monster(monster, player)
        big_monster = expand_monster(monster)
        valid_moves = get_moves(player)
        move = readchar.readchar()
        #move = move.lower()
        if move == 'q':
            print("See you next time!")
            quit()
        elif move in valid_moves:
            player = move_player(player, move)
        elif move in [right, left, up, down]:
            print("\n** Ouch! Watch out for those walls! **\n")
            readchar.readchar()
            continue
        else:
            print("\n** Sorry, that's not a valid entry. **\n")
            readchar.readchar()
            continue
        if player == treasure:
            "You got the treasure. Now get out!!!"
            treasure = False
        elif player == monster or player in big_monster:
            print("The monster got you!!")
            end_game()
        elif player == door:
            if treasure == False:
                print("You made it out! Mission accomplished!")
                end_game()
            else:
                print("You need to get the treasure first!")
                readchar.readchar()


intro()
game()

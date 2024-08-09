import random
import time

rooms = [
    [2, 8, 14],    #   0
    [7, 13, 19],   #   1
    [12, 18, 0],   #   2
    [16, 17, 19],  #   3
    [11, 14, 18],  #   4
    [13, 15, 18],  #   5
    [9, 14, 16],   #   6
    [1, 15, 17],   #   7
    [0, 10, 16],   #   8
    [6, 11, 19],   #   9
    [8, 12, 17],   #  10
    [4, 9, 13],    #  11
    [2, 10, 15],   #  12
    [1, 5, 11],    #  13
    [0, 4, 6],     #  14
    [5, 7, 12],    #  15
    [3, 6, 8],     #  16
    [3, 7, 10],    #  17
    [2, 4, 5],     #  18
    [1, 3, 9],     #  19
]

player_room_nr = 0
bat_1_room_nr = 0
bat_2_room_nr = 0
bottomless_pit_1_room_nr = 0
bottomless_pit_2_room_nr = 0
wumpus_room_nr = 0


def intro():
    print("")
    print("Welcome to hunt the WUMPUS")
    print("The WUMPUS lives in a cave of 20 rooms.")
    print("Each room has 3 tunnels leading to other rooms.")
    print("")
    print("You can smell the WUMPUS from 2 rooms away")
    print("There are 2 caves with SUPERBATS, they lift you up and drop you in another room.")
    print("You will feel a draft in a room next to the bottomless pit.")
    print("")


def initialize():
    random.seed()
    
    global player_room_nr
    global bat_1_room_nr
    global bat_2_room_nr
    global bottomless_pit_1_room_nr
    global bottomless_pit_2_room_nr
    global wumpus_room_nr

    player_room_nr = random.randint(0, 19)

    bat_1_room_nr = random.randint(0, 19)
    while bat_1_room_nr == player_room_nr:
        bat_1_room_nr = random.randint(0, 19)

    bat_2_room_nr = random.randint(0, 19)
    while bat_2_room_nr == player_room_nr or bat_2_room_nr == bat_1_room_nr:
        bat_2_room_nr = random.randint(0, 19)
    
    bottomless_pit_1_room_nr = random.randint(0,19)
    while bottomless_pit_1_room_nr == player_room_nr or bottomless_pit_1_room_nr == bat_1_room_nr or bottomless_pit_1_room_nr == bat_2_room_nr:
        bottomless_pit_1_room_nr = random.randint(0, 19)

    bottomless_pit_2_room_nr = random.randint(0,19)
    while bottomless_pit_2_room_nr == player_room_nr or bottomless_pit_2_room_nr == bat_1_room_nr or bottomless_pit_2_room_nr == bat_2_room_nr or bottomless_pit_2_room_nr == bottomless_pit_1_room_nr:
        bottomless_pit_2_room_nr = random.randint(0, 19)
    
    wumpus_room_nr = random.randint(0,19)
    while wumpus_room_nr == player_room_nr or wumpus_room_nr == bat_1_room_nr or wumpus_room_nr == bat_2_room_nr or wumpus_room_nr == bottomless_pit_1_room_nr or wumpus_room_nr == bottomless_pit_2_room_nr:
        wumpus_room_nr = random.randint(0, 19)


def report_hazards():
    global player_room_nr
    global bat_1_room_nr
    global bat_2_room_nr
    global bottomless_pit_1_room_nr
    global bottomless_pit_2_room_nr
    global wumpus_room_nr

    if bat_1_room_nr in rooms[player_room_nr] or bat_2_room_nr in rooms[player_room_nr]:
        print("I hear flapping wings!")

    if bottomless_pit_1_room_nr in rooms[player_room_nr] or bottomless_pit_2_room_nr in rooms[player_room_nr]:
        print("I feel a draft!")

    wumpus_nearby = False
    wumpus_adjacent_rooms = rooms[wumpus_room_nr]
    for r in rooms[player_room_nr]:
        if r == wumpus_room_nr or r in wumpus_adjacent_rooms:
            wumpus_nearby = True
            break
    if wumpus_nearby:
        print("I smell a WUMPUS!")


def check_hazards():
    global player_room_nr
    global bat_1_room_nr
    global bat_2_room_nr
    global bottomless_pit_1_room_nr
    global bottomless_pit_2_room_nr
    global wumpus_room_nr

    if player_room_nr == wumpus_room_nr:
        print("")
        print("The WUMPUS has found you.")
        print("The WUMPUS eats you, you are dead.")
        return True

    if player_room_nr == bottomless_pit_1_room_nr or player_room_nr == bottomless_pit_2_room_nr:
        print("")
        print("Aaah! You fall in a bottomless pit.")
        print("You are dead.")
        return True

    if player_room_nr == bat_1_room_nr or player_room_nr == bat_2_room_nr:
        print("")
        print("A group of Superbats lifts you up.")
        time.sleep(3)
        print("The Superbats have dropped you.")
        player_room_nr = random.randint(0,19)
        return False
    
    return False

def next_game():
    while True:
        print("")
        next = input("Do you want to play again? [y/n] ")
        if next == 'y':
            return True
        elif next == 'n':
            print("Thanks for playing.")
            return False
        

def ask_move():
    global player_room_nr

    player_room = rooms[player_room_nr]
    while True:
        next = input("To which room do you want to go? ")
        try:
            next = int(next)-1
        except:
            next is None
        
        if next is None or next not in player_room:
            print(f"Wrong room")
            continue
        else:
            player_room_nr = next
            break

def main():
    global player_room_nr
    
    while True:
        player_room = rooms[player_room_nr]

        print("")
        print(f"You are in room {player_room_nr+1}")
        report_hazards()
        print(f"Tunnels lead to: {player_room[0]+1}, {player_room[1]+1}, {player_room[2]+1}")

        ask_move()
        end = check_hazards()
        if end:
            next = next_game()
            if next:
                initialize()
            else:
                break


if __name__ == "__main__":
    intro()
    initialize()
    main()

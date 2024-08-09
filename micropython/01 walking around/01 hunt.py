import random
import time

import hunt_serial

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
    player_room_nr = random.randint(0, 19)

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
        print(f"Tunnels lead to: {player_room[0]+1}, {player_room[1]+1}, {player_room[2]+1}")

        ask_move()


if __name__ == "__main__":
    intro()
    initialize()
    main()

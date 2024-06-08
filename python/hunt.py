import random
import time


rooms = [
    [2, 8, 14],  #   0
    [7, 13, 19],  #   1
    [12, 18, 0],  #   2
    [16, 17, 19],  #   3
    [11, 14, 18],  #   4
    [13, 15, 18],  #   5
    [9, 14, 16],  #   6
    [1, 15, 17],  #   7
    [0, 10, 16],  #   8
    [6, 11, 19],  #   9
    [8, 12, 17],  #  10
    [4, 9, 13],  #  11
    [2, 10, 15],  #  12
    [1, 5, 11],  #  13
    [0, 4, 6],  #  14
    [5, 7, 12],  #  15
    [3, 6, 8],  #  16
    [3, 7, 10],  #  17
    [2, 4, 5],  #  18
    [1, 3, 9],  #  19
]



player_room_nr = 0
bat_1_room_nr = 0
bat_2_room_nr = 0
bottomless_pit_1_room_nr = 0
bottomless_pit_2_room_nr = 0
wumpus_room_nr = 0
arrows_remaining = 0


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

def intro_official():
    print("""
The WUMPUS lives in a CAVE of 20 rooms (called caverns in CAVES1, remember?) and the only pleasant
way out is to shoot it with one of your arrows - you get 5 to start with.  But watch out - if you fall into a
Bottomless Pit (there are two), you lose.

Two other caverns have swarms of Super Bats.  If you wander there, unpredictable things will happen
- they like to fly away with people and drop them elsewhereville, like another cavern way over on
the other side of the WUMPUS CAVES.  Makes mapmaking difficult...

Hey!  Forgot to tell you...  to be fair, you'll get warnings: if you are one cavern away from the WUMPUS,
you'll read

               I SMELL A WUMPUS!

and if you're one away from the Bats

               BATS NEARBY!

but watch out for

               I FEEL A DRAFT

'cause one false step and you've found a Bottomless Pit!

Be careful when you shoot!  An arrow is good for up to 5 rooms and then you lose it.  Make each shot
count!  Also, when you shoot, make sure the rooms you aim at are properly connected.  If the next room you
choose for the arrow's path isn't connected (to the last one), then the arrow goes wild.

You can get shot by your own arrows.  Ouch!

Whenever you shoot an arrow, the WUMPUS wakes up!

You'll also wake him up if you stumble into his room.  When the WUMPUS awakens, he usually moves.  And if he
moves into your room, CHOMP, you get eaten.

Good luck, and keep your map up to date.
          """)

def initialize():
    random.seed()
    
    global player_room_nr
    global bat_1_room_nr
    global bat_2_room_nr
    global bottomless_pit_1_room_nr
    global bottomless_pit_2_room_nr
    global wumpus_room_nr
    global arrows_remaining

    arrows_remaining = 5


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


def next_game():
    while True:
        print("")
        next = input("Do you want to play again? [y/n] ")
        if next == 'y':
            return True
        elif next == 'n':
            print("Thanks for playing.")
            return False


def ask_shoot_or_move():
    while True:
        answer = input("Do you want to move or schoot? [m/s] ")
        if answer == "m":
            return False
        elif answer == "s":
            return True


def ask_room():    
    while True:
        room = input("Which room should your arrow go? [1-20] ")
        try:
            room = int(room)
        except Exception:
            room = None
        if room is None or room < 1 or room > 20:
            print("Wrong room")
            continue
        else:
            break
    return room


def ask_shoot():
    global player_room_nr
    global arrows_remaining
    global wumpus_room_nr

    amount = ask_amount()
    arrow_rooms = []
    for _ in range(amount):
        room = ask_room()
        arrow_rooms.append(room)
    
    for i in range(amount):
        arrow_room_nr = player_room_nr
        mapping_correct = True
        if arrow_rooms[i] in rooms[arrow_room_nr] and mapping_correct:
            arrow_room_nr = arrow_rooms[i]
        else:
            if mapping_correct:
                # first time, give a warning to the user of the first wrong room
                print("")
                print(f"This room {arrow_rooms[i]} is not connected, your mapping is wrong, arrow flying in random room.")
                mapping_correct = False
            
            arrow_room_nr = random.choice(rooms[arrow_room_nr])

        if arrow_room_nr == wumpus_room_nr:
            print("")
            print("You killed the WUMPUS!")
            return True
        
        if arrow_room_nr == player_room_nr:
            print("")
            print("Your arrow killed yourself.")
            return True
    
    arrows_remaining -= 1
    if arrows_remaining <= 0:
        print("You are out of arrows, and the WUMPUS is still alive, it will eat you eventually.")
        return True
    
    print("")
    print("Your arrow woke The WUMPUS and it is moving around.")
    time.sleep(3)
    wumpus_room_nr = random.randint(0,19)
    while wumpus_room_nr == bat_1_room_nr or wumpus_room_nr == bat_2_room_nr or wumpus_room_nr == bottomless_pit_1_room_nr or wumpus_room_nr == bottomless_pit_2_room_nr:
        wumpus_room_nr = random.randint(0, 19)
    
    if wumpus_room_nr == player_room_nr:
        print("")
        print("The WUMPUS stumbled into your room, ")
        print("The WUMPUS eats you, you are dead.")
        return True


    return False


def ask_amount():    
    while True:
        amount = input("How many rooms do you want to shoot? [1-5] ")
        try:
            amount = int(amount)
        except Exception:
            amount = None
        if amount is None or amount < 1 or amount > 5:
            print("Wrong amount")
            continue
        else:
            break
    return amount


def main():
    global player_room_nr
    
    while True:
        player_room = rooms[player_room_nr]

        print("")
        print(f"You are in room {player_room_nr+1}")
        report_hazards()
        print(f"Tunnels lead to: {player_room[0]+1}, {player_room[1]+1}, {player_room[2]+1}")

        shoot = ask_shoot_or_move()
        if shoot:
            end = ask_shoot()
        else:
            ask_move()
            end = check_hazards()
        if end:
            end = next_game()
            if end:
                initialize()
            else:
                break


if __name__ == "__main__":
    # intro_official()
    intro()
    initialize()
    main()

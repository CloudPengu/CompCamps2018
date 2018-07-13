import location, player, item, enemy
import random
from datetime import datetime

seed = input("Enter a seed: ")

tile = location.Location(seed + "0,0")

user = player.Player(input("You have entered a verson of hell, What is your name travler: "))

x = 0
y = 0
tiles = {}
searched_tiles = []

def move (direction):
    global x, y
    if direction == "n":
        y += 1
    elif direction == "e":
        x += 1
    elif direction == "s":
        y -= 1
    elif direction == "w":
        x -= 1
    key = "{},{}".format(x, y)
    if key in tiles:
        return tiles [key]
    else:
        newtile = location.Location(seed + key)
        tiles[key] = newtile
        return newtile

running = True
while running and user.isAlive():
    print("You've teleported to {}".format(tile.name))
    if tile.enemy and tile.enemy.isAlive():
        print("Enemy nearby, this certain enemy as {} health".format(tile.enemy.health))
    command = input("> ")
    if command == "items":
        if user.inventory:
            print("You have: {}".format(user.getItems()))
        else:
            print("You have no items")
    elif command == "move":
        direction = input("N/E/S/W > ")[0].lower()
        if direction == "n":
            print ("Go North")
            tile = move ("n")
        elif direction == "e":
            print ("Go East")
            tile = move ("e")
        elif direction == "s":
            print ("Go South")
            tile = move ("s")
        elif direction == "w":
            print ("Go West")
            tile = move ("w")
        else:
            print ("Moving cancelled")
    elif command == "search":
        if tile.seed in searched_tiles:
            print("Greedy, you've already got everything here")
            continue
        random.seed(seed + str(x) + str(y))
        if random.randint(1, 5) == 1:
            print ("Wow, you lucky duck. You found a thing ÒwÓ")
            user.addItem(item.getRandomItem())
            searched_tiles.append(tile.seed)

        else:
            print ("Haha Lmao, You suck. You didn't find anything")
            searched_tiles.append(tile.seed)
    elif command == "fight":
        random.seed(datetime.now())
        while tile.enemy.isAlive() and user.isAlive():
            print("You have {} health!".format(user.health))
            command = input ("FIGHT CLUB > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    print ("You have punched someone, how rude")
                    tile.enemy.health -= 3
                else:
                    print("HAHA YOU CAN'T PUNCH")
            elif command == "curb stomp":
                if random.randint(1,5) == 1:
                    print("YOU CURB STOMPED SOMEONE, WHAT A MONSTER (You did a lot of damage though)")
                    tile.enemy.health -= 10
                else:
                    print ("You missed, just stop")
            if tile.enemy.health > 0:
                user.health -= tile.enemy.damage
        print("You have killed an innocent person")
    elif command.startswith("heal"):
        _, item = command.split (" ", 1)
        if user.hasItem(item):
            print("You have used {}".format(item))
            user.use(item)
            user.removeItem(item)
        else:
            print("You don't have {} you tard".format(item))
        if user.hasItem("Anti-Depressants"):
            print("You have chugged the bottle of Anti-Depressants")
            user.health += 10
            user.removeItem("Anti-Depressants")
        else:
            print("You have no healing supplies")

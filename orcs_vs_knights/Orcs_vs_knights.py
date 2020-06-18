import random


knights = ("knight1","knight2","knight3" )
orcs =  ("orc1","orc2","orc3")

knight1_health = 15
knight2_health = 25
knight3_health = 30
orc1_health = 19
orc2_health = 34
orc3_health = 17

steps = 0

while True:
    turn = random.randint(0,1)
    if turn:
        element = random.choice(knights)
        if element == "knight1":
            knight1_health -= 2
        if element == "knight2":
            knight2_health -= 2
        if element == "knight3":
            knight3_health -= 2
        if (not knight1_health or not knight2_health or not knight3_health):
            print("Orcs win!")
            break
        print(str(knight1_health)+"knight1_health",
        str(knight2_health)+"knight2_health",
        str(knight3_health)+"knight3_health",
        str(orc1_health)+"orc1_health",
        str(orc2_health)+"orc2_health",
        str(orc3_health)+"orc3_health")

    if not turn:
        element = random.choice(orcs)
        if element == "orc1":
            orc1_health -= 2
        if element == "orc2":
            orc2_health -= 2
        if element == "orc3":
            orc3_health -= 2
        if (not orc1_health or not orc2_health or not orc3_health):
            print("Knights win!")
            break
        print(str(knight1_health) + "knight1_health",
        str(knight2_health) + "knight2_health",
        str(knight3_health) + "knight3_health",
        str(orc1_health) + "orc1_health",
        str(orc2_health) + "orc2_health",
        str(orc3_health) + "orc3_health")

    steps += 1
    print("steps",steps)
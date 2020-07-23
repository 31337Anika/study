import random


knights = ["knight1","knight2","knight3"]
orcs =  ["orc1","orc2","orc3"]

knight1_health = 15
knight2_health = 25
knight3_health = 30
orc1_health = 19
orc2_health = 34
orc3_health = 17

knight1_power = 1
knight2_power = 2
knight3_power = 3
orc1_power = 1
orc2_power = 2
orc3_power = 3

steps = 0

while True:
    turn = random.randint(0,1)
    if turn:
        element = random.choice(knights)
        attack = random.choice(orcs)

        if attack == "orc1":
            if element == "knight1":
                knight1_health -= orc1_power
                if knight1_health <= 0:
                    knights.remove("knight1")
            if element == "knight2":
                knight2_health -= orc1_power
                if knight2_health <= 0:
                    knights.remove("knight2")
            if element == "knight3":
                knight3_health -= orc1_power
                if knight3_health <= 0:
                    knights.remove("knight3")

        elif attack == "orc2":

            if element == "knight1":
                knight1_health -= orc2_power
                if knight1_health <= 0:
                    knights.remove("knight1")
            if element == "knight2":
                knight2_health -= orc2_power
                if knight2_health <= 0:
                    knights.remove("knight2")
            if element == "knight3":
                knight3_health -= orc3_power
                if knight3_health <= 0:
                    knights.remove("knight3")




        elif attack == "orc3":

            if element == "knight1":
                knight1_health -= orc3_power
                if knight1_health <= 0:
                    knights.remove("knight1")
            if element == "knight2":
                knight2_health -= orc3_power
                if knight2_health <= 0:
                    knights.remove("knight2")
            if element == "knight3":
                knight3_health -= orc3_power
                if knight3_health <= 0:
                    knights.remove("knight3")


        if not len(knights):
            print("Orcs win!")
            exit()


        print(str(knight1_health)+"Knight1_health",
        str(knight2_health)+"knight2_health",
        str(knight3_health)+"knight3_health",
        str(orc1_health)+"orc1_health",
        str(orc2_health)+"orc2_health",
        str(orc3_health)+"orc3_health")

    if not turn:
        element = random.choice(orcs)

        attack = random.choice(knights)
        if attack == "knight1":

            if element == "orc1":
                orc1_health -= knight1_power
                if orc1_health <= 0:
                    orcs.remove("orc1")
            if element == "orc2":
                orc2_health -= knight1_power
                if orc2_health <= 0:
                    orcs.remove("orc2")
            if element == "orc3":
                orc3_health -= knight1_power
                if orc3_health <= 0:
                    orcs.remove("orc3")

        if attack == "knight2":

            if element == "orc1":
                orc1_health -= knight2_power
                if orc1_health <= 0:
                    orcs.remove("orc1")
            if element == "orc2":
                orc2_health -= knight2_power
                if orc2_health <= 0:
                    orcs.remove("orc2")
            if element == "orc3":
                orc3_health -= knight2_power
                if orc3_health <= 0:
                    orcs.remove("orc3")

        if attack == "knight3":

            if element == "orc1":
                orc1_health -= knight3_power
                if orc1_health <= 0:
                    orcs.remove("orc1")
            if element == "orc2":
                orc2_health -= knight3_power
                if orc2_health <= 0:
                    orcs.remove("orc2")
            if element == "orc3":
                orc3_health -= knight3_power
                if orc3_health <= 0:
                    orcs.remove("orc3")




        if not len(orcs):
            print("Knights win!")
            exit()


        print(str(knight1_health) + " - knight1_health;",
        str(knight2_health) + " - knight2_health;",
        str(knight3_health) + " - knight3_health;",
        str(orc1_health) + " - orc1_health;",
        str(orc2_health) + " - orc2_health;",
        str(orc3_health) + " - orc3_health;")

    steps += 1
    print("steps",steps)
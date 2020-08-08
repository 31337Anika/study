import random, shelve


name_player = input("введите имя: ")

steps = 0
comp = 3
player = 3

comp_elements = {"comp_head" : True, "comp_body" : True, "comp_legs" : True}
player_elements = {"player_head" : True, "player_body" : True, "player_legs" : True}

while comp and player:
    turn = random.randint(0,1)
    if turn:
        comp_choice = random.choice(list(comp_elements.keys()))
        new_comp_element = {comp_choice: False}
        comp_elements.update(new_comp_element)
        player_choice_of_attack = input("Time to attack! What would you like to kick? Head - 1, body - 2, legs - 3")
        if player_choice_of_attack == "1":
            if comp_elements["comp_head"]:
                comp -= 1
        if player_choice_of_attack == "2":
            if comp_elements["comp_head"]:
                comp -= 1
        if player_choice_of_attack == "3":
            if comp_elements["comp_head"]:
                comp -= 1

    else:
        player_choice_of_block = input("It's your time to defence! What would you like to block? Head - 1, body - 2, legs - 3")
        if player_choice_of_block == "1":
            new_player_element = {"player_head" : False}
            player_elements.update(new_player_element)
        if player_choice_of_block == "2":
            new_player_element = {"player_body" : False}
            player_elements.update(new_player_element)
        if player_choice_of_block == "3":
            new_player_element = {"player_legs" : False}
            player_elements.update(new_player_element)

        comp_choice = random.choice(list(player_elements.keys()))

        if player_elements[comp_choice]:
            player -= 1

    comp_elements = {"comp_head": True, "comp_body": True, "comp_legs": True}
    player_elements = {"player_head": True, "player_body": True, "player_legs": True}

    steps += 1
    print("player health is ",player,"comp health is ",comp)
    print("comp_elements - ",comp_elements,"\n","player_elements - ",player_elements)

if comp:
    print("Computer is winner! Haha")
else:
    records = shelve.open("records")
    records.sync()
    if "records" in records:
        current_record = records["records"]
        key = list(current_record)[0]
        current_steps = current_record[key]
        print("Your score is ",steps, ". Current champion defeated computer in ",current_steps)
        if current_steps > steps:
            records["records"] = {name_player : steps}
            records.sync()
            print("You are new champions, your score is ",steps)
    else:
        records["records"] = {name_player: steps}
        records.sync()
        print("You are new champion, your score is ", steps)

    records.close()
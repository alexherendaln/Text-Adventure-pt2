#a dictionary is like a variable with sub categories which you can filter through, this dict room_info's first subgategory is the different rooms so we can go to each room and check the subcategories and their values.
# so if you were to print out jsut the room_info dict it would show all the infor in it including the subcategories and their values, you can narrow it down by using square brackets fx. print(room_info[0]) which will then only show the values in the first room.
#in this case we fx use the same subcategories in each one so we can structure it like this: print(room_info[current_room][entrance_txt]) to print the entrance_txt no matter what room we are in.
#we do also have arrays in this where there are mutiple "variables" in one subkategory fx "searchables" where they are also given a corresponding value.

room_info = {
    0: {
        "entrance_txt": "You are in the starter room. You see a dead body, and an entrance to the outside, type 'help' to get a kick start",
        "searchables": {"fireplace":0, "cellphone": 1, "dead_body":2, "blood_pool":3, "rubbish":4, "furniture": 5},
        "talks": {},
        "exits": {"outside":1}
    },
    1: {
        "entrance_txt": "you are outside and there's 3 people, his neighbor, his ex, his friend, and a homeless man",
        "searchables": {},
        "talks":{"neighbor":0,"ex":1,"friend":2,"homeless man":3},
        "exits": {"inside":0, "outside policestation":2}
    },
    2:  {
        "entrance_txt": "You've made your way to the front of the police station. There's 2 police officers outside, Doakes and Dexter",
        "searchables": {},
        "talks":{"Doakes":0,"Dexter":1},
        "exits": {"outside apartment":1, "inside policestation":3}
    },
    3:  {
        "entrance_txt": "You're inside the police station now, and you see the Police Chief. There is a large desk where you can place the evidence you've collected.",
        "searchables": {},
        "talks":{"Police Chief":0},
        "exits": {"outside police station":2}
    },

    }

#a simpler dictionary is like this one where instead of having many variables just lying around called item_1 we can bunch them into a dictionary
#and give them values so we can call them like this: print(items_info[2]) which can be useful 
#if you are to use another variable as a number like this: " print(items_info[variable_number]) " which wouldnt be posible using many variables like item_1 cant just be written item_variable_number.

items_info = {
    0 : "the fire is burning and a gun in the flames, you scoop it out",
    1 : "A cell phone with the last call to his ex",
    2 : "You find a bullet after a deep search",
    3 : "Test blood to identify body",
    4 : "Extra large (used) condom, most likely used for a hooker",
    5 : "You found nothing, or maybe you didn't search deep enough"
}    

# map searchable object keys to the item name that should be added to inventory
items_lookup = {
    "blood_pool": "Blood sample",
    "fireplace": "Gun",
    "cellphone": "Cellphone",
    "dead_body": "Bullet",
    "rubbish": "Used condom",
    "furniture": "A crisp 5 dolla dolla bill",
}

npc_convo = {
    "neighbor": { 
        "inputs":{
            0 : "What did you think of the victim?",
            1 : "What were you doing the other day?",
            2 : "What do you know about the victims best friend?",
        },
        "outputs":{
            0 : "He was noisy and annoying",
            1 : "I was at home watering my plants",
            2 : "They were in a fight about a few months ago"
        },
    },
    "friend": {
        "inputs":{
            0: "What were your relation to him?",
            1: "Do you ever think he was anoying, or irritating?",
        },
        "outputs":{
            0: "We've been really good friends for a long time, but since we became older we haven't talked that much",
            1: "We had a pretty big argument a few months ago, but no, not necessarily"
        },
    },
    "ex": {
        "inputs":{
            0: "When did you two break up, and was it hard?",
            1: "How well do you know him, and for how long?",
            2: "Have either one of you tried getting back with the other?",
        },
        "outputs":{
            0: "We broke up about 6 months because i cheated on him with his friend. I think it was a bit hard for him, but he got over it i guess",
            1: "we've known each other for like 7 years in highschool. We was like the cute couple everyone dreamt of being, but it just got bored at the end",
            2: "He tried asking me out on a date like a month or two ago, but i rejected his little pity ass"
        }
    },
    "homeless man":{
        "inputs":{
            0: "Do you know the guy that got killed?",
            1: "Did you see or hear anything that could've led to his death?",
            2: "Why the hell are you naked?",
        },
        "outputs":{
            0: "You provoked the man, and he stabbed you to death",
            1: "You provoked the man, and he stabbed you to death",
            2: "You provoked the man, and he stabbed you to death"
        },
    },
    "Doakes": {
        "inputs": {
            0: "Who are you suspicious of?",
            1: "Why you be looking at Dexter like that?",
            2: "Do you think this was a professional job?",
            3: "How long have you been on the force?",
        },
        "outputs": {
            0: "Everyone's a suspect until I say otherwise. But something about this case stinks...",
            1: "That guy gives me the creeps. And i know he is up to something... i just can't prove it",
            2: "Shot with a gun anyone could have done it really.",
            3: "Been on the force for over a decade. Seen all kinds of scum, and I know when something doesn't add up like the weird guy by the van -Dexter-."
        },
    },
    "Dexter": {
        "inputs": {
            0: "What exactly do you do for a living?",
            1: "You seem tense, are you okay?",
            2: "What do you think about Sergeant Doakes?",
            3: "Do you think this done by a professional job?",
        },
        "outputs": {
            0: "I'm a blood spatter analyst. Not really much to special...",
            1: "I'm fine. Just... tired. These cases be making me feel like shit",
            2: "Doakes? He's... persistent. Always watching me like I'm hiding something.",
            3: "Yeah i dont know, not my area of specialty to answer if it was a pro that did it ask Doakes he would know",
            4: "Oh yeah i can help, give me a minute...... and here i got it, it seems its someone on the police database who did this, but its blocked somehow, like someone doesnt want to be found out."
        },
    }
}

def show_inventory():
    print("-----------------------------------------------------")
    print("You have the following items in your inventory:")
    print("-----------------------------------------------------")
    if not inventory:
        print("- (empty)")
        print("-----------------------------------------------------")
        return
    for it in inventory:
            print(f"- {it}")    
    print("-----------------------------------------------------")    

# start inventory should be three separate items so they can be checked/appended correctly
# start inventory should be a mutable list so items can be appended
inventory = ["Police badge", "Notebook", "Pen"]

# global notebook storage
notes = []

    # global evidence table storage
evidence_table = []

blood_collected = 0


REQUIRED_EVIDENCE = {
        "Gun",
        "Cellphone",
        "Bullet",
        "Blood sample",
        "Used condom"
    }

if set(evidence_table) == REQUIRED_EVIDENCE:
        print("\nThe Inspector looks at the fully assembled evidence...")
        print("He stares at you after having looked at the evidence")
        print("\n'Well...', he whispers. 'You actually figured it out.'")
        print("'That's a problem for me, detective.'")
        print("\nHe reaches inside his coat and before you could even react...")
        print("Kaplamo! he fires a shot")
        print("\nYou fall as your visionn fades black")
        print("\n 🥀🥀😭 GAME OVER — The Police Chief was the killer now you dead")
        quit()

def look(current_room):
    global blood_collected
    """Allows the player to search objects in the current room"""
    room = room_info[current_room]

    if not room["searchables"]:
        print("-----------------------------------------------------")
        print("There's nothing to search here.")
        print("-----------------------------------------------------")
        return
    
    while True:
        print("-----------------------------------------------------")
        print("You can search the following objects:")
        print("-----------------------------------------------------")
        for item in room["searchables"]:
            print(f"- {item}")

        print("-----------------------------------------------------")
        print("What do you want to search? (or type 'leave' to stop searching)")
        print("-----------------------------------------------------")
        raw = input(">")
        if raw.strip().lower() == "quit":
            quit()
        choice = raw.strip().lower()

        if choice == "leave":
            print("-----------------------------------------------------")
            print("You stop searching.")
            print("-----------------------------------------------------")
            return
        elif choice in room["searchables"]:
            item_id = room["searchables"][choice]
            print("-----------------------------------------------------")
            print(f"You search the {choice}...")
            print("-----------------------------------------------------")
            print(items_info[item_id])
            print("-----------------------------------------------------")

            # determine if this searchable yields an actual item to add
            item_name = items_lookup.get(choice)
            if item_name:
                if item_name not in inventory:
                    inventory.append(item_name)
                    print("You added it to your inventory.")
                    print("-----------------------------------------------------")
                else:
                    print("You already have that item in your inventory.")
                    print("-----------------------------------------------------")
            else:
                print("You didn't find any usable item.")
                print("-----------------------------------------------------")

            return  # stop after one search
        else:
            print("-----------------------------------------------------")
            print("You can't search that here.")
            print("-----------------------------------------------------")
            
def place_evidence(current_room):
    if current_room != 4:
        print("You need to be in the office of the inspector to place evidence.")
        print("-----------------------------------------------------")
        return
    
    valid_evidence = [item for item in inventory if item != "Police badge"]
    if not valid_evidence:
        print("-----------------------------------------------------")
        print("You have no evidence to place")
        print("-----------------------------------------------------")
        return
    print("-----------------------------------------------------")
    print("You can place the following evidences items on da table:")
    print("-----------------------------------------------------")
    for i, item in enumerate(valid_evidence):
        print(f"{i}: {item}")
        print("-----------------------------------------------------")
        print("which evidence do you want to place?(or type 'Leave' to cancel)")
        print("-----------------------------------------------------")
        choice = input(">").strip().lower()
        if choice == "Leave":
            print("-----------------------------------------------------")
            print("You decided not to place anything")
            print("-----------------------------------------------------")
            return
        if not choice.isdigit() or int(choice) >= len(valid_evidence):
            print("-----------------------------------------------------")
            print("Invalid choice.")
            print("-----------------------------------------------------")
            return
        item_to_place = valid_evidence[int(choice)]
        if item_to_place in inventory:
            print("-----------------------------------------------------")
            print("You have already placed that item.")
            print("-----------------------------------------------------")
            return
        evidence_table.append(item_to_place)
        print("-----------------------------------------------------")
        print(f"You place {item_to_place} on the Inspector's desk.")
        print("-----------------------------------------------------")
        if len(evidence_table) == 3:
            print("\nThe Inspector reviews the evidence carefully...")
            print("'This could be enough evidence to crack the case'he says.\n")
            print("-----------------------------------------------------")
        

def move(current_room):

    #a loop that continues until we either get a valid answer or a leave
    while True:
        # show available exits for the current room
        exits = room_info[current_room]["exits"]
        print("-----------------------------------------------------")
        print("You can go to the following places:")
        print("-----------------------------------------------------")
        for place in exits:
            print(f"- {place}")

        print("-----------------------------------------------------")
        print("Direction? (type 'leave' to stay in the same place)")
        print("-----------------------------------------------------")
        raw = input(">").strip()
        if raw.lower() == "quit":
            quit()
        direction = raw.lower()

        #checks if the given input is in the current room's exits
        if direction in exits:
            return exits[direction]
        elif direction == "leave":
            return None
        else:
            # if this direction exists somewhere in the game but not from here,
            # inform the player that the location isn't unlocked from this room
            all_exits = set()
            for room in room_info.values():
                all_exits.update(room.get("exits", {}).keys())
            if direction in all_exits:
                print("-----------------------------------------------------")
                print("this location hasn't been unlocked yet... Or maybe unlocked???")
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("not a direction")
                print("-----------------------------------------------------")
            continue

def print_inputs(person):
    #using the counter we can progresively show each line and at the same time print what number each line is
    counter = 0
    #repeats the print for each row there is in the dict's subcategory, given how different NPC's have differing amounts of options.
    for row in npc_convo[person]["inputs"]:
        print(f"{counter}   {npc_convo[person]["inputs"][counter]}")
        counter += 1

def conversation(person):
    #a loop that continues until we either get a valid answer or a leave
    while True:
        #uses the function print_inputs to display each line ofr itself instead of just using print(npc_convo[person]["inputs"]) which would print it all at once and not clearly represent what number each input is.
        print("-----------------------------------------------------")
        print_inputs(person)
        if person == "Dexter" and "Blood sample" in inventory:
            print("4   Can you help me with analysing this blood?")

        print("-----------------------------------------------------")
        print('"leave" to leave the conversation')
        print("-----------------------------------------------------")
        raw = input(">")
        if raw.strip().lower() == "quit":
            quit()
        input_sentence = raw.strip()

        if input_sentence == 4 and "Blood sample" in inventory and person == "Dexter":
            print("-----------------------------------------------------")
            print(npc_convo[person]["outputs"][int(input_sentence)])
            print("-----------------------------------------------------")
        #This time it checks if the value given (now a number using int() to make the input a number) to check if that response is 
        #in the npc_convo dictionary's subkatogory of the perons input like we did for the movement this time just a number so you dont have to type out the entire question.
        if input_sentence == "leave":
            print("-----------------------------------------------------")
            print(f"You left {person} for themselves\n")
            print("-----------------------------------------------------")
            return
        if int(input_sentence) in npc_convo[person]["inputs"]:
            #to remind who were talking to and clearly state what the answer was
            print("-----------------------------------------------------")
            print(f"{person} answers:")
            print("-----------------------------------------------------")
            #this prints the output of the specific person given the input. 
            print (npc_convo[person]["outputs"][int(input_sentence)])
            print("-----------------------------------------------------")
            if person == "homeless man" and "you provoked the man" in npc_convo[person]["outputs"][int(input_sentence)].lower():
                print("Wow, you really suck at this detective thing. Games over.")
                print("-----------------------------------------------------")
                quit()
            #prints to empty lines for aesthetics
        else:
            print("-----------------------------------------------------")
            print("not an input")
            print("-----------------------------------------------------")
            continue

def talk_to_person(current_room):

    #a loop that continues until we either get a valid answer or a leave
    while True:
        print("-----------------------------------------------------")
        print("Who do you want to talk to?")
        print("-----------------------------------------------------")
        raw = input(">")
        if raw.strip().lower() == "quit":
            quit()
        person = raw  # keep the original casing as the code expects exact keys
        
        #checks if the given input is in the current rooms array of "talks"
        if person in room_info[current_room]["talks"]:
            #if so runs the function "conversation" using a specific characters name, the room not needed anymore.
            conversation(person)
            return 
        elif person == "leave":
            return
        else:
            print("-----------------------------------------------------")
            print("not a person")
            print("-----------------------------------------------------")
            continue

def notebook():
    """Interactive notebook where players can add, edit, delete, and view notes."""
    print("-----------------------------------------------------")
    print("\n--- NOTEBOOK ---")
    print("Press Enter with empty input to exit.\n")
    print("-----------------------------------------------------")
    
    while True:
        print("\nNOTEBOOK MENU:")
        print("-----------------------------------------------------")
        print("1. View notes")
        print("2. Add note")
        print("3. Edit note")
        print("4. Delete note")
        print("(Press Enter to exit)")
        print("-----------------------------------------------------")
        
        raw = input("> ").strip()
        
        # Exit if empty input
        if raw == "":
            print("-----------------------------------------------------")
            print("Exiting notebook.\n")
            print("-----------------------------------------------------")
            return
        
        if raw.lower() == "quit":
            quit()
        
        choice = raw.lower()
        
        if choice == "1":
            # View notes
            if not notes:
                print("-----------------------------------------------------")
                print("\nYou have no notes yet.")
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("\n--- YOUR NOTES ---")
                print("-----------------------------------------------------")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
                print("-----------------------------------------------------")
        
        elif choice == "2":
            # Add note
            print("-----------------------------------------------------")
            note_text = input("Write your note: ").strip()
            if note_text:
                notes.append(note_text)
                print("-----------------------------------------------------")
                print(f"Note added: '{note_text}'")
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("No note was written.")
                print("-----------------------------------------------------")
        
        elif choice == "3":
            # Edit note
            if not notes:
                print("-----------------------------------------------------")
                print("\nYou have no notes to edit.")
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("\n--- YOUR NOTES ---")
                print("-----------------------------------------------------")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
                print("-----------------------------------------------------")
                
                note_choice = input("Which note do you want to edit? (number): ").strip()
                if note_choice.isdigit():
                    note_index = int(note_choice) - 1
                    if 0 <= note_index < len(notes):
                        new_text = input("Write the new text: ").strip()
                        if new_text:
                            old_text = notes[note_index]
                            notes[note_index] = new_text
                            print("-----------------------------------------------------")
                            print(f"Note updated from '{old_text}' to '{new_text}'")
                            print("-----------------------------------------------------")
                        else:
                            print("-----------------------------------------------------")
                            print("No new text was written.")
                            print("-----------------------------------------------------")
                    else:
                        print("-----------------------------------------------------")
                        print("Invalid note number.")
                        print("-----------------------------------------------------")
                else:
                    print("-----------------------------------------------------")
                    print("Please enter a valid number.")
                    print("-----------------------------------------------------")
        
        elif choice == "4":
            # Delete note
            if not notes:
                print("-----------------------------------------------------")
                print("\nYou have no notes to delete.")
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("\n--- YOUR NOTES ---")
                print("-----------------------------------------------------")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
                print("-----------------------------------------------------")
                
                note_choice = input("Which note do you want to delete? (number): ").strip()
                if note_choice.isdigit():
                    note_index = int(note_choice) - 1
                    if 0 <= note_index < len(notes):
                        deleted_note = notes.pop(note_index)
                        print("-----------------------------------------------------")
                        print(f"Note deleted: '{deleted_note}'")
                        print("-----------------------------------------------------")
                    else:
                        print("-----------------------------------------------------")
                        print("Invalid note number.")
                        print("-----------------------------------------------------")
                else:
                    print("-----------------------------------------------------")
                    print("Please enter a valid number.")
                    print("-----------------------------------------------------")
        
        else:
            print("-----------------------------------------------------")
            print("I do not understand that command.")
            print("-----------------------------------------------------")

### The main game loop ###

def help(current_room):
    #Displays help information to the player.
    print("---Available commands---")
    print("-----------------------------------------------------")
    print("move: Move to a different location.")
    print("-----------------------------------------------------")
    print("search: Search the current location for items.")
    print("-----------------------------------------------------")
    print("notebook: Open your notebook to view/add/edit notes.")
    print("-----------------------------------------------------")
    print("talk: Talk to people in the current location.")
    print("-----------------------------------------------------")
    print("help: Show this help message.")
    print("-----------------------------------------------------")
    print("quit: Exit the game.")
    print("-----------------------------------------------------")
    print("inventory: Show your current inventory.")
    print("-----------------------------------------------------")
    exits = room_info.get(current_room, {}).get("exits", {})
    if exits:
            print("Exits from this room:")
            for exit_name in exits:
                print(f"- {exit_name}")
                print("-----------------------------------------------------")
    else:
            print("\nThere are no exits from this room.")

def game_loop():
    """Main loop of the game - this is where the fun happens."""

    # We start in room 0
    current_room = 0

    # Display the room that we start in
    print("-----------------------------------------------------")
    print(room_info[current_room]["entrance_txt"])
    print("-----------------------------------------------------")
    # Enter the main loop, where the user can input commands.
    while True:
        raw = input("\n> ").strip()
        print()  # Add blank line after user input
        if not raw:
            continue

        lower_raw = raw.lower()

        # Ignore common runner/terminal echoes that VSCode or the shell may send when pressing Run
        ignore_substrings = ("python", ".py", "c:", "c:/", "c\\", "&", "run", "ps ", "powershell")
        if any(substr in lower_raw for substr in ignore_substrings):
            continue
        if lower_raw.startswith(("&", "cd ", "set ")):
            continue

        cmd = lower_raw

        if cmd == "quit":
            break

        elif cmd == "search":
            look(current_room)
            continue

        elif cmd == "move":
            new_room = move(current_room)
            # move returns None when player types 'leave' -> stay in same room
            if new_room is None:
                continue
            # protect against invalid room values
            if new_room in room_info:
                current_room = new_room
                print("-----------------------------------------------------")
                print(room_info[current_room]["entrance_txt"])
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("You can't go that way.")
                print("-----------------------------------------------------")
            continue

        elif cmd == "talk":
            # Prevent talking in room 0
            if current_room == 0:
                print("-----------------------------------------------------")
                print("There is no one to talk to here.")
                print("-----------------------------------------------------")
                continue
            talk_to_person(current_room)
            continue

        elif cmd == "help":
            help(current_room)
            continue

        elif cmd == "inventory":
            show_inventory()
            continue
        elif cmd == "place evidence":
            place_evidence(current_room)

        elif cmd == "notebook":
            notebook()
            continue

        else:
            print("-----------------------------------------------------")
            print("I do not understand the command:", raw)
            print("-----------------------------------------------------")

# Start the game!

game_loop()

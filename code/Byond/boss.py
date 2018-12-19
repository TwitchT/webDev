from sys import exit

def Boss_room():
    print("This room is cold and dim. Smells like rotten meat and dead bodies. You see a dead knight in front of your feet with an axe jamed into his ribs.")
    print("The door closes behind you and locks. You look around and see a 4 leged and 4 armed 39 feet tall Pop-Corn machine! With a mouth the size of a bear, with curnals for eyes.")
    
    choice = input("> ")
    Boss = True
    axe = False
    ignis = True
    spear = True
    bomb = True
    spark = True
    sword = True
    glasses = True
    fire = True
 
    while Boss:
        if "pick up axe" in choice:
            print("taken")
            axe = True
            choice = input("> ")
        if "attack boss" in choice and axe:
            print("You swing the axe and chop of one of its arms. It kicks you to the wall with one of its legs. It takes your axe and swallows it. ")
            axe = False
            choice = input(">")
            
        elif "use ignis" in choice and ignis: 
            print("You throw the fire ball at the monster's eye. It's eye pops into a giant peice of popcorn.")
            ignis = False
            choice = input(">")
            
        elif "use ignis" in choice and ignis and spear == False:
            print("You throw the fire ball at the spot were the spear had struck. The fire burns the monster's open wound, the monster screams in pain. The fire spreads though the monster's organs and...")
            print("The monster explodes into giant popcorn peices and is now dead.")
            ignis = False
            Boss = False
            print("Congrats you WIN. Sadly you cant get out.")
            choice = input(">")
            
        elif "use spark" in choice and spark:
            print("You electricute the monster but its not dead. You only stuned it for about 5 secounds.")
            spark = False
            choice = input(">")
            
        elif "use sword" in choice and sword:
            print("")
            choice = input(">")
            
        elif "use spear" in choice and spear:
            print("You charge the monster with your spear, dodging each one of its arms and legs. You slide under it's belly and as you slide under you throw the spear into its belly.")
            print("The monster screams in pain and pulls out the spear and throws it at you. You some how dodge it. The spear crashes into the floor breaking it, and leaving a giant whole.")
            print("You look in the hole and you see a giant pit of lava at the bottom of the whole.")
            spear = False
            choice = input(">")
            
        elif "use bomb" in choice and bomb and spear:
            print("You throw the bomb at the monster with your perfect timing skills. Th bomb explodes in its face knocking it backwards.")
            bomb = False
            choice = input(">")
            
        elif "use bomb" in choice and bomb and spear == False:
            print("You throw the bomb at the monster with your perfect timing skills. Th bomb explodes in its face knocking it backwards into the pit of lava.")
            print("The monster falls into the lava and is now dead. You start to walk away. But as you are walking away you hear the pit of lava start to rumble.")
            print("You look back towards the big whole and hear a loud BOOM. Pop corn starts to fly out the whole and land on the floor. Congrats you WIN sadly you cant get out")
            bomb = False
            Boss = False
            
        
        elif "use glasses" in choice and glasses and spear == False:
            print("You put on the glasses and nothing happens. You look like a nerd now and the monster kicks you into the pit of lava. You are dead now.")
            glasses = False
            choice = input(">")
            
        elif "use glasses" in choice and glasses:
            print("You put the glasses on and nothing happens. You look like a nerd now. The monster picks you up and throws you to the wall, breaking your glasses.")
            glasses = False
            choice = input(">")
            
        elif "use fire" in choice and fire:
            print("You scream Fire-style Fire-Ball jutsu, but as you are screaming that nonsense the monster sits on you and kills. ")
            print("You are dead now.")
            choice = input(">")
        else:
            print("i dont know what that means")
            choice = input("> ")
            
            
Boss_room()
    
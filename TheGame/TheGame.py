def TheGame():
    print("The Game")
    print("Mom:   Sweetie your coffie is ready.")
    print("Jimbo:   Ok just a secound mom.")
    print("You go down stairs to eat dinner. As you are eating diner you pet your pet bear named Takeo.")
    print("All of a sudden")
    print(" ")
    print("KABBOOOOOOMMMMMMMM!!!!!!!")
    print("A nuke blows up yor whole house. A nuclear war has started and its the end of the world.")
    print("5 days later you wake up.")
    
    choice = input("> ")
    
    rubble = False
    Takeo = False
    Jimbo = True
    skull = True
    
    
    while Jimbo:
        if "go north" in choice and rubble == False:
            print("You stand up from a pile of ruble.")
            choice = input("> ")
            rubble = True 
            
        elif "go north" in choice and rubble:
            print("You hear a whimper")
            Takeo = True
            choice = input("> ")
        
        elif "go south" in choice and rubble == True:
            print("you stand up from a pile of ruble")
            choice = input("> ")
            rubble = False
            
            
        elif "go south" in choice and rubble == False:
            print("You are standing in a pile of rubble")
            choice = input("> ")    
        

        
        elif "go west" in choice and rubble == False:
            print("you stand up from a pile of ruble")
            choice = input("> ")
            rubble = False
            
        elif "go east" in choice and rubble == False:
            print("you stand up from a pile of ruble")
            choice = input("> ")
            rubble = False
            
        elif "go east" in choice and rubble == False:
            print("Crack. You steped in something. You look down and see that you just stepped on your mothers skull. OOOOFFF! You know that its your mothers because she had the same dress on since the nuke hit.")
            skull = False
            choice = input("> ")
            
            
            
            
        else:
            print("Jokes on You, I dont know what that means.")
            choice = input("> ")
            
            
            
            
TheGame()
# Intro
print("You walk into the kitchen for breakfast. ")
print("You have a BIG game in the afternoon. ")
print("")


# choice 1
print("")
c1 = input("Do you choose to eat [chicken and rice] or [a donut and a burger]? ")
if "donut" in c1 or "burger" in c1:
    print("")
    print("You eat a donut and a burger. ")

    #choice 3
    print("")
    print ("Your stomach feels weird but your about to be late for your game! ")
    c3 = input ("Do you go to the [bathroom] or get to the [game] on time? ")
    if "bathroom" in c3:
        print("")
        print("You go to the bathroom but are late for the game. ")

        #choice 4
        print("")
        print("Your coach is really mad at you for being late.")
        c4 = input("Do you [talk back] or [stay quiet]? ")
        if "talk back" in c4 or "be mean" in c4:
            print("")
            print("You get kicked off the team. ")
        else:
            #choice 6
            print("")
            print ("You get to play a little bit in the second half!")
            c6 = input("Do you want to [play hard] or [play slow]? ")
            if"hard" in c6:
                print("")
                print("You play well and win the game but throw up after.")
            else:
                print("")
                print("Your team loses and you play bad. ")
        
    else:
        print("")
        print ("you get to the game on time but your stomach feels really bad. ")

        # choice 5
        print("")
        print("You feel like your about to throw up.")
        c5 = input("Do you ask for a sub or [stay] in the game? ")
        if "stay" in c5:
            print("")
            print("You throw up in the game but keep playing and win the game!")
        else:
            print("")
            print("You finally get out and go to the bathroom but your team loses without you.")

else:
    print("")
    print("You choose to eat chicken and rice... ")


   # choice 2
    print("But the chicken is undercooked! ")
    c2 = input("Do you [eat it], [keep cooking it], or just have [rice]")
    if "eat" in c2:
       print("")
       print ("You ate it and got salmonella :( You cant play todays game. ")
    elif"rice" in c2:
        print("You just have rice and you get there on time and play okay, but the team loses. ")
    else:
       print("")
       print("You cook it perfectly, get to the game on time, and have a really good game. ")
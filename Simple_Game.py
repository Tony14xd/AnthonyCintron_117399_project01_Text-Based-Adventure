import time 
from graphics import*
win = GraphWin('Text_Based_Adventure', 700,800)
win2 = GraphWin('Second Window of Adventure', 600,600)
time.sleep(1)
AnswerA = ["A", "a"]
AnswerB = ["B", "b"]
AnswerC = ["C","c"]
yes = ["yes","Yes"]
no = ["No", "no"]
death = Text(Point(3,4), "You Died")
must = ("\nUse Only A, B, or C\n")
#message3 = Text(Point(350,200),"After your introduction to this world, you enter a bar to monitor"
    #"the environment")
#message3.draw(win)

def option_ask():
    print("The two men look at one another. They begin laughing and this confuses you"
    "They ask you for how long have you been in the Knight Order. You kindly reply with the truth"
    "Just 2 days. The man on the left says: Rookie Numbers. No wonder he has no idea, and"
    "thinks everything is all ice cream and gumdrops. The man of the right coughs with a slight"
    "grin on his face. He says to you: Let me tell you something kid. These streets, this place"
    "your swooorn to protect. Its absolute crap. Theres no justice. You may save someone right now"
    "and they will be greatful sure. But the moment you aint lookin, they surely will be around the corner"
    "stealin from another helpless citizen. And guess what, your knight friends arent"
    "helpin. They get paid by criminals to keep their mouth shut. Look the other way, catch my drift?"
    "Now how about you do the same and look some place else.\n After hearing this you: ")
    time.sleep(1)
    choice = userinput("A. Walk away with helpless after what you heard. B. Grab a drink and sit down with them"
    "and contemplate life. C. Call the other knights and arrest these two men for speaking"
    "ill willed of the Knightly code.")
    if choice in AnswerA:
        message4 = Text(Point(350,320),"\nWell, your a pretty pathetic Knight...Go home and quit.")
    elif choice in AnswerB:
        message5 = Text(Point(350,320),"\nThe two men laugh. The man of the right says: Seems you got good"
        "decision makin' skills kid. Come on, drink our worries away!\n\nYou lost!")
    elif choice in AnswerC:
        option_evil()
    else:
        print(must)



def userinput(message):
    message1 = Text(Point(300,100), message)
    message1.draw(win2)
    inputBox = Entry(Point(300,139), 15)
    inputBox.draw(win2)
    win2.getMouse()
    choice = inputBox.getText()
    inputBox.undraw()
    message1.undraw()
    return choice

def intro():
    message1 = Text(Point(350,70),"Welcome Proud Knight, you have been chosen from a small gifted group of\n"
     " people to join our ranks. You have sworn an oath to protect the Kingdom\n"
     " of RossWell and its people from the maliciousness that dwells\n"
     " within the Kingdom. One must be wary of his surroundings, but as a qualified\n"
     " Knight, you already knew what trouble you would be facing. Now,\n"
     " please tell us your name to begin your journey..!\n")
    message1.draw(win)
    time.sleep(1)
    playername = userinput("Enter Your Name: ")
    message2 = Text(Point(350,180),f"What a powerful name that is! We are proud to have you, {playername},\n Now" 
    "now go out there and show the world what your capable of!\n")
    message2.draw(win)
    print("After your introduction to this world, you enter a bar to monitor"
    "the environment")
    print("You see two men having a discussion. You approach the bartender and buy"
    "a drink to not seem suspiscious. From your current distance you can overhear their"
    "conversation. To your surprise, they are belittling the Knight Order"
    "and the Kingdom who you have sworn to protect. This frustrates you thus, "
    "you approach their table. You are looking at them from above while they are sitting"
    "down enjoying their hard earned alcohol. Do you: ")
    time.sleep(1)
    choice = userinput("A. Politely ask them why they speak in this manner about their Kingdom?\n"
    "B. Angrily bash their table and spill their alcohol, thus ensuing a potential\n"
    "conflict. C. Look at them menacingly.\n")
    if choice in AnswerA:
        option_ask()
    elif choice in AnswerB:
        print("Angry one")
    elif choice in AnswerC:
        message3 = Text(Point(350,300),"What am I? The man on the left replies saying: A Knight?. \nYou"
        "have the biggest smirk on your face behind your helmet and say: You're Goddamn Right.\n"
        "\n\nPretty quick ending but hey, you left the scene pretty cool.\n")
        message3.draw(win)
        win.getMouse()
    else:
        print(must)



def option_evil():
    print("Whats the meaning of this?! Scream the men as they are being taken away from"
    "the bar and headed to the dungeon. As they are being taken away, you reflect on"
    "what the man said, which you believe certainly cannot be true. You follow the knights"
    "taking the prisoners to the dungeon, but just as you were warned, they bribed the two knights to let them"
    "go. This frustrates you but you do nothing. You decide to patrol the town for the rest of the day." 
    "You reach your house and you look for your mother. You shout and shout but can't find her. You"
    "walk toward her door and find that there is a shade of red creeping under the door...It's blood."
    "You smash open the door and find her dead. You see a figure across her body about to leap through the window."
    "It's the man from the bar. Do you pull out your sword? Y/N")
    choice = input(">>> ")
    if choice in yes:
        sword = 1 #adds a sword
    else:
        sword = 0
    print ("\nWhat do you do next?")
    time.sleep(1)
    print ("""  A. Speak with the man
    B. Rush towards him
    C. Stay still due to mothers passing and hate the Knight Order""")
    choice = input(">>> ")
    if choice in AnswerA:
        print ("\nYou....You're him!! You should've been arrested! If you were, this"
        "would never have happened! The man is starts confused but puts the situtation together"
        "Your the kid huh? What did I tell you? This place has no justice. Its a cycle kid."
        "Kinda sucks the fact that it had to be your place I was trying to steal, but I did warn you."
        "How about you let me go huh? Its not like im going to prison anyway. The mans words were filled with"
        "the truth. You knew that it wouldnt change anything if you turned him in again. By the time you made"
        "up a decision he escape.\n\nYou lost her..")
    elif choice in AnswerB:
        if sword > 0:
            print ("\nThere was fire in your eyes. You scream as you sprint towards him. Not a moment wasted as you" 
            "lunge your sword through his chest. Sadly, the neighbors heard the ruckus and you're taken away. Penalty"
            "is death.\n\nYou lose.")
        else: #If the user didn't grab the sword
            print ("\nYou should have taken out your sword. You're "
            "defenseless. \n\nYou died!")
            
    elif choice in AnswerC:
        print ("I hate this.I hate all of this. The man recognizes your voice. He feels sorry for your"
        "weak mind. He takes this opportunity to escape.")
        option_demise()
    else:
        print (must)
        


def option_demise():
    print ("\nYour story has taken a dark turn. (Quit the program if you cant handle hardcore"
    "violence). Your mother whom is all you hold dear has perished thus you have lost the"
    "will to live. You will:")
    time.sleep(1)
    print ("""  A.Stop living
    B. Revenge on the Knight Order
    C. Leave the Kingdom""")
    choice = input(">>> ")
    if choice in AnswerA:
        print ("Not much to say. "
        "\n\nYou died!")
    elif choice in AnswerB:
        print ("\nYou become a wanted killer. You are able to bring into justice the corrupted "
        "Knights by greeting them with death himself. You are later killed by cancer\n\nYou died.")
    elif choice in AnswerC:
        print("You have no way to survive the outside. You are hungry. You eat an venomous apple and slowly die."
        "\n\nYTerrible way to do")
    else:
        print (must)


intro()
# option_demise()
# option_evil()
# option_ask()

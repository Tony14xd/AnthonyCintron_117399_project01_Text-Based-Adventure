from graphics import *
from User_Input import *
from User_choices import *
from Opcion_Demise import *
def close_windows(win,win2,win3):
    win.getMouse()
    win.close()
    win2.close()
    win3.close()

def option_evil(win,win2,win3):
    message8 = Text(Point(360,90), "Whats the meanin' of this?! Scream the men as they are being taken away from\n"
    "the bar and headed to the dungeon. As they are being taken away, you reflect on\n"
    "what the man said, which you believe certainly cannot be true. You follow the knights\n"
    "taking the prisoners to the dungeon, but just as you were warned, they bribed the two knights to let them\n"
    "go. This frustrates you but you do nothing. You decide to patrol the town for the rest of the day.\n" 
    "You reach your house and you look for your mother. You shout and shout but can't find her. You\n"
    "walk toward her door and find that there is a shade of red creeping under the door...It's blood.\n"
    "You smash open the door and find her dead. You see a figure across her body about to leap through the window.\n"
    "It's the man from the bar. Do you pull out your sword? Y/N")
    message8.draw(win3)
    win.close()
    choice = userinput("Do you draw your sword?",win2)
    if choice in yes:
        sword = 1 
    else:
        sword = 0
    message9 = Text(Point(360,200),"What is your next move?")
    message9.draw(win3)
    time.sleep(1)
    choice = userinput("A. Speak with the man B. Rush towards him C. Stay still due to\n"
    " mothers passing and hate the Knight Order",win2)
    if choice in AnswerA:
        message10 = Text(Point(360,300),"\nYou....You're him!! You should've been arrested! If you were, this\n"
        "would never have happened! The man is starts confused but puts the situtation together\n"
        "Your the kid huh? What did I tell you? This place has no justice. Its a cycle kid.\n"
        "Kinda sucks the fact that it had to be your place I was trying to steal, but I did warn you.\n"
        "How about you let me go huh? Its not like im going to prison anyway. The mans words were filled with\n"
        "the truth. You knew that it wouldnt change anything if you turned him in again. By the time you made\n"
        "up a decision he escaped.\n\nYou lost her..You lose")
        message10.draw(win3)
        close_windows(win,win2,win3)

    elif choice in AnswerB:
        if sword > 0:
            message11 = Text(Point(360,310),"\nThere was fire in your eyes. You scream as you sprint towards him.\n Not a moment wasted as you" 
            "lunge your sword through his chest. Sadly, the neighbors heard the ruckus and you're taken away. Penalty"
            "is death.\n\nYou lose.")
            message11.draw(win3)
        else: 
            message12 = Text(Point(360,310),"\nYou should have taken out your sword. You're "
            "defenseless. \n\nYou died!")
            message12.draw(win3)
            close_windows(win,win2,win3)
        
    elif choice in AnswerC:
        message13 = Text(Point(360, 310),"God...I hate this.I hate all of this. The man recognizes your voice. He feels sorry for\n your"
        "weak mind. He takes this opportunity to escape.")
        message13.draw(win3)
        option_demise(win,win2,win3)
    else:
        print(must)
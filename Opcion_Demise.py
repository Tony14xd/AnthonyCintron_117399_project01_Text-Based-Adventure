from graphics import *
def option_demise():
    message14 = Text(Point(360,360),"\nYour story has taken a dark turn. (Quit the program if you cant handle hardcore\n"
    "violence). Your mother whom is all you hold dear has perished thus you have lost the\n"
    "will to live. You will:" )
    message14.draw(win3)
    time.sleep(1)
    choice = userinput2("A.Stop living B. Revenge on the Knight Order C. Leave the Kingdom")
    if choice in AnswerA:
        message15 = Text(Point(360,420),"You know what happened...\n\n Game Over" )
        message15.draw(win3)
    elif choice in AnswerB:
        message16 = Text(Point(360,420),"\nYou become a wanted killer. You are able to bring into justice the corrupted "
        "Knights by greeting them with death himself. You are later killed by cancer\n\nYou died." )
        message16.draw(win3)
    elif choice in AnswerC:
        message17 = Text(Point(360,420),"You have no way to survive the outside. You are hungry. You eat an venomous apple and slowly die."
        "\n\nYTerrible way to do")
        message17.draw(win3)
    else:
        print (must)

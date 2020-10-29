from graphics import *
from User_Input import *
from User_choices import *
from Opcion_mala import *
def option_ask(win,win2):
    message6 = Text(Point(350,505),"The two men look at one another. They begin laughing and this confuses you\n"
    "They ask you for how long have you been in the Knight Order. You kindly reply with the truth\n"
    "Just 2 days. The man on the left says: Rookie Numbers. No wonder he has no idea, and\n"
    "thinks everything is all ice cream and gumdrops. The man of the right coughs with a slight\n"
    "grin on his face. He says to you: Let me tell you somethin' kid. These streets, this place\n"
    "your swooorn to protect. It's absolute crap. There ain't no justice. You may save someone right now,\n"
    "and they will be greatful; sure. But the moment you aint lookin', they surely will be around the corner\n"
    "stealin' from another helpless citizen. And guess what, your knight friends aren't\n"
    "helpin'. They get paid by criminals to keep their mouth shut. Look the other way, catch my drift?\n"
    "Now, how about you do the same and look some place else.\n After hearing this you: ")
    message6.draw(win)
    time.sleep(1)
    choice = userinput("A. Walk away with helpless after what you heard.\n B. Grab a drink and sit down with them"
    " and contemplate life.\n C. Call the other knights and arrest these two men for speaking\n"
    "ill-willed of the Knightly Code.",win2)
    if choice in AnswerA:
        message4 = Text(Point(350,600),"\nWell, your a pretty pathetic Knight...Go home and quit.")
        message4.draw(win)
        win.getMouse()
    elif choice in AnswerB:
        message5 = Text(Point(350,600),"\nThe two men laugh. The man of the right says: Seems you got a good\n"
        "sense of judgement kid. Come on, drink our worries away!\n\nYou lost!")
        message5.draw(win)
        win.getMouse()
    elif choice in AnswerC:
        option_evil(win,win2,GraphWin('Once out of Space on Story', 750,700))
    else:
        print(must)

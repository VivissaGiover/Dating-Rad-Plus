# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.S


define e = Character("Ellie", image = "e")
define j = Character("Jacob", image = "j")
define t = Character("Tyler", image = "t")
define jo = Character("Jo", image = "jo")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    show jo
    jo "Hi im Jo"
    hide jo
    show e
    e "Hi im Ellie"
    hide e
    show t
    t "Hi im Tyler"
    hide t
    show j
    j "Hi im Jacob"

    # This ends the game.

    return

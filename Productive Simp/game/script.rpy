# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define god = Character("God")
define YN = Character(name=None)

# The game starts here.

label start:
    $ YN = ""
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    $ YN = renpy.input("What is your name? ")
    $ YN = YN.strip()
    if YN == "":
        $ YN = "Aigiarn"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show god you died

    # These display lines of dialogue.

    YN "You're floating.​"

    YN "Around you is a horizon of stars stretching into the dark backdrop of the universe.​"

    "And in front of you is a woman with a halo above your head looking at you with an unreadable expression on her face.​"

    show ascending

    god "Hmmm..."

    god "first choice options"

    # This ends the game.

    return

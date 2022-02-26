# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define god = Character("God")
define YN = Character(name=None)
define healthgod = Character("Goddess of Health")

# The game starts here.

label start:
    $ YN = ""
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg galaxy

    $ YN = renpy.input("What is your name? ")
    $ YN = YN.strip()
    if YN == "":
        $ YN = "Aigiarn"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show god you died

    # These display lines of dialogue.

    "You're floating.​"

    "Around you is a horizon of stars stretching into the dark backdrop of the universe.​"

    "And in front of you is a woman with a halo above your head looking at you with an unreadable expression on her face.​"

    show ascending

    god "Hmmm..."

    YN "What? Who are you?"

    god "Hello [YN]. I am what you call 'God' "

    YN "Where am I?"
    
    god "The afterlife. You were hit by a truck. Don't worry about it. "

    YN "What?! Am I dead?"

    god "Yes, unfortunately. But don't worry! You're going to go to a better place."

    YN "Where am I heading?"

    god "See, originally, you were supposed to be the savior of this neat world I had going on, right?"
    god "The whole, classic, hero from another dimension versus demon kind of thing..."
    god "Though, looking at you, that's not happening anytime soon."

    YN "What? Why??"

    god "Well, how are you suppposed to save the world when you can't even save yourself?"
    god "I'm sending you to Health Camp. Off you go!"

    "{i}She yeets you into the distance{/i} (cue Mario-like scream)?"

    scene camping

    "You fall right in front of the gates of Health Camp. On the gates, a text is inscribed:"
    "HEALTH CAMP, HEALTH LIMBO (get your shit together)"


    # This ends the game.

    return

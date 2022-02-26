# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define god = Character("God")
define YN = Character(name=None)
define healthgod = Character("God of Health")

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

    "{i} The god of Health arrives in front of the gates to see what all the ruckus is about {/i}"

    healthgod "What? Why do I get another slacker here again? The big god really doesn't pick the right
    people for her scenarios."
    healthgod "LISTEN HERE SLACKER. WELCOME TO HEALTH CAMP."
    healthgod "ONCE THIS CAMP IS FINISHED WITH YOU, YOU'LL BE THE PINNACLE OF HEALTH."
    healthgod "IN THE MEANTIME, YOU CAN EXPECT TO GO THROUGH HELL IN ORDER TO GET RID OF THOS BAGS UNDER YOUR EYES"
    healthgod "THOSE SORRY EXCUSES FOR ARMS"
    healthgod "AND THAT DEHYDRATED LOOK. EVEN A ROCK DRINKS MORE WATER THAN YOU DO "
    healthgod "HAVE YOU UNDERSTOOD SLACKER?"

    YN "Uhh, what?"

    healthgod "WHAT DID YOU SAY SLACKER? NO QUESTIONS!"
    healthgod "I WANT A 'YES GOD OF HEALTH' FROM YOU! DID YOU GET THAT SLACKER?"

    YN 'Yes God of Health'

    healthgod "LOUDER SLACKER. GET ALL THAT POLLUTION OUT OF YOUR LUNGS"

    YN "YES GOD OF HEALTH"

    healthgod "GOOD. GET OFF THOSE SORRY GLUTES SLACKER AND HEAD TO TENT 4. THAT'S WHERE YOU'LL
    BE STAYING DURING YOUR TRAINING ARC"
    healthgod "CAMPFIRE ORIENTATION IS AT 7PM SHARP. IF YOU'RE LATE, I'LL FINE YOU 500 PUSH UPS. DID YOU GET THAT SLACKER?"

    YN "YES GOD OF HEALTH"

    healthgod "VERY WELL SLACKER. YOU'RE DISMISSED"

    "You walk over to tent 4, sit down and look at the lake in the distance. What just happened to you?"
    "Did you really just die and get sent to a fitness bottcamp run by the most aggressive fitness trainer in the world? (or afterlife?)"
    "As you get lost in your thoughts, you slowly fall asleep. So much has happened, and you feel so tired."
    "A small nap wouldn't hurt right?"


    # This ends the game.

    return

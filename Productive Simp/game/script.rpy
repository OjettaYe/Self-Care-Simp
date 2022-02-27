# The script of the game goes in this file.
#python
init python:
    from datetime import datetime



# Declare characters used by this game. The color argument colorizes the
# name of the character.

define god = Character("God")
define YN = Character(name=None)
define healthgod = Character("Goddess of Health")
define guide = Character("Goddess of Guidance")
define guidep = Character("Caitlyn")
define unknown = Character("???")
define prezzz = Character("Prezzz")

#Other councillors
define food = Character("Shef")
define water = Character("H2wu")
define fitness = Character("Buffie")
define social = Character("Grass Lass")

define sleepstart = 0
define sleepend = 0
define sleeplength = 0
define firstTimeT1 = True
define firstTimeT2 = True
define firstTimeT3 = True
define firstTimeT4 = True
define firstTimeT5 = True
define isOvernight = False

define now = 0

define time1 = 0
define time2 = 0

# The game starts here.

label start:
    $ YN = ""
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #Scene 1
    scene bg-galaxy
    with fade

    $ YN = renpy.input("What is your name? ")
    $ YN = YN.strip()
    if YN == "":
        $ YN = "Y/N"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show god you died

    # These display lines of dialogue.

    "You're floating.​"

    "Around you is a horizon of stars stretching into the dark backdrop of the universe.​"

    "And in front of you is a woman with a halo above your head looking at you with an unreadable expression on her face.​"

    show god with fade

    god "Hmmm..."

    YN "What? Who are you?"

    god "Hello [YN]. I am what you call 'God' "

    YN "Where am I?"

    god "The afterlife. You were hit by a truck. Don't worry about it. "

    YN "What?! Am I dead?"

    god "Yes, unfortunately. But don't worry! You're going to go to a better place."

    YN "Where am I heading?"

    god "See, originally, you were supposed to be the savior of this neat little world I had going on, right?"
    god "The whole, classic, hero from another dimension versus demon kind of thing..."
    god "Though, looking at you, that's not happening anytime soon."

    YN "What? Why??"

    god "Well, how are you suppposed to save the world when you can't even save yourself?"
    god "I'm sending you to Health Camp. Off you go!"

    "{i}She punts you into the distance{/i}"

    # Scene 2
    scene gate
    with vpunch

    "You fall right in front of the gates of Health Camp. On the gates, a text is inscribed:"
    "HEALTH CAMP, HEALTH LIMBO (get your sh*t together)"

    "{i} The [healthgod] arrives in front of the gates to see what all the ruckus is about {/i}"

    show healthgod with moveinleft

    healthgod "What? Why do I get another slacker here again? The big god really doesn't pick the right
    people for her scenarios."
    healthgod "LISTEN HERE SLACKER. WELCOME TO HEALTH CAMP."
    healthgod "ONCE THIS CAMP IS FINISHED WITH YOU, YOU'LL BE THE PINNACLE OF HEALTH."
    healthgod "IF YOU EVER WANT TO LEAVE, YOU'LL HAVE TO GET A BADGE FROM ALL FIVE CAMP COUNSELORS."
    healthgod "IN THE MEANTIME, YOU CAN EXPECT TO GO THROUGH HELL IN ORDER TO GET RID OF THOSE BAGS UNDER YOUR EYES" with hpunch
    healthgod "THOSE SORRY EXCUSES FOR ARMS" with hpunch
    healthgod "AND THAT CRUSTY LOOK. EVEN A ROCK DRINKS MORE WATER THAN YOU DO " with hpunch
    healthgod "HAVE YOU UNDERSTOOD SLACKER?"

    YN "Uhh, what?"

    healthgod "WHAT DID YOU SAY SLACKER? NO QUESTIONS!" with hpunch
    healthgod "I WANT A 'YES GOD OF HEALTH' FROM YOU! DID YOU GET THAT SLACKER?"

    YN 'Yes [healthgod]'

    healthgod "LOUDER SLACKER. GET ALL THAT POLLUTION OUT OF YOUR LUNGS" with hpunch

    YN "YES GODDESS OF HEALTH" with hpunch

    healthgod "GOOD. GET OFF THOSE SORRY GLUTES, SLACKER, AND HEAD TO CAMPSITE 4. THAT'S WHERE YOU'LL
    BE STAYING DURING YOUR TRAINING ARC"
    healthgod "CAMPFIRE ORIENTATION IS AT 7PM SHARP. IF YOU'RE LATE, I'LL FINE YOU 500 PUSH UPS. DID YOU GET THAT SLACKER?"

    YN "YES GODDESS OF HEALTH" with hpunch

    healthgod "VERY WELL SLACKER. YOU'RE DISMISSED"

    hide healthgod with moveoutleft
    scene lake
    with slideleft

    "You walk over to campsite 4, sit down and look at the lake in the distance. What just happened to you?"
    "Did you really just die and get sent to a fitness bootcamp run by the most aggressive fitness trainer in the world? (or afterlife?)"
    "As you get lost in your thoughts, you slowly fall asleep. So much has happened, and you feel so, so tired."
    "A small nap wouldn't hurt right?"

    #Scene 3

    scene black
    with fade

    "You feel a slight chill run down your spine as you come back to consciousness. What is this ominous feeling you have?"
    
    scene sunset
    with fade

    "As you watch the sun set, you suddenly remember about the campfire orientation event!!!"
    YN "{b} OH NOOOO!!!!! {/b}" with hpunch

    "You look at your watch. 6:58 PM! Without skipping a beat, you dash across the tents and go sit by the campfire, sitting down on a log just as your watch indicates 7:00 PM!"

    show healthgod at right with moveinright

    "{i} The [healthgod] watches your antics with a disapproving look {/i}"

    hide healthgod at right with moveoutright

    "You look around. A handful of people sit on large wooden logs, chatting with each other or roasting marshmallows.
    Soft guitar strums are heard along with the crackling of the flames."

    "A tall woman with a bucket hat approaches you with a friendly smile."

    show guide at left with moveinleft

    guide "Well hello there! Welcome to Health Bootcamp! I'm the [guide], but you can just call
    me [guidep]!"
    guidep "Is there anything you'd like to know?"

    YN "What just happened to me?"

    guidep "Yeahhh, sorry about that. Our leaders can be quite eccentric, but I assure you that the normal folks here are great!"

    show healthgod at right with moveinright

    "The [healthgod] frowns. Is she able to hear your conversation? Are gods all-knowing? Can she read your thoughts?"

    hide healthgod at right with moveoutright

    guidep "Just neat people all around!"
    guidep "Don't worry too much okay? We're here to work on ourselves and have a good time!"

    YN "Could you show me around?"

    guidep "Of Course! We have 5 main tents here. Each one is adapted to a specific facet of your health."

    #show Shef
    scene tent1
    guidep "Tent 1 is dedicated to your nutritional habits."
    
    scene tent2
    #show h2uwu
    guidep "Tent 2 is for your hydration."

    scene tent3
    #show buff lad
    guidep "Tent 3 is the fitness space."

    scene tent4
    #show grass lass
    guidep "Tent 4 is for all your social needs."

    scene tent5
    show prezzz at right with moveinright
    guidep "And Tent 5 is to go to sleep."

    hide prezzz at right with moveoutright

    scene sunset
    guidep "I suggest you go meet them! Return to me afterwards if you have any other questions."
    hide guide at left with moveoutleft

    label mentorpick:
    scene sunset
    python:
        now = datetime.now()
        hour = float(now.strftime('%H'))
        if hour >= 23.0 or hour <= 6.0:
            isOvernight =  True
        else:
            isOvernight = False
    if isOvernight:
        show prezzz with moveinleft
        if firstTimeT5:
            unknown "Why in the afterlife are you awake?" with hpunch
            unknown "If you don't go back to sleep now, I'll knock you unconscious" with hpunch
        else:
            prezzz "Why in the afterlife are you awake?" with hpunch
            prezzz "If you don't go back to sleep now, I'll knock you unconscious" with hpunch
        hide prezzz with moveinleft


    menu:
        "Which camp counselor would you like to meet?"

        "Tent 1 counselor, [food]":
            "You walk towards tent 1"
            jump tent1
        "Tent 2 counselor, [water]":
            "You walk towards tent 2"
            jump tent2
        "Tent 3 counselor, [fitness]":
            "You walk towards tent 3"
            jump tent3
        "Tent 4 counselor, [social]":
            "You walk towards tent 4"
            jump tent4
        "Tent 5 counselor, [prezzz]":
            "You walk towards tent 5"
            jump tent5

#Food tent
label tent1:
    scene tent1
    "You arrive at the first tent"
    show food with moveinright
    if firstTimeT1:
        unknown "Hi! You must be new here. You look so thin and pale, have you been eating well recently?"
        unknown "Don't worry about it! With my food and nutrition plan, you'll be so organic,
        students will study you in chemistry."
        unknown "You can call me [food] btw."
    hide food with moveoutright
    jump mentorpick

#Hydration tent
label tent2:
    scene tent1
    "You arrive at the second tent. It seems drenched?"
    show water with moveinright
    if firstTimeT2:
        unknown "Oh noooo, you poor thing! (┬┬_┬┬) You look so dry..."
        unknown "I.. I... I mean thirsty... uh nooo"
        unknown "{i} I can do this! Remember [water], conversation 101"
        water "Hi! ☆*: .. o(≧▽≦)o ..:*☆ I'm [water]! I'll be making sure you stay nice and hydrated"
        water "And that your body is always composed of around 60 percent liquid!"
        water "{i} uhh that might have been too specific for a first conversation...{i}"
    hide water with moveoutright
    jump mentorpick

#Fitness tent
label tent3:
    scene tent3
    "You arrive at the third tent but... {i}UP 302{/i}"
    "{i}UP 303{/i}"
    "{i}UP 304{/i}"
    "Why does this sound like a beep test?!?!?!"
    "Painful memories from high school gym class flash before your eyes"
    show healthgod with moveinright
    "WAIT... WHAT IS SHE DOING HERE?!?!" with vpunch
    healthgod "THICKEN UP SLACKER! YOUR MUSCLES ARE SO THIN I THOUGHT YOU WERE A WALKING DRIED MANGO" with hpunch
    healthgod 'THAT THE GOD OF MEMORY LEFT OUT IN THE SUN TO DRY EVEN MORE' with hpunch
    healthgod 'AND THEN HE FORGOT ABOUT YOU WHILE ALL YOUR MUSCLES MELTED AWAY!' with hpunch
    "You have a bad feeling about this"
    healthgod "NO WORRIES SLACKER! ONCE I'M DONE WITH YOU, THEY'LL HAVE TO REMAKE THE PERIODIC TABLE WITH THE NEW
    HARDEST ELEMENT ON EARTH," with hpunch
    healthgod "THOSE ABS! ATOMIC NUMBER 12-PACK" with hpunch
    healthgod "NOW LET'S START WITH OUR FIRST SET OF A THOUSAND PUSH UPS" with hpunch
    "A THOUSAND WHAT?" with vpunch
    healthgod "IN POSITION NONMUSCULAR SLACKER. {i}UP 1, UP 2, UP 3, ...{/i}" with hpunch
    hide healthgod with moveoutright
    scene black
    with fade
    "After an infernal workout regiment that made you wonder what happens in hell, you scurried back to the campsite"
    jump mentorpick
    
label tent4:
    scene tent4
    "You arrive at the fourth tent. It seems very lively!"
    show guide with moveinright
    if firstTimeT4:
        guide "HI THERE SWEETIE! I'm the counselor who'll take take care of that unsocial social life of yours!"
        guide "You can call me [social]"
        YN "Wait, but aren't you [guidep]?"
        guide "Whatttt? [guidep]? Who is that? I've never heard of them before? Nu-uh? First time that name has reached these ears!"
        guide "Hahahaha I guess your social life is better than I thought! Maybe you could introduce me to them!"
        guide "{i} Aghhhhh, I think I've fooled them for now. This camp is so understaffed!{/i}"
        guide "{i} If only the [healthgod] didn't scare away all our interns...{/i}"
    hide guide with moveoutright
    jump mentorpick

label tent5:
    scene tent5
    "You arrive at the tent on the far right."
    show prezzz with moveinright
    if firstTimeT5:
        unknown "You must be the newbie. I'm assuming you're here for bedtime?"
        unknown "It's a little early for that, but hey, to each their own."
        unknown "You can call me Prezzz btw. It's short for Sleep President"
        $firstTimeT5 = False

    
    label menutent5:
    menu:
        "Yes, sleep. Please":
            "What's your sleep schedule like?"
            $sleeptxt = ''
            $validtime = True
            $error=''
            $overnight=""
            $timeslept = 0
            label entersleep:
            $sleeptxt = renpy.input("Please enter when you go to bed (h:min) ")
            python:
                from datetime import datetime
                try:
                    sleepstart = datetime.strptime(sleeptxt, "%H:%M")
                    validtime = True
                except Exception as e:
                    error = e
                    validtime = False
            if validtime != True :
                "Sorry, that's an invalid time."
                jump entersleep
            $sleeptxt = renpy.input("Please enter when you wake up (h:min) ")
            python:
                import time
                try:
                    sleepend = datetime.strptime(sleeptxt, "%H:%M")
                    validtime = True
                except Exception as e:
                    error = e
                    validtime = False
            if validtime != True :
                "Sorry, that's an invalid time."
                jump entersleep
            #Time choices
            python:
                def timeAdd(t1, t2):
                    time1 = float(t1.strftime('%H')) + (float(t1.strftime('%M')))/60
                    time2 = float(t2.strftime('%H')) + (float(t2.strftime('%M')))/60
                    if float(t2.strftime('%H')) < float(t1.strftime('%H')):
                        time2 = 24 + time2
                    return (time2-time1)
                sleeplength = timeAdd(sleepstart, sleepend)
            if sleeplength < 6.0:
                prezzz "Yikes, you really do need to work on that huh?"
                YN "I know... I feel so tired"
                prezzz "Well, maybe you wouldn't be as tired if you {i}*checks notes*{/i} ACTUALLY SLEPT!"
                prezzz "What do you even do all night camper?! Stream anime? Play Valorant?!"
                prezzz "Tsk... This is unacceptable behaviour. I'll be seeing you in tent 5's sleep detention tonight"
                prezzz "Don't forget to bring your sleeping bag. 
                I don't care if we have to make you sleep on the floor, as long as you sleep."
                prezzz "A plush will be provided for you though if you don't have one... I hope we can fix that sleep schedule of yours"
            else:
                prezzz "Hmm, and you actually stick to that?"
                YN "Yes! I try my best!"
                prezzz "Trying isn't enough! Your best? We'll see about that once you have exams and assignments piled up"
                YN "We... we even have exams in the afterlife?"
                prezzz "QUIZ TIME CAMPER! How many hours do cats sleep in a day?"
                YN "12 to 18 hours I think! As they age, cats also spend more time sleeping."
                prezzz "WELL DONE CAMPER!"
                prezzz "If a cat can do 12 to 18 hours a day, surely you can manage more than half of that no?"
                YN "I... I'll keep that in mind!!!"
                prezzz "Well done camper! I expect you to dream well as well."
            jump menutent5

        "I just wanted to meet the mentor":
            prezzz "I am the mentor for your poor soul's sleep schedule."

            YN "... but you don't look sleepy"

            prezzz "Exactly. Because I get enough sleep."

            "She squints at your eyebags, pointedly"

            prezzz "Unlike {i}you{/i}"
            jump menutent5
        "Mmh, actually no. (Return to all tents)":
            "See you later, {i}in your dreams.{/i}"
    hide prezzz at right with moveoutright
    jump mentorpick


        







    #Scene 4

    # This ends the game.
    return

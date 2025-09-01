define e = Character("Elias")
define mc = Character("[player_name]")
define n = Character(None)

default player_name = ("XXX")

define gui.text_font = "fonts/SourceCodePro-Regular.ttf"

default ending = 1

transform small_size:
    xysize (1800, 1800)
    xalign 0.5
    yalign 0.5
    fit "contain"

transform fit:
    xysize (1920, 1080)
    fit "cover"

label start:

    scene bg grey at fit

    $ player_name = renpy.input("What is your name?", length=20)

    mc "Elias. Why'd you call me here?"

    show eli at small_size

    e "Well. Am I not allowed to talk to you or something?"

    mc "No, that's not it. It just seems a little out of the blue..."

    e "Huh? What do you mean?"

    menu:
        "It's 3am.":
            e "So what?"

            show eli shock at small_size

            mc "The hell do you mean, 'so what?'"

            e "I just wanted to..."

            mc "What?"

            show eli at small_size

            e "Nevermind."

        "Why are we even at school?":
            show eli squint at small_size

            e "It's for the..."

            mc "Memories?"

            show eli at small_size

            e "No. No, nevermind."
    
    mc "So I guess we're just here to hang out, then."

    e "Yeah. That, yeah."

    n "It's obvious that he's here for something more."

    menu:
        # calm friend
        "Are you feeling okay?":
            show eli at small_size

            e "Yeah! Definitely! Haha..."

            show squint at small_size

            e "Yeah, no, I don't have a poker face. How do you do it?"

            n "He looks at your hands."

            show eli at small_size

            e "How do you do it?"

            mc "Do what?"

            e "Your face. It's hiding everything."

            mc "Eli?"

        # breaks down
        "Hey, you sure about that?":
            show eli at small_size

            e "Yeah...yeah, I guess."

            e "Yeah..."

            mc "Eli. Eli, are you...?"

            show eli squint at small_size

            e "..."

            jump break_eli

        # remembers
        "Shut up. You're hiding something from me.":
            scene bg grey eye at fit

            show eli tired at small_size

            e "Ha! You can't be serious right now."

            e "[player_name], it's been two years."

            e "Seven hundred and thirty days."

            show eli angry at small_size

            e "TWO YEARS."

            e "And I still remember {i}everything.{/i}"

            show eli squint at small_size

            e "But you've forgotten, haven't you?"

            e "Everyone always forgets."

            n "You shouldn't have said that..."

            jump rant_eli

label calm_eli:
    $ ending = 1

    show eli at small_size

    e "I guess...I guess it's alright..."

    mc "Yeah. Yeah, I'd hope so."

    n "But how much do you want to know?"

    menu:
        "Press further":
            show eli squint at small_size

            mc "But why did you bring me here?"

            mc "What are you - are you actually fine?"

            mc "Eli?"

            $ ending = 2

        "Don't provoke him"
            mc "..."

            e "I don't even know anymore..."

    if ending == 1:
        jump end1
    
    jump break_eli

label break_eli:
    $ ending = 2

    show eli_squint at small_size

    e "Don't...don't talk to me."

    e "Please get out."

    e "I don't want to hear...don't want to hear her voice anymore."

    mc "Who?"

    e "..."

    jump backstory

label rant_eli:
    $ ending = 3

    show eli tired at small_size

    mc "Forget what? Eli, what are you even talking about?"

    e "No. No, I can't do this."

    mc "Eli, what's going on?"

    show eli squint at small_size

    e "I hate December."

    n "Get him to tell you what he means."

    menu:
        "But why?":
            $ ending = 4

            show eli tired at small_size

            e "Ha!"

            e "Wouldn't you like to know."

            e "[player_name]."
        
        "It's just a month.":

            e "[player_name]."

            n "You can see despair in his eyes."

            e "It's everything."

    jump backstory

label backstory:
    show eli at small_size

    e "You don't remember what they did to her."

    e "They...two years ago, they brought her to the second floor. Of the school, of course."

    show eli squint at small_size

    e "You should know what happens next, right?"

    menu:
        "No...I really don't. I'm sorry.":
            e "..."

            e "Alright."

            e "Maybe I was wrong..."

            $ ending = 3

        "Let's just go home for the night.":
            e "..."
        
    if ending == 3:
        jump end3

    scene bg red eye at fit

    e "You were there. You saw everything."

    show eli at small_size

    e "I remember now. Your face. You were watching from below."

    e "Why didn't you stop them? Why didn't you try to catch her?"

    e "They thought I was lying. They charged ME with manslaughter."

    e "[player_name], I'm 15."

    show eli tired at small_size

    e "I'm just 15..."

    e "It's not over, though."

    e "No."

    e "You're not safe anymore."

    e "I can report you too. You know what, I'll-"

    menu:
        "Grab him":
            show eli shock at small_size

            e "NO!"

        "Grab him":
            show eli shock at small_size

            e "NO!"

        "Grab him":
            show eli shock at small_size

            e "NO!"

        "Grab him":
            show eli shock at small_size

            e "NO!"

        "Grab him":
            show eli shock at small_size

            e "NO!"

    e "NO! [player_name] - I - NO!"

    e "IT'S ALL YOUR FAULT SHE DIED!"

    e "YOU COULD HAVE CAUGHT HER!"
    
    e "WHY THE HELL DID YOU RUN AWAY?"

    jump end4

label end1:
    hide eli
    n "Ending 1/4: Calm...?"
    return

label end2:
    hide eli
    n "Ending 2/4: Silence"
    return

label end3:
    hide eli
    n "Ending 3/4: It's Okay"
    return

label end4:
    hide eli
    n "Ending 4/4: ATONE"
    return
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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg grey at fit

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show elias happy

    # add name asking thing

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

label break_eli:

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

            n "You can see two years' worth of despair rising from the depths of his sunken eyes."

            e "It's everything."


    return
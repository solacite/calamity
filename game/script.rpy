define e = Character("Elias")
define mc = Character("[player_name]")
define n = Character(None, what_style="italic_text")

default player_name = ("XXX")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show elias happy

    # add name asking thing

    $ player_name = renpy.input("What is your name?", length=20)

    mc "Elias. Why'd you call me here?"

    e "Well. Am I not allowed to talk to you or something?"

    mc "No, that's not it. It just seems a little out of the blue..."

    e "Huh? What do you mean?"

    n "His demeanor shifts. He's more...fragile."

    menu:
        "It's 3am.":
            e "So what?"

            mc "The hell do you mean, 'so what?'"

            e "I just wanted to..."

            mc "What?"

            e "Neevermind."

        "Why are we even at school?":
            e "It's for the..."

            mc "Memories?"

            e "No. No, nevermind."
    
    mc "So I guess we're just here to hang out, then."

    e "Yeah. That, yeah."

    n "It's obvious that he's here for something more."

    menu:
        "Are you feeling okay?":
            e "Yeah! Definitely! Haha..."

            e "Yeah, no, I don't have a poker face. How do you do it?"

            n "He looks at your hands."

            e "How do you do it?"

            mc "Do what?"

            e "Your face. It's hiding everything."

            mc "Eli?"

        "Hey, you sure about that?":
            e "Yeah...yeah, I guess."

        "Shut up. You're hiding something from me.":
            e "Ha! You can't be serious right now."

            e "[player_name], it's been two years."

            e "Seven hundred thirty days."

            e "TWO YEARS."

            e "And I still remember {i}everything.{/i}"

            e "But you've forgotten, haven't you?"

            e "Everyone always forgets."

    return

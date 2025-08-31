define e = Character("Elias")
define mc = Character("[player_name]")

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

    menu:
        "It's 3am."

        "Why are we even at school?"



    return

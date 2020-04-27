# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color='#0099ff', kind = nvl)

define c = Character("Creator", color="#00ff00", kind = nvl)

define menu = nvl_menu

init:
    $ count = 0

# The game starts here.

label start:


$ toPlay = True

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

while toPlay:

    e "Lets start from this."

    c '''try to increase this to [count]'''

    e "Start again!"

    $ count +=1

    menu:

        "Increase":
            nvl clear
            jump start

        "Go":
            nvl clear
            jump ends    


label ends:

$ toPlay = False

c "Here we go"

e "Again [toPlay]"

# This ends the game.

return

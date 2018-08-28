"""
CP1404 Practical
Hexadecimal Colour Codes
"""

HEX_COLOURS = {"Beige": "#f5f5dc", "Brown": "#a52a2a", "Cyan":
    "#00ffff", "Gray": "#bebebe", "Gold": "#ffd700", "Green":
    "#00ff00", "Lavender": "#e6e6fa", "Magenta": "ff00ff", "Orange":
    "#ffa500", "Black": "#000000"}

colour = input("Enter a colour: ")
while colour != "":
    # print("The code for \"{}\" is {}".format(colour,
    #                     HEX_COLOURS.get(colour)))
    # colour = input("Enter a colour: ")
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Sorry, this colour isn't available")
    colour = input("Enter a colour: ")

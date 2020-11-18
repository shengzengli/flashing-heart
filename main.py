basic.show_number(1)
basic.show_number(2)
basic.show_number(3)

def on_forever():
    basic.show_arrow(ArrowNames.NORTH)
    basic.show_arrow(ArrowNames.WEST)
    basic.show_arrow(ArrowNames.SOUTH)
    basic.show_arrow(ArrowNames.EAST)
basic.forever(on_forever)

from graphics import graphics
import random

def main():
    gui = graphics(600, 600, 'canvas')
    x = 0
    y = 100
    colour_1 = colour(gui)
    colour_2 = colour(gui)
    colour_3 = colour(gui)
    while y < 150:
        while True:
            gui.clear()
            gui.rectangle(0, 0, 600, 500, 'deep sky blue')
            sun(gui, colour_1, colour_2, colour_3)
            x, y = birds(gui, x, y)
            x, y = birds(gui, x, y)
            x, y = birds(gui, x, y)
            x, y = birds(gui, x, y)
            x, y = birds(gui, x, y)
            if x > 600:
                x = -25
                y = 100
            gui.update_frame(60)

def colour(gui):
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = gui.get_color_string(r, b, g)
    return color

def main_mountain_und_sky(gui, colour_1, colour_2, colour_3):
    '''
    This function prints out the mountain in the background.
    cs: is the colour string from the function colour.
    x: is the abscissa of the position of the mouse.
    y: is the ordinate of the position of the mouse.
    '''
    x = (gui.mouse_x/3) + 200
    y = (gui.mouse_y/3) + 200
    gui.triangle(x - 150, y + 200, x, y - 200, x + 150, y + 200, colour_1)
    side_pieces(gui, colour_1, colour_2, colour_3)

def side_pieces(gui, colour_1, colour_2, colour_3):
    '''
    This function prints out the side mountains..
    cs: is the colour string from the function colour.
    x: is the abscissa of the position of the mouse.
    y: is the ordinate of the position of the mouse.
    '''
    x = (gui.mouse_x/5) + 200
    y = (gui.mouse_y/5) + 200
    gui.triangle(x - 360, y + 240, x - 110, y - 110, x + 140, y + 240, colour_2)
    gui.triangle(x - 60, y + 240, x + 190, y - 90, x + 440, y + 240, colour_3)
    foreground(gui)

def sun(gui, colour_1, colour_2, colour_3):
    '''
    This function prints out the sun.
    x: is the abscissa of the position of the mouse.
    y: is the ordinate of the position of the mouse.
    '''
    x = (gui.mouse_x/4) + 200
    y = (gui.mouse_y/4) + 200
    gui.ellipse(x + 135, y - 170, 75, 75, 'gold')
    main_mountain_und_sky(gui, colour_1, colour_2, colour_3)

def foreground(gui):
    '''
    This function prints out the foreground.
    x: is the abscissa of the position of the mouse.
    y: is the ordinate of the position of the mouse.
    '''
    x = (gui.mouse_x/6) + 200
    y = (gui.mouse_y/6) + 200
    i = -25
    while i <= 600:
        gui.line(x - (300 - 5*i), y + 170, x - (300 - 5*i), y + 200, 'lawn green', 2)
        i += 1
        gui.rectangle(x - 400, y + 200, 800, 400, 'SpringGreen4')
        gui.rectangle(x + 150, y + 160, 30, 80, 'brown4')
        gui.ellipse(x + 165, y + 120, 85, 130, 'PaleGreen4')

def birds(gui, x, y):
    gui.line(x, y, x + 25, y + 10, 'black', 4)
    gui.line(x + 25, y + 10, x + 50 , y, 'black', 4)
    x += 50
    y += 10
    return x, y

main()
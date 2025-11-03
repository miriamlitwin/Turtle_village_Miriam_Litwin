

"""
                                            --- Pseudocode---
Function move_to()
    Raises the pen
    Moves the turtle to point x,y
    Lowers the pen
End function

Function draw_line()

    Function move_to()
        Raises the pen
        Moves the turtle to point x,y
        Lowers the pen
    End function
    
    Turtle goes to point x2, y2
End function 
    
Function fill_rect_center()
    Sets the fillcolor to assigned color
    Sets the pencolor to black
    Raises the pen
    Turtle goes to point (cx - w/2, cy + h/2)
    Lowers the pen
    Begins to fill
    For each number in the range of 2
        Turtle goes forward the amount of w
        Turtle turns a 90 degree angle to the right
        Turtle moves forward the amount of h
        Turtle turns a 90 degree angle to the right
    End for
    Turtle stops filling
    Raises the pen 
End function
    
Function fill_triangle()
    Sets the fillcolor to assigned color
    Sets the pencolor to black
    Raises the pen
    Turtle goes to point 1
    Lowers the pen
    Begins to fill
    Turtle goes to point 2
    Turtle goes to point 3
    Turtle goes to point 1
    Turtle stops filling
    Raises the pen
End function

Function fill_circle_center()
    Sets the fillcolor to assigned color
    Sets the pencolor to black
    
    Function move_to
        Raises the pen
        Moves the turtle to point (cx, cy - r)
        Lowers the pen
    End function
    
    Begins to fill
    Draws a circle 
    Turtle stops filling
    Raises the pen 
End function
    
Function ask_choice_int()
    While the code is true
        Try
            prompt user for an integer for the number of columns
            if the number is not in the columns list
                raise ValueError
            prompt user for an integer for the number of rows
            if the number is not in the rows list
                raise ValueError
            if columns and rows are both in the lists
                break out of the while loop
        Except ValueError
            print to the user a helpful message
            start loop again
    Prints the user input for columns and rows
    Returns the input of columns and rows
End function

Function ask_choice_str()
    While the code is true
        Try
            prompt user for a string for the house size
            if not in the size list
                raise ValueError
            prompt user for a string for the color theme
            if not in the theme list
                raise ValueError
            prompt user for a string for the roof style
            if not in the style list
                raise ValueError
            prompt user for a string for the sun choice
            if not in the sun choice list
                raise ValueError
            if all the strings are in the lists
                break out of the while loop
        Except ValueError
            print to the user a helpful message
            start loop again
    Prints the user input for house size, color theme, roof style and sun choice
    Returns house size, color theme, roof style and sun choice
End function

Function draw_roads()
    Sets the pencolor to black
    Sets the pen width to 3
    Assigns cell_w to CANVAS_W / columns choice
    Assigns cell_h to CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN / rows choice
    For each row in the range of rows
    
        Function draw_line()
            Function move_to()
                Raises the pen
                Moves the turtle to point left_x, CANVAS_H/2 - TOP_MARGIN - r*cell_h
                Lowers the pen
            End function
            Turtle goes to point CANVAS_H/2 - TOP_MARGIN - r*cell_h
        End function 
        
    For each column in range of columns 
    
        Function draw_line()
            Function move_to()
                Raises the pen
                Moves the turtle to point -CANVAS_W/2 + c*cell_w, bot_y
                Lowers the pen
            End function
            Turtle goes to point bot_y, -CANVAS_W/2 + c*cell_w, top_y
        End function 
        
End function
        
Function draw_house_centered()

    Function fill_rect_center()
        Sets the fillcolor to assigned color
        Sets the pencolor to black
        Raises the pen
        Turtle goes to point (cx - w/2, cy + h/2)
        Lowers the pen
        Begins to fill
        For each number in the range of 2
            Turtle goes forward the amount of w
            Turtle turns a 90 degree angle to the right
            Turtle moves forward the amount of h
            Turtle turns a 90 degree angle to the right
        End for
        Turtle stops filling
        Raises the pen 
    End function
    
    If user choice roof style "triangle"
    
        Function fill_triangle()
            Sets the fillcolor to assigned color
            Sets the pencolor to black
            Raises the pen
            Turtle goes to point 1, (cx - w / 2, cy + h / 2)
            Lowers the pen
            Begins to fill
            Turtle goes to point 2, (cx, (cy + h / 2) + 0.5 * h)
            Turtle goes to point 3, (cx + w / 2, cy + h / 2)
            Turtle goes to point 1, (cx - w / 2, cy + h / 2)
            Turtle stops filling
            Raises the pen
        End function
        
    Else
    
        Function fill_rect_center()
            Sets the fillcolor to assigned color
            Sets the pencolor to black
            Raises the pen
            Turtle goes to point (cx - w*.02, cy - h*.25)
            Lowers the pen
            Begins to fill
            For each number in the range of 2
                Turtle goes forward the amount of w*.20
                Turtle turns a 90 degree angle to the right
                Turtle moves forward the amount of h/2
                Turtle turns a 90 degree angle to the right
            End for
            Turtle stops filling
            Raises the pen 
        End function
        
    Raises the pen
End function
    
Function draw_tree_near()

    Function fill_rect_center()
        Sets the fillcolor to assigned color
        Sets the pencolor to black
        Raises the pen
        Turtle goes to point (tx - tw, ty + th)
        Lowers the pen
        Begins to fill
        For each number in the range of 2
            Turtle goes forward the amount of tw
            Turtle turns a 90 degree angle to the right
            Turtle moves forward the amount of th
            Turtle turns a 90 degree angle to the right
        End for
        Turtle stops filling
        Raises the pen 
    End function
    
    Function fill_circle_center()
        Sets the fillcolor to assigned color
        Sets the pencolor to black
        
        Function move_to
            Raises the pen
            Moves the turtle to point (tx, (ty+h*0.15) - r)
            Lowers the pen
        End function
        
        Begins to fill
        Draws a circle 
        Turtle stops filling
        Raises the pen 
    End function
    
End function

Function draw_village()
        If the user chooses to have 3 columns
            Assign cx = -266
            Assign cy = 266
        Else
            Assign cx = -200
            Assign cy = 400
        For each column in the range of columns + 1
            Assign cy = -150
            For each row in the range of rows + 1
                Function fill_rect_center()
                    Sets the fillcolor to assigned color
                    Sets the pencolor to black
                    Raises the pen
                    Turtle goes to point (cx - w/2, cy + h/2)
                    Lowers the pen
                    Begins to fill
                    For each number in the range of 2
                        Turtle goes forward the amount of w
                        Turtle turns a 90 degree angle to the right
                        Turtle moves forward the amount of h
                        Turtle turns a 90 degree angle to the right
                    End for
                    Turtle stops filling
                    Raises the pen 
                End function
    
                If user choice roof style "triangle"
    
                    Function fill_triangle()
                        Sets the fillcolor to assigned color
                        Sets the pencolor to black
                        Raises the pen
                        Turtle goes to point 1, (cx - w / 2, cy + h / 2)
                        Lowers the pen
                        Begins to fill
                        Turtle goes to point 2, (cx, (cy + h / 2) + 0.5 * h)
                        Turtle goes to point 3, (cx + w / 2, cy + h / 2)
                        Turtle goes to point 1, (cx - w / 2, cy + h / 2)
                        Turtle stops filling
                        Raises the pen
                    End function
        
                Else
    
                    Function fill_rect_center()
                        Sets the fillcolor to assigned color
                        Sets the pencolor to black
                        Raises the pen
                        Turtle goes to point (cx - w*.02, cy - h*.25)
                        Lowers the pen
                        Begins to fill
                        For each number in the range of 2
                            Turtle goes forward the amount of w*.20
                            Turtle turns a 90 degree angle to the right
                            Turtle moves forward the amount of h/2
                            Turtle turns a 90 degree angle to the right
                        End for
                        Turtle stops filling
                        Raises the pen 
                    End function
        
                Raises the pen
            End function
                
            Function draw_tree_near()

                Function fill_rect_center()
                    Sets the fillcolor to assigned color
                    Sets the pencolor to black
                    Raises the pen
                    Turtle goes to point (tx - tw, ty + th)
                    Lowers the pen
                    Begins to fill
                    For each number in the range of 2
                        Turtle goes forward the amount of tw
                        Turtle turns a 90 degree angle to the right
                        Turtle moves forward the amount of th
                        Turtle turns a 90 degree angle to the right
                    End for
                    Turtle stops filling
                    Raises the pen 
                End function
    
                Function fill_circle_center()
                    Sets the fillcolor to assigned color
                    Sets the pencolor to black
        
                    Function move_to
                        Raises the pen
                        Moves the turtle to point (tx, (ty+h*0.15) - r)
                        Lowers the pen
                    End function
        
                    Begins to fill
                    Draws a circle 
                    Turtle stops filling
                    Raises the pen 
                End function
    
            End function
            
            Assign cy += 300
            Assign cx += add_add
            If user chooses sun flag option "y"
                Assigns values to r, cx, cy
        
            Function fill_circle_center()
                Sets the fillcolor to assigned color
                Sets the pencolor to black
    
                Function move_to
                    Raises the pen
                    Moves the turtle to point (cx, cy - r)
                    Lowers the pen
                End function
    
                Begins to fill
                Draws a circle 
                Turtle stops filling
                Raises the pen 
            End function
            
End function
                                           --- End Pseudocode ---
                                           --- Short Reflection ---
    I used a while loop in the function ask_choice_int() and the function ask_choice_str().
In both these functions, the while forms a loop to prompt the user for information, reprompting
on error, and breaking out when the information is valid. The while loop allows the code to
continue infinitely until the user stops it. In contrast, I used a for loop in the functions
fill_rect_center(), draw_roads(), and draw_village(). In these function, the for creates a loop
to draw a rectangle, draw lines, and draw houses. In each of these cases, the for loop, which
allows one to iterate through a sequence of values,is ideal because the number of times that the
code is supposed to loop is known. I implemented try/except in the functions ask_choice_int and
ask_choice_str to validate that user entered a valid integer and a valid string.
                                           --- End Reflection ---
"""

import turtle as T
my_turtle = T.Turtle()
import random

# ---------- constants ----------
CANVAS_W, CANVAS_H = 800, 600
TOP_MARGIN, BOTTOM_MARGIN = 40, 40

# Size of houses
SIZES = {
    "s": (120, 80),
    "m": (150, 100),
    "l": (180, 120),
}
# To access the colors for the body, roof and door of the houses
THEMES = {
        "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7"),
        "primary": dict(body="red", roof="blue", door="gold"),
}

# Allowed set for number of columns and rows. Allowed list for house sizes, color theme,
# roof style and sun choice.
cols = [2, 3]
rows = [2]
size_key = ['s', 'm', 'l']
theme_key = ['pastel', 'primary']
roof_style = ['triangle', 'flat']
sun_flag = ['y', 'n']

def move_to(x,y):
    """
    Moves the turtle to the passing argument, an (x, y) coordinate, to begin drawing.
    x - position on x coordinate axis
    y - position on y coordinate axis
    """
    T.penup(); T.goto(x,y); T.pendown()

def draw_line(x1,y1,x2,y2):
    """
    Draws a line, using the move_to function above, from (x1, y1) to (x2, y2).
    x1 - position on x coordinate axis
    y1 - position on y coordinate axis
    x2 - position on x coordinate axis
    y2 - position on y coordinate axis
    """
    move_to(x1, y1); T.goto(x2,y2)

def fill_rect_center(cx, cy, w, h, color):
    """
    Draws a filled rectangle.

    Loops 2 times drawing the 'w', width, and 'h', height of the rectangle..

    cx - center of rectangle x coordinate
    cy - center of rectangle y coordinate
    w - width of rectangle
    h - height of rectangle
    color - color of rectangle
    """
    T.fillcolor(color); T.pencolor("black")
    T.penup()
    T.goto(cx - w / 2, cy + h / 2)
    T.pendown()
    T.begin_fill()
    for _ in range(2):
        T.forward(w); T.right(90); T.forward(h); T.right(90)
    T.end_fill()
    T.penup()

def fill_triangle(p1, p2, p3, roof_c):
    """
    Draw a filled triangle defined by three points.

    p1 — point 1 (x1, y1)
    p2 — point 2 (x2, y2)
    p3 — point 3 (x3, y3)
    color — fill color for the triangle
    """
    T.fillcolor(roof_c); T.pencolor("black")
    T.penup()
    T.goto(*p1)
    T.pendown()
    T.begin_fill()
    T.goto(*p2); T.goto(*p3); T.goto(*p1)
    T.end_fill()
    T.penup()

def fill_circle_center(cx, cy, r, color):
    """
    Draws and fills a circle.
    A circle is defined by:

    cx - the center of the circle, x coordinate
    cy - center of the circle, y coordinate
    r - radius
    color - color of the circle
    """

    T.fillcolor(color); T.pencolor("black")
    move_to(cx, cy - r)  # turtle draws circles from the bottom
    T.begin_fill(); T.circle(r); T.end_fill()
    T.penup()

def ask_choice_int():
    """
    Asks for an integer in the allowed set of columns and rows; reprompts on error.

    In a loop, if the user input is not in the allowed set, uses if statements to raise a ValueError.
    If the user input is in allowed set, breaks out of loop and prints and returns columns and rows.
    """

    while True:
        try:
            cols_choice = int(input("How many houses per row? [2, 3]: "))
            if cols_choice not in cols:
                raise ValueError
            rows_choice = int(input("How many rows? [2]: "))
            if rows_choice not in rows:
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid input. Must be an integer from the allowed set. Please try again.')
            continue

    print(f"{cols_choice}, {rows_choice}")

    return cols_choice, rows_choice

def ask_choice_str():
    """
    Asks for a string in the allowed list of sizes, color themes, roof styles and sun choices
    ;reprompt on error.

    In a loop, if the user input is not in the allowed list, uses if statements to raise a ValueError.
    If the user input is in allowed set, breaks out of loop and prints and returns size, color theme,
    roof style and sun choice.
    """

    while True:
        try:
            size_key_choice = input("House size ['S', 'M', 'L']: ").strip().lower()

            if size_key_choice not in size_key:
                raise ValueError
            theme_key_choice = input("Color theme ['pastel' 'primary']: ").strip().lower()
            if theme_key_choice not in theme_key:
                raise ValueError
            roof_style_choice = input("Roof type ['triangle', 'flat']: ").strip().lower()
            if roof_style_choice not in roof_style:
                raise ValueError
            sun_flag_choice = input("Draw a sun? ['y', 'n']: ").strip().lower()
            if sun_flag_choice not in sun_flag:
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid input. Must be a string from the allowed list. Please try again.')
            continue

    print(f'{size_key_choice} {theme_key_choice} {roof_style_choice} {sun_flag_choice}')

    return size_key_choice, theme_key_choice, roof_style_choice, sun_flag_choice

def draw_roads(cols_choice, rows_choice, cell_w, cell_h):
    """
    Draws straight separator lines between rows and columns.

    Loops the draw_line function by the amount of rows and columns.

    cols_choice = user input of an integer for number of columns.
    rows_choice = user input of an integer for number of rows.
    cell_w = width of each column.
    cell_h = height of each row.
    """

    top_y = CANVAS_H / 2 - TOP_MARGIN
    bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
    left_x = -CANVAS_W / 2
    right_x = CANVAS_W / 2

    T.pencolor('black')
    T.width(3)
    cell_w = CANVAS_W / cols_choice
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows_choice
    for r in range(1, rows_choice):
        draw_line(left_x, CANVAS_H/2 - TOP_MARGIN - r*cell_h, right_x, CANVAS_H/2 - TOP_MARGIN - r*cell_h)
    for c in range(1, cols_choice):
        draw_line(-CANVAS_W/2 + c*cell_w, bot_y, -CANVAS_W/2 + c*cell_w, top_y)

def draw_house_centered(cx, cy, size_key_choice, theme_key_choice, roof_style_choice):
    """
    Draws a simple house centered at (cx, cy).

    Uses an if/ else statement to determine what roof style to draw based on user input.

    cx - center of rectangle x coordinate.
    cy - center of rectangle y coordinate.
    size_key_choice = user input of a string for the size of the house.
    theme_key_choice = user input of a string for the color theme.
    roof_style_choice = user input of a string for the roof style.
    """

    w, h = SIZES[size_key_choice]
    colors = THEMES[theme_key_choice]
    body_c = colors["body"]
    roof_c = colors["roof"]
    door_c = colors["door"]

    fill_rect_center(cx, cy, w, h, body_c)

    if roof_style_choice == 'triangle':
        fill_triangle((cx - w / 2, cy + h / 2),(cx, (cy + h / 2) + 0.5 * h),
                      (cx + w / 2, cy + h / 2), roof_c)
    else:
        fill_rect_center(cx, cy + h/1.75, w, h/4, roof_c)

    fill_rect_center(cx - w*.02, cy - h*.25, w*.20, h/2, door_c)
    T.penup()

def draw_tree_near(cx, cy, size_key_choice):
    """
    Draws a small tree near the house (left or right).

    cx - center of rectangle x coordinate.
    cy - center of rectangle y coordinate.
    size_key_choice = user input of a string for the size of the house.
    """

    w, h = SIZES[size_key_choice]
    tw, th = w*0.10, h*0.40
    side = random.choice([-1,1])
    tx = cx + side * (w*0.45)
    ty = cy - h*0.5 + th/2

    fill_rect_center(tx, ty, tw, th, "Saddle Brown")

    fill_circle_center(tx, ty+h*0.15, tw*1.5, "Light Green")

def draw_village(cols_choice, rows_choice, size_key_choice, theme_key_choice, sun_flag_choice,
                 roof_style_choice):
    """
    Computes cell sizes, draw roads, and loop over grid to place houses and trees.
    Draws a sun if applicable.

    Uses an if/ else statement to determine how to calculate the center of each cell,
    different based on the amount of columns the user entered.
    Uses a nested loop to calculate the center coordinates of the cells and draw houses and trees.
    Uses an if statement to draw a sun if applicable.

    cols_choice = user input of an integer for number of columns.
    rows_choice = user input of an integer for number of rows.
    size_key_choice = user input of a string for the size of the house.
    theme_key_choice = user input of a string for the color theme.
    roof_style_choice = user input of a string for the roof style.
    sun_flag_choice = user input of a string to determine if turtle should draw a sun.
    """
    cell_w = CANVAS_W / cols_choice
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows_choice

    draw_roads(cols_choice, rows_choice, cell_w, cell_h)

    if cols_choice == 3:
        cx = -266
        add_add = 266
    else:
        cx = -200
        add_add = 400
    for c in range(1, cols_choice+1):
        cy = -150
        for r in range(1, rows_choice+1):
            draw_house_centered(cx, cy, size_key_choice, theme_key_choice, roof_style_choice)
            draw_tree_near(cx, cy, size_key_choice)
            cy += 300
        cx += add_add

    if sun_flag_choice == "y":
        r = 35
        cx = CANVAS_W / 2 - r - 20
        cy = CANVAS_H / 2 - r - 20
        fill_circle_center(cx, cy, r, "yellow")


# ---------- main ----------
def main():
    print("Welcome to Turtle Village - Lite!")
    cols_choice, rows_choice  = ask_choice_int()
    size_key_choice, theme_key_choice, roof_style_choice, sun_flag_choice = ask_choice_str()
    T.setup(CANVAS_W, CANVAS_H); T.speed(6); T.tracer(False)
    draw_village(cols_choice, rows_choice, size_key_choice, theme_key_choice, sun_flag_choice, roof_style_choice)
    T.shape('turtle')
    T.tracer(True); T.hideturtle(); T.done()

if __name__ == "__main__":
    main()







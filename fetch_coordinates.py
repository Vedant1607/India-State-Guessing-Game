import turtle
import pandas

coordinates = []

screen = turtle.Screen()
img = "india-political-map.gif"
screen.addshape(img)
turtle.shape(img)

screen.setup(height=950, width=800)
screen.title("Turtle Coordinate Finder")

def save_to_csv():
    df = pandas.DataFrame(coordinates)
    df.to_csv("India_states.csv")
    print("Coordinates saved")
    turtle.bye()

def get_coordinates(x,y):
    user_input = screen.textinput(title="State", prompt="Enter State Name").title()
    coordinates.append({"State":user_input,"x":x, "y":y})
    print(f"Coordinated of {user_input} are (x:{x}, y:{y})")
    
    if user_input == "Exit":
        save_to_csv()


screen.onscreenclick(get_coordinates)

screen.mainloop()
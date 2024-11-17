import turtle
import pandas

coordinates = []

screen = turtle.Screen()

# load the map image and add the image as a shape to the turtle screen
img = "india-political-map.gif"
screen.addshape(img)
turtle.shape(img)

screen.setup(height=950, width=800)
screen.title("Turtle Coordinate Finder")

# Function to save coordinates to a CSV file
def save_to_csv():
    df = pandas.DataFrame(coordinates)
    df.to_csv("India_states.csv")
    print("Coordinates saved")
    turtle.bye()

# Function to capture the clicked coordinates and user input (Name of the State)
def get_coordinates(x,y):
    user_input = screen.textinput(title="state", prompt="Enter State Name").title()
    coordinates.append({"State":user_input,"x":x, "y":y})
    print(f"Coordinated of {user_input} are (x:{x}, y:{y})")
    
    # If the user enters "Exit", save the data and close the program
    if user_input == "Exit":
        save_to_csv()

screen.onscreenclick(get_coordinates)

screen.mainloop()
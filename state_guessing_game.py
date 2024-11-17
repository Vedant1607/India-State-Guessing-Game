from turtle import Screen, Turtle
import pandas

screen = Screen()
turtle = Turtle()

# Path to the map image 
# make sure you remember that turtle only reads gif file, you cannot use jpg or jpeg files
img = "india-political-map.gif" 

screen.addshape(img)
screen.setup(height=950, width=800)
turtle.shape(img)

# Initialize game variables
score = 0
game_running = True

# Load the states data from the CSV file
data = pandas.read_csv("india_states.csv")
all_states = data.state.to_list() # convert the 'state' column into a list for easier access
correct_guesses = [] # list to keep track of correctly guessed states

while game_running:
    # Prompt the user to enter a state name
    user_input = screen.textinput(
        title=f"{score}/{len(all_states)} Guessed", 
        prompt="Enter State/Union Territory Name\nEnter 'exit' if you can no longer guess any state"
    ).title()
    
    # Check if the user's input matches a state in the list
    if user_input in all_states:
        correct_guesses.append(user_input)
        score += 1
        # get the data for the guessed state
        cuurent_state = data[data.state == user_input]
        
        # create a new turtle to write the state name on the map
        writer = Turtle()
        writer.penup()
        writer.hideturtle()
        
        # move the turtle to the state's coordinates and write the state name
        writer.goto(int(cuurent_state.x.item()), int(cuurent_state.y.item()))
        writer.write(user_input, align="center", font=("Ariel", 12, "normal"))
    
    # End the game if the user types "Exit"
    if user_input == "Exit":
        # Generate a list of states that were missed (not guessed)
        missed_state = [state for state in all_states if state not in correct_guesses]
        
        # save the missed states to a new CSV file for future learning
        missed_state_data = pandas.DataFrame(missed_state)
        missed_state_data.to_csv("states_needs_to_learn.csv")
        break
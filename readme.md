# **Turtle Coordinate Finder and State Guessing Game**

## **Overview**

This project consists of two Python programs built using the `turtle` and `pandas` libraries.

1. **Turtle Coordinate Finder**: A utility program for fetching coordinates of states or regions from an image (e.g., a political map) and saving them into a CSV file. This is primarily used to create a database for the main game, to save the state/union territory name along with it's coordinates.
2. **State Guessing Game**: An interactive game where users guess state names, with correct guesses displayed on the map.

## **NOTE**: YOU DON'T ACTUALLY NEED TO USE 'fetch_coordinates.py' FILE SINCE I'VE ALREADY PROVIDED YOU WITH THE DATABASE.

## **Files and Their Purpose**

### 1. **`fetch_coordinates.py`**

This script serves as a utility to help create a database of state/union territories names and their coordinates. It is not part of the game itself but is used to generate the CSV file required by the State Guessing Game. The CSV file generates by this program holds the data of state/union territories names and their coordinates as to where the lie on the turtle screen.

#### **How It Works:**

1. Load a political map (e.g., `india-political-map.gif`) as the Turtle screen background.
2. On clicking the map, a prompt asks the user to enter the corresponding state/union territory name.
3. The script stores the clicked coordinates `(x, y)` along with the entered state/union territory name.
4. When the user types `"Exit"`, the data is saved to `India_states.csv`.

#### **Key Features:**

- Captures coordinates dynamically based on user interaction.
- Saves data in a structured CSV format with columns: `State`, `x`, and `y`.

#### **Output Example (`India_states.csv`):**

```
State,x,y
Maharashtra,200,150
Karnataka,100,-50
Delhi,0,300
```

---

### 2. **`state_guessing_game.py`**

This is the main interactive game where users guess state/union territory names based on the map.

#### **How It Works:**

1. Load the same map as the background and read the `India_states.csv` file (created using `fetch_coordinates.py`).
2. The user is prompted to guess a state name.
3. If the guess is correct:
   - The state name is displayed at its corresponding location on the map.
   - The score increases.
4. If the user types `"Exit"`, the game ends and saves a list of states that were not guessed to `states_needs_to_learn.csv`.

#### **Key Features:**

- Keeps track of correct guesses and dynamically updates the map.
- Highlights states that need to be learned after the game.

#### **Output Example (`states_needs_to_learn.csv`):**

```
state
Rajasthan
Kerala
Goa
```

---

## **How to Use**

### **Setup**

1. Ensure you have Python installed along with the following libraries:
   - `turtle`
   - `pandas`
2. Place the map image (`india-political-map.gif`) in the same directory as the scripts.

### **Steps**

#### **Step 1: Fetch Coordinates (Database Creation)**

- Run the `fetch_coordinates.py` script:
  ```bash
  python fetch_coordinates.py
  ```
- Click on the map and enter the state name in the prompt.
- Type `"Exit"` to save the data to `India_states.csv`.

#### **Step 2: Play the State Guessing Game**

- Run the `state_guessing_game.py` script:
  ```bash
  python state_guessing_game.py
  ```
- Guess state names based on the map.
- Type `"Exit"` to end the game and generate `states_needs_to_learn.csv`.

---

## **Folder Structure**

```
project/
│
├── fetch_coordinates.py       # Utility to fetch state coordinates and create a database
├── state_guessing_game.py     # Main game script for guessing state names
├── india-political-map.gif    # Map image used in both scripts
├── India_states.csv           # Generated CSV file with state names and coordinates
└── states_needs_to_learn.csv  # Generated CSV file with missed states
```

---

## **Dependencies**

Ensure you have the following Python libraries installed:

- `turtle` (comes with Python by default)
- `pandas` (install via pip):
  ```bash
  pip install pandas
  ```

---
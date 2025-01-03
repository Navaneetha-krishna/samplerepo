#this is a python file
import random
import time

# Initial positions
lion = {"x": 0, "y": 0}
rabbit = {"x": random.randint(5, 10), "y": random.randint(5, 10)}

# Function to calculate distance
def calculate_distance(pos1, pos2):
    return ((pos1["x"] - pos2["x"]) ** 2 + (pos1["y"] - pos2["y"]) ** 2) ** 0.5

# Chase simulation
print("Lion starts chasing the rabbit!")
while True:
    # Display positions
    print(f"Lion is at ({lion['x']}, {lion['y']}), Rabbit is at ({rabbit['x']}, {rabbit['y']})")

    # Check if lion catches the rabbit
    if calculate_distance(lion, rabbit) < 1:
        print("The lion has caught the rabbit!")
        break

    # Rabbit moves randomly
    rabbit["x"] += random.choice([-1, 0, 1])
    rabbit["y"] += random.choice([-1, 0, 1])

    # Lion moves towards the rabbit
    if lion["x"] < rabbit["x"]:
        lion["x"] += 1
    elif lion["x"] > rabbit["x"]:
        lion["x"] -= 1

    if lion["y"] < rabbit["y"]:
        lion["y"] += 1
    elif lion["y"] > rabbit["y"]:
        lion["y"] -= 1

    # Pause for a moment to simulate real-time movement
    time.sleep(0.5)


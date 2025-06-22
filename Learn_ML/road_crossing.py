import numpy as np
import random

# Define environment parameters
num_positions = 5  # Positions: [0, 1, 2, 3, 4] where 0 is start and 4 is goal
actions = 3  # 0: Move Left, 1: Stay, 2: Move Right

# Initialize Q-table
Q = np.zeros((num_positions, actions))

# Define parameters
episodes = 2000  # Number of training episodes
learning_rate = 0.8  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.3  # Exploration rate

# Define the correct sequence: right, left, right
correct_sequence = [2, 0, 2]

# Training loop
for episode in range(episodes):
    state = 0  # Always start at position 0
    sequence_index = 0  # Track position in correct sequence
    
    while state < num_positions - 1:  # Continue until goal reached
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)  # Random action
        else:
            action = np.argmax(Q[state])  # Best known action
            
        # Determine next state based on action
        if action == 0:  # Move left
            next_state = max(0, state - 1)
        elif action == 1:  # Stay
            next_state = state
        else:  # Move right
            next_state = min(num_positions - 1, state + 1)
        
        # Reward system
        if next_state == num_positions - 1:  # Reached goal
            # Extra reward for following the correct sequence
            if sequence_index == len(correct_sequence) - 1 and action == correct_sequence[sequence_index]:
                reward = 20
            else:
                reward = 10
        else:
            # Reward for following the sequence
            if sequence_index < len(correct_sequence) and action == correct_sequence[sequence_index]:
                reward = 5
                sequence_index += 1
            else:
                reward = -1  # Penalty for wrong moves
        
        # Q-learning update
        Q[state, action] += learning_rate * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        
        state = next_state
        
        # Break if goal reached
        if state == num_positions - 1:
            break

# Test the trained agent
print("Testing trained agent...")
state = 0
sequence_index = 0
steps = 0
path = []

while state < num_positions - 1 and steps < 10:
    action = np.argmax(Q[state])
    
    if action == 0:
        next_state = max(0, state - 1)
        action_name = "LEFT"
    elif action == 1:
        next_state = state
        action_name = "STAY"
    else:
        next_state = min(num_positions - 1, state + 1)
        action_name = "RIGHT"
    
    path.append(action_name)
    print(f"Step {steps}: Position {state} -> Action {action_name} -> Position {next_state}")
    
    state = next_state
    steps += 1

print("\nAgent's path:", " -> ".join(path))
if state == num_positions - 1:
    print("Successfully crossed the road!")
else:
    print("Failed to cross the road.")

print("\nFinal Q-table:")
print(Q)
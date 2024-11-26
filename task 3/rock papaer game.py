import tkinter as tk
import random

# Mapping choices for the game
youdict = {"rok": 1, "ppr": -1, "scr": 0}
reversedict = {1: "Rock", -1: "Paper", 0: "Scissor"}

# Function to run the game logic
def play_game(youstr):
    # Get the computer's choice
    computer = random.choice([-1, 0, 1])
    you = youdict[youstr]
    
    # Display player and computer choices
    result_text = f"You chose: {reversedict[you]}\nComputer chose: {reversedict[computer]}\n"
    
    # Determine the result
    if computer == you:
        result_text += "OH! It's a draw, Try Again"
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        result_text += "YAY! You win"
    else:
        result_text += "OOOH SHITT! You lose"
    
    # Update result label
    result_label.config(text=result_text)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Display instructions
instructions = tk.Label(root, text="Choose your choice", font=("Helvetica", 14))
instructions.pack(pady=10)

# Buttons for the player's choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("rok"), width=10, font=("Helvetica", 12))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("ppr"), width=10, font=("Helvetica", 12))
paper_button.grid(row=0, column=1, padx=10)

scissor_button = tk.Button(button_frame, text="Scissor", command=lambda: play_game("scr"), width=10, font=("Helvetica", 12))
scissor_button.grid(row=0, column=2, padx=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

#**************************************************
# Name: TRIEU DO
# Course: CSCI 4313
# Assignment: Tic-tac-toe
# Date: 6/9/2025
#**************************************************

# Import library
import tkinter as tk

root = tk.Tk()                                      # Create main window
root.title("Tik tac toe")                           # Window title

# Get dimension of user screen
screenWidth = root.winfo_screenwidth()              # Get width
screenHeight = root.winfo_screenheight()            # Get height

# GUI window size in pixel
g_width = 127
g_height = 150

# Calculate the onsets of width and height after application pops up
x = int(screenWidth - g_width) // 2
y = int (screenHeight - g_height) // 2

root.geometry(f"{g_width}x{g_height}+{x}+{y}")      # Make GUI appear in the middle of the screen

board = [[None]*3 for _ in range(3)]                # Declare the size of the board
currentToken = "X"

# reference provided images from the folder
empty = tk.PhotoImage(file="./image/empty.gif")
x = tk.PhotoImage(file="./image/x.gif")
o = tk.PhotoImage(file="./image/o.gif")

class Cell(tk.Label):
    def __init__(self, master, row, col):
        super().__init__(master, width=40, height=40, bd=1, relief="sunken", image=empty)        # use default names of tkinter library
        
        self.row = row
        self.col = col
        self.token = " "                            # Make program track empty image as empty space
        self.img = empty                            # Make default empty space associating with empty.gif
        self.bind("<Button-1>", self.flip)          # Bind event to left mouse, pass even to flip function
    
    def flip(self, event):                          # Define function - logic of the game
        global currentToken
        global guiMessage

        if currentToken != "Over" and self.token == " ":       # If the game is not over and there is still empty space
            if currentToken == "X":
                self["image"] = x                               # Display the image
                self.img = x                                    # Keep the image in memory, tkinter requires these 2 lines together
                                                                # unless the image disappears after that
                self.token = "X"                                # Set the current array block to X
                currentToken = "O"                              # Change the turn 
            else:
                self["image"] = o
                self.img = o
                self.token = "O"
                currentToken = "X"
        
        winner = isWon()
        if winner:                                  # Declare the winner
            currentToken = "Over"
            guiMessage["text"] = f"Player {winner} wins!"
            unbindEvent()
        elif isFull():                               # Declare a draw
            currentToken = "Over"
            guiMessage["text"] = "Gameover"
            unbindEvent()

def isWon():
    for i in range(3):
        # Win in a row
        if board[i][0].token == board[i][1].token == board[i][2].token != " ":
            return board[i][0].token
        
        # Win in a row column
        if board[0][i].token == board[1][i].token == board[2][i].token != " ":
            return board[0][i].token
    
        # Win in a row diagonal
        if board[0][0].token == board[1][1].token == board[2][2].token != " ":
            return board[0][0].token
        elif board[0][2].token == board[1][1].token == board[2][0].token != " ":
            return board[2][0].token
    
    return None           # There is no winner
 
def isFull():                                       
    for i in range(3):
        for j in range(3):
            if board[i][j].token == " ":            # Check if there is empty space left
                return False
    return True

def unbindEvent():                                  # Disable all buttons once gameover
    for i in range(3):
        for j in range(3):
            board[i][j].unbind("<Button-1>")        # unbind the event from button

for i in range(3):                                  # make 3x3 board
    for j in range(3):
        cell = Cell(root, i, j)                     # Instantiate the Cell object
        cell.grid(row=i, column=j)
        board[i][j] = cell                          # Store cell into board  

guiMessage = tk.Label(root, text="", font=("Arial", 12))       # Format the message displayed in GUI
guiMessage.grid(row=3, column=0, columnspan=3)                 # Tkinter widget to position the message
root.mainloop()     # Start event loop
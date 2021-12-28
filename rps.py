import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

choices = ["Rock", "Paper", "Scissors"]
yourScore = 0
compScore = 0
roundCount = 0

# game functions
def game(yourChoice): ## chooses random compChoice, takes input for userChoice, compares choices, and adds a point to the winner's score 
    if roundCount == 0:
        global yourScore, compScore
        yourScore = 0
        compScore = 0
    #compChoice = compChoose()
    #winner = result(yourChoice,compChoice)
    reportScore(yourScore,compScore)
    return yourScore, compScore
def reportScore(yourScore,compScore): # prints the user's score and computer's score
    print("Your score is " + str(yourScore) + ".")
    print("The computer's score is " + str(compScore) + ".")  
    yourScore_label.grid(column = 0, row = 2, columnspan = 2)
    compScore_label.grid(column = 3, row = 2, columnspan = 2)
def resetScore(): #resets both computer and user score to 0
    global yourScore, compScore
    yourScore,compScore = 0
def choose(rps): #changes user choice to rock and starts game
    yourChoice = rps
    game(yourChoice)
#def compChoose():
#    return choices[random.randint(0,2)]
def result(yourChoice,compChoice):
    if (compChoice == "Rock" and yourChoice == "Scissors") or (compChoice == "Paper" and yourChoice == "Rock") or (compChoice =="Scissors" and yourChoice == "Paper"):
        print("You chose " + yourChoice + " and the computer chose " + compChoice + ". " + compChoice + " beats " + yourChoice + " so, the computer won.")
        showinfo("Computer Wins", "You chose " + yourChoice + " and the computer chose " + compChoice + ". " + compChoice + " beats " + yourChoice + " so, the computer won.")
    elif (compChoice == "Scissors" and yourChoice == "Rock") or (compChoice == "Rock" and yourChoice == "Paper") or (compChoice =="Paper" and yourChoice == "Scissors"):
        print("You chose " + yourChoice + " and the computer chose " + compChoice + ". " + yourChoice + " beats " + compChoice + " so, you won.")
        showinfo("You win", "You chose " + yourChoice + " and the computer chose " + compChoice + ". " + yourChoice + " beats " + compChoice + " so, you won.")
    elif compChoice == yourChoice:
        print("Tie! Nobody gains a point because both you and the computer chose " + yourChoice + ".")
        showinfo("Tie", "Tie! Nobody gains a point because both you and the computer chose " + yourChoice + ".")

# tkinter functions
def hide(widget): # the widget in the parameter
    widget.grid_forget()
def menu_to_game():
    if (rock_btn['state'] == tk.NORMAL):
        rock_btn['state'] = tk.DISABLED
    else:
        rock_btn['state'] = tk.NORMAL

    if (scissors_btn['state'] == tk.NORMAL):
        scissors_btn['state'] = tk.DISABLED
    else:
        scissors_btn['state'] = tk.NORMAL

    if (paper_btn['state'] == tk.NORMAL):
        paper_btn['state'] = tk.DISABLED
    else:
        paper_btn['state'] = tk.NORMAL
    hide(play_btn)
    hide(title_label)
    yourScore_label.grid(column = 0, row = 2, columnspan = 2)
    compScore_label.grid(column = 3, row = 2, columnspan = 2)
    reset_btn.grid(column = 2, row = 5, padx = 10, pady = 10)

# tkinter window
root = tk.Tk()
root.title('Rock, Paper, Scissors Game')
root.geometry('750x600+100+100')
root.attributes('-topmost', 1)
root.resizable(False,False)

#grid config
root.rowconfigure(3, weight = 6)

# title label
title_label = ttk.Label(
    root, 
    text = "Welcome to Varun's Rock, Paper, Scissors Game!",
    font = ("Times New Roman",18))
title_label.grid(column = 0, row = 0, columnspan = 5)
"""
title_label.pack(
    side='top')
"""

# play button
play_btn = ttk.Button(
    root, 
    text = "Click on me to play RPS", 
    #command = switchButtonState,
    width = 25)
play_btn.grid(column = 2, row = 1, padx = 10, pady = 10)

# exit button
exit_btn = ttk.Button(
    root, 
    text = "Exit", 
    command = exit,
    width = 15,)
exit_btn.grid(column = 2, row = 6, padx = 10, pady = 10)

# reset game button
reset_btn = ttk.Button(
    root, 
    text = "Reset Game", 
    command = resetScore,
    width = 15,)

#rock button
rock_img = tk.PhotoImage(file = r"rock.png")
rock_btn = tk.Button(
        root, 
        image = rock_img,
        state = tk.DISABLED, 
        command = lambda: choose("Rock"))
rock_btn.grid(column = 0, row = 3, rowspan = 1,padx = 10, pady = 5)

#paper button
paper_img = tk.PhotoImage(file = r"paper.png")
paper_btn = tk.Button(
        root, 
        image = paper_img,
        state = tk.DISABLED, 
        command = choose("Paper"))
paper_btn.grid(column = 2, row = 3, rowspan = 1, padx = 10, pady = 10)

# scissors button
scissors_img = tk.PhotoImage(file = r"scissors.png")
scissors_btn = tk.Button(
        root, 
        image = scissors_img, 
        state = tk.DISABLED, 
        command = choose("Scissors"))
scissors_btn.grid(column = 4, row = 3, rowspan = 1, padx = 10, pady = 10)

# user score label
yourScore_label = ttk.Label(
    root, 
    text = "Your Score: " + str(yourScore),
    font = ("Times New Roman",12))

# comp score label
compScore_label = ttk.Label(
    root, 
    text = "Computer Score: " + str(compScore),
    font = ("Times New Roman",12))

root.mainloop()    
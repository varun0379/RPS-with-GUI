import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

choices = ["Rock", "Paper", "Scissors"]
yourScore = 0
compScore = 0
yourChoice = ""
compChoice = ""
counter = 0
ties = 0

# tkinter functions
def hide(widget): # the widget in the parameter
    widget.grid_forget()

# tkinter window
root = tk.Tk()
root.title('Rock, Paper, Scissors Game')
root.geometry('750x400+400+200')
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

# exit button
exit_btn = ttk.Button(
    root, 
    text = "Exit", 
    command = exit,
    width = 15,)
exit_btn.grid(column = 2, row = 6, padx = 5, pady = 5)

"""
# reset game button
reset_btn = ttk.Button(
    root, 
    text = "Reset Game", 
    #command = resetScore,
    width = 15,)
reset_btn.grid(column = 2, row = 5, padx = 10, pady = 10)
"""
# user score label
yourScore_label = tk.Label(
    root, 
    text = 'Your Score: ' + str(yourScore) + '\n Your Last Choice: ' + yourChoice,
    font = ("Times New Roman",12))
yourScore_label.grid(column = 0, row = 2, columnspan = 2)

# comp score label
compScore_label = tk.Label(
    root, 
    text = ("Computer Score: " + str(compScore) + "\n Computer's Last Choice: " + compChoice),
    font = ("Times New Roman",12))
compScore_label.grid(column = 3, row = 2, columnspan = 2)

# rounds + ties label
counter_label = tk.Label(
        root,
        text = "Rounds Played: " + str(counter) + "\n Tie Rounds: " + str(ties),
        font = ("Times New Roman",12))
counter_label.grid(column = 2, row = 2)
def result(yourChoice,compChoice):
    global compScore, yourScore, counter, ties
    if (compChoice == "Rock" and yourChoice == "Scissors") or (compChoice == "Paper" and yourChoice == "Rock") or (compChoice =="Scissors" and yourChoice == "Paper"):
        compScore += 1
        counter += 1
    elif (compChoice == "Scissors" and yourChoice == "Rock") or (compChoice == "Rock" and yourChoice == "Paper") or (compChoice =="Paper" and yourChoice == "Scissors"):
        yourScore += 1
        counter += 1
    elif compChoice == yourChoice:
        showinfo("Tie!", "Nobody gains a point because both you and the computer chose " + yourChoice + ".")
        counter += 1
        ties += 1

def updateScoreboard():
    compScore_label['text'] = "Computer Score: " + str(compScore) + "\n Computer's Last Choice: " + compChoice
    yourScore_label['text'] = "Your Score: " + str(yourScore) + "\n Your Last Choice: " + yourChoice
    counter_label['text'] = "Rounds Played: " + str(counter) + "\n Tie Rounds: " + str(ties)

def rock():
    global yourChoice, compChoice
    compChoice = choices[random.randint(0,2)]
    yourChoice = "Rock"
    result(yourChoice,compChoice)
    updateScoreboard()
    
def paper():
    global yourChoice, compChoice
    compChoice = choices[random.randint(0,2)]
    yourChoice = "Paper"
    result(yourChoice,compChoice)
    updateScoreboard()

def scissors():
    global yourChoice, compChoice
    compChoice = choices[random.randint(0,2)]
    yourChoice = "Scissors"
    result(yourChoice,compChoice)
    updateScoreboard()

#rock button
rock_img = tk.PhotoImage(file = r"RPS gui/rock.png")
rock_btn = tk.Button(
        root, 
        image = rock_img, 
        command = rock
        )
rock_btn.grid(column = 0, row = 3, rowspan = 1,padx = 10)

#paper button
paper_img = tk.PhotoImage(file = r"RPS gui/paper.png")
paper_btn = tk.Button(
        root, 
        image = paper_img,
        command = paper
        )
paper_btn.grid(column = 2, row = 3, rowspan = 1, padx = 10)

# scissors button
scissors_img = tk.PhotoImage(file = r"RPS gui/scissors.png")
scissors_btn = tk.Button(
        root, 
        image = scissors_img, 
        command = scissors
        )
scissors_btn.grid(column = 4, row = 3, rowspan = 1, padx = 10)

root.mainloop() 
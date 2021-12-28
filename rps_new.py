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

# tkinter functions
def hide(widget): # the widget in the parameter
    widget.grid_forget()

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
# user score text
yourScore_label = tk.Label(
    root, 
    text = 'Your Score: ' + str(yourScore) + '\n Your Choice: ' + yourChoice,
    font = ("Times New Roman",12))
yourScore_label.grid(column = 0, row = 2, columnspan = 2)

# comp score text
compScore_label = tk.Label(
    root, 
    text = ('Computer Score: ' + str(compScore) + '\n Computer Choice: ' + compChoice),
    font = ("Times New Roman",12))
compScore_label.grid(column = 3, row = 2, columnspan = 2)

def result(yourChoice,compChoice):
    global compScore, yourScore, counter
    if (compChoice == "Rock" and yourChoice == "Scissors") or (compChoice == "Paper" and yourChoice == "Rock") or (compChoice =="Scissors" and yourChoice == "Paper"):
        print("You chose " + yourChoice + " and the computer chose " + compChoice + ". " + compChoice + " beats " + yourChoice + " so, the computer won.")
        showinfo("Computer Wins", "You chose " + yourChoice + " and the computer chose " + compChoice + ". " + compChoice + " beats " + yourChoice + " so, the computer won.")
        compScore += 1
        counter += 1
    elif (compChoice == "Scissors" and yourChoice == "Rock") or (compChoice == "Rock" and yourChoice == "Paper") or (compChoice =="Paper" and yourChoice == "Scissors"):
        print("You chose " + yourChoice + " and the computer chose " + compChoice + ". " + yourChoice + " beats " + compChoice + " so, you won.")
        showinfo("You win", "You chose " + yourChoice + " and the computer chose " + compChoice + ". " + yourChoice + " beats " + compChoice + " so, you won.")
        yourScore += 1
        counter += 1
    elif compChoice == yourChoice:
        print("Tie! Nobody gains a point because both you and the computer chose " + yourChoice + ".")
        showinfo("Tie", "Tie! Nobody gains a point because both you and the computer chose " + yourChoice + ".")

def updateScoreboard():
    compScore_label['text'] = 'Computer Score: ' + str(compScore) + '\n Computer Choice: ' + compChoice
    yourScore_label['text'] = 'Your Score: ' + str(yourScore) + '\n Your Choice: ' + yourChoice

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
def scissors():
    global yourChoice, compChoice
    compChoice = choices[random.randint(0,2)]
    yourChoice = "Scissors"
    result(yourChoice,compChoice)

#rock button
rock_img = tk.PhotoImage(file = r"RPS gui/rock.png")
rock_btn = tk.Button(
        root, 
        image = rock_img, 
        #command = rock
        )
rock_btn.grid(column = 0, row = 3, rowspan = 1,padx = 10)

#paper button
paper_img = tk.PhotoImage(file = r"RPS gui/paper.png")
paper_btn = tk.Button(
        root, 
        image = paper_img,
        #command = paper
        )
paper_btn.grid(column = 2, row = 3, rowspan = 1, padx = 10)

# scissors button
scissors_img = tk.PhotoImage(file = r"RPS gui/scissors.png")
scissors_btn = tk.Button(
        root, 
        image = scissors_img, 
        #command = scissors
        )
scissors_btn.grid(column = 4, row = 3, rowspan = 1, padx = 10)

root.mainloop() 
import random
import time
import tkinter as tk


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\n")
        time.sleep(1)
        t = t - 1
    return t

#Set the game's rule
    
def game(event=None):

    global game_answer, player_answer, tries_left, tries_print, status, catch

    p_answer = player_answer.get()
    answer = int(p_answer)


    if tries_left == 0:
        status.set("Vous avez perdu ...")
        return 0
    if game_answer == answer:
        status.set("Bonne réponse")
        main_color="green"
        window.config(bg="green")
        frame.config(bg="green")
        phrase.config(bg="green")
        stat.config(bg="green")
        tries_print_txt.config(bg="green")
        return 0
    if answer < game_answer:
        status.set("Your price is too low")
        tries_left = tries_left - 1
    if answer > game_answer:
        status.set("Your price is too high")
        tries_left= tries_left - 1
    tries_print.set(f"{tries_left} Tries left")


#Creates window

main_color = "#f5aa42"
window = tk.Tk()
window.geometry("700x300")
window.title("The price is right")
window.resizable(width=False, height=False)
window.config(bg=main_color)

#Frame 1

frame=tk.Frame(window)
frame.pack()
frame.config(bg=main_color)
frame.place(x=50, y=100)

#Set Tries Number

tries_left = 10

#Defines_answer

game_answer = random.randint(1, 100)

#Print catchphrase

catch = tk.StringVar()
catch.set("hello welcome to the Price is Right game, you need to guess the right price in 5 tries, the answer is between 0 and 100")
phrase = tk.Label(frame, textvariable=catch, bg=main_color, fg="blue")
phrase.pack()

#Player Answer

player_answer = tk.Entry(frame)
player_answer.bind('<Return>', game)
player_answer.pack()

#Create_Button

bouton = tk.Button(frame, text="Submit")
bouton.pack()

#Print status of answer

status = tk.StringVar()
status.set("Good luck have fun")
stat = tk.Label(frame, textvariable=status, bg=main_color, fg="blue")
stat.pack()

#Print remaining tries

tries_print = tk.StringVar()
tries_print.set("10 Tries left")
tries_print_txt = tk.Label(window, textvariable=tries_print, bg=main_color, fg="blue")
tries_print_txt.place(x=620, y=10)


window.mainloop()

import tkinter as tk
import random

#-------------------------------------------------------------------------

def print_matrix():
    print(" 1  2  3")
    print(" ⬇️  ⬇️  ⬇️")
    rownumber=1
    for row in grid_backend:
        print(f"{row}⬅️ {rownumber}\n")
        rownumber+=1

def O(row,column):
    grid[row][column]["text"]="🅾️"
    
def X(row,column):
    grid[row][column]["text"]="❌"

def restart():

    global count_internal
    count_internal=1
    global grid_backend
    grid_backend=[[0,0,0],[0,0,0],[0,0,0]] 
    for i in range(3):
                for j in range(3):
                    grid[i][j].config(state="normal")
                    grid[i][j].config(text=" ")
    chance["text"]="Player 1 - 🅾️"
    win["text"]=" "
    reset.config(state="disabled")

def clicked(button):
    global count_internal
    row=button.grid_info()["row"]
    column=button.grid_info()["column"]

    
    chance["text"]="Player 1 - 🅾️"
    grid_backend[row][column]=1
    O(row,column)
    print_matrix()
    result=win_check(player1,player2,count_internal)
        
    if count_internal>=3:
        if result==player1:
            win["text"]="PLAYER 1 🅾️ won"
        elif result==player2:
            win["text"]="COMPUTER ❌ won"
    if count_internal==9 and result==0:
        win["text"]="DRAW"
        reset.config(state="normal")   
    if result==player1 or result==player2 :
        for i in range(3):
            for j in range(3):
                grid[i][j].config(state="disabled")
        reset.config(state="normal")
    
    count_internal+=1   
    button.config(state="disabled")

    if result == player1 or count_internal>9:
        return
    
    avail=[]
    for i in range (3):
        for j in range (3):
            if grid_backend[i][j]==0:
                avail.append([i,j])
    index=random.choice(avail)
    row_comp,column_comp=index[0],index[1]
    chance["text"]="COMPUTER - ❌"
    grid_backend[row_comp][column_comp]=9 
    X(row_comp,column_comp)
    grid[row_comp][column_comp].config(state="disabled")
    print_matrix()
    
    avail.remove(index)
        
# win print #

    result=win_check(player1,player2,count_internal)
        
    if count_internal>=3:
        if result==player1:
            win["text"]="PLAYER 1 🅾️ won"
        elif result==player2:
            win["text"]="COMPUTER ❌ won"
    if count_internal==9 and result==0:
        win["text"]="DRAW"
        reset.config(state="normal")   
    if result==player1 or result==player2 :
        for i in range(3):
            for j in range(3):
                grid[i][j].config(state="disabled")
        reset.config(state="normal")
    
    count_internal+=1   
    button.config(state="disabled")        
                   
def win_check(player1,player2,count):

#horizntal check

    for i in range(3):
        sum=0
        for j in range(3):
            sum+=grid_backend[i][j]
        if count>=3:
            if sum==player1*3:
                return player1
            elif sum==player2*3:
                return player2
        else:
            break

#vertical check

    for i in range(3):
        sum=0
        for j in range(3):
            sum+=grid_backend[j][i]
        if count>=3:
            if sum==player1*3:
                return player1
            elif sum==player2*3:
                return player2
        else:
            break           
            
#diagonal checks
    if count>=3:
        if grid_backend[0][0]+grid_backend[1][1]+grid_backend[2][2]==player1*3:
            return player1
        elif grid_backend[0][0]+grid_backend[1][1]+grid_backend[2][2]==player2*3:
            return player2
        elif grid_backend[0][2]+grid_backend[1][1]+grid_backend[2][0]==player1*3:
            return player1
        elif grid_backend[0][2]+grid_backend[1][1]+grid_backend[2][0]==player2*3:
            return player2
    return 0

#-------------------------------------------------------------------------

#window buildup #
main_game_window=tk.Tk()
main_game_window.title("Tic Tac Toe")

main_game_window.geometry("400x400")

header=tk.Frame(main_game_window)
header.pack()
buttons=tk.Frame(main_game_window)
buttons.pack()
player1=1
player2=9
game_title=tk.Label(header, text="🅾️ - ❌", font=("Arial" , 16 , "bold") , pady=0)
game_title.pack()
chance=tk.Label(header, text="Chance", font=("Arial" , 16 , "bold"),pady=5)
chance.pack()
reset=tk.Button(header , text="Restart" ,font=("Arial" , 16 , "bold"),command=restart)
reset.pack()
reset.config(state="disabled")



button1=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button1))
button2=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button2))
button3=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button3))
button4=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button4))
button5=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button5))
button6=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button6))
button7=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button7))
button8=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button8))
button9=tk.Button(buttons, text=" " ,font=("Arial" , 16 , "bold"),height=3 , width=3, command=lambda : clicked(button9))

button1.grid(row=0, column=0 , padx=2 , pady=2)
button2.grid(row=0, column=1 , padx=2 , pady=2)
button3.grid(row=0, column=2 , padx=2 , pady=2)
button4.grid(row=1, column=0 , padx=2 , pady=2)
button5.grid(row=1, column=1 , padx=2 , pady=2)
button6.grid(row=1, column=2 , padx=2 , pady=2)
button7.grid(row=2, column=0 , padx=2 , pady=2)
button8.grid(row=2, column=1 , padx=2 , pady=2)
button9.grid(row=2, column=2 , padx=2 , pady=2)

win=tk.Label(header, text=" ", font=("Arial" , 16 , "bold"),pady=0)
win.pack()

count_internal=1
grid=[[button1,button2,button3] ,[button4,button5,button6],[button7,button8,button9]]
grid_backend=[[0,0,0],[0,0,0],[0,0,0]] 

main_game_window.mainloop()

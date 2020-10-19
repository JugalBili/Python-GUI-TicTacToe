# -*- coding: utf-8 -*-

""" Tic Tac Toe GUI """
import random 
from tkinter import *
from tkinter import messagebox

class TicTac():
    
    def __init__(self, root, type):
        
        self.window = Toplevel()
        self.window.geometry("380x400")
        
    
        self.grid = [0,0,0,
                     0,0,0,
                     0,0,0]
        self.available = [1,2,3,4,5,6,7,8,9]
        self.combinations = [0,1,2,3,4,5,6,7,8,0,3,6,1,4,7,2,5,8,0,4,8,2,4,6]
        self.type = type 
        
        self.x_photo = PhotoImage(file = "images/x.png")
        self.o_photo = PhotoImage(file = "images/o.png")
        self.turn = 1
        self.win = False
        
        self.btn_1 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(1))
        self.btn_2 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(2))
        self.btn_3 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(3))
        self.btn_4 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(4))
        self.btn_5 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(5))
        self.btn_6 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(6))
        self.btn_7 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(7))
        self.btn_8 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(8))
        self.btn_9 = Button(self.window, padx= 50, pady = 40, command = lambda: self.selected_box(9))
     
        self.display = Entry(self.window, justify = CENTER, width = 50, state = DISABLED)
        
        Label(self.window, pady = 5).grid(row = 0, column = 0, columnspan = 3)
        Label(self.window, padx = 10).grid(row = 1, column = 0, rowspan = 3)
        self.btn_1.grid(row = 1, column = 1)
        self.btn_2.grid(row = 1, column = 2)
        self.btn_3.grid(row = 1, column = 3)
        self.btn_4.grid(row = 2, column = 1)
        self.btn_5.grid(row = 2, column = 2)
        self.btn_6.grid(row = 2, column = 3)
        self.btn_7.grid(row = 3, column = 1)
        self.btn_8.grid(row = 3, column = 2)
        self.btn_9.grid(row = 3, column = 3)
        Label(self.window, pady = 5).grid(row = 4, column = 0, columnspan = 3)
        self.display.grid(row = 5, column = 1, columnspan = 3)
        
        self.display.config(state = NORMAL)
        self.display.insert(0, "Player 1 Turn")   
        self.display.config(state = DISABLED)
     
    
    def win_check(self):
        
        if(self.turn % 2 == 0): 
            letter = "O"
            if (self.type == "bot"): 
                winner = "Bot"
            else:  
                winner = "Player 2"
        else: 
            letter = "X"
            winner = "Player 1"
        
        x = 0

        while x <= 21: 
        
            slot_1 = self.combinations[x]
            slot_2 = self.combinations[x+1] 
            slot_3 = self.combinations[x+2]
            
            if (self.grid[slot_1] == self.grid[slot_2]) and (self.grid[slot_2] == self.grid[slot_3]) and (self.grid[slot_3] == letter):
                
                self.win = True 
                
                if (slot_1 == 0) or (slot_2 == 0) or (slot_3 == 0):
                    self.btn_1.config(bg = "#4BEA5D")
                if (slot_1 == 1) or (slot_2 == 1) or (slot_3 == 1):
                    self.btn_2.config(bg = "#4BEA5D")
                if (slot_1 == 2) or (slot_2 == 2) or (slot_3 == 2):
                    self.btn_3.config(bg = "#4BEA5D")   
                if (slot_1 == 3) or (slot_2 == 3) or (slot_3 == 3):
                    self.btn_4.config(bg = "#4BEA5D")
                if (slot_1 == 4) or (slot_2 == 4) or (slot_3 == 4):
                    self.btn_5.config(bg = "#4BEA5D")
                if (slot_1 == 5) or (slot_2 == 5) or (slot_3 == 5):
                    self.btn_6.config(bg = "#4BEA5D")
                if (slot_1 == 6) or (slot_2 == 6) or (slot_3 == 6):
                    self.btn_7.config(bg = "#4BEA5D")
                if (slot_1 == 7) or (slot_2 == 7) or (slot_3 == 7):
                    self.btn_8.config(bg = "#4BEA5D")
                if (slot_1 == 8) or (slot_2 == 8) or (slot_3 == 8):
                    self.btn_9.config(bg = "#4BEA5D")   
                 
                
                self.btn_1.config(state = DISABLED)
                self.btn_2.config(state = DISABLED)
                self.btn_3.config(state = DISABLED)
                self.btn_4.config(state = DISABLED)
                self.btn_5.config(state = DISABLED)
                self.btn_6.config(state = DISABLED)
                self.btn_7.config(state = DISABLED)
                self.btn_8.config(state = DISABLED)
                self.btn_9.config(state = DISABLED)
                
                messagebox.showinfo("Winner", winner+" Wins!", parent = self.window)
                
                break 
            
            elif(x == 21 and not self.available):
            
                self.win == False
                messagebox.showinfo("Draw"," It is a Draw :(", parent = self.window) 
                
                break
            
            else: 
                self.win = False
                x += 3   
            
 
        
    
    def selected_box(self, num):
        
        #print(self.turn)
        
        if(self.turn % 2 == 0): 
            letter = "O"
            photo = self.o_photo
        else: 
            letter = "X"
            photo = self.x_photo
        
        if(num == 1):
            self.btn_1.config(image = photo)
            self.btn_1.config(state = DISABLED)
            self.grid[0] = letter
            self.available.remove(1)
            
        if(num == 2):
            self.btn_2.config(image = photo)
            self.btn_2.config(state = DISABLED)
            self.grid[1] = letter
            self.available.remove(2)
            
        if(num == 3):
            self.btn_3.config(image = photo)
            self.btn_3.config(state = DISABLED)
            self.grid[2] = letter
            self.available.remove(3)
            
        if(num == 4):
            self.btn_4.config(image = photo)
            self.btn_4.config(state = DISABLED)
            self.grid[3] = letter
            self.available.remove(4)
            
        if(num == 5):
            self.btn_5.config(image = photo)
            self.btn_5.config(state = DISABLED)
            self.grid[4] = letter
            self.available.remove(5)
            
        if(num == 6):
            self.btn_6.config(image = photo)
            self.btn_6.config(state = DISABLED)
            self.grid[5] = letter
            self.available.remove(6)
            
        if(num == 7):
            self.btn_7.config(image = photo)
            self.btn_7.config(state = DISABLED)
            self.grid[6] = letter
            self.available.remove(7)
            
        if(num == 8):
            self.btn_8.config(image = photo)
            self.btn_8.config(state = DISABLED)
            self.grid[7] = letter
            self.available.remove(8)
            
        if(num == 9):
            self.btn_9.config(image = photo)
            self.btn_9.config(state = DISABLED)
            self.grid[8] = letter
            self.available.remove(9)
        
        self.win_check()
        if self.win == False: 
         
            if (self.type == "bot"): 
            
                if(self.turn % 2 != 0 and self.available):
                    self.turn = self.turn + 1
                    self.display.config(state = NORMAL)
                    self.display.delete(0,END)
                    self.display.insert(0, "Bot Turn")   
                    self.display.config(state = DISABLED)
                    self.bot_choose()
                else:
                    self.turn = self.turn + 1    
          
            elif(self.type == "player"):
                self.turn = self.turn + 1
                
                if(self.turn % 2 != 0): 
                    self.display.config(state = NORMAL)
                    self.display.delete(0,END)
                    self.display.insert(0, "Player 1 Turn")   
                    self.display.config(state = DISABLED)
                
                else: 
                    self.display.config(state = NORMAL)
                    self.display.delete(0,END)
                    self.display.insert(0, "Player 2 Turn")   
                    self.display.config(state = DISABLED)
                pass 
         
    def bot_choose(self):
        
        choice = random.randint(0,len(self.available)-1)
        #print(self.available)
        #print(self.available[choice])
        
        self.selected_box(self.available[choice])
               
        
        self.display.config(state = NORMAL)
        self.display.delete(0,END)
        self.display.insert(0, "Player 1 Turn")   
        self.display.config(state = DISABLED)
        
        self.turn = 1
        
                

if __name__ == "__main__":
    
    root = Tk()
    root.geometry("200x200")
    
    lbl_title = Label(root, text = "Tic Tac Toe", font = ("", 16, "bold"), fg = "Red", pady = 20)
    btn_bot = Button(root, text = "Player vs Bot", pady = 5, command = lambda: TicTac(root, "bot")) 
    btn_human = Button(root, text = "Player vs Player", pady = 5, command = lambda: TicTac(root, "player")) 
    
    lbl_title.pack()
    btn_bot.pack()
    Label(root, pady = 1).pack()
    btn_human.pack()
    
    root.mainloop()
import tkinter as tk 
import random
import time

available = [1,2,3,4,5,6,7,8,9]
X = [1,4,8]
O = [1,4,8]

x0 =0
y0=150
y1=150
x1=290

def check():
	X.sort()
	O.sort()
	update_button('X',button1)
	if len(X) == 3:
		if X[1] - X[0] == 3 and X[2] - X[1] == 3:
			#button.destroy()
			button1.destroy()
			button2.destroy()
			button3.destroy()
			button4.destroy()
			button5.destroy()
			button6.destroy()
			button7.destroy()
			button8.destroy()
			button9.destroy()
			jk.create_text(150,50,text='X wins', fill='red')
			jk.pack()
	if len(O) == 3:
		if O[1] - O[0] == 3 and O[2] - O[1] == 3:
			button1.destroy()
			button2.destroy()
			button3.destroy()
			button4.destroy()
			button5.destroy()
			button6.destroy()
			button7.destroy()
			button8.destroy()
			button9.destroy()
			jk.create_text(150,50,text='O wins', fill='blue')
			jk.pack()
		#update_button('X',button1,0,10)
			
def update_button(player, button):
	if button == 1:
		dabutton = locals()['button'+ str(cpuchoice)]
	else:
		dabutton = button
		
	if dabutton.cget('text') == "X" or dabutton.cget('text') == "O":
		pass
	else:
		dabutton.config(text=player)

	
def cpu():
	global cpuchoice 
	fakebutton = 1
	cpuchoice = random.choice(available)
	available.remove(cpuchoice)
	O.append(cpuchoice)
	globals()['button', cpuchoice] = cpuchoice 
	update_button('O', fakebutton)

def dagame():
	play.destroy()
	w.destroy()
	line = jk.create_line(x0, y0-50, x1, y1-50, fill="black")
	line2 = jk.create_line(x0, y0+50, x1, y1+50, fill = "black")
	line3 = jk.create_line(y0-50, x0, y1-50, x1)
	line4 = jk.create_line(y0+50, x0, y1+50, x1)
	jk.place(relx=5, rely=5, anchor="center")
	jk.pack() 

def main():
	check()
	cpu()
	
def dagame2():
	global button1, button2, button3, button4, button5, button6, button7, button8, button9
	play.destroy()
	w.destroy()
	button1 = tk.Button(TTT,  width= 300%9, height= 300%9, command=main)
	button2 = tk.Button(TTT,  width= 300%9, height= 300%9)
	button3 = tk.Button(TTT,  width= 300%9, height= 300%9)
	button4 = tk.Button(TTT,  width= 300%9, height= 300%9)
	button5 = tk.Button(TTT,  width= 300%9, height= 300%9)
	button6 = tk.Button(TTT,  width= 300%9, height= 300%9)
	button7 = tk.Button(TTT,  width= 300%9, height= 300%9)
	button8 = tk.Button(TTT,  width= 300%9, height= 300%9)
	button9 = tk.Button(TTT,  width= 300%9, height= 300%9)
	
	button1.place(x = 0, y = 10)
	
	button2.place(x = 130, y = 10)
	button3.place(x = 260, y = 10)
	button4.place(x = 0, y = 150)
	
	button5.place(x = 130, y = 150)
	button6.place(x = 260, y = 150)
	button7.place(x = 0, y = 290)
	
	button8.place(x = 130, y = 290)
	button9.place(x = 260, y = 290)
	
TTT = tk.Tk()
w = tk.Canvas (TTT, width = 300, height = 300)
jk = tk.Canvas (TTT, width = 300, height = 300)
w.create_text(150, 50, text= "TIC-TAC-TOE ")
play = tk.Button(TTT, text = "Play", command=dagame2)

menu = tk.Menu(TTT)
TTT.config(menu=menu)
Gamemenu = tk.Menu(menu)
menu.add_cascade(label='Game', menu=Gamemenu)
Gamemenu.add_command(label='New')
Gamemenu.add_command(label='Restart')
Gamemenu.add_separator()
Gamemenu.add_command(label='Exit', command=TTT.quit)

w.pack()
play.pack()
TTT.geometry("250x250+10+10")
TTT.mainloop()
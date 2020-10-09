from tkinter import *
import tkinter.messagebox
import re
import time
from math import *
from math import pi as π
from random import *

win = Tk()
win.geometry("500x880")

click = True
click2 = True
operator = ""

var = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
text_in = StringVar()
butn = StringVar()
playerX = IntVar()
playerO = IntVar()
player1 = IntVar()
player2 = IntVar()
OVpoint1 = IntVar()
OVpoint2 = IntVar()
score = IntVar()
score1 = IntVar()
var6 = StringVar()


playerX.set(0)
playerO.set(0)
player1.set(20)
player2.set(10)
OVpoint1.set(0)
OVpoint2.set(0)



#-----------------Rpss page----------------#
rock1 = "ROCK       "
paper1 = "PAPER      "
scissors1 = "SCISSORS"
shoe1 = "SHOE       "

def rpss():
	frame9 = Frame(win, bg="cornsilk2", width=480, height=850, bd=10, relief="sunken")
	frame9.place(x=0, y=0)

	btn19 = Button(frame9, text="HOME PAGE", bg="cornsilk3", fg="#000", relief="flat", width=9, activebackground="cornsilk2", activeforeground="#000", command=homePage)
	btn19.place(x=280, y=10)

def reset():
	lbl9 = Label(frame9, text="                           ", bg="cornsilk2", relief="flat")
	lbl9.place(x=170, y=270)

	lbl10 = Label(frame9, text="                           ",bg="cornsilk2", relief="flat")
	lbl10.place(x=170, y=400)

	lbl11 = Label(frame9, text="                                                      ", bg="cornsilk2", relief="flat", height=2)
	lbl11.place(x=100, y=510)
	player1.set(20)
	player2.set(10)
	OVpoint1.set(0)
	OVpoint2.set(0)

def NewGame():
	lbl9 = Label(frame9, text="                           ", bg="cornsilk2", relief="flat")
	lbl9.place(x=170, y=270)

	lbl10 = Label(frame9, text="                           ",bg="cornsilk2", relief="flat")
	lbl10.place(x=170, y=400)

	lbl11 = Label(frame9, text="                                                      ", bg="cornsilk2", relief="flat", height=2)
	lbl11.place(x=100, y=510)
	player1.set(20)
	player2.set(10)

def point1():
	n = float(player1.get())
	sco = (n - 1)
	score.set(int(sco))
	player1.set(score.get())

	if player1.get() == 0:
		tkinter.messagebox.showinfo("Player 2 won!!!", f"player1= {player1.get()}\nplayer2 = {player2.get()}")
	NewGame()
	n3 = score1.get()
	sco3 = OVpoint2.get() + n3
	OVpoint2.set(sco3)

def point2():
n1 = float(player2.get())
sco1 = (n1-1)
score1.set(int(sco1))
player2.set(score1.get())

if player2.get() == 0:
tkinter.messagebox.showinfo("Player1 won!!!", f"player1 = {player1.get()}\nplayer2 = {player2.get()}")
NewGame()
n3 = score.get()
sco3 = OVpoint1.get() + n3
OVpoint1.set(sco3)

def sco():
label6 = Label(frame9,text="MATCHED✓✓✓", font=("times", 13, "bold"), fg="green",bg="cornsilk2", relief="flat")
label6.place(x=130, y=510)

def loss():
label7 = Label(frame9,text="WRONG!!!              ", font=("times", 13, "bold"), fg="red", bg="cornsilk2", relief="flat")
label7.place(x=130, y=510)

def com():
r = randint(0, 3)
label5 = Label(frame9,textvariable=var6, font=("times", 12, "italic"), fg="black", bg="cornsilk2", relief="flat")
label5.place(x=170, y=390)
if r == 0:
var6.set("ROCK")
elif r == 1:
var6.set("PAPER")
elif r == 2:
var6.set("SCISSORS")
elif r == 3:
var6.set("SHOE")

def rock():
label = Label(frame9, text=rock1, font=("times", 12, "italic"), fg="black", bg="cornsilk2", relief="flat")
label.place(x=170, y=260)
com()
if (label["text"]==rock1 and var6.get()=="ROCK"):
sco()
point2()
else:
loss()
point1()

def paper():
label2 = Label(frame9,text=paper1, font=("times", 12, "italic"), fg="black", bg="cornsilk2", relief="flat")
label2.place(x=170, y=260)
com()
if (label2["text"]==paper1 and var6.get()=="PAPER"):
sco()
point2()
else:
loss()
point1()

def scissors():
label3 = Label(frame9, text=scissors1, font=("times", 12, "italic"), fg="black", bg="cornsilk2", relief="flat")
label3.place(x=170, y=260)
com()
if (label3["text"]==scissors1 and var6.get()=="SCISSORS"):
sco()
point2()
else:
loss()
point1()

def shoe():
label4 = Label(frame9, text=shoe1, font=("times", 12, "italic"), fg="black", bg="cornsilk2", relief="flat")
label4.place(x=170, y=260)
com()
if (label4["text"]==shoe1 and var6.get()=="SHOE"):
sco()
point2()
else:
loss()
point1()

lbl1 = Label(frame9, text="Rock-Paper-Scissors-Shoe", font=("helvetica", 13,"bold"), fg="black", bg="cornsilk2", relief="flat")
lbl1.place(x=5, y=60)

btn1 = Button(frame9, text="Rock", bg="grey",fg="white", relief="raised", width=5, height=2, activebackground="green3", bd=4, command=rock)
btn1.place(x=0, y= 600)

btn2 = Button(frame9, text="Paper", bg="grey", fg="white", relief="raised", width=5, height=2, activebackground="green3", bd=4, command=paper)
btn2.place(x=170, y=600)

btn3 = Button(frame9,text="Scissors", bg="grey", fg="white", relief="raised", width=5, height=2, activebackground="green3", bd=4, command=scissors)
btn3.place(x=340, y=600)

btn4 = Button(frame9, text="Shoe", bg="grey", fg="white", relief="raised", width=17, height=2, activebackground="green3", bd=4, command=shoe)
btn4.place(x=100, y=690)

lbl2 = Label(frame9, text="Player 1>>>", font=("times", 10, 'bold'), fg="black", bg="cornsilk2", relief="flat")
lbl2.place(x=0, y=260)

lbl3 = Label(frame9, text="Player 2>>>", font=("times", 10, "bold"), fg="black", bg="cornsilk2", relief="flat")
lbl3.place(x=0, y=400)

lbl4 = Label(frame9, text="Points = ", font=("times", 10), fg="black", bg="cornsilk2", relief="flat")
lbl4.place(x=0, y=320)

lbl5 = Label(frame9, text="Points =", font=("times", 10), fg="black", bg="cornsilk2", relief="flat")
lbl5.place(x=0, y=460)

lbl6 = Label(frame9,  textvariable=player1, font=("helvetica", 10, "bold"), bg="cornsilk2", fg="black", relief="flat")
lbl6.place(x=120, y=320)

lbl7 = Label(frame9,textvariable=player2, font=("helvetica", 10, "bold"), bg="cornsilk2", fg="black", relief="flat")
lbl7.place(x=120, y=460)

btn5 = Button(frame9, text="New Game", fg="white", bd=2, height=1, width=5, bg="grey", relief="raised", activebackground="black", activeforeground="white", command=NewGame)
btn5.place(x=10, y=160)

lbl8 = Label(frame9, text="Overall Points = ", font = ("times", 10), bg="cornsilk2", fg="black", relief="flat")
lbl8.place(x=180, y=320)

lbl9 = Label(frame9, text="Overall Points = ", font = ("times", 10), bg="cornsilk2", fg="black", relief="flat")
lbl9.place(x=180, y=460)

lbl10 = Label(frame9, textvariable=OVpoint1, font = ("helvetica", 10, "bold"), bg="cornsilk2", fg="black", relief="flat")
lbl10.place(x=410, y=320)

lbl11 = Label(frame9, textvariable=OVpoint2, font=("helvetica", 10, "bold"), bg="cornsilk2", fg="black", relief="flat")
lbl11.place(x=410, y=460)

btn6 = Button(frame9, text="Reset", fg="white", bd=2, height=1, width=5, bg="grey", relief="raised", activebackground="black", activeforeground="white", command=reset)
btn6.place(x=330, y=160)

#---------------Rpss page end-----------#

#----simultaneous equation page----#
def sim():
frame8 = Frame(win, bg="cornsilk2", width=480, height=850, bd=10, relief="sunken")
frame8.place(x=0, y=0)

btn18 = Button(frame8, text="HOME PAGE", bg="cornsilk3", fg="#000", relief="flat", width=9, activebackground="cornsilk2", activeforeground="#000", command=homePage)
btn18.place(x=280, y=10)

lebel=Label(frame8,text="Simultaneous Equation Solver",  relief="flat", bg="cornsilk2", fg="black", font=("arial black", 11, "bold"))
lebel.place(x=15, y=70)

lebel2 = Label(frame8, text="a(x) + b(y) = c", bg="cornsilk2", relief="flat", fg="grey", font=("helvetica", 10, "italic"))
lebel2.place(x=10, y=120)

lebel3 = Label(frame8, text="and    d(x) + e(y) = f", bg="cornsilk2", relief="flat", fg="grey", font=("helvetica", 10, "italic"))
lebel3.place(x=200, y=120)

lebel4 = Label(frame8, text="value of a", fg="grey", relief="flat", bg="cornsilk2", font=("time new roman", 10))
lebel4.place(x=0, y=280)

lebel5 = Label(frame8, text="value of b", fg="grey", relief="flat", bg="cornsilk2",font=("time new roman", 10))
lebel5.place(x=0, y=370)

lebel6 = Label(frame8, text="value of c", fg="grey", relief="flat", bg="cornsilk2",font=("time new roman", 10))
lebel6.place(x=0, y=470)

lebel7 = Label(frame8, text="value of d", fg="grey", relief="flat", bg="cornsilk2",font=("time new roman", 10))
lebel7.place(x=250, y=280)

lebel8 = Label(frame8, text="value of e", fg="grey", relief="flat", bg="cornsilk2", font=("time new roman", 10))
lebel8.place(x=250, y=370)

lebel9 = Label(frame8, text="value of f", fg="grey", relief="flat", bg="cornsilk2", font=("time new roman", 10))
lebel9.place(x=250, y=470)

entry = Entry(frame8, bd=3, width=4, bg="cornsilk2")
entry.place(x=130, y=280)

entry1 = Entry(frame8, bd=3, width=4, bg="cornsilk2")
entry1.place(x=130, y=370)

entry2 = Entry(frame8, bd=3, width=4, bg="cornsilk2")
entry2.place(x=130, y=470)

entry3 = Entry(frame8, bd=3, width=4, bg="cornsilk2")
entry3.place(x=380, y=280)

entry4 = Entry(frame8, bd=3, width=4, bg="cornsilk2")
entry4.place(x=380, y=370)

entry5 = Entry(frame8, bd=3, width=4, bg="cornsilk2")
entry5.place(x=380, y=470)

def result():
try:
#Using elimination method
a = float(entry.get())
b = float(entry1.get())
c = float(entry2.get())
d = float(entry3.get())
e = float(entry4.get())
f = float(entry5.get())
g = d*(a)
h = d*(b)
i = d*(c)
j = a *(d)
k = a*(e)
l = a *(f)
m = g-j
n = h - k
o = i - l
p = o/n
q = b * p
r = c - q
s = r / a
t = str(p)
u = str(s)
message = Message(frame8,textvariable=var2, font=("times", 10, "italic"), relief="groove", bg="cornsilk2", fg="grey",bd=5)
var2.set(f"x = {u}")
message.place(x=0, y=650)

message2 = Message(frame8,textvariable=var3, font=("times", 10, "italic"),bg="cornsilk2", fg="grey", bd=5, relief="groove")
var3.set(f"y = {t}")
message2.place(x=200, y=650)

label = Label(frame8,textvariable=var4, fg="grey", bg="cornsilk2", relief="flat", font=("helvetica", 10, "italic"))
var4.set(f"eq1--------> {entry.get()}x + ({entry1.get()}y) = {entry2.get()}      ")
label.place(x=0, y=170)

label2 = Label(frame8,textvariable=var5,fg="grey", bg="cornsilk2", relief="flat", font=("helvetica", 10, "italic"))
var5.set(f"eq2-------->  {entry3.get()}x + ({entry4.get()}y) = {entry5.get()}")
label2.place(x=0, y=210)
except:
message3 = Message(frame8,textvariable=var3, bd=3, relief="groove", bg="cornsilk2", fg="grey", font=("helvetica", 9, "bold"))
var3.set("ERROR!!!, CAN'T BE SOLVED      ")
message3.place(x=0, y=650)

message4 = Message(frame8,textvariable=var2, bd=3, relief="groove", bg="cornsilk2", fg="grey", font=("helvetica", 9, "bold"))
var2.set("ERROR!!!, CAN'T BE SOLVED      ")
message4.place(x=200, y=650)

label = Label(frame8,textvariable=var4, fg="grey", bg="cornsilk2", relief="flat", font=("helvetica", 10, "italic"))
var4.set(f"eq1--------> {entry.get()}x + ({entry1.get()}y) = {entry2.get()}      ")
label.place(x=0, y=170)

label2 = Label(frame8, textvariable=var5,fg="grey", bg="cornsilk2", relief="flat", font=("helvetica", 10, "italic"))
var5.set(f"eq2-------->  {entry3.get()}x + ({entry4.get()}y) = {entry5.get()}")
label2.place(x=0, y=210)

button = Button(frame8,text="SOLVE", bd=7, relief="raised", command= result, bg="grey", fg="white", activebackground="black", activeforeground="white")
button.place(x=170, y=550)

#-simultaneous equation page end-#

#--------quadratic equation page-----#
def qua():
frame7 = Frame(win, bg="grey", width=480, height=850, bd=10, relief="sunken")
frame7.place(x=0, y=0)

btn17 = Button(frame7, text="HOME PAGE", bg="grey", fg="#fff", relief="flat", width=9, activebackground="grey", activeforeground="#fff", command=homePage)
btn17.place(x=280, y=10)

var1 = StringVar()
label= Label(frame7, textvariable=var1, bg="grey", fg="#fff", relief="flat",font=("arial black", 10, "bold"))
var1.set("QUADRATIC EQUATION SOLVER")
label.place(x=20, y=90)

var2 = StringVar()
label2 = Label(frame7,textvariable=var2, relief="flat", font=("helvetica", 12, "italic"), bg="grey", fg="#fff")
var2.set("ax² + bx + c = 0")
label2.place(x=130, y=150)

lebel3 = Label(frame7, text="value of a", bg="grey", fg="#fff", relief="flat",font=("time new roman", 10))
lebel3.place(x=0, y=320)

lebel4= Label(frame7, text="value of b",bg="grey", fg="#fff", relief="flat", font=("time new roman", 10))
lebel4.place(x=0, y=420)

lebel5= Label(frame7, text="value of c", bg="grey", fg="#fff", relief="flat", font=("time new roman", 10))
lebel5.place(x=0, y=520)

ent= Entry(frame7, bd=3, width=4, bg="grey", fg="#fff")
ent.place(x=130, y=320)

ent1= Entry(frame7, bd=3, width=4, bg="grey", fg="#fff")
ent1.place(x=130, y=420)

ent2 = Entry(frame7, bd=3, width=4, bg="grey", fg="#fff")
ent2.place(x=130, y=520)

def result():
try:
#using general formular
a = ent.get()
b = ent1.get()
c = ent2.get()
k= float(a)
y=float(b)
z=float(c)
d = (-y)**2
e = 4*k*z
f = d - e
g = abs(f)
h = sqrt(g)
i = 2 * k
j = -y + h
l = -y - h
m = j/i
n = l / i
o = str(m)
p = str(n)
varA=StringVar()
var3 = StringVar()

label = Label(frame7,textvariable=var3, fg="#fff", bg="grey", relief="flat", font=("helvetica", 12, "italic"))
var3.set(f"{ent.get()}x² + ({ent1.get()}x) + ({ent2.get()}) = 0   ")
label.place(x=110, y=200)

message= Message(frame7,textvariable=varA, bg="grey", fg="#fff", relief="flat",font=("times", 8, "italic"))
varA.set(f"x = {o}\n\nx = {p}        \n")
message.place(x=190, y=350)
except:
var2=StringVar()
var3 = StringVar()
message2 = Message(frame7, textvariable=var2, bg="grey", fg="#fff", relief="flat",font=("helvetica", 10, "bold"))
var2.set("ERROR!!!, CAN'T BE SOLVED\n\n\n")
message2.place(x=195, y=350)

label = Label(frame7,textvariable=var3, fg="#fff", bg="grey", relief="flat", font=("helvetica", 12, "italic"))
var3.set(f"{ent.get()}x² + ({ent1.get()}x) + ({ent2.get()}) = 0   ")
label.place(x=110, y=200)

button= Button(frame7,text="SOLVE", bd=10,relief="groove", bg="#000", fg="white",activebackground="grey", activeforeground="white", command = result)
button.place(x=170, y=600)

#----quadratic equation page end---#

#-------------tic tac toe page--------#
def ticTac():

frame6 = Frame(win, bg="cornsilk", width=480, height=850, bd=10, relief="sunken")
frame6.place(x=0, y=0)

btn16 = Button(frame6, text="HOME PAGE", bg="cornsilk2", fg="#000", relief="flat", width=9, activebackground="cornsilk2", activeforeground="#000", command=homePage)
btn16.place(x=280, y=10)

def NewGame():
btn1["text"], btn1["bg"], btn1["activebackground"] = "", "grey", "grey"
btn2["text"], btn2["bg"], btn2["activebackground"] = "", "grey", "grey"
btn3["text"], btn3["bg"], btn3["activebackground"]= "", "grey", "grey"
btn4["text"], btn4["bg"], btn4["activebackground"] = "", "grey", "grey"
btn5["text"], btn5["bg"], btn5["activebackground"] = "", "grey", "grey"
btn6["text"], btn6["bg"], btn6["activebackground"] = "", "grey", "grey"
btn7["text"], btn7["bg"], btn7["activebackground"] = "", "grey", "grey"
btn8["text"], btn8["bg"], btn8["activebackground"] = "", "grey", "grey"
btn9["text"], btn9["bg"], btn9["activebackground"] = "", "grey", "grey"
def reset():
NewGame()
playerX.set(0)
playerO.set(0)

def scoX():
n = float(playerX.get())
sco = (n + 1)
score = int(sco)
playerX.set(score)

def scoO():
n = float(playerO.get())
sco = (n + 1)
score = int(sco)
playerO.set(score)

def des():
if (btn1["text"]=="X" and btn2["text"]== "X" and btn3["text"]=="X"):
btn1["activebackground"] = "green"
btn2["activebackground"] = "green"
btn3["activebackground"] ="green"
btn1.config(bg="green")
btn2.config(bg="green")
btn3.config(bg="green")
scoX()
tkinter.messagebox.showinfo("Winner!!!", "X won")
NewGame()

elif (btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X"):
btn4["activebackground"]= "green"
btn5["activebackground"] = "green"
btn6["activebackground"] = "green"
btn4.config(bg="green")
btn5.config(bg="green")
btn6.config(bg="green")
scoX()
tkinter.messagebox.showinfo("Winner!!!", "X won")
NewGame()

elif (btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X"):
btn7["activebackground"]= "green"
btn8["activebackground"] = "green"
btn9["activebackground"] = "green"
btn7.config(bg="green")
btn8.config(bg="green")
btn9.config(bg="green")
scoX()
tkinter.messagebox.showinfo("Winner!!!", "X won")
NewGame()

elif (btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X"):
btn1["activebackground"]= "green"
btn4["activebackground"] = "green"
btn7["activebackground"] = "green"
btn1.config(bg="green")
btn4.config(bg="green")
btn7.config(bg="green")
scoX()
tkinter.messagebox.showinfo("Winner!!!", "X won")
NewGame()

elif (btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X"):
btn2["activebackground"]= "green"
btn5["activebackground"] = "green"
btn8["activebackground"] = "green"
btn2.config(bg="green")
btn5.config(bg="green")
btn8.config(bg="green")
scoX()
tkinter.messagebox.showinfo("Winner!!!", "X won")
NewGame()

elif (btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X"):
btn3["activebackground"]= "green"
btn6["activebackground"] = "green"
btn9["activebackground"] = "green"
btn3.config(bg="green")
btn6.config(bg="green")
btn9.config(bg="green")
scoX()
tkinter.messagebox.showinfo("Winner!!!", "X won")
NewGame()

elif (btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X"):
btn1["activebackground"]= "green"
btn5["activebackground"] = "green"
btn9["activebackground"] = "green"
btn1.config(bg="green")
btn5.config(bg="green")
btn9.config(bg="green")
scoX()
tkinter.messagebox.showinfo("Winner!!!", "X won")
NewGame()

elif (btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X"):
btn3["activebackground"]= "green"
btn5["activebackground"] = "green"
btn7["activebackground"] = "green"
btn3.config(bg="green")
btn5.config(bg="green")
btn7.config(bg="green")
scoX()
tkinter.messagebox.showinfo("Winner!!!", "X won")
NewGame()

def desO():
if (btn1["text"]=="O" and btn2["text"]== "O" and btn3["text"]=="O"):
btn1["activebackground"] = "red"
btn2["activebackground"] = "red"
btn3["activebackground"] ="red"
btn1.config(bg="red")
btn2.config(bg="red")
btn3.config(bg="red")
scoO()
tkinter.messagebox.showinfo("Winner!!!", "O won")
NewGame()

elif (btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O"):
btn4["activebackground"]= "red"
btn5["activebackground"] = "red"
btn6["activebackground"] = "red"
btn4.config(bg="red")
btn5.config(bg="red")
btn6.config(bg="red")
scoO()
tkinter.messagebox.showinfo("Winner!!!", "O won")
NewGame()

elif (btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O"):
btn7["activebackground"]= "red"
btn8["activebackground"] = "red"
btn9["activebackground"] = "red"
btn7.config(bg="red")
btn8.config(bg="red")
btn9.config(bg="red")
scoO()
tkinter.messagebox.showinfo("Winner!!!", "O won")
NewGame()

elif (btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O"):
btn1["activebackground"]= "red"
btn4["activebackground"] = "red"
btn7["activebackground"] = "red"
btn1.config(bg="red")
btn4.config(bg="red")
btn7.config(bg="red")
scoO()
tkinter.messagebox.showinfo("Winner!!!", "O won")
NewGame()

elif (btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O"):
btn2["activebackground"]= "red"
btn5["activebackground"] = "red"
btn8["activebackground"] = "red"
btn2.config(bg="red")
btn5.config(bg="red")
btn8.config(bg="red")
scoO()
tkinter.messagebox.showinfo("Winner!!!", "O won")
NewGame()

elif (btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O"):
btn3["activebackground"]= "red"
btn6["activebackground"] = "red"
btn9["activebackground"] = "red"
btn3.config(bg="red")
btn6.config(bg="red")
btn9.config(bg="red")
scoO()
tkinter.messagebox.showinfo("Winner!!!", "O won")
NewGame()

elif (btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O"):
btn1["activebackground"]= "red"
btn5["activebackground"] = "red"
btn9["activebackground"] = "red"
btn1.config(bg="red")
btn5.config(bg="red")
btn9.config(bg="red")
scoO()
tkinter.messagebox.showinfo("Winner!!!", "O won")
NewGame()

elif (btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"):
btn3["activebackground"]= "red"
btn5["activebackground"] = "red"
btn7["activebackground"] = "red"
btn3.config(bg="red")
btn5.config(bg="red")
btn7.config(bg="red")
scoO()
tkinter.messagebox.showinfo("Winner!!!", "O won")
NewGame()

def check(butn):
global click2
if butn["text"]==""and click2 == True:
butn["text"] = "X"
click2 = False
des()
elif butn["text"]=="" and click2 == False:
butn["text"] = "O"
click2 = True
desO()

btn1 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforeground="white", command= lambda: check(btn1))
btn1.place(x=70, y=230)

btn2 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforeground="white", command= lambda: check(btn2))
btn2.place(x=180, y=230)

btn3 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforeground="white", command= lambda: check(btn3))
btn3.place(x=290, y=230)

btn4 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforeground="white", command= lambda: check(btn4))
btn4.place(x=70, y=360)

btn5 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforeground="white", command= lambda:check(btn5))
btn5.place(x=180, y=360)

btn6 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforeground="white", command=lambda: check(btn6))
btn6.place(x=290, y=360)

btn7 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforeground="white", command= lambda: check(btn7))
btn7.place(x=70, y=490)

btn8 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforegroun="white", command=lambda: check(btn8))
btn8.place(x=180, y=490)

btn9 = Button(frame6, text="", bg="grey", fg="white", relief="flat", activebackground="grey", height=4, width=5, activeforeground="white", command=lambda: check(btn9))
btn9.place(x=290, y=490)

new = Button(frame6, text="New Game", bg="grey", fg="white", relief="raised", bd=5, height=1, width=6, activebackground="grey", command= NewGame)
new.place(x=300, y=640)

reset = Button(frame6, text="Reset", bg="grey", fg="white", relief="raised", bd=5, height=1, width=6, activebackground="grey", command=reset)
reset.place(x=30, y=640)

label = Label(frame6, text="TIC-TAC-TOE", font=("arial black", 12, "bold"), relief="flat", bg="cornsilk", fg="black")
label.place(x=120, y=70)

lbl2 = Label(frame6, text="PlayerX = ", font=("times", 10, "italic"), bg="cornsilk", relief="flat")
lbl2.place(x=10, y=150)

lbl3 = Label(frame6, text="PlayerO = ", font=("times", 10, "italic"), bg="cornsilk", relief="flat")
lbl3.place(x=270, y=150)

lbl4 = Label(frame6,textvariable=playerX, width=3, relief="flat", bg="cornsilk", font=("helvetica", 12, "italic"))
lbl4.place(x=135, y=145)

lbl5 = Label(frame6,textvariable=playerO, width=3, relief="flat", bg="cornsilk", font=("helvetica", 12, "italic"))
lbl5.place(x=400, y=145)

#----------tic tac toe page end-----#

#---------calculator page----------#
def calculator():

frame5 = Frame(win, width=480, height=850, bd=10, relief="sunken")
frame5.place(x=0, y=0)

btn15 = Button(frame5, text="HOME PAGE", fg="#000", relief="flat", width=9, activeforeground="#fff", command=homePage)
btn15.place(x=286, y=7)

def btnclk(num):
global operator
operator = operator + str(num)
text_in.set(operator)

def clear():
global operator
operator=""
text_in.set("")

def Equal():
try:
global operator
sum = str(eval(operator))
text_in.set(sum)
except:
text_in.set("SYNTAX ERROR")

def Sin():
try:
global operator
re = sin(eval(operator))
text_in.set(re)
except:
text_in.set("SYNTAX ERROR")

def Cos():
try:
global operator
re = cos(eval(operator))
text_in.set(re)
except:
text_in.set("SYNTAX ERROR")

def Tan():
try:
global operator
re= tan(eval(operator))
text_in.set(re)
except:
text_in.set("SYNTAX ERROR")

def sqr():
try:
global operator
re = sqrt(eval(operator))
text_in.set(re)
except:
text_in.set("SYNTAX ERROR")

def sq():
try:
global operator
y = int(operator)
re = pow(y, 2)
text_in.set(re)
except:
text_in.set("SYNTAX ERROR")

def func(bg, fg):
btnclear = Button(frame5,text="C", bg=bg, relief="sunken", bd=5, width=4, activebackground="green", fg=fg, command=clear)
btnclear.place(x=350, y=200)

btn_sin = Button(frame5,text="Sin", fg=fg, bg=bg, relief="sunken", width=3, height=2, bd=5, activebackground="green", command= Sin)
btn_sin.place(x=0, y=260)

btn_cos = Button(frame5,text="Cos", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command = Cos)
btn_cos.place(x=110, y=260)

btn_tan = Button(frame5,text="Tan", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command=Tan)
btn_tan.place(x=230, y=260)

btn_exp = Button(frame5,text="EXP", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk("*10**"))
btn_exp.place(x=350, y=260)

pi_btn = Button(frame5, text="π", fg=fg, bg=bg, relief="sunken", width=3, height=2, bd=5, activebackground="green", command=lambda: btnclk(π))
pi_btn.place(x=0, y=350)

ob_btn = Button(frame5, text="(", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command=lambda: btnclk("("))
ob_btn.place(x=110, y=350)

cb_btn = Button(frame5, text=")", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command = lambda: btnclk(")"))
cb_btn.place(x=230, y=350)

percen_btn = Button(frame5,text="%", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command=lambda: btnclk("/100"))
percen_btn.place(x=350, y=350)

bt7 = Button(frame5, text="7", fg=fg, bg=bg, relief="sunken", width=3, height=2, bd=5, activebackground="green", command= lambda: btnclk(7))
bt7.place(x=0, y=450)

bt8 = Button(frame5, text="8", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk(8))
bt8.place(x=110, y=450)

bt9 = Button(frame5, text="9", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk(9))
bt9.place(x=230, y=450)

divide = Button(frame5, text="/", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk("/"))
divide.place(x=350, y=450)

bt4 = Button(frame5, text="4", fg=fg, bg=bg, relief="sunken", width=3, height=2, bd=5, activebackground="green", command= lambda: btnclk(4))
bt4.place(x=0, y=550)

bt5 = Button(frame5, text="5", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command=lambda: btnclk(5))
bt5.place(x=110, y=550)

bt6 = Button(frame5,text="6", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk(6))
bt6.place(x=230, y=550)

times = Button(frame5, text="×", fg=fg,bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk("*"))
times.place(x=350, y=550)

bt1 = Button(frame5, text="1", fg=fg, bg=bg, relief="sunken", width=3, height=2, bd=5, activebackground="green", command= lambda: btnclk(1))
bt1.place(x=0, y=650)

bt2 = Button(frame5, text="2", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk(2))
bt2.place(x=110, y=650)

bt3 = Button(frame5, text="3", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk(3))
bt3.place(x=230, y=650)

minus = Button(frame5,text="-", fg=fg,bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk("-"))
minus.place(x=350, y=650)

dot = Button(frame5, text=".", fg=fg, bg=bg, relief="sunken", width=3, height=2, bd=5, activebackground="green", command=lambda: btnclk("."))
dot.place(x=0, y=750)

zero = Button(frame5, text="0", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk(0))
zero.place(x=110, y=750)

equal = Button(frame5, text="=", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= Equal)
equal.place(x=230, y=750)

plus= Button(frame5, text="+", fg=fg, bg=bg, relief="sunken", width=4, height=2, bd=5, activebackground="green", command= lambda: btnclk("+"))
plus.place(x=350, y=750)

label = Label(frame5,text="scientific calculator", bg=bg, fg=fg, bd=5, relief="groove")
label.place(x=60, y=15)

label1 = Label(frame5,text="Theme", fg=fg, bg=bg, bd=5, relief="groove")
label1.place(x=0, y=130)

root = Button(frame5, text="√", fg=fg, bg=bg, bd=5, width=3, relief="sunken", activebackground="green", command=sqr)
root.place(x=0, y=200)

square = Button(frame5,text="x²", fg=fg, bg=bg, bd=5, width=4,relief="sunken", activebackground="green", command=sq)
square.place(x=230, y=200)

def black():
func("black", "white")

def white():
func("white", "black")

def WB():
func("pink", "black")

def blue():
func("blue", "white")

def red():
func("cornsilk2", "black")

def default():
func("purple", "white")

if __name__ == "__main__":
default()

entry = Entry(frame5, bd=10, width=37, textvariable = text_in)
entry.place(x=0, y=70)

radio = Radiobutton(frame5, text="B", value=1, command=black)
radio.place(x=100, y=130)

radio2 = Radiobutton(frame5, text="W", value=2, command = white)
radio2.place(x=170, y=130)

radio3 = Radiobutton(frame5, text="pink", value=3, command=WB)
radio3.place(x=237, y=130)

radio4 = Radiobutton(frame5, text="blue", value=4, command=blue)
radio4.place(x=360, y=130)

radio5 = Radiobutton(frame5, text="milk", value=5, command=red)
radio5.place(x=300, y=160)

radio6 = Radiobutton(frame5, text="default", value=6, command=default)
radio6.place(x=100, y=165)

#-----------calculator page end-------#

#----------stop watch page--------#
def stopWatch():
frame4 = Frame(win, bg="#236144", width=480, height=850, bd=10, relief="sunken")
frame4.place(x=0, y=0)

btn11 = Button(frame4, text="HOME PAGE", bg="#236144", fg="#fff", relief="flat", width=9, activebackground="#236144", activeforeground="#fff", command=homePage)
btn11.place(x=280, y=10)

def donothing():
pass

def Fstart():
global click, sec, min, hour, chr
if click == False:
if click == False:
btn12["command"] = donothing
i = True
while i:
chr += 1
if chr == 90:
sec, chr = sec + 1, 0
elif sec == 60:
min, sec = min + 1, 0
elif min == 60:
hour, min = hour + 1, 0
i = False
var.set(f"{hour}  :  {min}  :  {sec}  :  {chr}")
lbl9.after(8, Fstart)
elif click == True:
btn12["command"] = start

def start():
global click, sec, min, hour, chr
if click == True:
if click == True:
btn12["command"] = donothing
i = True
while i:
chr += 1
if chr == 90:
sec, chr = sec + 1, 0
elif sec == 60:
min, sec = min + 1, 0
elif min == 60:
hour, min = hour + 1, 0
i = False
var.set(f"{hour}  :  {min}  :  {sec}  :  {chr}")
lbl9.after(8, start)
elif click == False:
btn12["command"] = startIt

def stop():
global click
if click == True:
click = False
elif click == False:
click = True

def startIt():
Fstart()

def reset():
stop()
global click, sec, min, hour, chr
i = True
while i:
chr *= 0
sec *= 0
min *= 0
hour *= 0
i = False
var.set(f"{hour}  :  {min}  :  {sec}  :  {chr}")


frame4a = Frame(frame4, bg="grey", width=150, height=70, bd=5, relief="sunken")
frame4a.place(x=3, y=410)

frame4b = Frame(frame4, bg="grey", width=150, height=70, bd=5, relief="sunken")
frame4b.place(x=153, y=410)

frame4c = Frame(frame4, bg="grey", width=150, height=70, bd=5, relief="sunken")
frame4c.place(x=303, y=410)

frame4d = Frame(frame4, bg="grey", width=455, height=90, bd=5, relief="sunken")
frame4d.place(x=3, y=320)

btn12 = Button(frame4a, text="Start", font=("helvetica", 12, "bold"), bg="grey", fg="white", relief="groove", width=4, activebackground="#000", activeforeground="#fff", command=start)
btn12.place(x=4, y=0)

btn13 = Button(frame4b, text="Stop", font=("helvetica", 12, "bold"), bg="grey", fg="white", relief="groove",width=4, activebackground="#000", activeforeground="#fff",command=stop)
btn13.place(x=4, y=0)

btn14 = Button(frame4c, text="Reset",font=("helvetica", 12, "bold"), bg="grey", fg="white", relief="groove",width=4, activebackground="#000", activeforeground="#fff", command=reset)
btn14.place(x=4, y=0)

lbl9 = Label(frame4d,textvariable=var, bg="#236144", bd=4, relief="sunken", width=29, height=2, fg="#fff", font=("helvetica", 10, "bold"))
var.set("0  :  0  :  0  :  0")
lbl9.place(x=0, y=0)

lbl8 = Label(frame4, text="STOP-WATCH", bg="#236144", fg="#34eab6",relief="flat", font=("Times", 14, "bold italic"))
lbl8.place(x=90, y=80)

#-----------stop watch page end-----#

#----------digital clock page---------#
def digitalClock():
frame3 = Frame(win, bg="#ccbabc", width=480, height=850, bd=10, relief="sunken")
frame3.place(x=0, y=0)

btn10 = Button(frame3, text="HOME PAGE", bg="#ccbabc", fg="#000", relief="flat", width=9, activebackground="#ccbabc", activeforeground="#000", command=homePage)
btn10.place(x=280, y=10)

lbl6 = Label(frame3, text = "DIGITAL CLOCK", fg="purple", bg="#ccbabc", font=("helvetica", 12, "bold"), relief="flat")
lbl6.place(x=110, y=90)

frame3a = Frame(frame3, bg="purple",bd=20,relief="groove")
lbl7 = Label(frame3a,bg="skyBlue1", font=("Times", 12, "italic"))
lbl7.pack()
frame3a.place(x=120, y=370)

def setTime():
getTime = time.strftime("%l : %M : %S")
lbl7.config(text=getTime)
lbl7.after(200,setTime)

if __name__=="__main__":
setTime()

#----------digital clock page end------#

#---------home page----------#
def homePage():
frame2 = Frame(win, bg="#dddeab", width=480, height=850, bd=10, relief="sunken")
frame2.place(x=0, y=0)

lbl4 = Label(frame2, text = "Welcome  to  MEGA-APP", fg="#000", bg="#dddeab", font=("black", 12, "bold"), relief="flat")
lbl4.place(x=40, y=50)

lbl5 = Label(frame2, text="Available Apps:", fg="#000", bg="#dddeab", font=("helvetiva", 10),relief="flat")
lbl5.place(x=10, y=170)

btn3 = Button(frame2, text="• TIC-TAC-TOE", fg="#000", bg="#dddeab", relief="flat", activebackground="#dddeab", activeforeground="#000", font=("Times", 9, "bold"), bd=3, command=ticTac)
btn3.place(x=0, y=270)

btn4 = Button(frame2, text="• Digital Clock", fg="#000", bg="#dddeab", relief="flat", activebackground="#dddeab", activeforeground="#000", font=("Times", 9, "bold"), bd=3, command = digitalClock)
btn4.place(x=0, y=340)

btn5 = Button(frame2, text="• Stop Watch", fg="#000", bg="#dddeab", relief="flat", activebackground="#dddeab", activeforeground="#000", font=("Times", 9, "bold"), bd=3, command=stopWatch)
btn5.place(x=0, y=410)

btn6 = Button(frame2, text="• Calculator", fg="#000", bg="#dddeab", relief="flat", activebackground="#dddeab", activeforeground="#000", font=("Times", 9, "bold"), bd=3, command=calculator)
btn6.place(x=0, y=480)

btn7 = Button(frame2, text="• Quadratic Equation Solver", fg="#000", bg="#dddeab", relief="flat", activebackground="#dddeab", activeforeground="#000", font=("Times", 9, "bold"), bd=3, command=qua)
btn7.place(x=0, y=550)

btn8 = Button(frame2, text="• Simultaneous Equation Solver", fg="#000", bg="#dddeab", relief="flat", activebackground="#dddeab", activeforeground="#000", font=("Times", 9, "bold"), bd=3, command=sim)
btn8.place(x=0, y=620)

btn9 = Button(frame2, text="• Rock-Paper-Scissors-Shoe", fg="#000", bg="#dddeab", relief="flat", activebackground="#dddeab", activeforeground="#000", font=("Times", 9, "bold"), bd=3, command=rpss)
btn9.place(x=0, y=690)

#---------home page end-------------#
chr = 0
min = 0
sec = 0
hour = 0

#-----------login page---------------#
frame1 = Frame(win, bg="#003366", width=480, height=850, bd=10, relief="sunken")
frame1.place(x=0, y=0)


lbl1 = Label(frame1, text="MEGA-APP", fg="#34eab6", bg="#003366", relief="flat", font=("arial black", 12, "bold"))
lbl1.place(x=140, y=50)

lbl2 = Label(frame1, text="User Name:", fg="#fff", bg="#003366", relief="flat", font=("helvetica", 10, "italic"))
lbl2.place(x=0, y=265)

lbl3 = Label(frame1, text="Password:", fg="white", bg="#003366", relief="flat", font=("helvetica", 10, "italic"))
lbl3.place(x=0, y=360)

entry1 = Entry(frame1, width=22, relief="sunken",fg="#000", font=("helvetica", 8, "italic"))
entry1.place(x=160, y=265)

entry2 = Entry(frame1, width=24, relief="flat", bg="white", fg="black", show="•")
entry2.place(x=155, y=365)

user1 = "kafeel kazeem"
user2 = "k"
pas1 = "78789898"
pas2 = "2"

def log():
if re.match(user1, entry1.get()) and re.match(pas1, entry2.get()) or re.match(user2, entry1.get()) and re.match(pas2, entry2.get()):
homePage()
else:
btn1["activebackground"] = "red"
btn1["activeforeground"] = "#fff"
tkinter.messagebox.askretrycancel("Error!!!", "wrong username or password")

def forget():
if entry1.get() == "kafeel kazeem" or "k":
tkinter.messagebox.showinfo("password", "78789898")
else:
tkinter.messagebox.showinfo("Warning!!!", "please input a valid user name")

btn1 = Button(frame1, text="Login", fg="white",bg="grey", bd=5, relief="ridge", width=7, activebackground="green3",  command=log)
btn1.place(x=160, y=470)

btn2 = Button(frame1, text="forgot password???", fg="silver", bg="#003366", relief="flat", activebackground="#003366", activeforeground="silver", command=forget)
btn2.place(x=3, y=600)
#-------------login page end--------------#

win.mainloop()
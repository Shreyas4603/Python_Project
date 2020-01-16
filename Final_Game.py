from tkinter import *
import random
from tkinter import messagebox


import os
uc = 0
cc = 0
gc = 0
ball=1 ### 1=user 0 = comp
root = Tk()
root.geometry("1400x1400")
root.maxsize(1400, 1400)
root.minsize(1400, 1400)
root.configure(background="BLACK")
global comment
global n
def rules():
    exec(open("rules_of_game.py").read())
def rules2():
    exec(open("rules_of_game.py").read())


def msgbox():

     MsgBox = messagebox.askquestion('Exit Application', 'Do you want to continue the game??',
                                        icon='warning')
     if MsgBox == 'yes' :
         win.destroy()
         root.state('zoomed')
     else :
        win.destroy()
        root.destroy()



def change(ch):
    global flag
    if ch=='u':
        flag=0##0
        moveball(1,'c')
    elif ch=='c':
        flag=1##1
        moveball(1,'u')



def goalwin(s) :
    root.wm_state('iconic')
    global win
    win = Tk()
    win.geometry("1152x648")
    win.title("GOAL WINDOW!!")
    win.minsize(1152, 648)
    win.maxsize(1152, 648)
    win.configure(background="BLACK")

    def goal(event) :
        global gcU
        global gcC

        n = event.widget.cget("text")
        displayu.configure(text=(n))
        un = int(n)
        cn = random.randint(2, 3)
        displayc.configure(text=str(cn))
        if s == 'u' :
            if un != cn :
                gcU = int(gcU) + 1
                gcountU.configure(text=str(gcU))
                combox.configure(text=('GOAL!!!!!! BY YOUUUU'))
                change('u')
                moveball(n)
                
                msgbox()
            elif cn == un :
                combox.configure(text="OHHH BLOCKED..!!!")
                change("u")#(who got blocked)
                moveball(str(0))
                
                msgbox()
            if gcC == 5 :
                comment.configure(text="Computer Won the Game")
                win.destroy()
            elif gcU == 5 :
                comment.configure(text="You Won the Game")
                win.destroy()





        if s == 'c' :
            if cn != un :
                gcC = int(gcC) + 1
                change('c')
                gcountC.configure(text=str(gcC))
                combox.configure(text='GOAL!!!!!! BY COMPUTER')
                moveball(n)
                
                msgbox()

            elif cn == un :
                combox.configure(text="OHHH BLOCKED..!!!")
                moveball(str(0))
                change('c')
                
                msgbox()

            if gcC == 5 :
                combox.configure(text="Computer Won the Game")
                win.update()
            elif gcU == 5 :
                combox.configure(text="You Won the Game")
                win.update()





    def moveball(pos1) :  # moveball(player postion) function for moving the ball

        l = can.coords(im)
        x = l[0]
        y = l[1]
        can.move(im, -x, -y)  ##ball goes back to origin
        x = pos[pos1][0]
        y = pos[pos1][1]
        can.move(im, x, y)

    can = Canvas(win, width=1152, height=648)
    can.pack()
    picg = PhotoImage(master=can, file="goalgrd.png")
    can.create_image(576, 324, image=picg)
    gball = PhotoImage(master=can, file="nobgball.png")
    im = can.create_image(580, 330, image=gball)

    b1 = Button(win, text="1", bg="white", height=3, width=5)
    b1.place(x=400, y=520)
    b1.bind("<Button-1>", goal)
    b2 = Button(win, text="2", bg="white", height=3, width=5)
    b2.place(x=560, y=520)
    b2.bind("<Button-1>", goal)
    b3 = Button(win, text="3", bg="white", height=3, width=5)
    b3.place(x=720, y=520)
    b3.bind("<Button-1>", goal)

    rule = Button(win, text="RULES",command=rules2, bg="white")
    rule.place(x=1080, y=600)

    combox = Label(win, text="", height=3, width=51, borderwidth=5, relief="solid", bg="white")
    combox.place(x=399, y=580)

    displayu = Label(win, text="", height=5, width=20, bg="white", relief="ridge", borderwidth=5)
    displayu.place(x=80, y=460)

    desu = Label(win, text="USER NUMBER", bg="red", fg="yellow", font="ArialBlack 15 bold")
    desu.place(x=80, y=430)

    desc = Label(win, text="COMPUTER NUMBER", bg="red", fg="yellow", font="ArialBlack 15 bold")
    desc.place(x=900, y=440)

    displayc = Label(win, text="", height=5, width=20, bg="white", relief="ridge", borderwidth=5)
    displayc.place(x=930, y=470)

    user = Label(win, text='USER', bg='red', fg='yellow', font="ArialBlack 12 bold")
    user.place(x=1045, y=35)

    goalcountHU = Label(win, text='GOAL COUNT', bg='red', fg='yellow', font="ArialBlack 12 bold")
    goalcountHU.place(x=1020, y=60)

    gcountU = Label(win, text=gcU, height=3, width=7, bg="white", relief="ridge", borderwidth=5)
    gcountU.place(x=1047, y=100)
    #########################
    comp = Label(win, text='COMP', bg='red', fg='yellow', font="ArialBlack 12 bold")
    comp.place(x=50, y=35)

    goalcountHC = Label(win, text='GOAL COUNT', bg='red', fg='yellow', font="ArialBlack 12 bold")
    goalcountHC.place(x=20, y=60)

    gcountC = Label(win, text=gcC, height=3, width=7, bg="white", relief="ridge", borderwidth=5)
    gcountC.place(x=50, y=100)

    win.mainloop()




# WINDOW CREATION N CONFIGURATION


##########
# ALL FUNCTIONS WITHIN THIS{

flag=1

def  maingame(event):#main game logic

    global uc
    global cc
    global ball
    n = event.widget.cget("text")#grabs the value of button
    displayu.configure(text=(n))
    global flag
    dlist = tuple(canvas.coords(ballpic))
    if dlist in posU.values() :
        flag = 1
    else :
        flag = 0

    if flag==0:
        ball=flag
    elif flag==1:
        ball=flag



    un = int(n)

    cn = random.randint(2, 6)
    displayc.configure(text=str(cn))
    if ball == 1 and un != cn :
        ball = 1
        print("BAll with u ")
        moveball(un,"u")
        cc=0
        uc = uc + 1

        print("User pass count = ", uc)
        print("Computer pass count = ", cc)
    elif ball == 1 and un == cn :
        ball = 0
        print("BAll with comp1 ")
        moveball(cn,"c")
        uc = 0
        cc = cc + 1


        print("User pass count = ", uc)
        print("Computer pass count = ", cc)
    elif ball == 0 and un != cn :
        ball = 0
        print("BAll with comp2")
        moveball(cn,"c")
        cc = cc + 1
        uc = 0


        print("User pass count = ", uc)
        print("Computer pass count = ", cc)
    elif ball == 0 and un == cn :
        ball = 1
        print("BAll with u ")
        moveball(un,"u")
        cc = 0
        uc = uc + 1


        print("User pass count = ", uc)
        print("Computer pass count = ", cc)
    if uc==6 :
        uc = 0
        cc = 0
        ball = 1

        comment.configure(text=("Goal Time User"))
        goalwin("u")


    elif cc==6:
        uc = 0
        cc = 0
        gc = 0
        ball = 0

        comment.configure(text=("Goal Time computer"))
        goalwin("c")


def moveball(pos,s):# moveball(player postion) function for moving the ball
    if s=="u":
        l = canvas.coords(ballpic)
        x = l[0]
        y = l[1]
        canvas.move(ballpic, -x, -y)  ##ball goes back to origin
        x = posU[pos][0]
        y = posU[pos][1]
        canvas.move(ballpic, x, y)
    elif s=="c":
        l = canvas.coords(ballpic)
        x1 = l[0]
        y1 = l[1]
        canvas.move(ballpic, -x1, -y1)  ##ball goes back to origin
        x1 = posCo[pos]
        x1=x1[0]
        y1 = posCo[pos]
        y1=y1[1]
        canvas.move(ballpic, x1, y1)


# FUCTION BLOCK ENDS }


# variable block##########{
posU = {1: (140, 400), 2: (250, 120), 3: (500, 320), 4: (540, 640), 5: (900, 190), 6: (980, 690)}
posCo = {1: (960, 400), 2: (730, 300), 3: (750, 660), 4: (450, 150), 5: (310, 480), 6: (130, 700)}
gcU='0'
gcC='0'
pos={'0':(590,200),'1':(380,70),'2':(580,70),'3':(760,70)}

# }###########
 ### 1=user 0 = comp
# SETTING BACKGROUND########3
canvas = Canvas(root, width=1400, height=1400)  # creating canvas
canvas.pack()  # this makes it visible
b1 = Button(root, text="1", bg="white", height=3, width=5)
b1.place(x=1150, y=340)
b1.bind("<Button-1>", maingame)
print(b1)

b2 = Button(root, text="2", bg="white", height=3, width=5)
b2.place(x=1210, y=340)
b2.bind("<Button-1>", maingame)
b3 = Button(root, text="3", bg="white", height=3, width=5)
b3.place(x=1270, y=340)
b3.bind("<Button-1>", maingame)
b4 = Button(root, text="4", bg="white", height=3, width=5)
b4.place(x=1150, y=420)
b4.bind("<Button-1>", maingame)
b5 = Button(root, text="5", bg="white", height=3, width=5)
b5.place(x=1210, y=420)
b5.bind("<Button-1>", maingame)
b6 = Button(root, text="6", bg="white", height=3, width=5)
b6.place(x=1270, y=420)
b6.bind("<Button-1>", maingame)

displayu = Label(root, text="", height=5, width=35, bg="white", relief="ridge", borderwidth=5)
displayu.place(x=1110, y=230)
desu = Label(root, text="USER NUMBER", bg="red", fg="yellow", font="ArialBlack 15 bold")
desu.place(x=1160, y=195)

desc = Label(root, text="COMPUTER NUMBER", bg="red", fg="yellow", font="ArialBlack 15 bold")
desc.place(x=1130, y=490)

displayc = Label(root, text="", height=5, width=35, bg="white", relief="ridge", borderwidth=5)
displayc.place(x=1110, y=530)

comment = Label(root, text="", height=9, width=43, borderwidth=5, relief="solid", bg="white")

comment.place(x=1080, y=30)

rules = Button(root, text="RULES",command=rules, bg="white", height=3, width=40)
rules.place(x=1094, y=700)
#########Graphics
img = PhotoImage(file="bg.png")  # loading image to window
im=canvas.create_image(742, 394, image=img)  # Placing it in background

###########
## adding football
img3 = PhotoImage(file="nobgball.png")
ballpic = canvas.create_image(140, 400, image=img3)

####

root.mainloop()


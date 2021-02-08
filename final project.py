from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image
import string

main_window=Tk()
main_window.title("WELCOME TO HANGMAN")
 
def first_page1():
        
        
        root=Tk()
        root.title("WELCOME TO HANGMAN")
        root.configure(bg="#C0C0C0")
        width = 600
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        img=Image.open('hang.jpg')
        img = img.resize((200,200), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img)
        Ll = Label(root, image = img)
        Ll.grid(column=0, row=0)

        L1 = Label(root, text="User Name",bg='pink')
        L1.place(x=210,y=10)
        E1 = Entry(root, bd =2,bg='skyblue')
        name=E1.get()
        E1.place(x=290,y=10)


        l3=Label(root,text='choose Level',bg='yellow')
        l3.place(x=210,y=40)
        
        var=IntVar()
        selection=var.get()

        def check():
                
                
                name=E1.get()
                selection=var.get()
                if selection==1 and name!='':
                        
                        root.destroy()
                        easy()
                elif selection==2 and name!='':
                        root.destroy()
                        meadium()
                       
                elif selection==3 and name!='':
                        root.destroy()
                        hard()
                        
                else:
                        messagebox.showinfo('select','select the level and enter name')
        def exit1():
                root.destroy()
        def help1():
                        
                        window_db=Tk()

                        conn = sqlite3.connect('hangman record.db')
                        c = conn.cursor()
                        #c.execute("CREATE TABLE player11 (help)")

                        #c.execute("INSERT INTO player11 VALUES('wrie coorect word for given image')")

                        c.execute('SELECT *FROM player11')
                        l1=Label(window_db,text=c.fetchone())
                        l1.place(x=50,y=20)


                        conn.commit()

                        conn.close()
                        window_db.mainloop()
        R1 = Radiobutton(root, text="EASY", variable=var, value=1,bg='orange')
        R1.place(x=300,y=40)
        R2 = Radiobutton(root, text="MEDIUM", variable=var,value=2,bg='skyblue')
        R2.place(x=360,y=40)
        R3 = Radiobutton(root, text="HARD", variable=var, value=3,bg='blue')
        R3.place(x=440,y=40)
        b1=Button(root,text='PLAY',bg='green',justify='center',relief=RAISED,width=10,command=check)
        b1.place(x=300,y=80)
        b2=Button(root,text='EXIT',bg='red',relief=SUNKEN,width=10,command=exit1)
        b2.place(x=420,y=80)
        b3=Button(root,text='HELP',bg='yellow',relief=RAISED,width=10,command=help1)
        b3.place(x=520,y=80)


                
        root.mainloop()


def easy():
        
        window=Tk()
        window.title('Hangman Level 1')
        
        global chances
        global score
        width = 1000
        height = 700
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        window.resizable(0, 0)
        chances=3
        score=0
        image_paths=['hang.jpg','apple.png','apple.png','apple.png']
        img = Image.open(image_paths[chances])
        img = img.resize((300,300), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img)
        Ll = Label(window, image = img)
        Ll.grid(column=0, row=0)
        
        
        def clicked(alphabet):
                
                global score
                global chances
                answer= "APPLE"
                if alphabet in answer:
                        if alphabet=="A":
                                btn01["text"] = alphabet
                        elif alphabet=="P":
                        
                                btn02["text"] = alphabet
                                btn03["text"] = alphabet
                                
                        
                        elif alphabet=="L":
                                btn04["text"] = alphabet
                        elif alphabet=="E":
                                btn05["text"] = alphabet
                        
                else:
                        txt="Chances remaining "+str(chances-1)
                        label1.configure(text=txt)
                        image = Image.open(image_paths[chances])
                        image = image.resize((300, 300), Image.ANTIALIAS)
                        imgnew = ImageTk.PhotoImage(image)
                        Ll.configure(image=imgnew)
                        Ll.image = imgnew
                        chances = chances - 1
                        if chances<=0:
                                messagebox.showinfo("Loose to guess","Hanged!!!Restart the game again")
                                
                                     
                if btn01["text"]=="A" and btn02["text"]=="P" and btn03["text"]=="P" and btn04["text"]=="L" and btn05["text"]=="E" :
                        messagebox.showinfo("congratulations", "YOU GUESS THE WORD!!!!")
                        txt='your score is :'+str(score+5)
                        label4.configure(text=txt)
                        new_word()
        
        def correct_word():
                n=E1.get()
                global chances
                if n=='apple' or n=='Apple' or n=='APPLE':
                        messagebox.showinfo('GUESS','YOUR GUESS IS COORECT')
                        new_word()
                else:
                        txt="Chances remaining "+str(chances-1)
                        label1.configure(text=txt)
                        image = Image.open(image_paths[chances-1])
                        image = image.resize((300, 300), Image.ANTIALIAS)
                        imgnew = ImageTk.PhotoImage(image)
                        Ll.configure(image=imgnew)
                        Ll.image = imgnew
                        chances = chances - 1
                        if chances<=0:
                                messagebox.showinfo("Loose to guess","Hanged!!!!!")
        def hints():
                
                window_db=Tk()

                conn = sqlite3.connect('hangman record.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE player3 (hint)")

                #c.execute("INSERT INTO player3 VALUES(' correct answer is APPLE')")

                c.execute('SELECT * FROM player3')
                l1=Label(window_db,text=c.fetchone())
                l1.place(x=50,y=20)


                conn.commit()

                conn.close()
                window_db.mainloop()
        def new_word():
                window.destroy()
                window1=Tk()
                window1.title('HANGMAN LEVEL 2')
                global chances
                global score
                score=5
                width = 1000
                height = 700
                screen_width = window1.winfo_screenwidth()
                screen_height = window1.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                window1.geometry("%dx%d+%d+%d" % (width, height, x, y))
                window1.resizable(0, 0)
                chances=3
                image_paths=['hang.jpg','banana.jpg','banana.jpg','banana.jpg']
                img = Image.open(image_paths[chances])
                img = img.resize((300,300), Image.ANTIALIAS)
                img= ImageTk.PhotoImage(img)
                Ll = Label(window1, image = img)
                Ll.grid(column=0, row=0)
                
                def clicked(alphabet):
                        
                        global chances
                        global score
                        answer= "BANANA"
                        if alphabet in answer:
                                
                                if alphabet=="B":
                                        btn01["text"] = alphabet
                                elif alphabet=="A":
                        
                                        btn02["text"] = alphabet
                                        btn04["text"] = alphabet
                                        btn06["text"] = alphabet
                                
                                elif alphabet=="N":
                                        btn03["text"] = alphabet
                                        btn05["text"] = alphabet
                        
                        else:
                                txt="Chances remaining "+str(chances-1)
                                label2.configure(text=txt)
                                image = Image.open(image_paths[chances])
                                image = image.resize((300, 300), Image.ANTIALIAS)
                                imgnew = ImageTk.PhotoImage(image)
                                Ll.configure(image=imgnew)
                                Ll.image = imgnew
                                chances = chances - 1
                                if chances<=0:
                                        messagebox.showinfo("Loose to guess","Hanged!!!Restart the game again")
                               
                        if btn01["text"]=="B" and btn02["text"]=="A" and btn03["text"]=="N" and btn04["text"]=="A" and btn05["text"]=="N" and btn06["text"]=="A" :
                                messagebox.showinfo("congratulations", "GREAT BUDDY YOU WIN THE GAME!!!!")
                                txt='your score is :'+str(score+5)
                                label5.configure(text=txt)
                               
                        
                def correct_word():
                        n=E1.get()
                        global chances
                        if n=='BANANA' or n=='banana' or n=='Banana':
                                messagebox.showinfo('GUESS','YOUR GUESS IS COORECT')
                        else:
                                txt="Chances remaining "+str(chances-1)
                                label2.configure(text=txt)
                                image = Image.open(image_paths[chances-1])
                                image = image.resize((300, 300), Image.ANTIALIAS)
                                imgnew = ImageTk.PhotoImage(image)
                                Ll.configure(image=imgnew)
                                Ll.image = imgnew
                                chances = chances - 1
                                if chances<=0:
                                        
                                        messagebox.showinfo("Loose to guess","Hanged!!!!!")
                def hints1():
                        
                          
                        window_db=Tk()

                        conn = sqlite3.connect('hangman record.db')
                        c = conn.cursor()
                        #c.execute("CREATE TABLE player4 (hint)")

                        #c.execute("INSERT INTO player4 VALUES(' correct answer is Banana')")

                        c.execute('SELECT * FROM player4')
                        l1=Label(window_db,text=c.fetchone())
                        l1.place(x=50,y=20)


                        conn.commit()

                        conn.close()
                        window_db.mainloop()
                def back():
                        window1.destroy()
                        easy()


        
                
                B1=Button(window1,text='New word',bg='skyblue',width=10)
                B1.place(x=750,y=80)
                B2=Button(window1,text='submit',bg='green',width=10,command=correct_word)
                B2.place(x=750,y=200)
                E1=Entry(window1,width=15,bd=1,bg='pink')
                E1.place(x=750,y=140)
                B3=Button(window1,text='Hint',bg='pink',width=10,command=hints1)
                B3.place(x=860,y=80)
                B4=Button(window1,text='Back',bg='orange',width=10,command=back)
                B4.place(x=860,y=200)
        
                btn01 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn01.grid(column=2, row=0)
                btn02 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn02.grid(column=3, row=0)
                btn03 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn03.grid(column=4, row=0)
                btn04 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn04.grid(column=5, row=0)
                btn05 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn05.grid(column=6, row=0)
                btn06 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn06.grid(column=7, row=0)


                btn1 = Button(window1, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
                btn1.grid(column=1, row=1)
                btn2 = Button(window1, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
                btn2.grid(column=2, row=1)
                btn3 = Button(window1, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
                btn3.grid(column=3, row=1)
                btn4 = Button(window1, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
                btn4.grid(column=4, row=1)
                btn5 = Button(window1, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
                btn5.grid(column=5, row=1)
                btn6 = Button(window1, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
                btn6.grid(column=6, row=1)
                btn7 = Button(window1, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
                btn7.grid(column=7, row=1)
                btn8 = Button(window1, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
                btn8.grid(column=8, row=1)
                btn9 = Button(window1, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
                btn9.grid(column=9, row=1)
                btn10 = Button(window1, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
                btn10.grid(column=10, row=1)

                btn11 = Button(window1, text="K",bg="skyBlue",  fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
                btn11.grid(column=2, row=2)
                btn12 = Button(window1, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
                btn12.grid(column=3, row=2)
                btn13 = Button(window1, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
                btn13.grid(column=4, row=2)
                btn14 = Button(window1, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
                btn14.grid(column=5, row=2)
                btn15 = Button(window1, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
                btn15.grid(column=6, row=2)
                btn16 = Button(window1, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
                btn16.grid(column=7, row=2)
                btn17 = Button(window1, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
                btn17.grid(column=8, row=2)
                btn18 = Button(window1, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
                btn18.grid(column=9, row=2)

                btn19 = Button(window1, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
                btn19.grid(column=3, row=3)
                btn20 = Button(window1, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
                btn20.grid(column=4, row=3)
                btn21 = Button(window1, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
                btn21.grid(column=5, row=3)
                btn22 = Button(window1, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
                btn22.grid(column=6, row=3)
                btn23 = Button(window1, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
                btn23.grid(column=7, row=3)
                btn24 = Button(window1, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
                btn24.grid(column=8, row=3)

                btn25 = Button(window1, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
                btn25.grid(column=5, row=4)
                btn26 = Button(window1, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
                btn26.grid(column=6, row=4)


                label2=Label(window1,text="Total Chances are : 3")
                label2.grid(row=5,column=0)
                label5=Label(window1,text='your score is : 5')
                label5.place(x=350,y=30)
                window1.mainloop()
        def checkpoint():
                window.destroy()
                first_page1()
        B1=Button(window,text='New word',bg='skyblue',width=10,command=new_word)
        B1.place(x=700,y=80)
        B2=Button(window,text='submit',bg='green',width=10,command=correct_word)
        B2.place(x=700,y=200)
        E1=Entry(window,width=15,bd=1,bg='pink')
        E1.place(x=700,y=140)
        B3=Button(window,text='Hint',bg='pink',width=10,command=hints)
        B3.place(x=830,y=80)
        B4=Button(window,text='Back',bg='orange',width=10,command=checkpoint)
        B4.place(x=830,y=200)
        

        btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn01.grid(column=2, row=0)
        btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn02.grid(column=3, row=0)
        btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn03.grid(column=4, row=0)
        btn04 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn04.grid(column=5, row=0)
        btn05 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn05.grid(column=6, row=0)
       
        btn1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
        btn1.grid(column=1, row=1)
        btn2 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
        btn2.grid(column=2, row=1)
        btn3 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
        btn3.grid(column=3, row=1)
        btn4 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
        btn4.grid(column=4, row=1)
        btn5 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
        btn5.grid(column=5, row=1)
        btn6 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
        btn6.grid(column=6, row=1)
        btn7 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
        btn7.grid(column=7, row=1)
        btn8 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
        btn8.grid(column=8, row=1)
        btn9 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
        btn9.grid(column=9, row=1)
        btn10 = Button(window, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
        btn10.grid(column=10, row=1)

        btn11 = Button(window, text="K",bg="skyBlue",  fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
        btn11.grid(column=2, row=2)
        btn12 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
        btn12.grid(column=3, row=2)
        btn13 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
        btn13.grid(column=4, row=2)
        btn14 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
        btn14.grid(column=5, row=2)
        btn15 = Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
        btn15.grid(column=6, row=2)
        btn16 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
        btn16.grid(column=7, row=2)
        btn17 = Button(window, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
        btn17.grid(column=8, row=2)
        btn18 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
        btn18.grid(column=9, row=2)

        btn19 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
        btn19.grid(column=3, row=3)
        btn20 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
        btn20.grid(column=4, row=3)
        btn21 = Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
        btn21.grid(column=5, row=3)
        btn22 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
        btn22.grid(column=6, row=3)
        btn23 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
        btn23.grid(column=7, row=3)
        btn24 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
        btn24.grid(column=8, row=3)

        btn25 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
        btn25.grid(column=5, row=4)
        btn26 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
        btn26.grid(column=6, row=4)


        label1=Label(window,text="Total Chances are : 3")
        label1.grid(row=5,column=0)
        label4=Label(window,text='your score is : 0')
        label4.place(x=350,y=30)
        window.mainloop()
# *************************************************************     END OF EASY PART *******************************************************************************

def meadium():
        window=Tk()
        global chances
        global score
        score=0
        width = 1100
        height = 800
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        window.resizable(0, 0)
        chances=3
        image_paths=['hang.jpg','kangaroo.png','kangaroo.png','kangaroo.png']
        img = Image.open(image_paths[chances])
        img = img.resize((300,300), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img)
        Ll = Label(window, image = img)
        Ll.grid(column=0, row=0)
        answer_arr=[]
        
        
        def clicked(alphabet):
                global chances
                answer= 'KANGAROO'
                if alphabet in answer:
                        if alphabet=="K":
                                btn01["text"] = alphabet
                        elif alphabet=="A":
                        
                                btn02["text"] = alphabet
                                btn05["text"] = alphabet
                                
                        elif alphabet=="N":
                                btn03["text"] = alphabet
                        elif alphabet=="G":
                                btn04["text"] = alphabet
                        elif alphabet=="R":
                                btn06["text"] = alphabet
                        elif alphabet=="O":
                                btn07["text"] = alphabet
                                btn08["text"] = alphabet
                                
 
                else:
                        txt="Chances remaining "+str(chances)
                        label1.configure(text=txt)
                        image = Image.open(image_paths[chances])
                        image = image.resize((300, 300), Image.ANTIALIAS)
                        imgnew = ImageTk.PhotoImage(image)
                        Ll.configure(image=imgnew)
                        Ll.image = imgnew
                        chances = chances - 1
                        txt="Chances remaining "+str(chances)
                        label7.configure(text=txt)

                        
                        if chances<=0:
                                messagebox.showinfo("Loose to guess","HANGED!!!Restart the game again")
                                window.destroy()
                                     
                if btn01["text"]=="K" and btn02["text"]=="A" and btn03["text"]=="N" and btn04["text"]=="G" and btn05["text"]=="A"and btn06["text"]=="R"and btn07["text"]=="O"and btn08["text"]=="O":
                        
                        
                        messagebox.showinfo("congratulations", "YOU GUESS THE WORD!!!!")
                        txt='your score is :'+str(score+5)
                        label7.configure(text=txt)
                        new_word1()
                
        def correct_word():
                n=E1.get()
                global chances
                global score
                if n=='kangaroo' or n=='Kangaroo' or n=='KANGAROO':
                        messagebox.showinfo('GUESS','YOUR GUESS IS COORECT')
                        txt='your score is :'+str(score+5)
                        label7.configure(text=txt)
                        new_word1()
                else:
                        txt="Chances remaining "+str(chances-1)
                        label1.configure(text=txt)
                        image = Image.open(image_paths[chances-1])
                        image = image.resize((300, 300), Image.ANTIALIAS)
                        imgnew = ImageTk.PhotoImage(image)
                        Ll.configure(image=imgnew)
                        Ll.image = imgnew
                        chances = chances - 1
                        if chances<=0:
                                messagebox.showinfo("Loose to guess","Hanged!!!!!")
        def new_word1():
                window.destroy()
                window1=Tk()
                window1.title('HANGMAN LEVEL 2')
                global chances
                global score
                score=0
                width = 1000
                height = 700
                screen_width = window1.winfo_screenwidth()
                screen_height = window1.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                window1.geometry("%dx%d+%d+%d" % (width, height, x, y))
                window1.resizable(0, 0)
                chances=3
                image_paths=['hang.jpg','lion.png','lion.png','lion.png']
                img = Image.open(image_paths[chances])
                img = img.resize((300,300), Image.ANTIALIAS)
                img= ImageTk.PhotoImage(img)
                Ll = Label(window1, image = img)
                Ll.grid(column=0, row=0)
                answer_arr=[]
        
        
        
                def clicked(alphabet):
                        
                
                        global chances
                        global score
                        answer= "LION"
                        if alphabet in answer:
                                
                                if alphabet=="L":
                                        btn01["text"] = alphabet
                                elif alphabet=="I":
                        
                                        btn02["text"] = alphabet
                                        
                                
                                elif alphabet=="O":
                                        btn03["text"] = alphabet
                                elif alphabet=="N":
                                        btn04["text"] = alphabet
                        
                        else:
                                txt="Chances remaining "+str(chances-1)
                                label2.configure(text=txt)
                                image = Image.open(image_paths[chances])
                                image = image.resize((300, 300), Image.ANTIALIAS)
                                imgnew = ImageTk.PhotoImage(image)
                                Ll.configure(image=imgnew)
                                Ll.image = imgnew
                                chances = chances - 1
                                if chances<=0:
                                        messagebox.showinfo("Loose to guess","Hanged!!!Restart the game again")
                                
                                     
                        if btn01["text"]=="L" and btn02["text"]=="I" and btn03["text"]=="O" and btn04["text"]=="N":
                                messagebox.showinfo("congratulations", "GREAT BUDDY YOU WIN THE GAME!!!!")
                                txt='your score is :'+str(score+10)
                                label6.configure(text=txt)
                                
                        
                def correct_word():
                        n=E1.get()
                        global chances
                        if n=='LION' or n=='lion' or n=='Lion':
                                messagebox.showinfo('GUESS','YOUR GUESS IS COORECT')
                                txt='your score is :'+str(score+10)
                                label6.configure(text=txt)
                        else:
                                txt="Chances remaining "+str(chances-1)
                                label2.configure(text=txt)
                                image = Image.open(image_paths[chances-1])
                                image = image.resize((300, 300), Image.ANTIALIAS)
                                imgnew= ImageTk.PhotoImage(image)
                                Ll.configure(image=imgnew)
                                Ll.image = imgnew
                                chances = chances - 1
                                if chances<=0:
                                        messagebox.showinfo("Loose to guess","Hanged!!!!!Restart the game again")
                def hints3():
                        window_db=Tk()

                        conn = sqlite3.connect('hangman record.db')
                        c = conn.cursor()
                        #c.execute("CREATE TABLE player6 (hint)")

                        #c.execute("INSERT INTO player6 VALUES(' correct answer is LION')")
                        c.execute('SELECT * FROM player6')
                        l1=Label(window_db,text=c.fetchone())
                        l1.place(x=50,y=20)


                        conn.commit()

                        conn.close()
                        window_db.mainloop()
                def back1():
                        window1.destroy()
                        meadium()
        
                
                B1=Button(window1,text='New word',bg='skyblue',width=10)
                B1.place(x=750,y=80)
                B2=Button(window1,text='submit',bg='green',width=10,command=correct_word)
                B2.place(x=750,y=200)
                E1=Entry(window1,width=15,bd=1,bg='pink')
                E1.place(x=750,y=140)
                B4=Button(window1,text='Hint',bg='pink',width=10,command=hints3)
                B4.place(x=850,y=80)
                B5=Button(window1,text='Back',bg='orange',width=10,command=back1)
                B5.place(x=850,y=200)

                btn01 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn01.grid(column=2, row=0)
                btn02 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn02.grid(column=3, row=0)
                btn03 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn03.grid(column=4, row=0)
                btn04 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn04.grid(column=5, row=0)
                


                btn1 = Button(window1, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
                btn1.grid(column=1, row=1)
                btn2 = Button(window1, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
                btn2.grid(column=2, row=1)
                btn3 = Button(window1, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
                btn3.grid(column=3, row=1)
                btn4 = Button(window1, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
                btn4.grid(column=4, row=1)
                btn5 = Button(window1, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
                btn5.grid(column=5, row=1)
                btn6 = Button(window1, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
                btn6.grid(column=6, row=1)
                btn7 = Button(window1, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
                btn7.grid(column=7, row=1)
                btn8 = Button(window1, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
                btn8.grid(column=8, row=1)
                btn9 = Button(window1, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
                btn9.grid(column=9, row=1)
                btn10 = Button(window1, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
                btn10.grid(column=10, row=1)

                btn11 = Button(window1, text="K",bg="skyBlue",  fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
                btn11.grid(column=2, row=2)
                btn12 = Button(window1, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
                btn12.grid(column=3, row=2)
                btn13 = Button(window1, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
                btn13.grid(column=4, row=2)
                btn14 = Button(window1, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
                btn14.grid(column=5, row=2)
                btn15 = Button(window1, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
                btn15.grid(column=6, row=2)
                btn16 = Button(window1, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
                btn16.grid(column=7, row=2)
                btn17 = Button(window1, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
                btn17.grid(column=8, row=2)
                btn18 = Button(window1, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
                btn18.grid(column=9, row=2)

                btn19 = Button(window1, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
                btn19.grid(column=3, row=3)
                btn20 = Button(window1, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
                btn20.grid(column=4, row=3)
                btn21 = Button(window1, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
                btn21.grid(column=5, row=3)
                btn22 = Button(window1, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
                btn22.grid(column=6, row=3)
                btn23 = Button(window1, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
                btn23.grid(column=7, row=3)
                btn24 = Button(window1, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
                btn24.grid(column=8, row=3)

                btn25 = Button(window1, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
                btn25.grid(column=5, row=4)
                btn26 = Button(window1, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
                btn26.grid(column=6, row=4)


                label2=Label(window1,text="Total Chances are : 3")
                label2.grid(row=5,column=0)
                label6=Label(window1,text="your score is : 5")
                label6.place(x=350,y=30)
                window1.mainloop()
        def hints2():
                window_db=Tk()

                conn = sqlite3.connect('hangman record.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE player5 (hint)")

                #c.execute("INSERT INTO player5 VALUES(' correct answer is KANGAROO')")
                c.execute('SELECT * FROM player5')
                l1=Label(window_db,text=c.fetchone())
                l1.place(x=50,y=20)


                conn.commit()

                conn.close()
                window_db.mainloop()
        def checkpoint():
                window.destroy()
                first_page1()

        
        B1=Button(window,text='New word',bg='skyblue',width=10,command=new_word1)
        B1.place(x=850,y=80)
        B2=Button(window,text='submit',bg='green',width=10,command=correct_word)
        B2.place(x=850,y=200)
        E1=Entry(window,width=15,bd=1,bg='pink')
        E1.place(x=850,y=140)
        B3=Button(window,text='Hint',bg='pink',width=10,command=hints2)
        B3.place(x=1000,y=80)
        B4=Button(window,text='Back',bg='orange',width=10,command=checkpoint)
        B4.place(x=1000,y=200)



        btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn01.grid(column=2, row=0)
        btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn02.grid(column=3, row=0)
        btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn03.grid(column=4, row=0)
        btn04 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn04.grid(column=5, row=0)
        btn05 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn05.grid(column=6, row=0)
        btn06 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn06.grid(column=7, row=0)
        btn07 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn07.grid(column=8, row=0)
        btn08 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn08.grid(column=9, row=0)


        btn1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
        btn1.grid(column=1, row=1)
        btn2 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
        btn2.grid(column=2, row=1)
        btn3 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
        btn3.grid(column=3, row=1)
        btn4 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
        btn4.grid(column=4, row=1)
        btn5 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
        btn5.grid(column=5, row=1)
        btn6 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
        btn6.grid(column=6, row=1)
        btn7 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
        btn7.grid(column=7, row=1)
        btn8 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
        btn8.grid(column=8, row=1)
        btn9 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
        btn9.grid(column=9, row=1)
        btn10 = Button(window, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
        btn10.grid(column=10, row=1)

        btn11 = Button(window, text="K",bg="skyBlue",  fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
        btn11.grid(column=2, row=2)
        btn12 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
        btn12.grid(column=3, row=2)
        btn13 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
        btn13.grid(column=4, row=2)
        btn14 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
        btn14.grid(column=5, row=2)
        btn15 = Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
        btn15.grid(column=6, row=2)
        btn16 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
        btn16.grid(column=7, row=2)
        btn17 = Button(window, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
        btn17.grid(column=8, row=2)
        btn18 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
        btn18.grid(column=9, row=2)

        btn19 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
        btn19.grid(column=3, row=3)
        btn20 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
        btn20.grid(column=4, row=3)
        btn21 = Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
        btn21.grid(column=5, row=3)
        btn22 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
        btn22.grid(column=6, row=3)
        btn23 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
        btn23.grid(column=7, row=3)
        btn24 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
        btn24.grid(column=8, row=3)

        btn25 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
        btn25.grid(column=5, row=4)
        btn26 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
        btn26.grid(column=6, row=4)


        label1=Label(window,text="Total Chances are : 3")
        label1.grid(row=5,column=0)
        label7=Label(window,text="your score is : 0")
        label7.place(x=350,y=30)
        window.mainloop()
#************************************************************* END OF MEADIUM PART ******************************************************************
def hard():
        
        window=Tk()
        window.title('Hangman-Level1')
        global chances
        global score
        score=0
        width = 1000
        height = 700
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        window.resizable(0, 0)
        chances=3
        image_paths=['hang.jpg','eagle.jpg','eagle.jpg','eagle.JPG']
        img = Image.open(image_paths[chances])
        img = img.resize((300,300), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img)
        Ll = Label(window, image = img)
        Ll.grid(column=0, row=0)
        answer_arr=[]
        
        
        def clicked(alphabet):
                
                global chances
                global score
                answer= 'EAGLE'
                if alphabet in answer:
                        if alphabet=="E":
                                btn01["text"] = alphabet
                                btn05["text"]=alphabet
                        elif alphabet=="A":
                        
                                btn02["text"] = alphabet
                              
                                
                        elif alphabet=="G":
                                btn03["text"] = alphabet
                        elif alphabet=="L":
                                btn04["text"] = alphabet
                        elif alphabet=="E":
                                btn06["text"] = alphabet
                        
                else:
                        txt="Chances remaining "+str(chances)
                        label2.configure(text=txt)
                        image = Image.open(image_paths[chances])
                        image = image.resize((300, 300), Image.ANTIALIAS)
                        imgnew = ImageTk.PhotoImage(image)
                        Ll.configure(image=imgnew)
                        Ll.image = imgnew
                        chances = chances - 1
                        txt="Chances remaining "+str(chances)
                        label2.configure(text=txt)

                        
                        if chances<=0:
                                messagebox.showinfo("Loose to guess","Hanged!!!!!")
                                
                                     
                if btn01["text"]=="E" and btn02["text"]=="A" and btn03["text"]=="G" and btn04["text"]=="L" and btn05["text"]=="E":
                        
                        
                        messagebox.showinfo("congratulations", "YOU GUESS THE WORD!!!!")
                        txt='your score is :'+str(score+5)
                        label9.configure(text=txt)
                        new_word2()
                
        def correct_word():
                        n=E1.get()
                        global chances
                        global score
                        if n=='EAGLE' or n=='Eagle' or n=='eagle':
                                messagebox.showinfo('GUESS','YOUR GUESS IS COORECT')
                                txt='your score is :'+str(score+5)
                                label9.configure(text=txt)
                                new_word2()
                        else:
                                txt="Chances remaining "+str(chances-1)
                                label2.configure(text=txt)
                                image = Image.open(image_paths[chances-1])
                                image = image.resize((300, 300), Image.ANTIALIAS)
                                imgnew = ImageTk.PhotoImage(image)
                                Ll.configure(image=imgnew)
                                Ll.image = imgnew
                                chances = chances - 1
                                if chances<=0:
                                        messagebox.showinfo("Loose to guess","Hanged!!!!!")
        def new_word2():
                window.destroy()
                window1=Tk()
                window1.title('HANGMAN LEVEL 2')
                global chances
                global score
                width = 1000
                height = 700
                screen_width = window1.winfo_screenwidth()
                screen_height = window1.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                window1.geometry("%dx%d+%d+%d" % (width, height, x, y))
                window1.resizable(0, 0)
                chances=3
                image_paths=['hang.jpg','Parrot.jpg','Parrot.jpg','Parrot.jpg']
                img = Image.open(image_paths[chances])
                img = img.resize((300,300), Image.ANTIALIAS)
                img= ImageTk.PhotoImage(img)
                Ll = Label(window1, image = img)
                Ll.grid(column=0, row=0)
                answer_arr=[]
        
        
        
                def clicked(alphabet):

                        global score
                
                        global chances
                        answer= "PARROT"
                        if alphabet in answer:
                                
                                if alphabet=="P":
                                        btn01["text"] = alphabet
                                elif alphabet=="A":
                        
                                        btn02["text"] = alphabet
                                        
                                
                                elif alphabet=="R":
                                        btn03["text"] = alphabet
                                        btn04["text"] = alphabet
                                elif alphabet=="O":
                                        btn05["text"] = alphabet
                                elif alphabet=="T":
                                        btn06["text"] = alphabet
                        
                        else:
                                txt="Chances remaining "+str(chances-1)
                                label2.configure(text=txt)
                                image = Image.open(image_paths[chances])
                                image = image.resize((300, 300), Image.ANTIALIAS)
                                imgnew = ImageTk.PhotoImage(image)
                                Ll.configure(image=imgnew)
                                Ll.image = imgnew
                                chances = chances - 1
                                if chances<=0:
                                        messagebox.showinfo("Loose to guess","Hanged!!!Restart the game again")

                                     
                        if btn01["text"]=="P" and btn02["text"]=="A" and btn03["text"]=="R" and btn04["text"]=="R"and btn05["text"]=="O" and btn06["text"]=="T":
                                messagebox.showinfo("congratulations", "GREAT BUDDY YOU WIN THE GAME!!!!")
                                txt='your score is :'+str(score+10)
                                label8.configure(text=txt)
                               
                                
                        
                def correct_word():
                        n=E1.get()
                        global chances
                        if n=='PARROT' or n=='parrot' or n=='Parrot':
                                messagebox.showinfo('GUESS','YOUR GUESS IS COORECT')
                                txt='your score is :'+str(score+10)
                                label8.configure(text=txt)
                        else:
                                txt="Chances remaining "+str(chances-1)
                                label2.configure(text=txt)
                                image = Image.open(image_paths[chances-1])
                                image = image.resize((300, 300), Image.ANTIALIAS)
                                imgnew = ImageTk.PhotoImage(image)
                                Ll.configure(image=imgnew)
                                Ll.image = imgnew
                                chances = chances - 1
                                if chances<=0:
                                        messagebox.showinfo("Loose to guess","Hanged!!!!Restart the game again")
                def hints4():
                        
                        window_db=Tk()

                        conn = sqlite3.connect('hangman record.db')
                        c = conn.cursor()
                        #c.execute("CREATE TABLE player10 (hint)")

                        #c.execute("INSERT INTO player10 VALUES(' correct answer is Parrot')")
                        c.execute('SELECT * FROM player10')
                        l1=Label(window_db,text=c.fetchone())
                        l1.place(x=50,y=20)


                        conn.commit()

                        conn.close()
                        window_db.mainloop()
                def back2():
                        window1.destroy()
                        hard()
        
        
                
                B1=Button(window1,text='New word',bg='skyblue',width=10)
                B1.place(x=750,y=80)
                B2=Button(window1,text='submit',bg='green',width=10,command=correct_word)
                B2.place(x=750,y=200)
                E1=Entry(window1,width=15,bd=1,bg='pink')
                E1.place(x=750,y=140)
                B3=Button(window1,text='Hint',bg='pink',width=10,command=hints4)
                B3.place(x=850,y=80)
                B4=Button(window1,text='Back',bg='orange',width=10,command=back2)
                B4.place(x=850,y=200)


                btn01 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn01.grid(column=2, row=0)
                btn02 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn02.grid(column=3, row=0)
                btn03 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn03.grid(column=4, row=0)
                btn04 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn04.grid(column=5, row=0)
                btn05 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn05.grid(column=6, row=0)
                btn06 = Button(window1, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
                btn06.grid(column=7, row=0)
                



                btn1 = Button(window1, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
                btn1.grid(column=1, row=1)
                btn2 = Button(window1, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
                btn2.grid(column=2, row=1)
                btn3 = Button(window1, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
                btn3.grid(column=3, row=1)
                btn4 = Button(window1, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
                btn4.grid(column=4, row=1)
                btn5 = Button(window1, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
                btn5.grid(column=5, row=1)
                btn6 = Button(window1, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
                btn6.grid(column=6, row=1)
                btn7 = Button(window1, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
                btn7.grid(column=7, row=1)
                btn8 = Button(window1, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
                btn8.grid(column=8, row=1)
                btn9 = Button(window1, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
                btn9.grid(column=9, row=1)
                btn10 = Button(window1, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
                btn10.grid(column=10, row=1)

                btn11 = Button(window1, text="K",bg="skyBlue",  fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
                btn11.grid(column=2, row=2)
                btn12 = Button(window1, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
                btn12.grid(column=3, row=2)
                btn13 = Button(window1, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
                btn13.grid(column=4, row=2)
                btn14 = Button(window1, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
                btn14.grid(column=5, row=2)
                btn15 = Button(window1, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
                btn15.grid(column=6, row=2)
                btn16 = Button(window1, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
                btn16.grid(column=7, row=2)
                btn17 = Button(window1, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
                btn17.grid(column=8, row=2)
                btn18 = Button(window1, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
                btn18.grid(column=9, row=2)

                btn19 = Button(window1, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
                btn19.grid(column=3, row=3)
                btn20 = Button(window1, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
                btn20.grid(column=4, row=3)
                btn21 = Button(window1, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
                btn21.grid(column=5, row=3)
                btn22 = Button(window1, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
                btn22.grid(column=6, row=3)
                btn23 = Button(window1, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
                btn23.grid(column=7, row=3)
                btn24 = Button(window1, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
                btn24.grid(column=8, row=3)

                btn25 = Button(window1, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
                btn25.grid(column=5, row=4)
                btn26 = Button(window1, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
                btn26.grid(column=6, row=4)


                label2=Label(window1,text="Total Chances are : 3")
                label2.grid(row=5,column=0)
                label8=Label(window1,text="your score is : 5")
                label8.place(x=350,y=30)
                window1.mainloop()
        def hints5():
                window_db=Tk()
                conn = sqlite3.connect('hangman record.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE player9 (hint)")

                #c.execute("INSERT INTO player9 VALUES('correct answer is Eagle')")

                c.execute('SELECT * FROM player9')
                l1=Label(window_db,text=c.fetchone())
                l1.place(x=50,y=20)


                conn.commit()

                conn.close()
                window_db.mainloop()
        def checkpoint():
                window.destroy()
                first_page1()
                
        
        
        B1=Button(window,text='New word',bg='skyblue',width=10,command=new_word2)
        B1.place(x=750,y=80)
        B2=Button(window,text='submit',bg='green',width=10,command=correct_word)
        B2.place(x=750,y=200)
        E1=Entry(window,width=15,bd=1,bg='pink')
        E1.place(x=750,y=140)
        B3=Button(window,text='Hint',bg='pink',width=10,command=hints5)
        B3.place(x=850,y=80)
        B4=Button(window,text='Back',bg='orange',width=10,command=checkpoint)
        B4.place(x=850,y=200)


        btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn01.grid(column=2, row=0)
        btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn02.grid(column=3, row=0)
        btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn03.grid(column=4, row=0)
        btn04 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn04.grid(column=5, row=0)
        btn05 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn05.grid(column=6, row=0)

        btn1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
        btn1.grid(column=1, row=1)
        btn2 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
        btn2.grid(column=2, row=1)
        btn3 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
        btn3.grid(column=3, row=1)
        btn4 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
        btn4.grid(column=4, row=1)
        btn5 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
        btn5.grid(column=5, row=1)
        btn6 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
        btn6.grid(column=6, row=1)
        btn7 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
        btn7.grid(column=7, row=1)
        btn8 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
        btn8.grid(column=8, row=1)
        btn9 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
        btn9.grid(column=9, row=1)
        btn10 = Button(window, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
        btn10.grid(column=10, row=1)

        btn11 = Button(window, text="K",bg="skyBlue",  fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
        btn11.grid(column=2, row=2)
        btn12 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
        btn12.grid(column=3, row=2)
        btn13 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
        btn13.grid(column=4, row=2)
        btn14 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
        btn14.grid(column=5, row=2)
        btn15 = Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
        btn15.grid(column=6, row=2)
        btn16 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
        btn16.grid(column=7, row=2)
        btn17 = Button(window, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
        btn17.grid(column=8, row=2)
        btn18 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
        btn18.grid(column=9, row=2)

        btn19 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
        btn19.grid(column=3, row=3)
        btn20 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
        btn20.grid(column=4, row=3)
        btn21 = Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
        btn21.grid(column=5, row=3)
        btn22 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
        btn22.grid(column=6, row=3)
        btn23 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
        btn23.grid(column=7, row=3)
        btn24 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
        btn24.grid(column=8, row=3)

        btn25 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
        btn25.grid(column=5, row=4)
        btn26 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
        btn26.grid(column=6, row=4)


        label2=Label(window,text="Total Chances are : 3")
        label2.grid(row=5,column=0)
        label9=Label(window,text="your score is : 0")
        label9.place(x=350,y=30)
        window.mainloop()
# ********************************************************* END OF HARD PART ******************************************************
def first_page():
        main_window.destroy()
        
        root=Tk()
        root.title("WELCOME TO HANGMAN")
        
        root.configure(bg="#C0C0C0")
        width = 600
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        img=Image.open('hang.jpg')
        img = img.resize((200,200), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img)
        Ll = Label(root, image = img)
        Ll.grid(column=0, row=0)

        L1 = Label(root, text="User Name",bg='pink')
        L1.place(x=210,y=10)
        E1 = Entry(root, bd =2,bg='skyblue')
        name=E1.get()
        E1.place(x=290,y=10)


        l3=Label(root,text='choose Level',bg='yellow')
        l3.place(x=210,y=40)
        var=IntVar()
        selection=var.get()

        def check():
                
                
                name=E1.get()
                selection=var.get()
                if selection==1 and name!='':
                        
                        root.destroy()
                        easy()
                elif selection==2 and name!='':
                        root.destroy()
                        meadium()
                       
                elif selection==3 and name!='':
                        root.destroy()
                        hard()
                        
                else:
                        messagebox.showinfo('select','select the level and enter name')
        def exit1():
                root.destroy()
        def help1():
                        
                        window_db=Tk()

                        conn = sqlite3.connect('hangman record.db')
                        c = conn.cursor()
                        #c.execute("CREATE TABLE player11 (help)")

                        #c.execute("INSERT INTO player11 VALUES('wrie coorect word for given image')")
                        c.execute('SELECT *FROM player11')
                        l1=Label(window_db,text=c.fetchone())
                        l1.place(x=50,y=20)


                        conn.commit()

                        conn.close()
                        window_db.mainloop()
        R1 = Radiobutton(root, text="EASY", variable=var, value=1,bg='orange')
        R1.place(x=300,y=40)
        R2 = Radiobutton(root, text="MEDIUM", variable=var,value=2,bg='skyblue')
        R2.place(x=360,y=40)
        R3 = Radiobutton(root, text="HARD", variable=var, value=3,bg='blue')
        R3.place(x=440,y=40)
        b1=Button(root,text='PLAY',bg='green',justify='center',relief=RAISED,width=10,command=check)
        b1.place(x=300,y=80)
        b2=Button(root,text='EXIT',bg='red',relief=SUNKEN,width=10,command=exit1)
        b2.place(x=420,y=80)
        b3=Button(root,text='HELP',bg='yellow',relief=RAISED,width=10,command=help1)
        b3.place(x=520,y=80)

                
        root.mainloop()
first_page()
main_window.mainloop()


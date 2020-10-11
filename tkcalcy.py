from tkinter import *
#create mainwindow
root=Tk()

#mainwindowsize
root.geometry("450x600")
root.minsize(450,600)   
root.maxsize(450,600)
#title
root.title("calcy-by prajwal")
root.wm_iconbitmap("tk19.ico")
root.configure(bg="light steel blue")


#alll function 
def onclick(event):
    global inpval
    textinp=event.widget.cget("text")  #inbuilt fun giving text stored in wid(button)
    print(textinp)

    if textinp=="=":
        if inpval.get().isdigit():
            editval=int(inpval.get())
        else:
            try:
                editval=eval(inpscreen.get())
            except Exception as e:
                editval="input-error"
                
                print(e)

        inpval.set(editval)
        inpscreen.update()

    elif textinp=="c":
        inpval.set("")
        inpscreen.update()
    else:
        inpval.set(inpval.get()+textinp)
        inpscreen.update()












#input for calcy in var
inpval=StringVar()
inpval.set(" ")

#input screen
inpscreen=Entry(root,textvariable=inpval,bg="lemon chiffon",fg="black",font="comicsansms 25 bold",borderwidth=7,relief=GROOVE)
inpscreen.pack(side=TOP,fill="both",padx=15,pady=15)


# ---------------------------------
frame1=Frame(root,bg="purple")



b9=Button(frame1,text="9",font="comicsansms 20 bold",padx=15,pady=15)
b9.pack(side=LEFT,padx=10,pady=5)
b9.bind("<Button-1>",onclick)

b8=Button(frame1,text="8",font="comicsansms 20 bold",padx=15,pady=15)
b8.pack(side=LEFT,padx=10,pady=5)
b8.bind("<Button-1>",onclick)

b7=Button(frame1,text="7",font="comicsansms 20 bold",padx=15,pady=15)
b7.pack(side=LEFT,padx=10,pady=5)
b7.bind("<Button-1>",onclick)

frame1.pack()
#-----------------------------------------------------------------------------------------
frame2=Frame(root,bg="purple")


b6=Button(frame2,text="6",font="comicsansms 20 bold",padx=15,pady=15)
b6.pack(side=LEFT,padx=10,pady=5)
b6.bind("<Button-1>",onclick)



b5=Button(frame2,text="5",font="comicsansms 20 bold",padx=15,pady=15)
b5.pack(side=LEFT,padx=10,pady=5)
b5.bind("<Button-1>",onclick)

b4=Button(frame2,text="4",font="comicsansms 20 bold",padx=15,pady=15)
b4.pack(side=LEFT,padx=10,pady=5)
b4.bind("<Button-1>",onclick)
frame2.pack()
#----------------------------------------------------------------------------------------
frame3=Frame(root,bg="purple")
b3=Button(frame3,text="3",font="comicsansms 20 bold",padx=15,pady=15)
b3.pack(side=LEFT,padx=10,pady=5)
b3.bind("<Button-1>",onclick)

b2=Button(frame3,text="2",font="comicsansms 20 bold",padx=15,pady=15)
b2.pack(side=LEFT,padx=10,pady=5)
b2.bind("<Button-1>",onclick)

b1=Button(frame3,text="1",font="comicsansms 20 bold",padx=15,pady=15)
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind("<Button-1>",onclick)

frame3.pack()
#------------------------------------------------------------------------------------------
frame4=Frame(root,bg="purple")

b0=Button(frame4,text="0",font="comicsansms 20 bold",padx=15,pady=15)
b0.pack(side=LEFT,padx=10,pady=5)
b0.bind("<Button-1>",onclick)

badd=Button(frame4,text="+",font="comicsansms 20 bold",padx=15,pady=15)
badd.pack(side=LEFT,padx=10,pady=5)
badd.bind("<Button-1>",onclick)

bsub=Button(frame4,text="-",font="comicsansms 20 bold",padx=15,pady=15)
bsub.pack(side=LEFT,padx=10,pady=5)
bsub.bind("<Button-1>",onclick)


frame4.pack()
#------------------------------------------------------------------------------------------------


frame5=Frame(root,bg="purple")

bmul=Button(frame5,text="*",font="comicsansms 20 bold",padx=5,pady=10)
bmul.pack(side=LEFT,padx=10,pady=5)
bmul.bind("<Button-1>",onclick)

bdiv=Button(frame5,text="/",font="comicsansms 20 bold",padx=5,pady=10)
bdiv.pack(side=LEFT,padx=10,pady=5)
bdiv.bind("<Button-1>",onclick)

bres=Button(frame5,text="=",font="comicsansms 20 bold",padx=5,pady=10)
bres.pack(side=LEFT,padx=10,pady=5)
bres.bind("<Button-1>",onclick)


bcan=Button(frame5,text="c",font="comicsansms 20 bold",padx=3,pady=10)
bcan.pack(side=LEFT,padx=10,pady=5)
bcan.bind("<Button-1>",onclick)



frame5.pack()
# ----------------------------------
root.mainloop()
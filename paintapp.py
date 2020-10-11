from tkinter import * 

from PIL import ImageGrab
import tkinter.messagebox as msgbox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

#functions
def savefile():
    file = asksaveasfilename(initialfile = 'Untitled.jpg',defaultextension='.jpg',filetypes=[("JPEG", "*.jpg")])

    

    p=root.winfo_rootx()+can_widget.winfo_x()
    q=root.winfo_rooty()+can_widget.winfo_y()
    print(p,q)
    p1=p+can_widget.winfo_width()
    q1=q+can_widget.winfo_height()
    print(p1,q1)
    img=ImageGrab.grab().crop((p,q,p1,q1))
    img.save(file)
        


    
  
    
def exitpaint():
    root.quit()
def query():
    msgbox.showinfo("for query and more info","please email us at:\n prajsa99@gmail.com")
def about_us():
    msgbox.showinfo("DRAWING BOARD","is inly meant for scribblking,not an paint app.\nwil see to upgrade it in future")


col_var="red"

def plot(event):
    n=slider.get()
    x1,y1=(event.x-n)+1,(event.y-n)+1
    x2,y2=(event.x+n)+1,(event.y+n)+1
    can_widget.create_oval(x1,y1,x2,y2,fill=col_var,outline=col_var)

def resetcanvas():
    can_widget.delete(ALL)
def maker():
    global col_var
    col_var ="red"

def makeb():
    global col_var
    col_var ="blue"


def makey():
    global col_var
    col_var ="yellow"


def makebg():
    global col_var
    col_var ="green"




    
#-----------------
root=Tk()
screenw=root.winfo_screenwidth()
screenh=root.winfo_screenheight()

win_wid=screenw
win_hei=screenh
root.geometry(f"{win_wid}x{win_hei}")
root.minsize(win_wid,win_hei)   
root.maxsize(win_wid,win_hei)
root.config(bg="white")
root.title("DRAWING BOARD-by PRAJWAL")



# --------------------------------------------
#meuubar

menubar=Menu(root)

#submenu 1
menu_file=Menu(menubar,tearoff=0)



menu_file.add_command(label="save file",command=savefile)
menu_file.add_command(label="clear canvas",command=resetcanvas)
menu_file.add_command(label="exit",command=exitpaint)


menubar.add_cascade(label="file",menu=menu_file)



#submenu 2
menu_help=Menu(menubar,tearoff=0)


menu_help.add_command(label="query",command=query)
menu_help.add_command(label="about us",command=about_us)
menubar.add_cascade(label="help",menu=menu_help)

#frame 1
f1=Frame(root,bg="grey",borderwidth=3,padx=30,pady=30,relief=SUNKEN)

c1=Button(f1,text="RED",fg="white",bg="Red",height=3,width=6,command=maker)
c2=Button(f1,text="BLUE",fg="white",bg="blue",height=3,width=6,command=makeb)
c3=Button(f1,text="YELLOW",fg="black",bg="yellow",height=3,width=6,command=makey)
er=Button(f1,text="ERASER",fg="black",bg="white",height=3,width=6,command=makebg)
c1.pack(padx=5,pady=5,anchor="nw")
c2.pack(padx=5,pady=5,anchor="nw")
c3.pack(padx=5,pady=5,anchor="nw")
er.pack(padx=5,pady=15,anchor="sw")
slidescale=Label(f1,text="width (pointer)",fg="black",bg="blue",pady=10)
slidescale.pack()
slider=Scale(f1,from_=0,to=20,orient=HORIZONTAL)
slider.set(2)  #sets initial slider position
slider.pack()


f1.pack(side=LEFT,anchor="nw",fill=Y,padx=10,pady=10)
#canvas
can_widget=Canvas(root,bg="green")
can_widget.pack(expand=True,fill="both")


#event handling

can_widget.bind('<B1-Motion>',plot)

root.config(menu=menubar)
root.mainloop()
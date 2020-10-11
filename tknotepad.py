from tkinter import *
import tkinter.messagebox as msgbox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
#create mainwindow
root=Tk()

#mainwindowsize
root.geometry("850x600")
root.minsize(850,600)   
root.maxsize(850,600)
#title
root.title("notepad-by prajwal")
root.wm_iconbitmap("tk19.ico")


#input area
inptextarea=Text(root,font="lucida 15")
inptextarea.pack(expand=True,fill="both")

#-----------------------
File=None
#-----------------------------
#functions

def newfile():
    global File
    root.title("untitled_")
    File=None
    inptextarea.delete(1.0,END)
   
# 3------------------------------
def openfile():
    global File
    File=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if File=="":
        File=None
    else:
        root.title(os.path.basename(File)+"-notepad")
        inptextarea.delete(1.0,END)
        f=open(File,"r")
        inptextarea.insert(1.0,f.read())
        f.close()


def savefile():
    global File
    if File == None:
        File = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if File =="":
            File = None

        else:
            #Save as a new file
            f = open(File, "w")
            f.write(inptextarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(File) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(File, "w")
        f.write(inptextarea.get(1.0, END))
        f.close()

    
def exitnp():
    root.destroy()
#---------
def cut():
    inptextarea.event_generate(("<<Cut>>"))  #inbilut logic
def paste():
    inptextarea.event_generate(("<<Paste>>"))
def copy():
    inptextarea.event_generate(("<<Copy>>"))
#-----------------------------


def about():
    msgbox.showinfo("NOtepad by prajwal","for more details visit:ww.xyz.com")
    

#---------------------------------------


















# --------------------------------------------
#meuubar

menubar=Menu(root)

#submenu 1
menu_file=Menu(menubar,tearoff=0)

menu_file.add_command(label="new file",command=newfile)
menu_file.add_command(label="open file",command=openfile)
menu_file.add_command(label="save file",command=savefile)
menu_file.add_command(label="exit",command=exitnp)

menubar.add_cascade(label="file",menu=menu_file)

#submenu 2
menu_edit=Menu(menubar,tearoff=0)

menu_edit.add_command(label="cut",command=cut)
menu_edit.add_command(label="copy",command=copy)
menu_edit.add_command(label="paste",command=paste)


menubar.add_cascade(label="edit",menu=menu_edit)

#submenu 3
menu_help=Menu(menubar,tearoff=0)


menu_help.add_command(label="about us",command=about)
menubar.add_cascade(label="help",menu=menu_help)



root.config(menu=menubar)
#-------------------------------------------------------------------------------------
# scroll bar


sbar=Scrollbar(inptextarea)
sbar.pack(side=RIGHT,fill=Y)
sbar.config(command=inptextarea.yview)
inptextarea.config(yscrollcommand=sbar.set)

#---------------------------------------------------
root.mainloop()
from tkinter import*
from tkinter import ttk, messagebox
import tkinter
from VirtualKeyboard import create
from PIL import Image,ImageTk
from VirtualMouse import Virtual_Mouse
from FingerCount import Finger_Count
from developer import Developer
from support import Support


class VirtualWorld:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x675+0+0")
        self.root.title("Hand Guster Based Virtual Mouse And Virtual Keyboard")

        f_lbl = Label(self.root,text="Hand Guster Based Virtual Mouse And Virtual Keyboard",
        font = ("times new roman",30,"bold"),bg = "darkblue", fg = "cyan")
        f_lbl.place(x=0, y=0, width=1370, height=80)

        # Background Image
        img2 = Image.open(r"C:\\Users\vsanj\Downloads\SEM 2\mini project\Project code\keys\cg1.jpg")
        img2 = img2.resize((1370, 650), Image.ANTIALIAS)
        self.pics2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.pics2)
        bg_img.place(x=0, y=80, width=1370, height=650)

        # Virtual Mouse Botton
        img3 = Image.open(r"C:\Users\vsanj\Downloads\SEM 2\mini project\Project code\keys\vm.jpg")  
        img3 = img3.resize((240, 200), Image.ANTIALIAS)
        self.pics3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img, image = self.pics3, command =  self.virtual_mouse, cursor = "hand2")  ##
        b1.place(x=100, y=70, width=240, height=200)

        b1_nm = Button(bg_img, text = "VIRTUAL MOUSE", command =  self.virtual_mouse, cursor="hand2", 
        font = ("times new roman",15,"bold"),bg = "darkblue", fg = "white")
        b1_nm.place(x=100, y=225, width=240, height=50)

        # Virtual Keyboard
        img4 = Image.open(r"C:\Users\vsanj\Downloads\SEM 2\mini project\Project code\keys\keyb.png")
        img4 = img4.resize((240, 200), Image.ANTIALIAS)
        self.pics4 = ImageTk.PhotoImage(img4)

        b2 = Button(bg_img, image=self.pics4, cursor="hand2", command =  self.virtual_keyboard)
        b2.place(x=580, y=70, width=240, height=200)

        b2_nm = Button(bg_img, text="VIRTUAL KEYBOARD", command =  self.virtual_keyboard, cursor="hand2", 
        font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b2_nm.place(x=580, y=225, width=240, height=50)


        # Finger Count Button
        img6 = Image.open(r"C:\Users\vsanj\Downloads\SEM 2\mini project\Project code\keys\fc.png")
        img6 = img6.resize((240, 200), Image.ANTIALIAS)
        self.pics6 = ImageTk.PhotoImage(img6)

        b4 = Button(bg_img, image=self.pics6, command =  self.finger_count, cursor="hand2")   #
        b4.place(x=1020, y=70, width=240, height=200)

        b4_nm = Button(bg_img, text="FINGER COUNT", command =  self.finger_count, cursor="hand2", 
        font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b4_nm.place(x=1020, y=225, width=240, height=50)

        # Support Button
        img7 = Image.open(r"C:\Users\vsanj\Downloads\SEM 2\mini project\Project code\keys\hd.jpg")
        img7 = img7.resize((240, 200), Image.ANTIALIAS)
        self.pics7 = ImageTk.PhotoImage(img7)

        b5 = Button(bg_img, image=self.pics7, command =  self.helpDesk, cursor="hand2")
        b5.place(x=100, y=330, width=240, height=200)

        b5_nm = Button(bg_img, text="SUPPORT", cursor="hand2", command =  self.helpDesk, 
        font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b5_nm.place(x=100, y=490, width=240, height=50)

        # Developer Button
        img8 = Image.open(r"C:\Users\vsanj\Downloads\SEM 2\mini project\Project code\keys\dv.png")
        img8 = img8.resize((240, 200), Image.ANTIALIAS)
        self.pics8 = ImageTk.PhotoImage(img8)

        b6 = Button(bg_img, image=self.pics8, command =  self.aboutDev, cursor="hand2")
        b6.place(x=580, y=330, width=240, height=200)

        b6_nm = Button(bg_img, text="DEVELOPER", command =  self.aboutDev, cursor="hand2", 
        font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b6_nm.place(x=580, y=490, width=240, height=50)

        # Exit Button
        img10 = Image.open(r"C:\Users\vsanj\Downloads\SEM 2\mini project\Project code\keys\ex.png")
        img10 = img10.resize((240, 200), Image.ANTIALIAS)
        self.pics10 = ImageTk.PhotoImage(img10)

        b8 = Button(bg_img, image=self.pics10, command =  self.isExit, cursor="hand2")
        b8.place(x=1020, y=330, width=240, height=200)

        b8_nm = Button(bg_img, text="EXIT", command =  self.isExit, cursor="hand2", 
        font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b8_nm.place(x=1020, y=490, width=240, height=50)

    #***********Functions************

    # For Virtual Mouse Button
    def virtual_mouse(self):
        self.new_window = Toplevel(self.root)
        self.tab = Virtual_Mouse(self.new_window)

    #For Virtual Keybord Button
    def virtual_keyboard(self):
        root=tkinter.Tk()
        textArea = Text(root, bg="light pink", fg="dark blue", font=("times new roman",15,"bold"))
        textArea.grid(row=1, column=0, sticky='news')

        buttonMain = Button(root, text='Virtual Keyboard', fg="red", bg="cyan", font=("times new roman",20,"bold"),
        command=lambda:create(root, textArea))
        buttonMain.place(x=10, y=490, width=780, height=60)

    #For Finger Count Button
    def finger_count(self):
        self.new_window = Toplevel(self.root)
        self.tab = Finger_Count(self.new_window)

    # For Devloper Button.
    def aboutDev(self):
        self.new_window = Toplevel(self.root)
        self.tab = Developer(self.new_window)

    #For Support Button
    def helpDesk(self):
        self.new_window = Toplevel(self.root)
        self.tab = Support(self.new_window)

    # For Exit Button
    def isExit(self):
        self.Exit = tkinter.messagebox.askyesno("Virtual World!!", "Are You Sure, You Want To Exit?",parent=self.root)
        if self.Exit > 0:
            self.root.destroy()
        else:
            return 
        
        
if __name__=="__main__":
    root = Tk()
    obj = VirtualWorld(root)
    root.mainloop()

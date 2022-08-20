from tkinter import*
from PIL import Image,ImageTk


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x675+0+0")
        self.root.title("DEVLOPER")

        f_lbl = Label(self.root,text="DEVELOPER",
        font = ("times new roman",30,"bold"),bg = "darkblue", fg = "cyan")
        f_lbl.place(x=0, y=0, width=1370, height=80)

        # Background Image
        img2 = Image.open(r"F:\Virtual Mouse\keys\dev.png")
        img2 = img2.resize((1370, 675), Image.ANTIALIAS)
        self.pics2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.pics2)
        bg_img.place(x=0, y=80, width=1370, height=650)

        # Frame
        DevFrame =  Frame(bg_img, bd=2, bg="cyan")
        DevFrame.place(x=950, y=25, width= 400, height=525)

        d_lbl = Label(self.root,text="DEVELOPER INFORMATION",font = ("times new roman",18,"bold"),
        bg = "red", fg = "cyan")
        d_lbl.place(x=1000, y=110)

        d_lbl = Label(self.root,text="Name :- Sanjeet Kumar",font = ("times new roman",14,"bold"), fg = "red")
        d_lbl.place(x=970, y=180)

        d_lbl = Label(self.root,text="Reg No. :- 20PGMCA16",font = ("times new roman",14,"bold"), fg = "red")
        d_lbl.place(x=970, y=240)

        d_lbl = Label(self.root,text="Master Of Computer Application (M.C.A.)",font = ("times new roman",14,"bold"), 
        fg = "red")
        d_lbl.place(x=970, y=300)

        d_lbl = Label(self.root,text="Under Guidence :- Dr. Parshuram M. Kamble",font = ("times new roman",14,"bold"), 
        fg = "red")
        d_lbl.place(x=970, y=350)

        d_lbl = Label(self.root,text="Assistant Professor",font = ("times new roman",14,"bold"), 
        fg = "red")
        d_lbl.place(x=970, y=410)

        d_lbl = Label(self.root,text="School Of Computer Science",font = ("times new roman",14,"bold"), 
        fg = "red")
        d_lbl.place(x=970, y=460)

        d_lbl = Label(self.root,text="Centeral University Of Karnataka",font = ("times new roman",14,"bold"), 
        fg = "red")
        d_lbl.place(x=970, y=510)



if __name__=="__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()

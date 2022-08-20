from tkinter import*
from PIL import Image,ImageTk


class Support:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x675+0+0")
        self.root.title("SUPPORT")
        f_lbl = Label(self.root,text="SUPPORT",
        font = ("times new roman",30,"bold"),bg = "darkblue", fg = "cyan")
        f_lbl.place(x=0, y=0, width=1370, height=80)


        # Background Image
        img2 = Image.open(r"F:\Virtual Mouse\keys\Sup.png")
        img2 = img2.resize((1370, 675), Image.ANTIALIAS)
        self.pics2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.pics2)
        bg_img.place(x=0, y=80, width=1370, height=650)

        d_lbl = Label(self.root,text="Contact Us",font = ("times new roman",18,"bold"),bg="yellow", fg = "red")
        d_lbl.place(x=670, y=240)

        d_lbl = Label(self.root,text="Email Id : vsanjeet8@gmail.gom",font = ("times new roman",15,"bold"), bg="yellow",
        fg = "red")
        d_lbl.place(x=600, y=300)



if __name__=="__main__":
    root = Tk()
    obj = Support(root)
    root.mainloop()

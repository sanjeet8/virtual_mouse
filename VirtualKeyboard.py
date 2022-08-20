#1. Importing Packages
import tkinter as tk

#2. Set Keyboard Buttons in List
buttons = [
    ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace'],
    ['Tab','q','w','e','r','t','y','u','i','o','p','[',']',"\\"],
    ['Caps Lock','a','s','d','f','g','h','j','k','l',';',"'",'Enter'],
    ['Shift','z','x','c','v','b','n','m',',','.','/','Shift'],
    ['Space']
]    
#3. Creat Global Variable
uppercase = False  # use uppercase chars. 

#4. Setting values for some special keys
def select(entry, value):
    global uppercase

    if value == "Space":
        value = ' '
    elif value == 'Enter':
        value = '\n'
    elif value == 'Tab':
        value = '\t'

    if value == "Backspace":
        if isinstance(entry, tk.Entry):
            entry.delete(len(entry.get())-1, 'end')
        
        else: # tk.Text
            entry.delete('end - 2c', 'end')
    elif value in ('Caps Lock', 'Shift'):
        uppercase = not uppercase # change True to False, or False to True
    else:
        if uppercase:
            value = value.upper()
        entry.insert('end', value)

#5. creating floating window keyboard layout
def create(root, entry):

    window = tk.Toplevel(root)
    window.configure(background="cornflowerblue")
    window.wm_attributes("-alpha", 1.0)

    for y, row in enumerate(buttons):

        x = 0

        #for x, text in enumerate(row):
        for text in row:

            if text in ('Enter', 'Shift','Caps Lock', 'Backspace', 'Tab'):
                width = 15
                columnspan = 2
            elif text == 'Space':
                width = 130
                columnspan = 16
            else:                
                width = 5
                columnspan = 1

            tk.Button(window, text=text, width=width, 
                      command=lambda value=text: select(entry, value),
                      padx=3, pady=3, bd=12, bg="black", fg="white"
                     ).grid(row=y, column=x, columnspan=columnspan)

            x += columnspan

# --- main ---

if __name__ == '__main__':
    # Creating Object
    root = tk.Tk()
    root.title('Virtual Keyboard')

    #f_lbl = tk.Label(root,text="Virtual Keyboard", font = ("times new roman",30,"bold"),bg = "darkblue", fg = "cyan")
    #f_lbl.place(x=0, y=10, width=800, height=70)

    textArea = tk.Text(root, bg="light pink", fg="dark blue", font=("times new roman",15,"bold"))
    textArea.grid(row=1, column=0, sticky='news')

    buttonMain = tk.Button(root, text='Virtual Keyboard', fg="red", bg="cyan", font=("times new roman",20,"bold"),
    command=lambda:create(root, textArea))
    buttonMain.place(x=10, y=490, width=780, height=60)

    root.mainloop()



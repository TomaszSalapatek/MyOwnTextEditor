import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def openfile(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files","*.txt")]) # gwiazdka spraia że ma się kończyć na txt
    if not filepath:
       return
    
    text_edit.delete(1.0,tk.END) # 1.0 -> first line, 0 character // tk.END - koniec dokumentu
    with open(filepath,"r") as f:
        content = f.read()
        text_edit.insert(tk.END,content)
    window.title(f"Open File: {filepath}")

def savefile(window, text_edit):
    filepath = asksaveasfilename(filetypes =[("Text Files","*.txt")])
    if not filepath:
        return
    
    with open(filepath,"w") as f:
        content = text_edit.get(1.0,tk.END)
        f.write(content)
        window.title(f"Open File: {filepath}")



def main():
    window = tk.Tk()
    window.title("Me own Text Editor")
    window.rowconfigure(0,minsize=400)
    window.columnconfigure(1,minsize=400)


    text_edit = tk.Text(window,font="Helvetica 18 bold") # można tu między "" dodawać rozmiar i pogruboenie/kursywa itd
    text_edit.grid(row=0,column=1)

    frame = tk.Frame(window, relief=tk.RAISED,bd=2) #releief = aby wyglądało na 3d, bd = border
    save_button = tk.Button(frame, text="Save",command = lambda: savefile(window,text_edit))
    open_button = tk.Button(frame, text = "Open", command= lambda: openfile(window,text_edit)) # gdy dajemy funkcje ktora przyjmuje argumenty to musimy lambdą, bo inaczej byśmy wywołali tą funkcje odrazu, a nie gdy ktoś to kliknie

    save_button.grid(row=0,column=0,padx=5,pady=5, sticky ="ew") # pad -> padding
    open_button.grid(row=1,column=0,padx=5,pady=5, sticky ="ew")
    frame.grid(row=0,column=0,sticky="ns") # sticky przykleja, ns-> sticks to the north  i south side


    #key comands:
    window.bind("<Control-s>", lambda x: savefile(window,text_edit)) #ctrls , uwaga przy lambdzie musi być x, bo ta afunkcja chce jakiś argument
    window.bind("<Control-o>", lambda x: openfile(window,text_edit)) #ctrls , uwaga przy lambdzie musi być x, bo ta afunkcja chce jakiś argument

    window.mainloop()

main()
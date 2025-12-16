import tkinter as tk
import random

main = tk.Tk()
main.title("SLUMPEN")
main.geometry("400x500")



def slump(event=None):
    
    value = random.randint(1,6)
    mapping = {
        1: "hoppa",
        2: "snurra 3 gånger",
        3: "krama någon",
        4: "rita ett porträtt av din vän",
        5: "ta ett varv runt skolan",
        6: "...67",
    }
    text = mapping.get(value, str(value))
    
    output.configure(state= tk.NORMAL)
    output.insert(tk.END, text + "\n")
    output.see(tk.END)
    output.configure(state="disabled")
    output.delete('1.0', tk.END)


output = tk.Text(main,height=10, width=32, state="disabled")
output.grid()

add_button = tk.Button(main,text="random", command=slump)
add_button.grid()

clicked = output.bind("<Button-1>", slump)
main.mainloop()
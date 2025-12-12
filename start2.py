import tkinter as tk
import random

main = tk.Tk()
main.title("SLUMPEN")
main.geometry("400x500")



def slump(event=None):
    
    value = random.randint(1,6)
    mapping = {
        1: "hoppa",
        2: "japp",
        3: "tihi",
        4: "jahopp",
        5: "raaaa",
        6: "lalala",
    }
    text = mapping.get(value, str(value))
    
    output.config(state="normal")
    output.insert(tk.END, text + "\n")
    output.see(tk.END)
    output.config(state="disabled")

output = tk.Text(main,height=10, width=32, state="disabled")
output.grid()

add_button = tk.Button(main,text="random", command=slump)
add_button.grid()

main.mainloop()
import tkinter as tk


main = tk.Tk()
main.title("SLUMPEN")
main.grid()

def slump(event):
    import random
    value = random.randint(1,6)
    if value==1:
        print("hoppa")
    elif value==2:
        print("japp")
    elif value==3:
        print("tihi")
    elif value==4:
        print("jahopp")
    elif value==5:
        print("raaaa")
    elif value==6:
        print("lalala")

add_button = tk.Button(main, text = "test")
add_button.bind("<Button-1>", slump)
add_button.pack()

main.mainloop()
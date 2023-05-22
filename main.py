import tkinter as tk
from screeninfo import get_monitors
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height

def change_text():
    name = entry.get()
    who = radio_var.get()
    label.config(text="Witaj " + name + "\nJesteś " + who)

    jezyki = "Znasz nastepujace jezyki programowania: \n"
    for i in range(len(checkbox_vars)):
        if checkbox_vars[i].get() == 1:
            jezyki = jezyki+checkboxes[i].cget("text")+", "
    jezyki = jezyki[:-2]
    label_jezyki.config(text=jezyki)


root = tk.Tk()
root.title("Bookstore")
# root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}")
#root.iconbitmap("./bookshelf.ico")
root.resizable(width=False, height=False)

left_frame = tk.Frame(root, borderwidth=4, relief="ridge", width=int(screen_width / 8), height=int(screen_height / 4))
left_frame.pack(side="left", padx=10, pady=10)
left_frame.pack_propagate(False)

right_frame = tk.Frame(root, borderwidth=4, relief="ridge", width=left_frame["width"] * 2, height=left_frame["height"])
right_frame.pack(side="left", padx=10, pady=10)
right_frame.pack_propagate(False)

# left frame
entry = tk.Entry(left_frame)
entry.pack(anchor="w", padx=10, pady=10)

button = tk.Button(left_frame, text="OK", command=change_text)
button.pack(anchor="w", padx=10)

radio_var = tk.StringVar(value=" ")

radio_button1 = tk.Radiobutton(left_frame, text="tester", variable=radio_var, value="testerem")
radio_button1.pack(anchor="w", padx=10, pady=10)

radio_button2 = tk.Radiobutton(left_frame, text="programista", variable=radio_var, value="programistą")
radio_button2.pack(anchor="w", padx=10, pady=10)

checkbox_vars = []
checkboxes = []

checkbox_vars.append(tk.IntVar())
checkbox1 = tk.Checkbutton(left_frame,text="java",variable=checkbox_vars[0])
checkbox1.pack(anchor="w",padx=10,pady=10)
checkboxes.append(checkbox1)
checkbox_vars.append(tk.IntVar())
checkbox2 = tk.Checkbutton(left_frame,text="python",variable=checkbox_vars[1])
checkbox2.pack(anchor="w",padx=10,pady=10)
checkboxes.append(checkbox2)




# right frame

label = tk.Label(right_frame, text="Podaj dane:")
label.pack(anchor="center", padx=10, pady=10)

label_jezyki = tk.Label(right_frame, text="")
label_jezyki.pack(anchor="center",padx=10,pady=10)

root.mainloop()
import tkinter as tk


def get_response(response):
    if response == "health":
        res_window = tk.Tk()
        res_label = tk.Label(text=response)
        res_label.pack()
        res_window.mainloop()
    elif response == "financial":
        res_window = tk.Tk()
        res_label = tk.Label(text=response)
        res_label.pack()
        res_window.mainloop()
    else:
        pass


window = tk.Tk()
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
label = tk.Label(master=frame, text="What do you want?")
entry = tk.Entry(master=frame)
button = tk.Button(master=frame, text="Submit")

label.pack()
entry.pack()
button.pack()
frame.pack()

button.bind("<Button-1>", get_response(entry.get()))
window.mainloop()

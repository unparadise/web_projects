import tkinter as tk


root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Today's Exchange Rate",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
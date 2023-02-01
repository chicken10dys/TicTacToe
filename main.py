import tkinter as tk

root = tk.Tk()
# Adjust size
winSize = 600
root.geometry((str)(winSize) + "x" + (str)(winSize))

# set minimum window size value
root.minsize(winSize, winSize)

# set maximum window size value
root.maxsize(winSize, winSize)

# Create a canvas widget
canvas = tk.Canvas(root, width=winSize, height=winSize)
canvas.pack()

# Draw play area
canvas.create_rectangle(0, 0, winSize, winSize, fill="grey")
playArea = canvas.create_rectangle(0, 0, 500, 500, fill="white")
canvas.create_line((500 / 3) - 5, 0, (500 / 3) - 5, 500, fill="black", width=10)
canvas.create_line((500 / 1.5) - 5, 0, (500 / 1.5) - 5, 500, fill="black", width=10)
canvas.create_line(0, (500 / 3) - 5, 500, (500 / 3) - 5, fill="black", width=10)
canvas.create_line(0, (500 / 1.5) - 5, 500, (500 / 1.5) - 5, fill="black", width=10)
root.mainloop()
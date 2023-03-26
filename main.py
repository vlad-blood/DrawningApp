import time
import tkinter as tk
import random
window = tk.Tk()
window.title("some title")
window.geometry('600x600')
c = tk.Canvas(window,width=450,height=450,bg="grey")
c.pack()

def draw(event):
    brush_size = 5
    c.create_oval(event.x - brush_size,
        event.y - brush_size,
        event.x + brush_size,
        event.y + brush_size,fill='black')
def clean(event):
    brush_size = 200
    c.create_oval(event.x - brush_size,
                  event.y - brush_size,
                  event.x + brush_size,
                  event.y + brush_size, fill='grey',outline='grey')



c.bind('<B1-Motion>',draw)
c.bind('<B2-Motion>',clean)
c.bind('<Button-3>',rand_dot)
window.mainloop()
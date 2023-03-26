import tkinter as tk

class DrawApp():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Простая рисовалка")
        self.window.geometry('600x600')
        self.brush_size = 2
        self.c = tk.Canvas(self.window, width=450, height=450, bg="grey")
        self.c.pack()
        self.c.bind('<B1-Motion>', self.draw)
        self.c.bind('<B2-Motion>', self.clean)
        self.window.mainloop()

    def draw(self,event):
        brush_size = 5
        self.c.create_oval(event.x - brush_size,
                      event.y - brush_size,
                      event.x + brush_size,
                      event.y + brush_size, fill='black')

    def clean(self,event):
        brush_size = 200
        self.c.create_oval(event.x - brush_size,
                      event.y - brush_size,
                      event.x + brush_size,
                      event.y + brush_size, fill='grey', outline='grey')


if __name__ == '__main__':
    DrawApp()

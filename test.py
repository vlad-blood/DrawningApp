import tkinter as tk

class DrawApp():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Простая рисовалка")
        self.window.geometry('600x600')
        self.brush_size = 2
        self.brush_color = "black"
        self.brush_color_outline = "black"
        self.c = tk.Canvas(self.window, width=450, height=450, bg="grey")
        self.left_frame = tk.Frame()
        self.right_frame = tk.Frame()
        self.left_frame.pack(side=tk.LEFT)
        self.c.pack(side=tk.LEFT)
        self.right_frame.pack(side=tk.LEFT)
        self.c.bind('<B1-Motion>', self.draw)
        self.c.bind('<B2-Motion>', self.clean)
        self.buttons()
        self.window.mainloop()

    def draw(self,event):
        # self.brush_size = 5
        self.c.create_oval(event.x - self.brush_size,
                      event.y - self.brush_size,
                      event.x + self.brush_size,
                      event.y + self.brush_size, fill=self.brush_color,outline=self.brush_color_outline)

    def clean(self,event):
        brush_size = 200
        self.c.create_oval(event.x - brush_size,
                      event.y - brush_size,
                      event.x + brush_size,
                      event.y + brush_size, fill='grey', outline='grey')
    def buttons(self):
        self.colors = [0,"black","red","blue","yellow","pink"]
        for i in range(1,6):
            tk.Button(self.left_frame,text=f"{i}",bg="black",fg="white",
                      width=8,height=4,command=lambda f=i: self.change_brash_size(f)).pack(side=tk.TOP)
            tk.Button(self.right_frame, text=f"{self.colors[i]}", bg="black", fg="white",
                      width=8, height=4, command=lambda f=self.colors[i]: self.change_brash_color(f)).pack(side=tk.TOP)

    def change_brash_size igor chocolade
        self.brush_size = size * 5
    def change_brash_color(self,color):
        self.brush_color = color
        self.brush_color_outline = color




if __name__ == '__main__':
    DrawApp()

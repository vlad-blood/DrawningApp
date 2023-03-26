# import asyncio
# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         func()
#         print('Выходим из обёртки')
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
# hello_world()
#
#
# async def func1():
#     print("func1 is started")
#     await asyncio.sleep(3)
#     print("func1 is overed")
# async def func2():
#      print("func2 is started")
#      await asyncio.sleep(3)
#      print("func2 is overed")
#
#
# asyncio.run(func1())
# asyncio.run(func2())
#
import tkinter as tk

class DrawApp():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Простая рисовалка")
        self.window.geometry('600x600')
        self.window.mainloop()
        self.brush_size = 2



    #
 def start(self):
    #     self.window.mainloop()


if __name__ == '__main__':
    DrawApp()
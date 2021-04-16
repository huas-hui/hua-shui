import tkinter as tk #tkinter库
import os
window = tk.Tk()
window.title('阅读之窗')
window.geometry('500x500')
label = tk.Label(window,text = '我喜欢阅读',height = 10,width = 40,bg = 'blue')
label.pack()
counter = 0
def menuClick():
    global counter
    label.config(text='第'+str(counter)+'次点击')
    counter += 1

def nine():
    p = os.system('九九乘法表.py')
    


def MP3():
    m = os.system('mp3.py')
    

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label = '文件',menu = filemenu)
filemenu.add_command(label = '新建',command = menuClick)
filemenu.add_command(label = '打开',command = menuClick)
filemenu.add_command(label = '保存',command = menuClick)
filemenu.add_separator()
filemenu.add_command(label = '退出',command = window.destroy)

studymenu = tk.Menu(menubar)
menubar.add_cascade(label = '学习',menu = filemenu)
filemenu.add_command(label = '九九乘法表',command = nine)
filemenu.add_separator()
menubar.add_cascade(label = '播放器',menu = filemenu)
filemenu.add_command(label = 'mp3',command = MP3)

window.config(menu = menubar)
window.mainloop

import pygame
import os
from tkinter import *
root = Tk()
root.title('专用播放器')
root.geometry('800x600')
pygame.init()

music_path = r'C:\music'
current_play = '鹏泊 - 啷个哩个啷mp3'
music_name = StringVar()

def play():
 music_name.set(current_play)
 pygame.mixer.music.load(os.path.join(music_path, current_play))
 pygame.mixer.music.play()

Label(root, textvariable=music_name, font=('宋体', 14), justify='center',
 bg='#ADD8E6').place(relx=0, rely=0.1, relwidth=1, relheight=0.3)
Button(root, text="播放", command=play).place(relx=0, rely=0.5, relwidth=0.2, relheight=0.1)
Button(root, text="暂停", command=lambda: pygame.mixer.music.pause()).place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.1)
Button(root, text="恢复", command=lambda: pygame.mixer.music.unpause()).place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.1)
Button(root, text="停止", command=lambda: pygame.mixer.music.stop()).place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.1)
Button(root, text="重播", command=lambda: pygame.mixer.music.rewind()).place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.1)
root.mainloop()

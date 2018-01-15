import tkinter as tk

def hello():
    print('hello!')
    
arbiter = tk.Tk()

menubar = tk.Menu(arbiter)
#Game
gamemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Game", menu=gamemenu)
gamemenu.add_command(label='New', command=hello, accelerator='F2')
gamemenu.add_command(label
mouse = tk.Menu(optionmenu, tearoff=0)
optionmenu.add_cascade(label="Mouse Setup", menu=mouse)

irc_text.add_command(label="TXT")
irc.add_command(label="Silent Mode Output")

    #Open Folder
folder = tk.Menu(optionmenu, tearoff=0)
optionmenu.add_cascade(label="Open Folder", menu=folder)
folder.add_command(label="Game Folder", accelerator="H")
folder.add_command(label="Screenshots Folder", accelerator="Ctrl+9")
folder.add_command(label="Boards Folder", accelerator="Ctrl+8")
folder.add_command(label="Board presets Folder", accelerator="Ctrl+7")
folder.add_command(label="Plugins Folder", accelerator="Ctrl+6")
    #Screenshot
screenshot = tk.Menu(optionmenu, tearoff=0)
optionmenu.add_cascade(label="Screenshot", menu=screenshot)
screenshot.add_command(label="Make JPG Screenshot", accelerator="F12")
screenshot.add_command(label="Make BMP Screenshot", accelerator="Ctrl+F12")
screenshot.add_command(label="Save Board as BMP")
screenshot.add_command(label="Save Board as TXT")
screenshot.add_separator()
screenshot.add_command(label="Make FULL Screenshot", accelerator="Shift+F12")

optionmenu.add_command(label="Draw Mouse Chart")
optionmenu.add_command(label="Show Counters", command=hello, accelerator="C")
optionmenu.add_command(label="Show Debug Protocol", command=hello, accelerator="D")
optionmenu.add_separator()
optionmenu.add_command(label="Plugins", command=hello)

#help
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="?", menu=helpmenu)
helpmenu.add_command(label="About", command=hello, accelerator="F1")
helpmenu.add_command(label="Index", command=hello, accelerator="Ctrl+F1")
helpmenu.add_separator()
helpmenu.add_command(label="Send Feedback")
helpmenu.add_command(label="Homepage", accelerator="Home")
helpmenu.add_separator()
helpmenu.add_command(label="Join #minesweeprt channel")

community = tk.Menu(helpmenu, tearoff=0)
helpmenu.add_cascade(label="Community", menu=community)
community.add_command(label="ENG Authoritative Minesweeper Site")
community.add_command(label="ENG Authoritative Minesweeper Guestbook")
community.add_command(label="ENG Active Ranking")
community.add_command(label="ENG Russian Bestever Players")




arbiter.config(menu=menubar)

tk.mainloop()

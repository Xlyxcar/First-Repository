import tkinter as tk

def hello():
    print('hello!')
    
arbiter = tk.Tk()

menubar = tk.Menu(arbiter)
#Game
gamemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Game", menu=gamemenu)
gamemenu.add_command(label='New', command=hello, accelerator='F2')
gamemenu.add_command(label="Restart", command=hello, accelerator="F3")
gamemenu.add_command(label="Play Video", command=hello, accelerator="F4")
gamemenu.add_command(label="Load Custom Board", command=hello, accelerator="Ctrl+V")
gamemenu.add_separator()
gamemenu.add_command(label="Save Replay File", command=hello, accelerator="Ctrl+S")
gamemenu.add_command(label="Save Custom Board", command=hello, accelerator="Ctrl+C")
gamemenu.add_command(label="Preview Replay", command=hello, accelerator="Ctrl+Z")
gamemenu.add_separator()
gamemenu.add_checkbutton(label="Beginner", command=hello, accelerator="1")
gamemenu.add_checkbutton(label="Intermediate", command=hello, accelerator="2")
gamemenu.add_checkbutton(label="Expert", command=hello, accelerator="3")
gamemenu.add_checkbutton(label="Custom Board", command=hello, accelerator="4")
gamemenu.add_separator()
gamemenu.add_command(label="Local High Scores", command=hello, accelerator="F6")
gamemenu.add_command(label="Statistics", command=hello, accelerator='F7', font=("msyh", "10", "bold"))
gamemenu.add_command(label="Save Stats CSV", command=hello)
gamemenu.add_separator()
gamemenu.add_command(label="Boss-Key", command=hello, accelerator="Alt+F2")
gamemenu.add_command(label="Exit", command=hello, accelerator="Alt+F4")

#Options
optionmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Options", menu=optionmenu)
optionmenu.add_command(label="Preferences", command=hello, accelerator="F5", font=("arial", "10", "bold"))
optionmenu.add_command(label="Language", command=hello, accelerator="L")
    #Mouse
mouse = tk.Menu(optionmenu, tearoff=0)
optionmenu.add_cascade(label="Mouse Setup", menu=mouse)
mouse.add_command(label="Open Mouse Control Panel", accelerator="M")
                  
optionmenu.add_separator()
    #IRC
irc = tk.Menu(optionmenu, tearoff=0)
optionmenu.add_cascade(label="IRC Addon", menu=irc)
irc.add_command(label="Copy Last Game Info", accelerator="Ctrl+L")
irc.add_command(label="Copy Game Info by Number")
irc.add_command(label="Copy Time Records Info")
irc.add_command(label="Copy 3BV/s Records Info")
irc.add_command(label="Copy Averages Info")
irc.add_command(label="Copy Today`s BEG Playing Info")
irc.add_command(label="Copy Today`s INT Playing Info")
irc.add_command(label="Copy Today`s EXP Playing Info")
irc.add_separator()
        #IRC Text
irc_text = tk.Menu(irc, tearoff=0)
irc.add_cascade(label="IRC Text Format", menu=irc_text)
irc_text.add_command(label="mlRC")
irc_text.add_command(label="CGI")
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

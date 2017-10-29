# Copyright (C) 2017 mrdlee1 <mrdlee1@gmail.com>
# 
# "Survivor" is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# "Survivor" is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
from Tkinter import *

class survivor:

    def __init__(self):
        #initializing variables
        self.Path = "/home/m0rd/survivor/Assets/"
        self.X = ("Purisa", 10)
        #array for the unusual characters and symbols
        self.SpecialChar = [u"\u25cf", u"\u263c", u"\u263e"]
        self.night = False
        self.root = Tk()
        self.root.title("Survivor")
        self.Icon = PhotoImage(file=self.Path + "icon.png")
        self.root.call('wm', 'iconphoto', self.root._w, self.Icon)
        self.Photo1 = PhotoImage(file=self.Path + "sea.png")
        self.Photo2 = PhotoImage(file=self.Path + "shelter.png")
        self.Photo3 = PhotoImage(file=self.Path + "tree.png")
        self.Photo4 = PhotoImage(file=self.Path + "wood.png")
        self.Photo5 = PhotoImage(file=self.Path + "steak.png")
        self.Photo6 = PhotoImage(file=self.Path + "back.png")
        self.Photo7 = PhotoImage(file=self.Path + "pole.png")
        self.Photo8 = PhotoImage(file=self.Path + "embark.png")
        self.Photo9 = PhotoImage(file=self.Path + "store.png")
        self.Photo10 = PhotoImage(file=self.Path + "corn.png")
        self.Photo11 = PhotoImage(file=self.Path + "raft.png")
        self.Photo12 = PhotoImage(file=self.Path + "anvil.png")
        self.HungerBar = StringVar()
        self.HungerBar = "Hunger::"
        self.TimeBar = StringVar()
        self.TimeBar = ''
        self.Food = IntVar()
        self.Food = 100
        self.Wood = IntVar()
        self.Wood = 100
        self.Raft = IntVar()
        self.Raft = 0
        self.Hunger = IntVar()
        self.Hunger = 100
        self.CurrentWindowID = StringVar()
        self.CurrentWindowID = "mainmenu"
        #Hunger & time indicator
        self.TopBar = Frame(self.root)
        self.HungerLabel = Label(self.TopBar, font=self.X, text=self.HungerBar, bg="white", fg="crimson")  # .pack(side=LEFT)
        self.TimeLabel = Label(self.TopBar, font=self.X, text=self.TimeBar, bg="white", fg="gold")  # .pack(side=RIGHT)
        self.hlb()
        self.TopBar.pack(side=TOP, fill=X)
        self.mainmenu = Frame(self.root)
        topbuttons = Frame(self.mainmenu)
        Button(topbuttons, image=self.Photo10, command=self.farm, bg="wheat").pack(side=LEFT, anchor=E)
        Button(topbuttons, image=self.Photo8, command=self.travel, bg="lightgreen").pack(side=RIGHT, anchor=W)
        Button(topbuttons, image=self.Photo9, command=self.store, bg="lightgray").pack(side=BOTTOM)
        topbuttons.pack()
        bottombuttons = Frame(self.mainmenu)
        Button(bottombuttons, image=self.Photo3, command=self.forest, bg="lightgreen").pack(side=LEFT, anchor=E)
        Button(bottombuttons, image=self.Photo2, command=self.shelter, bg="burlyWood").pack(side=RIGHT, anchor=W)
        Button(bottombuttons, image=self.Photo1, command=self.sea, bg="lightblue").pack(side=BOTTOM)
        bottombuttons.pack()
        self.mainmenu.pack(fill=BOTH)
        #the label for giving feedback
        self.feedback = Frame(self.root)
        self.textbox = Message(self.feedback, font=self.X, text="This is working", bd=3, relief="sunken", bg="tan", fg="white").pack(pady=6, fill=X)
        self.feedback.pack(side=BOTTOM, fill=X)
        self.refresh()
        self.root.mainloop()

    #functions for handling the menus
    def back(self, cmid):
        if cmid == "smenu":
            self.storemenu.pack_forget()
            self.mainmenu.pack(fill=BOTH)
        elif cmid == "fmenu":
            self.forestmenu.pack_forget()
            self.mainmenu.pack(fill=BOTH)
        elif cmid == "stmenu":
            self.sheltermenu.pack_forget()
            self.mainmenu.pack(fill=BOTH)
        elif cmid == "cmenu":
            self.craftmenu.pack_forget()
            self.sheltermenu.pack()
        elif cmid == "seamenu":
            self.seamenu.pack_forget()
            self.mainmenu.pack(fill=BOTH)
        elif cmid == "trmenu":
            self.map.pack_forget()
            self.mainmenu.pack(fill=BOTH)

    def hungerf(self):
        self.Hunger = self.Hunger - 5
        if self.Hunger < 1:
            if self.CurrentWindowID == "forest":
                self.forestmenu.pack_forget()
            elif self.CurrentWindowID == "sea":
                self.seamenu.pack_forget()
            elif self.CurrentWindowID == "craft":
                self.craftmenu.pack_forget()
            elif self.CurrentWindowID == "shelter":
                self.sheltermenu.pack_forget()
            elif self.CurrentWindowID == "travel":
                self.map.pack_forget()
            self.starvemenu = Frame(self.root)
            self.CurrentWindowID = "starved"
            Label(self.starvemenu, font=self.X, text="You just starved to death!").pack()
            Button(self.starvemenu, font=self.X, text="Respawn", command=self.shelter).pack()
            self.starvemenu.pack()
        self.hlb()

    def store(self):
        self.mainmenu.pack_forget()
        self.storemenu = Frame(self.root)
        Label(self.storemenu, font=self.X, text="Hunger:: " + repr(self.Hunger), bg="chocolate", fg="black").pack(pady=5)
        Label(self.storemenu, font=self.X, text="Wood:: " + repr(self.Wood), bg="chocolate", fg="white").pack(pady=5)
        Label(self.storemenu, font=self.X, text="Food:: " + repr(self.Food), bg="red", fg="white").pack(pady=5)
        Label(self.storemenu, font=self.X, text="Rafts:: " + repr(self.Raft), bg="chocolate", fg="white").pack(pady=5)
        Button(self.storemenu, image=self.Photo6, command=lambda *arg: self.back("smenu"), bg="white").pack(pady=5)
        self.storemenu.pack()
    #everything related to forest will follow from here

    def Woodcollect(self):
        self.CurrentWindowID = "forest"
        self.hungerf()
        self.Wood = self.Wood + 20
        print repr(self.Wood)

    def trap(self):
        self.CurrentWindowID = "forest"
        self.hungerf()
        if self.Wood >= 5:
            self.Food = self.Food + 20
            print repr(self.Food)
            self.Wood = self.Wood - 5
        else:
            print "Not enough Wood"

    def forest(self):
        self.mainmenu.pack_forget()
        self.forestmenu = Frame(self.root)
        self.CurrentWindowID = "forest"
        self.hungerf()
        Label(self.forestmenu, font=self.X, text="Hunger:: " + repr(self.Hunger), bg="chocolate", fg="black").pack()
        Button(self.forestmenu, image=self.Photo4, command=self.Woodcollect, bg="burlyWood").pack(side=LEFT, anchor=E)
        Button(self.forestmenu, image=self.Photo5, command=self.trap, bg="moccasin").pack(side=RIGHT, anchor=W)
        Button(self.forestmenu, image=self.Photo6, command=lambda *arg: self.back("fmenu"), bg="white").pack(side=BOTTOM)
        self.forestmenu.pack()
        #####################################################
        #all the functions for shelter

    def eat(self):
        if self.Food >= 10 and self.Hunger <= 90:
            self.Food = self.Food - 10
            self.Hunger = self.Hunger + 10
            print repr(self.Food)
            print repr(self.Hunger)
        else:
            print "Not enough Food or you are not hungry"
        self.hlb()

    def builds(self, buildid):
        if buildid == "Raft":
            if self.Wood >= 20:
                self.Raft = self.Raft + 1
                print self.Raft
            else:
                print "You are lacking Wood to craft this!"
        #use elif statements for the rest of the crafts

    def craft(self):
        self.CurrentWindowID = "craft"
        self.hungerf()
        self.sheltermenu.pack_forget()
        self.craftmenu = Frame(self.root)
        Button(self.craftmenu, image=self.Photo11, command=lambda *arg: self.builds("Raft")).pack()
        Button(self.craftmenu, image=self.Photo6, command=lambda *arg: self.back("cmenu"), bg="white").pack()
        self.craftmenu.pack()

    def shelter(self):
        if self.CurrentWindowID == "starved":
            self.starvemenu.pack_forget()
            self.Hunger = 105
        self.CurrentWindowID = "shelter"
        self.hungerf()
        self.mainmenu.pack_forget()
        self.sheltermenu = Frame(self.root)
        Label(self.sheltermenu, font=self.X, text="Hunger:: " + repr(self.Hunger), bg="chocolate", fg="black").pack()
        Button(self.sheltermenu, font=self.X, image=self.Photo5, command=self.eat, bg="wheat").pack(side=LEFT, anchor=E)
        Button(self.sheltermenu, font=self.X, image=self.Photo12, command=self.craft, bg="palegoldenrod").pack(side=RIGHT, anchor=W)
        Button(self.sheltermenu, image=self.Photo6, command=lambda *arg: self.back("stmenu"), bg="white").pack(side=BOTTOM)
        self.sheltermenu.pack()
    #############################################
    #all the functions for the seamenu from here onwards

    def fish(self):
        self.CurrentWindowID = "sea"
        self.hungerf()
        self.Food = self.Food + 10
        print repr(self.Food)

    def embark(self):
        if self.Raft <= 0:
            print "You need a Raft to travel on the sea"
        else:
            print "Let's sail!"

    def sea(self):
        self.CurrentWindowID = "sea"
        self.hungerf()
        self.mainmenu.pack_forget()
        self.seamenu = Frame(self.root)
        Label(self.seamenu, font=self.X, text="Hunger:: " + repr(self.Hunger), bg="chocolate", fg="black").pack()
        Button(self.seamenu, image=self.Photo7, command=self.fish, bg="lightblue",).pack(side=LEFT, anchor=E)
        Button(self.seamenu, image=self.Photo8, command=self.embark, bg="blue").pack(side=RIGHT, anchor=W)
        Button(self.seamenu, image=self.Photo6, command=lambda *arg: self.back("seamenu"), bg="white").pack(side=BOTTOM)
        self.seamenu.pack()

    #the farm code
    def farm(self):
        print "This works!"

    #travel code
    def travel(self):
        self.CurrentWindowID = "travel"
        self.hungerf()
        self.mainmenu.pack_forget()
        self.map = Frame(self.root)
        #the 'map' on which the user can move
        Message(self.map, text='###- A Place Holder -###', fg='black', bg='gold').pack(fill=X)
        Button(self.map, image=self.Photo6, command=lambda *arg: self.back("trmenu"), bg="white").pack()
        self.map.pack(fill=X)

    def hlb(self):
        hsymb = self.SpecialChar[0]
        prntcount = 1
        hg = 90
        pc = hg / 10 + 1
        interrupt = False
        while True:
            if self.Hunger > hg:
                while prntcount <= pc:
                    self.HungerBar = self.HungerBar + hsymb
                    prntcount += 1
                prntcount = 1
                interrupt = True
            hg = hg - 10
            pc = hg / 10 + 1
            self.HungerLabel.config(text=self.HungerBar)
            self.HungerLabel.pack(side=RIGHT)
            self.HungerBar = "Hunger::"  # initialize the var for the next time
            if interrupt:
                break

        self.TimeLabel.pack(side=LEFT)

    def refresh(self):
        self.TimeBar = self.TimeBar[: -1]
        if self.TimeBar == '':
            if self.night is False:
                tsymb = self.SpecialChar[1]
                self.TimeBar = tsymb * 10
                self.TimeLabel.config(fg='gold')
                self.night = True
            elif self.night is True:
                tsymb = self.SpecialChar[2]
                self.TimeBar = tsymb * 10
                self.TimeLabel.config(fg='black')
                self.night = False
        self.TimeLabel.config(text="Time::" + self.TimeBar)
        self.root.after(2000, self.refresh)

survivor()


from Tkinter import *
#as of now all on my mind is implemented. next one will be farming i think. 28/7/17
#Important: starving is not yet implemented
#ignore that. starving is now implemented. well sort of.
#as of now, starving is implemented completely.
#just a note. all the images are 39x38 and exported. then later imported, bitmap traced on 0.0 exposure
#using edge detection  i think, background removed from the bitmap tracing, grouped and then again exported
#doubt is on whether or not edge detection is used. most probably it was edge detection.
#one way to achieve the delay between button presses(Wood collection, fishing etc) is to pack_forget the
#button and then use the time module to delay it for a few seconds and then pack it again. write up
#a function for that. something better is to make the function return nothing for 6 seconds and change the button
#releif to sunken then normal and then raised with an interval of 2 seconds each.
#U263B and u263a are happy faces.
#u2665 is a heart. u263c is a sun, u25cb and u25cf are perfect for the hunger bar


class survivor:

    def __init__(self):
        #initializing variables
        self.Path = "/home/m0rd/survivor/Assets/"
        self.X = ("Purisa", 10)
        #array for the unusual characters and symbols
        self.SpecialChar = [u"\u25cf", u"\u263c"]
        self.root = Tk()
        self.root.title("Survivor")
        self.Icon = PhotoImage(file=self.Path + "icon.png")
        self.root.call('wm', 'iconphoto', self.root._w, self.Icon)
        #photos should be here, tried to move it didnt work
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
        self.HungerBar = StringVar()
        self.HungerBar = "Hunger::"
        self.TimeBar = StringVar()
        self.TimeBar = "Noon::"
        self.Food = IntVar()
        self.Food = 100
        self.Wood = IntVar()
        self.Wood = 100
        self.Raft = IntVar()
        self.Raft = 0
        self.Hunger = IntVar()
        self.Hunger = 100
        #similiar to cmid but with a different purpose and cmid wasnt designed that way
        self.CurrentWindowID = StringVar()
        self.CurrentWindowID = "mainmenu"
        #Hunger & time indicator
        self.TopBar = Frame(self.root)
        self.HungerLabel = Label(self.TopBar, font=self.X, text=self.HungerBar, bg="white", fg="crimson")  # .pack(side=LEFT)
        self.TimeLabel = Label(self.TopBar, font=self.X, text=self.TimeBar, bg="white", fg="gold")  # .pack(side=RIGHT)
        self.hlb()
        self.TopBar.pack(side=TOP, fill=X)
        #the main program
        self.mainmenu = Frame(self.root)
        #separate frames for each row of buttons should have used grid but im just gonna brute force pack
        #until i get the result i want
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
        #the console for giving feedback
        self.feedback = Frame(self.root)
        self.textbox = Message(self.feedback, font=self.X, text="This is working", bd=3, relief="sunken", bg="tan", fg="white").pack(pady=6, fill=X)
        self.feedback.pack(side=BOTTOM, fill=X)
        self.refresh()
        self.root.mainloop()

    #functions for handling the menus
    #cmid is short for Current Menu ID. useful for the back button. universal back function sounds good does work
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
            self.starvemenu = Frame(self.root)
            self.CurrentWindowID = "starved"
            Label(self.starvemenu, font=self.X, text="You just starved to death!").pack()
            Button(self.starvemenu, font=self.X, text="Respawn", command=self.shelter).pack()
            self.starvemenu.pack()
        self.hlb()

    #store function and menu finished as the last version
    def store(self):
        self.mainmenu.pack_forget()
        self.storemenu = Frame(self.root)
        Label(self.storemenu, font=self.X, text="Hunger:: " + repr(self.Hunger), bg="chocolate", fg="black").pack(pady=5)
        Label(self.storemenu, font=self.X, text="Wood:: " + repr(self.Wood), bg="chocolate", fg="white").pack(pady=5)
        Label(self.storemenu, font=self.X, text="Food:: " + repr(self.Food), bg="red", fg="white").pack(pady=5)
        Label(self.storemenu, font=self.X, text="Rafts:: " + repr(self.Raft), bg="chocolate", fg="white").pack(pady=5)
        Button(self.storemenu, image=self.Photo6, command=lambda *arg: self.back("smenu"), bg="white").pack(pady=5)
        self.storemenu.pack()
    #remember to reduce Hunger in these menu operations
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
        Button(self.sheltermenu, font=self.X, text="Eat", command=self.eat, bg="wheat", fg="black").pack(side=LEFT, anchor=E)
        Button(self.sheltermenu, font=self.X, text="CRafting", command=self.craft, bg="white", fg="black").pack(side=RIGHT, anchor=W)
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
        print "this woooooooooorkd"

    def hlb(self):
        hsymb = self.SpecialChar[0]
        tsymb = self.SpecialChar[1]
        prntcount = 1
        loopr = True
        hg = 90
        pc = hg / 10 + 1
        #this loop is a mess it wont work, fix that. unfortunately the fix is increasing the Hunger meter
        #f*ck the above comment, totally got this to work
        while loopr:
            if self.Hunger > hg:
                while prntcount <= pc:
                    self.HungerBar = self.HungerBar + hsymb
                    prntcount += 1
                prntcount = 1
                loopr = False
            hg = hg - 10
            pc = hg / 10 + 1
            self.HungerLabel.config(text=self.HungerBar)
            self.HungerLabel.pack(side=RIGHT)
            self.HungerBar = "Hunger::"  # initialize the var for the next time

        self.TimeBar = tsymb + tsymb + tsymb + tsymb + tsymb + tsymb + tsymb + tsymb + tsymb + tsymb
        self.TimeLabel.config(text="Time:: " + self.TimeBar)
        self.TimeLabel.pack(side=LEFT)

    def refresh(self):
        self.TimeBar = self.TimeBar[: -1]
        if self.TimeBar == '':
            print 'well shit!'
        self.TimeLabel.config(text=self.TimeBar)
        self.root.after(1000, self.refresh)

survivor()
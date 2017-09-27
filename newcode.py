from Tkinter import *
#as of now all on my mind is implemented. next one will be farming i think. 28/7/17
#Important: starving is not yet implemented
#ignore that. starving is now implemented. well sort of.
#as of now, starving is implemented completely.
#just a note. all the images are 39x38 and exported. then later imported, bitmap traced on 0.0 exposure
#using edge detection  i think, background removed from the bitmap tracing, grouped and then again exported
#doubt is on whether or not edge detection is used. most probably it was edge detection.
#one way to achieve the delay between button presses(wood collection, fishing etc) is to pack_forget the
#button and then use the time module to delay it for a few seconds and then pack it again. write up
#a function for that. something better is to make the function return nothing for 6 seconds and change the button
#releif to sunken then normal and then raised with an interval of 2 seconds each.
#U263B and u263a are happy faces.
#u2665 is a heart. u263c is a sun, u25cb and u25cf are perfect for the hunger bar


class survivor:

    def __init__(self):
        #initializing variables
        self.path = "/home/m0rd/survivor/Assets/"
        self.x = ("Purisa", 10)
        #array for the unusual characters and symbols
        self.spchar = [u"\u25cf", u"\u263c"]
        self.root = Tk()
        self.root.title("Survivor")
        self.icon = PhotoImage(file=self.path + "icon.png")
        self.root.call('wm', 'iconphoto', self.root._w, self.icon)
        #photos should be here, tried to move it didnt work
        self.photo1 = PhotoImage(file=self.path + "sea.png")
        self.photo2 = PhotoImage(file=self.path + "shelter.png")
        self.photo3 = PhotoImage(file=self.path + "tree.png")
        self.photo4 = PhotoImage(file=self.path + "wood.png")
        self.photo5 = PhotoImage(file=self.path + "steak.png")
        self.photo6 = PhotoImage(file=self.path + "back.png")
        self.photo7 = PhotoImage(file=self.path + "pole.png")
        self.photo8 = PhotoImage(file=self.path + "embark.png")
        self.photo9 = PhotoImage(file=self.path + "store.png")
        self.photo10 = PhotoImage(file=self.path + "corn.png")
        self.photo11 = PhotoImage(file=self.path + "raft.png")
        self.hungrbr = StringVar()
        self.hungrbr = "Hunger::"
        self.timebr = StringVar()
        self.timebr = "Noon::"
        self.food = IntVar()
        self.food = 100
        self.wood = IntVar()
        self.wood = 100
        self.raft = IntVar()
        self.raft = 0
        self.hunger = IntVar()
        self.hunger = 100
        #similiar to cmid but with a different purpose and cmid wasnt designed that way
        self.currentwindowid = StringVar()
        self.currentwindowid = "mainmenu"
        #hunger & time indicator
        self.topbar = Frame(self.root)
        self.hlbl = Label(self.topbar, font=self.x, text=self.hungrbr, bg="white", fg="crimson")  # .pack(side=LEFT)
        self.tlbl = Label(self.topbar, font=self.x, text=self.timebr, bg="white", fg="gold")  # .pack(side=RIGHT)
        self.hlb()
        self.topbar.pack(side=TOP, fill=X)
        #the main program
        self.mainmenu = Frame(self.root)
        #separate frames for each row of buttons should have used grid but im just gonna brute force pack
        #until i get the result i want
        topbuttons = Frame(self.mainmenu)
        Button(topbuttons, image=self.photo10, command=self.farm, bg="wheat").pack(side=LEFT, anchor=E)
        Button(topbuttons, image=self.photo8, command=self.travel, bg="lightgreen").pack(side=RIGHT, anchor=W)
        Button(topbuttons, image=self.photo9, command=self.store, bg="lightgray").pack(side=BOTTOM)
        topbuttons.pack()
        bottombuttons = Frame(self.mainmenu)
        Button(bottombuttons, image=self.photo3, command=self.forest, bg="lightgreen").pack(side=LEFT, anchor=E)
        Button(bottombuttons, image=self.photo2, command=self.shelter, bg="burlywood").pack(side=RIGHT, anchor=W)
        Button(bottombuttons, image=self.photo1, command=self.sea, bg="lightblue").pack(side=BOTTOM)
        bottombuttons.pack()
        self.mainmenu.pack(fill=BOTH)
        #the console for giving feedback
        self.feedback = Frame(self.root)
        self.textbox = Message(self.feedback, font=self.x, text="This is working", bd=3, relief="sunken", bg="tan", fg="white").pack(pady=6, fill=X)
        self.feedback.pack(side=BOTTOM, fill=X)
        #self.topbar.update_idletasks()
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
        self.hunger = self.hunger - 5
        if self.hunger < 1:
            if self.currentwindowid == "forest":
                self.forestmenu.pack_forget()
            elif self.currentwindowid == "sea":
                self.seamenu.pack_forget()
            elif self.currentwindowid == "craft":
                self.craftmenu.pack_forget()
            elif self.currentwindowid == "shelter":
                self.sheltermenu.pack_forget()
            self.starvemenu = Frame(self.root)
            self.currentwindowid = "starved"
            Label(self.starvemenu, font=self.x, text="You just starved to death!").pack()
            Button(self.starvemenu, font=self.x, text="Respawn", command=self.shelter).pack()
            self.starvemenu.pack()
        self.hlb()

    #store function and menu finished as the last version
    def store(self):
        self.mainmenu.pack_forget()
        self.storemenu = Frame(self.root)
        Label(self.storemenu, font=self.x, text="Hunger:: " + repr(self.hunger), bg="chocolate", fg="black").pack(pady=5)
        Label(self.storemenu, font=self.x, text="Wood:: " + repr(self.wood), bg="chocolate", fg="white").pack(pady=5)
        Label(self.storemenu, font=self.x, text="Food:: " + repr(self.food), bg="red", fg="white").pack(pady=5)
        Label(self.storemenu, font=self.x, text="Rafts:: " + repr(self.raft), bg="chocolate", fg="white").pack(pady=5)
        Button(self.storemenu, image=self.photo6, command=lambda *arg: self.back("smenu"), bg="white").pack(pady=5)
        self.storemenu.pack()
    #remember to reduce hunger in these menu operations
    #everything related to forest will follow from here

    def woodcollect(self):
        self.currentwindowid = "forest"
        self.hungerf()
        self.wood = self.wood + 20
        print repr(self.wood)

    def trap(self):
        self.currentwindowid = "forest"
        self.hungerf()
        if self.wood >= 5:
            self.food = self.food + 20
            print repr(self.food)
            self.wood = self.wood - 5
        else:
            print "Not enough wood"

    def forest(self):
        self.mainmenu.pack_forget()
        self.forestmenu = Frame(self.root)
        self.currentwindowid = "forest"
        self.hungerf()
        Label(self.forestmenu, font=self.x, text="Hunger:: " + repr(self.hunger), bg="chocolate", fg="black").pack()
        Button(self.forestmenu, image=self.photo4, command=self.woodcollect, bg="burlywood").pack(side=LEFT, anchor=E)
        Button(self.forestmenu, image=self.photo5, command=self.trap, bg="moccasin").pack(side=RIGHT, anchor=W)
        Button(self.forestmenu, image=self.photo6, command=lambda *arg: self.back("fmenu"), bg="white").pack(side=BOTTOM)
        self.forestmenu.pack()
        #####################################################
        #all the functions for shelter

    def eat(self):
        if self.food >= 10 and self.hunger <= 90:
            self.food = self.food - 10
            self.hunger = self.hunger + 10
            print repr(self.food)
            print repr(self.hunger)
        else:
            print "Not enough food or you are not hungry"
        self.hlb()

    def builds(self, buildid):
        if buildid == "raft":
            if self.wood >= 20:
                self.raft = self.raft + 1
                print self.raft
            else:
                print "You are lacking wood to craft this!"
        #use elif statements for the rest of the crafts

    def craft(self):
        self.currentwindowid = "craft"
        self.hungerf()
        self.sheltermenu.pack_forget()
        self.craftmenu = Frame(self.root)
        Button(self.craftmenu, image=self.photo11, command=lambda *arg: self.builds("raft")).pack()
        Button(self.craftmenu, image=self.photo6, command=lambda *arg: self.back("cmenu"), bg="white").pack()
        self.craftmenu.pack()

    def shelter(self):
        if self.currentwindowid == "starved":
            self.starvemenu.pack_forget()
            self.hunger = 105
        self.currentwindowid = "shelter"
        self.hungerf()
        self.mainmenu.pack_forget()
        self.sheltermenu = Frame(self.root)
        Label(self.sheltermenu, font=self.x, text="Hunger:: " + repr(self.hunger), bg="chocolate", fg="black").pack()
        Button(self.sheltermenu, font=self.x, text="Eat", command=self.eat, bg="wheat", fg="black").pack(side=LEFT, anchor=E)
        Button(self.sheltermenu, font=self.x, text="Crafting", command=self.craft, bg="white", fg="black").pack(side=RIGHT, anchor=W)
        Button(self.sheltermenu, image=self.photo6, command=lambda *arg: self.back("stmenu"), bg="white").pack(side=BOTTOM)
        self.sheltermenu.pack()
    #############################################
    #all the functions for the seamenu from here onwards

    def fish(self):
        self.currentwindowid = "sea"
        self.hungerf()
        self.food = self.food + 10
        print repr(self.food)

    def embark(self):
        if self.raft <= 0:
            print "You need a raft to travel on the sea"
        else:
            print "Let's sail!"

    def sea(self):
        self.currentwindowid = "sea"
        self.hungerf()
        self.mainmenu.pack_forget()
        self.seamenu = Frame(self.root)
        Label(self.seamenu, font=self.x, text="Hunger:: " + repr(self.hunger), bg="chocolate", fg="black").pack()
        Button(self.seamenu, image=self.photo7, command=self.fish, bg="lightblue",).pack(side=LEFT, anchor=E)
        Button(self.seamenu, image=self.photo8, command=self.embark, bg="blue").pack(side=RIGHT, anchor=W)
        Button(self.seamenu, image=self.photo6, command=lambda *arg: self.back("seamenu"), bg="white").pack(side=BOTTOM)
        self.seamenu.pack()

    #the farm code
    def farm(self):
        print "This works!"

    #travel code
    def travel(self):
        print "this woooooooooorkd"

    def hlb(self):
        hsymb = self.spchar[0]
        tsymb = self.spchar[1]
        prntcount = 1
        loopr = 'false'
        hg = 90
        pc = hg / 10 + 1
        #this loop is a mess it wont work, fix that. unfortunately the fix is increasing the hunger meter
        #f*ck the above comment, totally got this to work
        while loopr == 'false':
            if self.hunger > hg:
                while prntcount <= pc:
                    self.hungrbr = self.hungrbr + hsymb
                    prntcount += 1
                prntcount = 1
                loopr = 'true'
            hg = hg - 10
            pc = hg / 10 + 1
            self.hlbl.config(text=self.hungrbr)
            self.hlbl.pack(side=RIGHT)
            self.hungrbr = "Hunger::"  # initialize the var for the next time
            self.timebr = tsymb + tsymb + tsymb + tsymb + tsymb + tsymb + tsymb + tsymb + tsymb + tsymb
            self.tlbl.config(text="Time:: " + self.timebr)
            self.tlbl.pack(side=LEFT)


survivor()
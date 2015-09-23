import math, tkinter, string, random
from tkinter import *

class Application(Frame):
    #Functions go on the top
    def say_hi(self):
        l = Label(self)
        l["text"] = "Hi there, everyone!"
        l.pack()
    def addition(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(x + y)
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def subtraction(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(x - y)
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def multiplication(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(x * y)
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def division(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(x / y)
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)

    def CLS(self):
        self.display.delete('1.0', 'end')
        print("##############")
        print("")
        print("CLEARED")
        print("")
        print("##############")
    def ceiling(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.ceil(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def factorial(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = int(float(x))
        z = float(math.factorial(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def copysign(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.copysign(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def modulus(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.fmod(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def absolute(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.fabs(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def floor(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.floor(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def floatsum(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.fsum(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def greatestcd(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.gcd(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def exp_e(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.exp(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def logarithm(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.log(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def logtwo(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.log2(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def logten(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.log10(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def power(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.pow(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def sqroot(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.sqrt(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arccos(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.acos(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arcsin(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.asin(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arctan(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.atan(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def cosine(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.cos(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def sine(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.sin(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def tangent(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.tan(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def hyper_acos(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.acosh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def hyper_asin(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.asinh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def hyper_atan(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.atanh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def hyper_cos(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.cosh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def hyper_sin(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.sinh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def hyper_tan(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.tanh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def degrees(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.degrees(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def radians(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.radians(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def pi(self):
        z = math.pi
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def e(self):
        z = math.e
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def carryX(self):
        disp = self.display.get('1.0', 'end-1c')
        disp = str(disp)
        print(disp)
        self.display.delete('1.0', 'end')
        self.xinput.delete('1.0', 'end')
        self.xinput.insert(END, disp)
    def rand(self):
        rand = random.randint(0, 1000000000)
        print(rand)
        rand = str(rand)
        rand = rand + "\n"
        self.display.insert(END, rand)
    #Creates Widgets for the window GUI
    def createWidgets(self):
        #DISPLAY BOX
        displabel = Label(self)
        displabel["text"] = "Display Output"
        displabel.pack()
        
        self.display = Text(self)
        self.display["height"] = "10"
        self.display["width"] = "50"
        self.display["fg"] = "royal blue"

        self.display.pack({"side":"top"})

        #X input
        self.xinput = Text(self)
        self.xinput["height"] = "2"
        self.xinput["width"] = "15"

        xlabel = Label(self)
        xlabel["text"] = "X input"
        xlabel.pack()
        self.xinput.pack({"side":"top"})

        #Y input
        self.yinput = Text(self)
        self.yinput["height"] = "2"
        self.yinput["width"] = "15"

        ylabel = Label(self)
        ylabel["text"] = "Y input"
        ylabel.pack()
        self.yinput.pack({"side":"top"})
        ########################################
        

        #QUITS THE PROGRAM
        #fg is the text color
        #bg is the background color
        self.QUIT = Button(self) #Makes a button with the parameter
        self.QUIT["text"] = "QUIT" #text on button
        self.QUIT["bg"]   = "red"
        self.QUIT["command"] =  self.quit #Command of the button,
                                         #This command closes the program.
        self.QUIT.pack(fill=X) #Places the button anywhere on the screen

        ########################################

        self.carryx = Button(self) #Makes a button with the parameter
        self.carryx["text"] = "CARRY TO X (ANS)" #text on button
        self.carryx["bg"]   = "blue"
        self.carryx["fg"] = "white"
        self.carryx["command"] =  self.carryX #Command of the button,
                                         #This command closes the program.
        self.carryx.pack(fill=X) #Places the button anywhere on the screen

        ########################################

        self.random = Button(self) #Makes a button with the parameter
        self.random["text"] = "Generate a RANDOM number" #text on button
        self.random["bg"]   = "orange"
        self.random["command"] =  self.rand #Command of the button,
                                         #This command closes the program.
        self.random.pack(fill=X) #Places the button anywhere on the screen
        
        ######################################## Separate buttons accordingly

        self.clear = Button(self)
        self.clear["text"] = "Clear"
        self.clear["bg"] = "tomato"
        self.clear["command"] = self.CLS

        self.clear.pack({"side":"left"})
        ######################################## Clears out display box
        #HELLO WORLD
        
        #self.hi_there = Button(self)
        #self.hi_there["text"] = "Hello", 
        #self.hi_there["command"] = self.say_hi

        #self.hi_there.pack({"side": "left"})
        ########################################
        #4 FUNCTIONS

        self.add = Button(self)
        self.add["text"] = "x + y"
        self.add["bg"] = "lime"
        self.add["command"] = self.addition
        self.add.pack(fill=X)
        self.minus = Button(self)
        self.minus["text"] = "x - y"
        self.minus["bg"] = "lime"
        self.minus["command"] = self.subtraction
        self.minus.pack(fill=X)
        self.multi = Button(self)
        self.multi["text"] = "x * y"
        self.multi["bg"] = "lime"
        self.multi["command"] = self.multiplication
        self.multi.pack(fill=X)
        self.div = Button(self)
        self.div["text"] = "x / y"
        self.div["bg"] = "lime"
        self.div["command"] = self.division
        self.div.pack(fill=X)
        ########################################
        #Math Module Functions go here
        self.ceil = Button(self)
        self.ceil["text"] = "ceil(x)"
        self.ceil["command"] = self.ceiling

        self.ceil.pack({"side":"left"})

        self.fact = Button(self)
        self.fact["text"] = "factorial(x)"
        self.fact["command"] = self.factorial

        self.fact.pack({"side":"left"})

        self.copys = Button(self)
        self.copys["text"] = "copysign(x)"
        self.copys["command"] = self.copysign

        self.copys.pack({"side":"left"})

        self.fabs = Button(self)
        self.fabs["text"] = "fabs(x)"
        self.fabs["command"] = self.absolute

        self.fabs.pack({"side":"left"})

        self.fmod = Button(self)
        self.fmod["text"] = "fmod(x)"
        self.fmod["command"] = self.modulus

        self.fmod.pack({"side":"left"})

        self.flr = Button(self)
        self.flr["text"] = "floor(x)"
        self.flr["command"] = self.floor

        self.flr.pack({"side":"left"})

        self.fsum = Button(self)
        self.fsum["text"] = "fsum(x)"
        self.fsum["command"] = self.floatsum

        self.fsum.pack({"side":"left"})

        self.gcd = Button(self)
        self.gcd["text"] = "gcd(x)"
        self.gcd["command"] = self.greatestcd

        self.gcd.pack({"side":"left"})
        
        self.exp = Button(self)
        self.exp["text"] = "exp(x)"
        self.exp["command"] = self.exp

        self.exp.pack({"side":"left"})

        self.log = Button(self)
        self.log["text"] = "log(x, y)"
        self.log["command"] = self.logarithm

        self.log.pack({"side":"left"})

        self.log2 = Button(self)
        self.log2["text"] = "log2(x)"
        self.log2["command"] = self.logtwo

        self.log2.pack({"side":"left"})

        self.log10 = Button(self)
        self.log10["text"] = "log10(x)"
        self.log10["command"] = self.logten

        self.log10.pack({"side":"left"})

        self.pow = Button(self)
        self.pow["text"] = "pow(x, y)"
        self.pow["command"] = self.power

        self.pow.pack({"side":"left"})

        self.deg = Button(self)
        self.deg["text"] = "deg(x)"
        self.deg["command"] = self.degrees

        self.deg.pack({"side":"left"})

        self.rad = Button(self)
        self.rad["text"] = "rad(x)"
        self.rad["command"] = self.radians

        self.rad.pack({"side":"left"})
        
        self.sin = Button(self)
        self.sin["text"] = "sin(x)"
        self.sin["command"] = self.sine

        self.sin.pack({"side":"left"})

        self.cos = Button(self)
        self.cos["text"] = "cos(x)"
        self.cos["command"] = self.cosine

        self.cos.pack({"side":"left"})

        self.tan = Button(self)
        self.tan["text"] = "tan(x)"
        self.tan["command"] = self.tangent

        self.tan.pack({"side":"left"})
        
        self.asin = Button(self)
        self.asin["text"] = "asin(x)"
        self.asin["command"] = self.arcsin

        self.asin.pack({"side":"left"})

        self.acos = Button(self)
        self.acos["text"] = "acos(x)"
        self.acos["command"] = self.arccos

        self.acos.pack({"side":"left"})

        self.atan = Button(self)
        self.atan["text"] = "atan(x)"
        self.atan["command"] = self.arctan

        self.atan.pack({"side":"left"})

        self.sinh = Button(self)
        self.sinh["text"] = "hyp_sin(x)"
        self.sinh["command"] = self.hyper_sin

        self.sinh.pack({"side":"left"})

        self.cosh = Button(self)
        self.cosh["text"] = "hyp_cos(x)"
        self.cosh["command"] = self.hyper_cos

        self.cosh.pack({"side":"left"})

        self.tanh = Button(self)
        self.tanh["text"] = "hyp_tan(x)"
        self.tanh["command"] = self.hyper_tan

        self.tanh.pack({"side":"left"})

        self.asinh = Button(self)
        self.asinh["text"] = "hyp_asin(x)"
        self.asinh["command"] = self.hyper_asin

        self.asinh.pack({"side":"left"})

        self.acosh = Button(self)
        self.acosh["text"] = "hyp_acos(x)"
        self.acosh["command"] = self.hyper_acos

        self.acosh.pack({"side":"left"})
        
        self.atanh = Button(self)
        self.atanh["text"] = "hyp_atan(x)"
        self.atanh["command"] = self.hyper_atan

        self.atanh.pack({"side":"left"})

        self.pibutton = Button(self)
        self.pibutton["text"] = "Pi"
        self.pibutton["command"] = self.pi

        self.pibutton.pack({"side":"left"})

        self.ebutton = Button(self)
        self.ebutton["text"] = "E"
        self.ebutton["command"] = self.e

        self.ebutton.pack({"side":"left"})
#Initializes the program, DO NOT TOUCH
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("Calculator++")
app = Application(master=root)
app.mainloop()
root.destroy()

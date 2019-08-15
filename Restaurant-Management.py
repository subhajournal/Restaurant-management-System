#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

#Basic window is created
root = Tk()
root.geometry("1350x750+0+0")
root.title("RESTURANT MANAGEMENT SYSYTEM")
root.configure(background = "VioletRed1")
#Frames are created
Tops = Frame(root, width = 850, height = 100, bd = 5, relief = "raise")
Tops.pack(side = TOP)
f1 = Frame(root, width = 400, height = 650, bd = 5, relief = "raise")
f1.pack(side = LEFT)
f2 = Frame(root, width = 440, height = 650, bd = 5, relief = "raise")
f2.pack(side = RIGHT)
f1a = Frame(f1, width = 900, height = 330, bd = 5, relief = "raise")
f1a.pack(side = TOP)
f2a = Frame(f1, width = 900, height = 320, bd = 5, relief = "raise")
f2a.pack(side = BOTTOM)
ft2 = Frame(f2, width = 440, height = 450, bd = 5, relief = "raise")
ft2.pack(side = TOP)
fb2 = Frame(f2, width = 440, height = 250, bd = 5, relief = "raise")
fb2.pack(side = BOTTOM)
f1aa = Frame(f1a, width = 450, height = 330, bd = 5, relief = "raise")
f1aa.pack(side = LEFT)
f1ab = Frame(f1a, width = 400, height = 330, bd = 5, relief = "raise")
f1ab.pack(side = RIGHT)
f2aa = Frame(f2a, width = 450, height = 330, bd = 5, relief = "raise")
f2aa.pack(side = LEFT)
f2ab = Frame(f2a, width = 450, height = 330, bd = 5, relief = "raise")
f2ab.pack(side = RIGHT)
Tops.configure (background = 'VioletRed1')
f1.configure (background = 'VioletRed1')
f2.configure (background = 'VioletRed1')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>HEADING<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblInfo = Label(Tops, font  = ('arial', 30, 'bold'), text = " \t RESTURANT MANAGEMENT SYSTEM \t\t", bd = 10)
lblInfo.grid(row = 0, column = 0)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>COST OF ITEMS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def CostofItems():
    Item1 = float(E_chicken65.get())
    Item2 = float(E_cheeseballs.get())
    Item3 = float(E_tangrikebabs.get())
    Item4 = float(E_friedcheesecubes.get())
    Item5 = float(E_chickenafgani.get())
    Item6 = float(E_frenchfries.get())
    Item7 = float(E_friedonionring.get())
    Item8 = float(E_porkcutlet.get())
    Item9 = float(E_hyderabadibiriyani.get())
    Item10 = float(E_kadaipaneer.get())
    Item11 = float(E_palakpaneer.get())
    Item12 = float(E_chickenbharta.get())
    Item13 = float(E_rarachicken.get())
    Item14 = float(E_kashmiripulao.get())
    Item15 = float(E_muttonstew.get())
    Item16 = float(E_boiledpork.get())
    PriceofStarters = (Item1 * 120) + (Item2 * 75) + (Item3 * 260) + (Item4 * 180) + (Item5 * 116) + (Item6 * 99) + (Item7 * 77) + (Item8 * 149)
    PriceofMainCourse =  (Item9 * 350) + (Item10 *135) + (Item11 * 189) + (Item12 * 149) + (Item13 * 280) + (Item14 * 167) + (Item15 * 220) + (Item16 * 199)
    StartersPrice = "Rs." + str('%.2f'%(PriceofStarters))
    MainCoursePrice = "Rs." + str('%.2f'%(PriceofMainCourse))
    CostofMainCourse.set(MainCoursePrice)
    CostofStarters.set(StartersPrice)
    SC = "Rs." + str('%.2f'%(29.55))
    ServiceCharge.set(SC)
    SubTotalofITEMS = "Rs." + str('%.2f'%(PriceofStarters + PriceofMainCourse + 29.55))
    SubTotal.set(SubTotalofITEMS)
    Tax = "Rs." + str('%.2f'%(PriceofStarters + PriceofMainCourse + 29.55))
    PaidTax.set(Tax)
    TT = ((PriceofStarters + PriceofMainCourse + 29.55))
    TC = "Rs." + str('%.2f'%(PriceofStarters + PriceofMainCourse + 29.55 + TT))
    TotalCost.set(TC)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CREATING METHOD FOR EXIT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit:
        root.quit()
        return
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RESET METHOD START<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofStarters.set("")
    CostofMainCourse.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_chicken65.set("0")
    E_cheeseballs.set("0")
    E_tangrikebabs.set("0")
    E_friedcheesecubes.set("0")
    E_chickenafgani.set("0")
    E_frenchfries.set("0")
    E_friedonionring.set("0")
    E_porkcutlet.set("0")
    E_hyderabadibiriyani.set("0")
    E_kadaipaneer.set("0")
    E_palakpaneer.set("0")
    E_chickenbharta.set("0")
    E_rarachicken.set("0")
    E_kashmiripulao.set("0")
    E_muttonstew.set("0")
    E_boiledpork.set("0")
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtchicken65.configure(state=DISABLED)
    txtcheeseballs.configure(state=DISABLED)
    txttangrikebabs.configure(state=DISABLED)
    txtfriedcheesecubes.configure(state=DISABLED)
    txtchickenafgani.configure(state=DISABLED)
    txtfrenchfries.configure(state=DISABLED)
    txtfriedonionring.configure(state=DISABLED)
    txtporkcutlet.configure(state=DISABLED)
    txthyderabadibiriyani.configure(state=DISABLED)
    txtkadaipaneer.configure(state=DISABLED)
    txtpalakpaneer.configure(state=DISABLED)
    txtchickenbharta.configure(state=DISABLED)
    txtrarachicken.configure(state=DISABLED)
    txtkashmiripulao.configure(state=DISABLED)
    txtmuttonstew.configure(state=DISABLED)
    txtboiledpork.configure(state=DISABLED)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CHECKBUTTONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def chkbutton_value():
    if(var1.get() == 1):
        txtchicken65.configure(state = NORMAL)
    elif var1.get() == 0:
        txtchicken65.configure(state = DISABLED)
        E_chicken65.set("0")
    if(var2.get() == 1):
        txtcheeseballs.configure(state = NORMAL)
    elif var2.get() == 0:
        txtcheeseballs.configure(state = DISABLED)
        E_cheeseballs.set("0")
    if(var3.get() == 1):
        txttangrikebabs.configure(state = NORMAL)
    elif var3.get() == 0:
        txttangrikebabs.configure(state = DISABLED)
        E_tangrikebabs.set("0")
    if(var4.get() == 1):
        txtfriedcheesecubes.configure(state = NORMAL)
    elif var4.get() == 0:
        txtfriedcheesecubes.configure(state = DISABLED)
        E_friedcheesecubes.set("0")
    if(var5.get() == 1):
        txtchickenafgani.configure(state = NORMAL)
    elif var5.get() == 0:
        txtchickenafgani.configure(state = DISABLED)
        E_chickenafgani.set("0")
    if(var6.get() == 1):
        txtfrenchfries.configure(state = NORMAL)
    elif var6.get() == 0:
        txtfrenchfries.configure(state = DISABLED)
        E_frenchfries.set("0")
    if(var7.get() == 1):
        txtfriedonionring.configure(state = NORMAL)
    elif var7.get() == 0:
        txtfriedonionring.configure(state = DISABLED)
        E_friedonionring.set("0")
    if(var8.get() == 1):
        txtporkcutlet.configure(state = NORMAL)
    elif var8.get() == 0:
        txtporkcutlet.configure(state = DISABLED)
        E_porkcutlet.set("0")
    if(var9.get() == 1):
        txthyderabadibiriyani.configure(state = NORMAL)
    elif var9.get() == 0:
        txthyderabadibiriyani.configure(state = DISABLED)
        E_hyderabadibiriyani.set("0")
    if(var10.get() == 1):
        txtkadaipaneer.configure(state = NORMAL)
    elif var10.get() == 0:
        txtkadaipaneer.configure(state = DISABLED)
        E_kadaipaneer.set("0")
    if(var11.get() == 1):
        txtpalakpaneer.configure(state = NORMAL)
    elif var11.get() == 0:
        txtpalakpaneer.configure(state = DISABLED)
        E_palakpaneer.set("0")
    if(var12.get() == 1):
        txtchickenbharta.configure(state = NORMAL)
    elif var12.get() == 0:
        txtchickenbharta.configure(state = DISABLED)
        E_chickenbharta.set("0")
    if(var13.get() == 1):
        txtrarachicken.configure(state = NORMAL)
    elif var13.get() == 0:
        txtrarachicken.configure(state = DISABLED)
        E_rarachicken.set("0")
    if(var14.get() == 1):
        txtkashmiripulao.configure(state = NORMAL)
    elif var14.get() == 0:
        txtkashmiripulao.configure(state = DISABLED)
        E_kashmiripulao.set("0")
    if(var15.get() == 1):
        txtmuttonstew.configure(state = NORMAL)
    elif var15.get() == 0:
        txtmuttonstew.configure(state = DISABLED)
        E_muttonstew.set("0")
    if(var16.get() == 1):
        txtboiledpork.configure(state = NORMAL)
    elif var16.get() == 0:
        txtboiledpork.configure(state = DISABLED)
        E_boiledpork.set("0")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RECEIPT start<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)
    txtReceipt.insert(END, 'Receipt Ref: \t\t\t'+Receipt_Ref.get()+"\t\t\t"+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t'+'Quantity\t\t\t'+"Price \n\n")
    if E_chicken65.get() > 0:
        txtReceipt.insert(END, 'Chicken65:\t\t\t'+str(E_chicken65.get())+'\t\t\t'+str('Rs %.2f'%(E_chicken65.get()*120))+'\n')
    if E_cheeseballs.get() > 0:
        txtReceipt.insert(END, 'CheeseBalls:\t\t\t'+str(E_cheeseballs.get())+'\t\t\t'+str('Rs %.2f'%(E_cheeseballs.get()*75))+'\n')
    if E_tangrikebabs.get() > 0:
        txtReceipt.insert(END, 'TangriKebabs:\t\t\t'+str(E_tangrikebabs.get())+'\t\t\t'+str('Rs %.2f'%(E_tangrikebabs.get()*260))+'\n')
    if E_friedcheesecubes.get() > 0:
        txtReceipt.insert(END, 'FriedCheeseCubes:\t\t\t'+str(E_friedcheesecubes.get())+'\t\t\t'+str('Rs %.2f'%(E_friedcheesecubes.get()*180))+'\n')
    if E_chickenafgani.get() > 0:
        txtReceipt.insert(END, 'ChickenAfgani:\t\t\t'+str(E_chickenafgani.get())+'\t\t\t'+str('Rs %.2f'%(E_chickenafgani.get()*116))+'\n')
    if E_frenchfries.get() > 0:
        txtReceipt.insert(END, 'FrenchFries:\t\t\t'+str(E_frenchfries.get())+'\t\t\t'+str('Rs %.2f'%(E_frenchfries.get()*99))+'\n')
    if E_friedonionring.get() > 0:
        txtReceipt.insert(END, 'FriedOnionRing:\t\t\t'+str(E_friedonionring.get())+'\t\t\t'+str('Rs %.2f'%(E_friedonionring.get()*77))+'\n')
    if E_porkcutlet.get() > 0:
        txtReceipt.insert(END, 'PorkCutlet:\t\t\t'+str(E_porkcutlet.get())+'\t\t\t'+str('Rs %.2f'%(E_porkcutlet.get()*149))+'\n')
    if E_hyderabadibiriyani.get() > 0:
        txtReceipt.insert(END, 'HyderabadiBiriyani:\t\t\t'+str(E_hyderabadibiriyani.get())+'\t\t\t'+str('Rs %.2f'%(E_hyderabadibiriyani.get()*350))+'\n')
    if E_kadaipaneer.get() > 0:
        txtReceipt.insert(END, 'KadaiPaneer:\t\t\t'+str(E_kadaipaneer.get())+'\t\t\t'+str('Rs %.2f'%(E_kadaipaneer.get()*135))+'\n')
    if E_palakpaneer.get() > 0:
        txtReceipt.insert(END, 'PalakPaneer:\t\t\t'+str(E_palakpaneer.get())+'\t\t\t'+str('Rs %.2f'%(E_palakpaneer.get()*189))+'\n')
    if E_chickenbharta.get() > 0:
        txtReceipt.insert(END, 'ChickenBharta:\t\t\t'+str(E_chickenbharta.get())+'\t\t\t'+str('Rs %.2f'%(E_chickenbharta.get()*149))+'\n')
    if E_rarachicken.get() > 0:
        txtReceipt.insert(END, 'RaraChicken:\t\t\t'+str(E_rarachicken.get())+'\t\t\t'+str('Rs %.2f'%(E_rarachicken.get()*280))+'\n')
    if E_kashmiripulao.get() > 0:
        txtReceipt.insert(END, 'KashmiriPulao:\t\t\t'+str(E_kashmiripulao.get())+'\t\t\t'+str('Rs %.2f'%(E_kashmiripulao.get()*167))+'\n')
    if E_muttonstew.get() > 0:
        txtReceipt.insert(END, 'MuttonStew:\t\t\t'+str(E_muttonstew.get())+'\t\t\t'+str('Rs %.2f'%(E_muttonstew.get()*220))+'\n')
    if E_boiledpork.get() > 0:
        txtReceipt.insert(END, 'BoiledPork:\t\t\t'+str(E_boiledpork.get())+'\t\t\t'+str('Rs%.2f'%(E_boiledpork.get()*199))+'\n')
    txtReceipt.insert(END, '\nCost of Starter:\t'+CostofStarters.get()+"\tTax Paid:\t"+ PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Cost of Main Course:\t'+CostofMainCourse.get()+"\tSubTotal:\t"+ SubTotal.get()+"\n")
    txtReceipt.insert(END, 'Service Charge:\t'+ServiceCharge.get()+"\tTotal Cost:\t"+ TotalCost.get()+"\n")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RECEIPT END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CHECKBUTTONS END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofStarters = StringVar()
CostofMainCourse = StringVar()
ServiceCharge = StringVar()

E_chicken65=IntVar()
E_cheeseballs=IntVar()
E_tangrikebabs=IntVar()
E_friedcheesecubes=IntVar()
E_chickenafgani=IntVar()
E_frenchfries=IntVar()
E_friedonionring=IntVar()
E_porkcutlet=IntVar()

E_hyderabadibiriyani=IntVar()
E_kadaipaneer=IntVar()
E_palakpaneer=IntVar()
E_chickenbharta=IntVar()
E_rarachicken=IntVar()
E_kashmiripulao=IntVar()
E_muttonstew=IntVar()
E_boiledpork=IntVar()

E_chicken65.set(0)
E_cheeseballs.set(0)
E_tangrikebabs.set(0)
E_friedcheesecubes.set(0)
E_chickenafgani.set(0)
E_frenchfries.set(0)
E_friedonionring.set(0)
E_porkcutlet.set(0)

E_hyderabadibiriyani.set(0)
E_kadaipaneer.set(0)
E_palakpaneer.set(0)
E_chickenbharta.set(0)
E_rarachicken.set(0)
E_kashmiripulao.set(0)
E_muttonstew.set(0)
E_boiledpork.set(0)

DateofOrder.set(time.strftime("%d/%m/%Y"))


#Widget created
# f1aa == left hand box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>STARTER<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
chicken65 = Checkbutton(f1aa, text="chicken 65 \t\t", variable = var1, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 0, sticky = W)
cheeseballs = Checkbutton(f1aa, text="cheese balls  \t\t", variable = var2, onvalue = 1, offvalue = 0,command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 1, sticky = W)
tangrikebabs = Checkbutton(f1aa, text="tangri kebabs  \t\t", variable = var3, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 2, sticky = W)
friedcheesecubes = Checkbutton(f1aa, text="fried cheese cubes \t\t", variable = var4, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 11, 'bold')).grid(row = 3, sticky = W)
chickenafgani  = Checkbutton(f1aa, text="chicken afgani  \t\t", variable = var5, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 11, 'bold')).grid(row = 4, sticky = W)
frenchfries = Checkbutton(f1aa, text="french fries  \t\t", variable = var6, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 11, 'bold')).grid(row = 5, sticky = W)
friedonionring = Checkbutton(f1aa, text="fried onion ring \t\t", variable = var7, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 11, 'bold')).grid(row = 6, sticky = W)
porkcutlet = Checkbutton(f1aa, text="pork cutlet  \t\t", variable = var8, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 11, 'bold')).grid(row = 7, sticky = W)


#f1ab == right hand box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MAIN COURSE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

hyderabadibiriyani= Checkbutton(f1ab, text="hyderabadi biriyani\t", variable = var9, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 0, sticky = W)
kadaipaneer = Checkbutton(f1ab, text="kadai paneer\t", variable = var10, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 1, sticky = W)
palakpaneer = Checkbutton(f1ab, text="palak paneer\t", variable = var11, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 2, sticky = W)
chickenbharta = Checkbutton(f1ab, text="chicken bharta\t", variable = var12, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 3, sticky = W)
rarachicken = Checkbutton(f1ab, text="rara chicken\t", variable = var13, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 4, sticky = W)
kashmiripulao = Checkbutton(f1ab, text="kashmiri pulao\t", variable = var14, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 5, sticky = W)
muttonstew = Checkbutton(f1ab, text="mutton stew\t", variable = var15, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 6, sticky = W)
boiledpork = Checkbutton(f1ab, text="boiled pork\t", variable = var16, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 11, 'bold')).grid(row = 7, sticky = W)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter widget for STARTER<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
txtchicken65 = Entry(f1aa, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_chicken65, state = DISABLED)
txtchicken65.grid(row = 0, column = 1)
txtcheeseballs = Entry(f1aa, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_cheeseballs, state = DISABLED )
txtcheeseballs.grid(row = 1, column = 1)
txttangrikebabs = Entry(f1aa, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_tangrikebabs , state = DISABLED )
txttangrikebabs.grid(row = 2, column = 1)
txtfriedcheesecubes = Entry(f1aa, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_friedcheesecubes, state = DISABLED )
txtfriedcheesecubes.grid(row = 3, column = 1)
txtchickenafgani = Entry(f1aa, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_chickenafgani, state = DISABLED )
txtchickenafgani.grid(row = 4, column = 1)
txtfrenchfries = Entry(f1aa, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_frenchfries, state = DISABLED )
txtfrenchfries.grid(row = 5, column = 1)
txtfriedonionring = Entry(f1aa, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_friedonionring, state = DISABLED )
txtfriedonionring.grid(row = 6, column = 1)
txtporkcutlet = Entry(f1aa, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_porkcutlet, state = DISABLED )
txtporkcutlet.grid(row = 7, column = 1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter widget for MAIN COURSE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
txthyderabadibiriyani = Entry(f1ab, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_hyderabadibiriyani, state = DISABLED )
txthyderabadibiriyani.grid(row = 0, column = 1)
txtkadaipaneer = Entry(f1ab, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_kadaipaneer, state = DISABLED )
txtkadaipaneer.grid(row = 1, column = 1)
txtpalakpaneer = Entry(f1ab, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_palakpaneer, state = DISABLED )
txtpalakpaneer.grid(row = 2, column = 1)
txtchickenbharta = Entry(f1ab, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_chickenbharta, state = DISABLED )
txtchickenbharta.grid(row = 3, column = 1)
txtrarachicken = Entry(f1ab, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_rarachicken, state = DISABLED )
txtrarachicken.grid(row = 4, column = 1)
txtkashmiripulao = Entry(f1ab, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_kashmiripulao, state = DISABLED )
txtkashmiripulao.grid(row = 5, column = 1)
txtmuttonstew = Entry(f1ab, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_muttonstew, state = DISABLED )
txtmuttonstew.grid(row = 6, column = 1)
txtboiledpork  = Entry(f1ab, font=('arial', 11, 'bold'), bd = 5, width = 6, justify = 'left', textvariable = E_boiledpork , state = DISABLED )
txtboiledpork.grid(row = 7, column = 1)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RECEIPT INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt",bd = 2, anchor = "w")
lblReceipt.grid(row = 0, column = 0, sticky = W)
txtReceipt = Text(ft2, font=('arial', 11, 'bold'), width = 59, height =22, bg="white", bd=8)
txtReceipt.grid(row = 1, column = 0)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Cost Item INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

lblCostofStarters = Label(f2aa, font=('arial', 11, 'bold'), text = "Cost of Starters        \t", bd = 5, anchor="w")
lblCostofStarters.grid(row = 0, column = 0, sticky = W)
txtCostofStarters = Entry(f2aa,font=('arial', 11, 'bold'), bd = 5, justify = "left", textvariable =CostofStarters)
txtCostofStarters.grid(row = 0, column = 1, sticky = W)

lblCostofMainCourse = Label(f2aa, font=('arial', 11, 'bold'), text = "Cost of Main Course", bd = 5, anchor="w")
lblCostofMainCourse.grid(row = 1, column = 0, sticky = W)
txtCostofMainCourse = Entry(f2aa,font=('arial', 11, 'bold'), bd = 5, justify = "left", textvariable =CostofMainCourse)
txtCostofMainCourse.grid(row = 1, column = 1, sticky = W)

lblServiceCharge = Label(f2aa, font=('arial', 11, 'bold'), text = "Sevice charge\t", bd = 5, anchor = "w")
lblServiceCharge.grid(row = 2, column = 0, sticky = W)
txtServiceCharge = Entry(f2aa,font=('arial', 11, 'bold'), bd = 5, justify = "left", textvariable = ServiceCharge)
txtServiceCharge.grid(row = 2, column = 1, sticky = W)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Payment INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblPaidTax = Label(f2ab, font=('arial', 11, 'bold'), text = "Tax", bd = 5)
lblPaidTax.grid(row = 0, column = 0, sticky = W)
txtPaidTax = Entry(f2ab,font=('arial', 11, 'bold'), bd = 5, justify = "left", textvariable = PaidTax)
txtPaidTax.grid(row = 0, column = 1, sticky = W)

lblSubTotal = Label(f2ab, font=('arial', 11, 'bold'), text = "Sub Total         \t", bd = 5)
lblSubTotal.grid(row = 1, column = 0, sticky = W)
txtSubTotal = Entry(f2ab,font=('arial', 11, 'bold'), bd = 5, justify = "left", textvariable = SubTotal)
txtSubTotal.grid(row = 1, column = 1, sticky = W)

lblTotalCost = Label(f2ab, font=('arial', 11, 'bold'), text = "Total", bd = 5)
lblTotalCost.grid(row = 2, column = 0, sticky = W)
txtTotalCost = Entry(f2ab,font=('arial', 11, 'bold'), bd = 5, justify = "left", textvariable = TotalCost)
txtTotalCost.grid(row = 2, column = 1, sticky = W)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BUTTONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
btnTotal = Button(fb2, padx = 16, pady = 1, bd = 4, fg = "black", font = ('arial', 11, 'bold'), width = 5, text = "Total", command = CostofItems).grid(row = 0, column = 0)
btnReceipt = Button(fb2, padx = 16, pady = 1, bd = 4, fg = "black", font = ('arial', 11, 'bold'), width = 5, text = "Receipt", command = Receipt).grid(row = 0, column = 1)
btnReset = Button(fb2, padx = 16, pady = 1, bd = 4, fg = "black", font = ('arial', 11, 'bold'), width = 5, text = "Reset", command = reset).grid(row = 0, column = 2)
btnExit = Button(fb2, padx = 16, pady = 1, bd = 4, fg = "black", font = ('arial', 11, 'bold'), width = 5, text = "Exit", command=qExit).grid(row = 0, column = 3)

root.mainloop()






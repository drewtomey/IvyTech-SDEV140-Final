#Drew Tomey
#SDEV 140 - Final Project
#Professor Carver

#importing required modules
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk,messagebox

#setting title, window, and background color
root=tk.Tk()
root.title("Drew's $5 Prints") #window root title
width=600 #width of window
height=600 #height of window
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.configure(bg='lightblue') #setting background color for window

#setting my four images using PhotoImage
photoOne=ImageTk.PhotoImage(Image.open('one.jpg')) #photo one
photoTwo=ImageTk.PhotoImage(Image.open('two.jpg')) #photo two
photoThree=ImageTk.PhotoImage(Image.open('three.jpg')) #photo three
photoFour=ImageTk.PhotoImage(Image.open('four.jpg')) #photo four

#configures title header text, placement, background color, and font
Label(root,text="        Drew's $5 Prints",font="none 25 bold",bg='light blue').grid(row=0,column=8)

#configurations for row 5
Label(root,image=photoOne,height=80,width=80).grid(row=5,column=4) #setting photo one
currentValueOne= tk.StringVar(value=0) #setting value for spinBoxOne
spinBoxOne = ttk.Spinbox(root,from_=0,to=100,textvariable=currentValueOne,wrap=True) #configurations for spinBoxOne
spinBoxOne.grid(row=5,column=8) #spinBoxOne placement
Label(root,text="$5 Each",font='none 11 bold',bg='light blue').grid(row=5,column=15) #label for cost

#configurations for row 6
Label(root,text="4x3 Print",font='none 11 bold',bg='light blue').grid(row=6,column=4) #setting text under photoOne

#configurations for row 8
Label(root,image=photoTwo,height=80,width=80).grid(row=8,column=4) #setting photo two
currentValueTwo = tk.StringVar(value=0) #setting value for spinBoxTwo
spinBoxTwo = ttk.Spinbox(root,from_=0,to=100,textvariable=currentValueTwo,wrap=True) #configurations for spinBoxTwo
spinBoxTwo.grid(row=8,column=8) #spinBoxTwo placement
Label(root,text="$5 Each",font='none 11 bold',bg='light blue').grid(row=8,column=15) #label for cost

#configurations for row 9
Label(root,text="4x6 Print",font='none 11 bold',bg='light blue').grid(row=9,column=4) #setting text under photoTwo

#configurations for row 11
Label(root,image=photoThree,height=80,width=80).grid(row=11,column=4) #setting photo three
currentValueThree = tk.StringVar(value=0) #setting value for spinBoxThree
spinBoxThree = ttk.Spinbox(root,from_=0,to=100,textvariable=currentValueThree,wrap=True) #configurations for spinBoxThree
spinBoxThree.grid(row=11,column=8) #spinBoxThree placement
Label(root,text="$5 Each",font='none 11 bold',bg='light blue').grid(row=11,column=15) #label for cost

#configurations for row 12
Label(root,text="5x7 Print",font='none 11 bold',bg='light blue').grid(row=12,column=4)#setting text under photoThree

#configurations for row 14
Label(root,image=photoFour,height=80,width=80).grid(row=14,column=4) #setting photo four
currentValueFour = tk.StringVar(value=0) #setting value for spinBoxFour
spinBoxFour = ttk.Spinbox(root,from_=0,to=100,textvariable=currentValueFour,wrap=True) #configurations for spinBoxFour
spinBoxFour.grid(row=14,column=8) #spinBoxFour placement
Label(root,text="$5 Each",font='none 11 bold',bg='light blue').grid(row=14,column=15) #label for cost

#configurations for row 14
Label(root,text="6x9 Print",font='none 11 bold',bg='light blue').grid(row=15,column=4) #setting text under photoFour

Label(root,text="",font='none 11 bold',bg='light blue').grid(row=17,column=1) #label for cost

totalCost=0 #defininf totalCost variable

#defining the total cost
def findCost():
    totalCost=(int(currentValueOne.get())+int(currentValueTwo.get())+int(currentValueThree.get())+int(currentValueFour.get()))*5  #calculation for total cost
    global totalCostLabel
    totalCostLabel=Label(root,text="Total Cost: $"+str(totalCost),font='none 11 bold',bg='light blue') #label for configured total cost
    totalCostLabel.grid(row=16,column=15) #placement for totalCostLabel

#defining the exit button
def exitButton():
    exit()

#defining the order button
def orderButton():
    printOne=int(currentValueOne.get()) #variable for spinBoxOne
    printTwo=int(currentValueTwo.get()) #variable for spinBoxTwo
    printThree=int(currentValueThree.get()) #variable for spinBoxThree
    printFour=int(currentValueFour.get()) #variable for spinBoxFour

    #if any spinboxes are greater than the value "0" open new window
    if printOne>0 or printTwo>0 or printThree>0 or printFour>0: #if statement
        newWindow = Toplevel(root) #creating new window
        root.iconify()
        newWindow.title("Order") #creating new window title
        newWindow.geometry("450x300") #creating new window size and resizable
        newWindow.resizable(width=False, height=False)
        newWindow.configure(bg='lightblue') #setting background color for new window
        #creating entry fields for name, setting background, and placement
        Label(newWindow,font ="none 11 bold",bg="light blue",text="").grid(row=2,column=2)
        Label(newWindow,font ="none 11 bold",bg="light blue",text="Name: ").grid(row=4,column=1)
        nameText=Entry(newWindow, width=30)
        nameText.focus_set()
        nameText.grid(row=4,column=3)
        #creating entry fields for email, setting background, and placement
        Label(newWindow,font ="none 11 bold",bg="light blue",text="Email: ").grid(row=6,column=1)
        emailText=Entry(newWindow, width=30)
        emailText.focus_set()
        emailText.grid(row=6,column=3)
        Label(newWindow,font ="none 11 bold",bg="light blue",text="").grid(row=7,column=3)
        Label(newWindow,font ="none 11 bold",bg="light blue",text="").grid(row=9,column=3)

        #defining the confirm order button
        def confirmOrder():
            name=nameText.get()
            emailt=emailText.get()
            #validation for entry boxes
            if name=="" or emailt=="": #if one is blank
                messagebox.showerror(title="Error",message='Please enter the required information!') #display error

            else:
                text= "Name: "+ str(name)+", Email: "+str(emailt)+", " #print name and email to text document
                if printOne>0: #print the 4x3 into document if it's greater than 0
                    text=text+"4x3: "+str(printOne)+", "
                if printTwo>0: #print the 4x6 into document if it's greater than 0
                    text=text+"4x6: "+str(printTwo)+", "
                if printThree>0: #print the 5x7 into document if it's greater than 0
                    text=text+"5x7: "+str(printThree)+", "
                if printFour>0:#print the 6x9 into document if it's greater than 0
                    text=text+"6x9: "+str(printFour)+", "
                newWindow.destroy() #destroy window
                text=text+"Total: $"+str((printOne+printTwo+printThree+printFour)*5)+"\n" #print total into text document
                file=open("orders.txt",'a+')
                file.write(text)
                messagebox.showinfo(title="Order",message="Order Placed Successfully! We will contact you shortly.") #order placed successfully prompt

        finalOrderButton=Button(newWindow,font='none 11 bold',bg='light blue',justify = "center",text = "Confirm Order",command=confirmOrder).grid(row=10,column=2) #setting final order button, background color, and text 
    else:
        messagebox.showerror(title="Error",message='Please select prints to place an order!')#Error message
    
    
#defining the clear button and setting values back to 0    
def clearButton():
    global currentValueOne
    currentValueOne=tk.StringVar(value=0)
    spinBoxOne.config(textvariable=currentValueOne)
    global currentValueTwo
    currentValueTwo=tk.StringVar(value=0)
    spinBoxTwo.config(textvariable=currentValueTwo)
    global currentValueThree
    currentValueThree=tk.StringVar(value=0)
    spinBoxThree.config(textvariable=currentValueThree)
    global currentValueFour
    currentValueFour=tk.StringVar(value=0)
    spinBoxFour.config(textvariable=currentValueFour)
    try:
        totalCostLabel.destroy()
    except Exception as ex:
        pass
    
#configuring the buttons
theCostButton=Button(root,font='none 11 bold',bg='light blue',justify = "center",text = "Compute Cost",command=findCost).grid(row=16,column=8) #compute cost button
theExitButton=Button(root,font='none 11 bold',bg='light blue',justify = "center",text = "     Exit     ",command=exitButton).grid(row=21,column=15) #exit button
theOrderButton=Button(root,font='none 11 bold',bg='light blue',justify = "center",text = "     Order     ",command=orderButton).grid(row=21,column=8) #order button 
theClearButton=Button(root,font='none 11 bold',bg='light blue',justify = "center",text = "     Clear     ",command=clearButton).grid(row=21,column=4) #clear button


#infinte loop used to run GUI
root.mainloop()


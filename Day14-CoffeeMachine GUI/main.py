import tkinter as tk
from tkinter import messagebox
import db_check as md

root = tk.Tk()
root.title("Cafe Bunny")

top_frame = tk.LabelFrame(root, text="MENU", font=("Helvetica", 10), padx=100, pady=10, bd=10)
top_frame.pack(pady=10)

bottom_frame = tk.LabelFrame(root, text="ENTER MONEY", font=("Helvetica", 10), bd=10)
bottom_frame.pack(pady=5)
bottom_most = tk.LabelFrame(root)
bottom_most.pack(pady=5)


# checks money transaction
def click():
    global money
    global coins_ent
    global name
    coins = coins_ent.get()
    if (coins.isdigit()):
        a = md.calculate(coins, money)
        if a == 1:
            val_label = tk.Label(bottom_frame,
                                 text=f"Payment Successful\nCollect Your change {md.val:.2f}\nHere is your {name} .Enjoy!",
                                 font=("Arial Bold", 10))
            val_label.grid(column=3, row=15)
        elif a == 2:
            val_label = tk.Label(bottom_frame, text="Payment successful", font=("Helvetica", 7))
            val_label.grid(column=3, row=15)
        else:
            val_label = tk.Label(bottom_frame,
                                 text=f"Sorry!!! you don't have enough money \n Refunded money {md.cus_money:.2f}",
                                 font=("Arial Bold", 10))
            val_label.grid(column=3, row=15)
        md.save(name)
    else:
        tk.messagebox.showwarning("Wrong data", "Invalid data,Numbers Only")

    # prints report
    def report():
        global water
        global milk
        global coffee
        global coins
        water = tk.Label(bottom_frame, text=f"Water :{md.Tot_water}ml", font=("Helvetica", 10), fg="red")
        water.grid(column=4, row=1)
        milk = tk.Label(bottom_frame, text=f"Milk :{md.Tot_milk}ml", font=("Helvetica", 10), fg="red")
        milk.grid(column=4, row=2)
        coffee = tk.Label(bottom_frame, text=f"Coffee :{md.Tot_coffee}gm", font=("Helvetica", 10), fg="red")
        coffee.grid(column=4, row=3)
        coins = tk.Label(bottom_frame, text=f"Money :${money:.2f}", font=("Helvetica", 10), fg="red")
        coins.grid(column=4, row=4)

    tk.Button(bottom_most, text="Report", width=10, font=("Helvetica", 7), bd=5, command=report,bg="black"
                       ,fg="white").grid(column=0, row=1)

    def reset():
        try:
            val_label.grid_forget()
            water.grid_forget()
            milk.grid_forget()
            coffee.grid_forget()
            coins.grid_forget()

        except NameError:
            pass

    tk.Button(bottom_frame, text="Clear", width=10, font=("Helvetica", 10), bd=5, command=reset, bg="black",
                      fg="white").grid(column=4, row=6)

#enter money
def insert_coins():
    global coins_ent
    a = tk.StringVar()
    money_label = tk.Label(bottom_frame, text="Money", font=("Helvetica", 10), pady=9)
    money_label.grid(column=2, row=1)
    coins_ent = tk.Entry(bottom_frame, textvariable="a", width=10)
    coins_ent.grid(column=3, row=1)

    def resetvalue():
        coins_ent.delete(0, 'end')

    tk.Button(bottom_frame, text="Reset Value", width=10, font=("Helvetica", 10), bd=5, command=resetvalue,
                         bg="black", fg="white").grid(column=2, row=6)

#seperate menu function
def espresso():
    global money
    global name
    if md.resource_check(70, 50, 10) == True:
        insert_coins()
        money = 100
        name = "ESPRESSO"
        pro = tk.Button(bottom_frame, text="Proceed", width=10, font=("Helvetica", 10), bd=5, command=click, bg="black",
                        fg="white").grid(column=3, row=6)


def latte():
    global money
    global name
    if md.resource_check(100, 50, 5) == True:
        insert_coins()
        money = 100
        name = "LATTE"
        tk.Button(bottom_frame, text="Proceed", width=10, font=("Helvetica", 10), bd=5, command=click, bg="black",
                        fg="white").grid(column=3, row=6)


def cappucino():
    global money
    global name
    if md.resource_check(70, 70, 7) == True:
        insert_coins()
        money = 150
        name = "CAPPUCCINO"
        tk.Button(bottom_frame, text="Proceed", width=10, font=("Helvetica", 10), bd=5, command=click, bg="black",
                        fg="white").grid(column=3, row=6)


#takes order
def order():
    tk.Label(top_frame, text="What would you like?", font=("Helvetica", 10)).grid(column=3, row=3)
    tk.Button(top_frame, text="ESPRESSO", padx=10, pady=5, width=10, font=("Helvetica", 10), bd=5,
                           fg="white", bg="black", command=espresso).grid(column=3, row=4)
    tk.Button(top_frame, text="LATTE", padx=10, pady=5, width=10, font=("Helvetica", 10), bd=5, fg="white",
                           bg="black", command=latte).grid(column=3, row=5)
    tk.Button(top_frame, text="CAPPUCCINO", padx=10, pady=5, width=10, font=("Helvetica", 10), fg="white",
                            bg="black", bd=5, command=cappucino).grid(column=3, row=6)
    tk.Button(bottom_most, text="OFF", font=("Helvetica", 10), fg="white", bg="black", bd=5,
                           command=root.quit).grid(column=1, row=1)


tk.Button(top_frame, text="ON", font=("Helvetica", 10), bg="black", fg="white", command=order, bd=5,
                      width=3).grid(column=3, row=0)

root.mainloop()

choice = input("Do you want the details?:y/n")
if choice == 'y':
    md.show()
else:
    print("Done")

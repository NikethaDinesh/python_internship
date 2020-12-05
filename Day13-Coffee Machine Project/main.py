money = 0
water = 500
milk = 500
coffee = 100
def resource_report():
    print("Water:", water, "ml")
    print("Milk:", milk, "ml")
    print("Coffee:", coffee, "gm")
    print("Money:", money, "Rs")
def order():
    print("enter code:")
    code = input()
    if code == "on":
        code_on()
    if code == "off":
     code_off()
    if code=="report":
        resource_report()

def report(need_milk,need_water,need_coffee,need_money):
    print("Water:",need_water,"ml")
    print("Milk:",need_milk,"ml")
    print("Coffee:",need_coffee,"gm")
    print("Money:",need_money,"Rs")
def wallet(need_money):

    print("Enter money:")
    money=float(input())
    if money<need_money:
        print("Sorry ! thats not enough money")
    elif money>need_money:
        money-=need_money
        print("your money",money,"Rs. is refunded")
        print("your order is successful! Enjoy")
        order()

    else:
       print("your order is successful! Enjoy")
       order()

def resource_check(need_milk,need_water,need_coffee):

    if milk<need_milk :
        print("Sorry!There is no enough milk.")

    if water<need_water :
        print("Sorry!There is no enough water.")

    if coffee < need_coffee:
        print("Sorry!There is no enough coffee.")



def makecoffee(choice):
    global money,water,milk,coffee
    if choice==1:
        if not resource_check(need_milk=50,need_water=100,need_coffee=5):
            need_money=50
            water-=100
            milk-=50
            coffee-=5
            report(need_milk=50,need_water=100,need_coffee=5,need_money=50)
            wallet(need_money)
    if choice==2:
        if not resource_check(need_milk=100,need_water=70,need_coffee=7):
            need_money=50
            water-=70
            milk-=100
            coffee-=7
            report(need_milk=100,need_water=70,need_coffee=7,need_money=50)
            wallet(need_money)
    if choice==3:
        if not resource_check(need_milk=70,need_water=70,need_coffee=5):
            need_money=100
            water-=70
            milk-=70
            coffee-=5
            report(need_milk=70,need_water=70,need_coffee=5,need_money=100)
            wallet(need_money)



def code_off():
    print("Machine turned off for maintenance")


def code_on():
        print("WHAT DO YOU LIKE? "
          "1.espresso 2.latte  3.capuccino ")
        choice=int(input())
        if choice == 1 or 2 or 3:
            makecoffee(choice)
        else:
            print("wrong choice")

class coffeemachine:

    print("-----------cafe bunny---------------")
    order()




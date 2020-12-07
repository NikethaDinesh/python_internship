class coffeeMachine():

#initializing resources
    def __init__(self,milk,water,coffee):
        self.milk = milk
        self.water = water
        self.coffee = coffee

#check resources available in machine

    def resource_check (self,needmilk,needwater,needcoffee):
        if cafe_obj.milk < needmilk :
            print("Sorry ! Milk not available")

        elif cafe_obj.water < needwater :
            print("Sorry ! Water not available")

        elif cafe_obj.coffee < needcoffee :
            print("Sorry ! Coffee not available")

        else :
            cafe_obj.milk -= needmilk
            cafe_obj.water -= needwater
            cafe_obj.coffee -= needcoffee

#transaction process
    def wallet(self,needmoney):
        print("Enter money :")
        money=float(input())
        if money < needmoney:
            print("Sorry ! That's not enough money")
        elif money > needmoney:
            money -= needmoney
            print("money",money,"is refunded.Your order is successful enjoy!!")
            cafe_obj.action()
        else:
            print("Your order is successful enjoy!")
            cafe_obj.action()


#prints recipt

    def recipt(self,needmilk,needwater,needcoffee,needmoney):
        print("Water:", needwater, "ml")
        print("Milk:", needmilk, "ml")
        print("Coffee:", needcoffee, "gm")
        print("Money:", needmoney, "Rs")
        cafe_obj.wallet(needmoney)



#action to be performed by machine

    def action(self):
        print("Enter code:")
        code=input()
        if code=="on":
            cafe_obj.code_on()
        if code=="off":
            cafe_obj.code_off()
        if code=="report":
            cafe_obj.report()
#when machine off

    def code_off(self):
        print("Machine turned off for maintenance")

#when machine on

    def code_on(self):
        print("WHAT DO YOU LIKE? 1.ESPRESSO 2.LATTE 3.CAPPUCCINO ")
        choice=int(input())
        if choice==1:
            cafe_obj.resource_check(needmilk=70,needwater=50,needcoffee=10)
            cafe_obj.recipt(needmilk=70,needwater=50,needcoffee=10,needmoney=100)
        if choice==2:
            cafe_obj.resource_check(needmilk=100, needwater=50, needcoffee=5)
            cafe_obj.recipt(needmilk=100, needwater=50, needcoffee=5,needmoney=150)
        if choice==3:
            cafe_obj.resource_check(needmilk=70, needwater=70, needcoffee=7)
            cafe_obj.recipt(needmilk=70, needwater=70, needcoffee=7,needmoney=100)

#when machine report
    def report(self):
        print("Water:", cafe_obj.water, "ml")
        print("Milk:", cafe_obj.milk, "ml")
        print("Coffee:", cafe_obj.coffee, "gm")

#class object
cafe_obj=coffeeMachine(500,500, 100)
print("------cafe bunny--------")
cafe_obj.action()

class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def coffee_machine_state(self):
        print(f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money
        """)

    def buying_coffee(self):
        coffee_type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.cups < 1:
            print("Sorry, not enough disposable cups!\n")
            return False
        if coffee_type == "1":
            if self.water < 250:
                print("Sorry, not enough water!\n")
                return False
            elif self.coffee < 16:
                print("Sorry, not enough coffee beans!\n")
                return False
            else:
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!\n")
        elif coffee_type == "2":
            if self.water < 350:
                print("Sorry, not enough water!\n")
                return False
            elif self.milk < 75:
                print("Sorry, not enough milk!\n")
                return False
            elif self.coffee < 20:
                print("Sorry, not enough coffee beans!\n")
                return False
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.cups -= 1
        elif coffee_type == "3":
            if self.water < 200:
                print("Sorry, not enough water!\n")
                return False
            elif self.milk < 100:
                print("Sorry, not enough milk!\n")
                return False
            elif self.coffee < 12:
                print("Sorry, not enough coffee beans!\n")
                return False
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.cups -= 1
        elif coffee_type == "back":
            return False

    def filling_coffee_machine(self):
        print("Write how many ml of water you want to add:")
        self.water += int(input())
        print("Write how many ml of milk you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.coffee += int(input())
        print("Write how many disposable coffee cups you want to add:")
        self.cups += int(input())

    def taking_money(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0


first_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    option = input("Write action (buy, fill, take, remaining, exit):\n")
    if option == "buy":
        if first_coffee_machine.buying_coffee() is False:
            continue
    elif option == "fill":
        first_coffee_machine.filling_coffee_machine()
    elif option == "take":
        first_coffee_machine.taking_money()
    elif option == "remaining":
        first_coffee_machine.coffee_machine_state()
    elif option == "exit":
        break

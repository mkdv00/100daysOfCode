class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resourses = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    
    def report(self):
        """Prints a report of all resourses"""
        print(f"Water: {self.resourses['water']}ml")
        print(f"Mllk: {self.resourses['milk']}ml")
        print(f"Coffee: {self.resourses['coffee']}g")
    

    def is_resourses_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resourses[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    

    def make_coffee(self, order):
        """Deducts the reqired ingredients from the resourses"""
        for item in order.ingredients:
            self.resourses[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")


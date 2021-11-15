from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    
    my_menu = Menu()
    my_coffee_maker = CoffeeMaker()
    my_money_machine = MoneyMachine()
    
    while True:
    
        request = input(f"What would you like? ({my_menu.get_items()}) ")
        
        if request == "off":
            break
        
        if request == "report":
            my_coffee_maker.report()
            my_money_machine.report()
            
        else:
            request = my_menu.find_drink(request)
            
            if (request is not None and 
                my_coffee_maker.is_resource_sufficient(request) and 
                my_money_machine.make_payment(request.cost)):
                my_coffee_maker.make_coffee(request)
                
    
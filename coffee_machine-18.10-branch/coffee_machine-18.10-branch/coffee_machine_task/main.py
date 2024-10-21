import json
from menu import menu, resources


print("What coffee would you like?:")
user_coffee_choice = input()


def check_values(user_input, is_user_charged):
    
    #if User input is not a coffee type included in menu.py
    if not (user_input in menu) and not user_input == "refill":
        print("Machine is not capable of doing that, please try again.")
        return

    for i in menu:
        if(i == user_input):
            ingr = menu.get(i).get("skladniki")
            
            #Makes a coffee (consumes resources from a manu.py dictionary)
            if ( (resources.get("woda") > ingr.get("woda")) and (resources.get("mleko") > ingr.get("mleko")) and (resources.get("kawa") > ingr.get("kawa")) ):
                
                    resources["woda"] -= ingr.get("woda")
                    resources["mleko"] -= ingr.get("mleko")
                    resources["kawa"] -= ingr.get("kawa")
                    
                    with open('menu.py', 'w') as f:
                        f.write(f'resources = {repr(resources)}\n')
                        f.write(f'menu = {repr(menu)}\n')
                    print("Your coffee is done!")
            
            #Checks which resource is lacking and inform user about it
            else:
                if resources.get("woda") <= ingr.get("woda"):
                    print("Out of water!") 
                elif resources.get("milk") <= ingr.get("milk"):
                    print("Out of milk!") 
                elif resources.get("coffee") <= ingr.get("coffee"):
                    print("Out of coffee!")
                    
                print ("Please refill the Machine")


#Refills the machine
def refill():
    resources["woda"] = 500
    resources["mleko"] = 500
    resources["kawa"] = 1000

    with open('menu.py', 'w') as f:
        f.write(f'resources = {repr(resources)}\n')
        f.write(f'menu = {repr(menu)}\n')
    print("Machine is refilled!")    



if (user_coffee_choice == "refill"):
    refill()

                
check_values(user_coffee_choice, True)           
    
    
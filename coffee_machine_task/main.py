from menu import menu, resources


print("What coffee would you like?:")
user_coffee_choice = input()


def check_values(user_input): 
    for i in menu:
        print(i)
        if(i == user_input):
            ingr = menu.get("latte").get("skladniki")
            
            if ( (resources.get("woda") > ingr.get("woda")) and (resources.get("mleko") > ingr.get("mleko")) and (resources.get("kawa") > ingr.get("kawa")) ):
                print('ok')
            else:
                print("Out of water!") if resources.get("woda") <= ingr.get("woda")) else
                print("Not enough recources!")
            
                
check_values(user_coffee_choice)           
    
    
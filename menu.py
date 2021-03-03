"""
This module contains only one class Menu,
which helps to interact with user.
"""

import blessed
import pprint
from orders import Order, Item
from system import LogisticSystem, Vehicle
from tracking import Location

class Menu:
    '''
    Display a menu and respond to choices when run.
    '''

    def __init__(self, lst, param):
        term = blessed.Terminal()
        self.items = []
        self.lst = lst
        self.param = param
        if not param:
            pass
        else:
            print(term.move_y(term.height//3) +
        term.center(f"{term.purple}Hello!{term.normal} Here you can ma\
ke an {term.yellow}order{term.normal} to deliver your {term.green}items\
!{term.normal}"))
        print()
        print(term.center(f"Select option:"))
        print()
        print(term.move_x(term.width//4) + f"1 : Add {term.green}item\
s{term.normal} to list")
        print(term.move_x(term.width//4) + f"2 : Make an {term.purple}o\
rder{term.normal}")
        print(term.move_x(term.width//4) + f"3 : {term.red}Quit{term.normal}")
        key = input()
        self.key = key
        self.option()

    def quit(self) -> None:
        """
        Quits the program.
        """
        term = blessed.Terminal()
        print(term.clear + term.move_y(term.height//3) +
        term.center(f"{term.green}{term.bold}Thank you{term.normal} fo\
r using this program today :)"))
        return

    def option(self):
        """
        Large method, which ineracts with user and,
        based on user's choice, makes actions.
        """
        term = blessed.Terminal()
        try:
            case = 1
            key = int(self.key) 
            if key == 3:
                return self.quit()
            elif key == 1:
                lst = []
                case = 2
                print(term.clear + term.move_y(term.height//3) +
                term.center(f"Type {term.green}items{term.normal} to add t\
hem in {term.orange}(name, price){term.normal} format."))
                print(term.center(f"If you added all items, pres\
s {term.blue}'X'{term.normal}+ENTER"))
                while True:
                    item = input()
                    if item == "x" or item == "X":
                        print(term.clear + term.move_y(term.height//3))
                        return self.__init__(lst, param=False)
                    data = item.split(",")
                    data[0] = data[0][1:]
                    data[1] = data[1][1:-1]
                    if "(" + ", ".join(data) + ")" != item:
                        return self.option()
                    data[1] = int(data[1])
                    lst.append(Item(data[0],data[1]))
            elif key == 2:
                if self.lst == []:
                    print(term.clear + term.move_y(term.height//3) +
                    term.center(f"You {term.red}didn't add{term.normal} a\
ny {term.green}items{term.normal} to list!"))
                    print()
                    print(term.center(f"Type {term.blue}'X'{term.normal} +\
 ENTER to return"))
                    while True:
                        key_1 = input()
                        if key_1 == "x" or key_1 == "X":
                            print(term.clear + term.move_y(term.height//3))
                            return self.__init__(lst = [], param=False)
                print(term.clear + term.move_y(term.height//3) +
                term.center(f"To make an {term.purple}order{term.normal}, y\
ou have to enter some {term.orange}info{term.normal}:"))
                print()
                print(term.move_x(term.width//5) + f"Enter your {term.orange}n\
ame{term.normal}: ", end="")
                name = input()
                print()
                print(term.move_x(term.width//5) + f"Enter your {term.orange}c\
ity{term.normal}: ", end="")
                city = input()
                print()
                print(term.move_x(term.width//5) + f"Enter {term.orange}numb\
er of postoffice{term.normal}: ", end="")
                post = input()
                print()
                order_1 = Order(name, city, post, self.lst)
                print()
                print(term.center(f"Type {term.green}'P'{term.normal} + ENT\
ER to place {term.purple}order{term.normal}, {term.cyan}'T'{term.normal} + E\
NTER to track {term.purple}order{term.normal}"))
                print(term.center(f"Note: if you won't {term.bold}plac\
e{term.normal} your {term.purple}order{term.normal}, it will be {term.red}de\
leted!{term.normal}"))
                key_2 = input()
                if key_2 == "p" or key_2 == "P":
                    success = logSystem.placeOrder(order_1)
                    if success == "fail":
                        print(term.center(f"Type {term.red}'Q'{term.normal} +\
 ENTER to quit, {term.cyan}'T'{term.normal} + ENTER to track."))
                        print(term.center(order_1))
                        while True:
                            key_n = input()
                            if key_n == "q" or key_n == "Q":
                                return self.quit()
                            elif key_n == "t" or key_n == "T":
                                print(term.move_x(term.width//5) + f"Enter id\
: ", end="")
                                key_3 = int(input())
                                logSystem.trackOrder(key_3)
                                print(term.center(f"Type {term.blue}'X\
'{term.normal} + ENTER to return"))
                                while True:
                                    key_4 = input()
                                    if key_4 == "x" or key_4 == "X":
                                        print(term.clear +
                                        term.move_y(term.height//3))
                                        return self.__init__(self.lst, param=False)
                print(term.center(f"Your {term.purple}order{term.normal} ha\
s been placed!"))
                key_2 = input()
                if key_2 == "t" or key_2 == "T":
                    print(term.move_x(term.width//5) + f"Enter id: ", end="")
                    key_3 = int(input())
                    logSystem.trackOrder(key_3)
                    print(term.center(f"Type {term.blue}'X'{term.normal} + EN\
TER to return"))
                    while True:
                        key_4 = input()
                        if key_4 == "x" or key_4 == "X":
                            print(term.clear + term.move_y(term.height//3))
                            return self.__init__(self.lst, param=False)
        except:
            if case == 1:
                print(term.clear + term.move_y(term.height//3) +
                term.center(f"{term.red}Enter correct data!{term.normal}"))
                print()
                return self.__init__(lst = [], param=False)
            if case == 2:
                return self.option()


if __name__ == "__main__":
    term = blessed.Terminal()
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    print(term.clear)
    menu = Menu(lst = [], param=True)

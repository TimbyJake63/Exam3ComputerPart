###############################################################################
# DONE: 1. (4 pts)
#
#   For this _todo_, create a parent class called Vehicle. It should have an
#   __init__() function that sets two properties:
#       - year      <- int
#       - make      <- int
#       - model     <- int
#
#   It should have two methods:
#       - horn
#       - vehicle_info
#
#   This Shape class should assume that the vehicle is a car, so these
#   functions should behave as follows.
#
#       horn() -> should print the sound of a car horn
#               "BEEP BEEP"
#
#       vehicle_info() -> should print the vehicle's information
#                       Year: 2012
#                       Make: Chevrolet
#                       Model: Colorado
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
class Vehicle:
    def __init__(self, year, make, model):
        self.year=year
        self.make=make
        self.model=model

    def horn(self):
        print()
        print("BEEP BEEP!!!")

    def vehicle_info(self):
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print()
###############################################################################
# DONE: 2. (2 pts)
#
#   For this _todo_, create a child class called Car that inherits its
#   class from Vehicle. Since Vehicle already assumes the vehicle is a car, we
#   don't really need to modify anything. Remember that you can create an empty
#   class by using the pass keyword.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
class Car(Vehicle):
    pass
###############################################################################
# DONE: 2. (4 pts)
#
#   For this _todo_, create a child class called Boat that inherits its class
#   from Vehicle.
#
#   Now, a boat is a little bit different because we don't really need a
#   make and model. We will simply give the boat a name and a year. So, it's
#   __init__() method should only have two parameters:
#       - year
#       - name
#
#   A Boat's methods should work as follows.
#
#       horn() -> should print the sound of a boat horn
#               "TOOT TOOT"
#
#       vehicle_info() -> should print the vehicle's information
#                       Year: 2010
#                       Name: Seas the Day
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
class Boat(Vehicle):
    def __init__(self, year, name):
        super().__init__(year, "", "")
        self.name=name

    def horn(self):
        print("TOOT TOOT!!!")

    def vehicle_info(self):
        print(f"Year: {self.year}")
        print(f"Name: {self.name}")
        print()
#Used Chat GPT because I kept getting an error saying I needed to use make and model and chat GPT said to do this.
###############################################################################
# DONE: 3. (4 pts)
#
#   For this _todo_, create a child class called Train that inherits its class
#   from Vehicle. A Train has only two parameter:
#       - number    <- a number that identifies a train
#       - length    <- which is just a number of train cars
#
#   A Train's methods should work as follows.
#
#       horn() -> should print the sound of a train horn
#               "CHOO CHOO"
#
#       vehicle_info() -> should print the vehicle's information
#                         Number: 74
#                         Length: 20
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
class Train(Vehicle):
    def __init__ (self, number, length):
        self.number=number
        self.length=length

    def horn(self):
        print("CHOO CHOO!!!")

    def vehicle_info(self):
        print(f"Number: {self.number}")
        print(f"Length: {self.length}")
        print()
###############################################################################
# TODO: 4. (3 pts)
#
#   For this _todo_, create three different objects and save each to a
#   variable. Create a Car, Boat, and Train.
#
#   You should also call each one's horn() and vehicle_info() methods.
#   (Remember that each method already does the printing for you, so you don't
#   need to use print here.)
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
Vroom = Car("2011", "BMW", "535i xDrive")
Vroom.horn()
Vroom.vehicle_info()


Boat_Noise = Boat("2020", "Adventurer of the Seas")
Boat_Noise.horn()
Boat_Noise.vehicle_info()

Chugga = Train("A113", "63")
Chugga.horn()
Chugga.vehicle_info()
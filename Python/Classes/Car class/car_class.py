'''
put everything we've covered together
create a car class
give max speed
keep track of current speed
don't adjust speed directly so put _ infront of it
impliment speed_getter as well as accelerator and break setter methods that change speed in a logical way

questions:
Do your methods make sense
does braking pass 0 cause a speed increase
can you faster than the top speed?
'''

game_running = True
max_speed = 300 #hard limit for max speed

#Car class and functions
class Car:

    def __init__(self, name, max_speed = 300):
        self.name = name
        self.max_speed = max_speed
        self._current_speed = 0
        self.acc = 0 #TODO: build true acceleration
        self.breaks = 0

    def get_current_speed(self):
        return self._current_speed

    def set_acc(self):
        if self._current_speed >= self.max_speed:
            print(f"You're already going {self.max_speed}km/h, that's your max speed!")
        else: self._current_speed += 10

    def set_breaks(self):
        if self._current_speed <= 0:
            print("it's hard to go slower than 0!")
        else:
            self._current_speed -= 10

#User car controls
def user_chooses():
    user_choice = input(f"press A to go faster or B to slow down, E to exit\n")
    if user_choice.lower() == "a":
        Car.set_acc(user_car)

    elif user_choice.lower() == "b":
        Car.set_breaks(user_car)

    elif user_choice.lower() == "exit" or user_choice == "e":
        print("Thank you for playing the car game")
        game_running = False

    else: print("not an option, please select A, B or E")


#gather input
print(f"welcome to the car game")
user_car_name = input("what car do you have?\n")
user_max_speed = int(input("How fast can it go?\n"))

#check car is possible
if user_max_speed > max_speed:
    user_max_speed = 300
    print(f"don't be silly, no car can go faster than {user_max_speed}km/h. Your cars max speed has been set to {user_max_speed}km/h")

#generate car
user_car = Car(user_car_name, user_max_speed)

while game_running == True:
    print(f"Your {user_car.name} is currently going {user_car.get_current_speed()}")
    user_chooses()

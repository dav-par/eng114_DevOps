'''
us1 = checking assistant wants to list all flight trips available so they can sell tickets or check passenger list on specific flight_trip
us2 = checking assistant wants to see the origin, destination and date of any flight
us3 = ca wants to list all passengers and pasport numbers on any flight_trip
us4 = ca wants to register passenger with first name, last name and passport num
us5 = register specific passenger to flight_trip
us6 =
'''
from typing import List

from airplane_class import Aeroplane
from flight_trip_class import Flight_trip
from passenger_class import Passenger

# Three lists of key data
planes = []  # This is a list of plane objects
passengers = []  # This is a list of passengers objects
flights = []  # This is a list of flight_trip objects


def create_plane():
    plane_id = input("Please enter the unique plane id\n")
    plane_seats = input("How many seats does it have?\n")
    plane_unique_id = f"{plane_id}{plane_seats}{len(planes)}"
    plane = Aeroplane()
    plane.set_aeroplane(plane_id, plane_seats, plane_unique_id)
    return plane


def create_passenger():
    pass_first = input("Passenger first name?\n")
    pass_last = input("Passenger last name?\n")
    pass_passport = input("Passenger passport num?\n")
    pass_unique_id = f"{pass_first}{pass_last}{pass_passport}{len(passengers)}"
    passen = Passenger()
    passen.set_passenger(pass_first, pass_last, pass_passport, pass_unique_id)
    return passen


def create_trip():
    start = input("What's the flight origin?\n")
    finish = input("What's the flight destination?\n")
    flight_num = input("what's the flight number?\n")
    date = input("what day is the flight is on?\n")
    flight = Flight_trip()
    flight.set_flight_trip(start, finish, flight_num, date)
    return flight


# dummy_data
for i in range(10):  # This makes 10 planes and 10 flights
    planes.append(Aeroplane())
    planes[i].set_aeroplane(i, ((i * 4) + 20), (i + i + i + i + 1))
    passengers.append(Passenger())
    passengers[i].set_passenger(("bob" + str(i)), ("smith" + str(i)), (i + i + i + 0), (i + i + i + 2))
    flights.append(Flight_trip())
    flights[i].set_flight_trip("London", ("Paris" + str(i)), (i + i + i + 3), "1/6/22")

for i in range(10):  # this adds 10 passengers to 10 flights
    for j in range(10):
        flights[int(i)].add_passenger((passengers[j].get_passenger_unique_id()))
        flights[int(i)].add_passenger((passengers[j].get_passenger_unique_id()))


def list_all_flight_nums(temp_list=[]):
    for i in range(len(flights)):
        temp_list.append(flights[i].get_flight_numbers())
    print(temp_list)


def find_flight(flight_num):  # finds the list index for the flight based on flight id
    for i in range(len(flights)):
        if flights[i].get_flight_numbers() == int(flight_num):
            return i


def sell_ticket():
    flight_num = input("What is the flight number you would like to sell a ticket for?\n")
    pass_unique_id = input("What is the passport number of the customer?\n")
    flights[int(find_flight(flight_num))].add_passenger(pass_unique_id)


def check_passengers():
    flight_num = input("What flight would you like to see the passenger list for?\n")
    print(flights[find_flight(flight_num)].get_passengers())


def see_flight_details():
    flight_num = input("which flight would you like to see details for?\n")
    print(flights[int(find_flight(flight_num))].get_flight_details())


def add_passenger_to_flight():
    flight_num = input("which flight would you like add a passenger to?\n")
    passport = input("what's the passport of the passenger you want to add?\n")
    flights[int(find_flight(flight_num))].add_passenger(int(passport))


# checking assistant controls
def user_controls():
    choice = int(input(
        "what would you like to do today?\n1 - list all flights numbers\n2 - sell ticket\n3 - check passenger list\n4 - see flight details\n5 - register passenger\n6 - add passenger\n"))
    if choice == 1:
        list_all_flight_nums()
    elif choice == 2:
        sell_ticket()
    elif choice == 3:
        check_passengers()
    elif choice == 4:
        see_flight_details()
    elif choice == 5:
        create_passenger()
    elif choice == 6:
        add_passenger_to_flight()

    else:
        print("not an option")


def main(sys_on=True):
    while sys_on == True:
        user_controls()


main()
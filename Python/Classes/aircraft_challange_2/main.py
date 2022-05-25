from passenger_class import Passenger
from flight_trip_class import Flight_trip

# set up lists
passengers = {}
flights = {}


def create_auto_passenger():
    passenger = Passenger()
    passenger.set_passenger("David", "Park", 12345)
    return passenger

passengers[12345] = create_auto_passenger()

def create_auto_flight():
    flight = Flight_trip()
    flight.set_flight_trip("London", "Paris", 1000, "1/6/22", "Plane PL123")
    return flight


flights[1000] = create_auto_flight()
flights[1000].add_passenger(12345)


def create_passenger():
    passenger = Passenger()
    f_name = input("What's the first name of the passenger you would like to add to the passenger list?\n")
    s_name = input("What's the last name of the passenger you would like to add to the passenger list?\n")
    passport = int(input("What's the passport number of the passenger you would like to add to the passenger list?\n"))
    passenger.set_passenger(f_name, s_name, passport)
    passengers[passport] = passenger

def get_flight_details():
    flight_num = int(input("Which flight would you like the details for?\n"))
    if flight_num not in flights.keys():
        print("flight not found\n")
    else:
        print(flights[flight_num].get_flight_details())


def check_passengers_on_specific_flight():
    flight_num = int(input("Which flight would you like to see the passenger list for?\n"))
    if flight_num not in flights.keys():
        print("flight not found\n")
    else:
        for passport_num in (flights[flight_num].get_passenger_list()):
            print(passengers[passport_num].get_passenger_details())

def sell_ticket():
    flight_num = int(input("Which flight would you like to add a passenger too?\n"))
    passport = int(input("What's the passport number of the passenger you would like to add?\n"))
    if flight_num not in flights.keys() and passport not in passengers.keys():
        print("flight or passenger not found\n")
    else:
        flights[flight_num].add_passenger(passport)


def list_all_passengers():
    for passport_num in passengers:
        print(passengers[passport_num].get_passenger_details())

def list_all_flights():
    lst = []
    for flight in flights:
        lst.append(flight)
    print(lst)



print("list all flights")
list_all_flights()
print("list all passengers")
list_all_passengers()
print("create passenger")
create_passenger()
print("list all passengers again")
list_all_passengers()
print("check passengers on specific flight")
check_passengers_on_specific_flight()
print("sell ticket to a specific flight")
sell_ticket()
print("check passengers on specific flight again")
check_passengers_on_specific_flight()
print("check flight info")
get_flight_details()
print("add to excel file TODO") #TODO
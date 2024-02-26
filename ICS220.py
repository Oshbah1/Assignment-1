from datetime import datetime

class Flight:
    def __init__(self, flight_number, departure_time, arrival_time, capacity):
        self.flightNumber = flight_number
        self.departureTime = departure_time
        self.arrivalTime = arrival_time
        self.capacity = capacity
        self.tickets = []

    def createTicket(self):
        new_ticket = Ticket(self)
        self.tickets.append(new_ticket)
        return new_ticket

    def getPassengerList(self):
        return [ticket.getPassenger() for ticket in self.tickets if ticket.getPassenger()]

class Ticket:
    def __init__(self, flight):
        self.flight = flight
        self.passenger = None

    def __str__(self):
        return f"Ticket for Flight {self.flight.flightNumber}"

    def bookFlight(self):
        if not self.passenger:
            self.passenger = Passenger(self)
        return self.passenger

    def getPassenger(self):
        return self.passenger

class Passenger:
    def __init__(self, ticket):
        self.ticket = ticket

    def __str__(self):
        return f"Passenger with {self.ticket}"

    def checkIn(self):
        print(f"{self} has checked in.")

    def requestLoungeAccess(self):
        print(f"{self} has requested lounge access.")

class Lounge:
    def __init__(self):
        # Initialize any necessary attributes
        pass

    def verifyAccess(self, passenger):
        # Placeholder logic to verify access, returning True for demonstration
        return True

    def listAmenities(self):
        # Placeholder logic to list amenities
        return ["Free Wi-Fi", "Refreshments", "Comfortable Seating"]

# Example Usage
flight = Flight("F123", datetime.now(), datetime.now(), 200)

ticket1 = flight.createTicket()
passenger1 = ticket1.bookFlight()

ticket2 = flight.createTicket()
passenger2 = ticket2.bookFlight()

passenger3 = flight.createTicket().bookFlight()

passenger_list = flight.getPassengerList()

lounge = Lounge()

for passenger in passenger_list:
    print(f"{passenger} on Flight {flight.flightNumber}")
    if lounge.verifyAccess(passenger):
        print(f"Access to the lounge verified for {passenger}")
        amenities = lounge.listAmenities()
        print(f"Amenities available: {', '.join(amenities)}")

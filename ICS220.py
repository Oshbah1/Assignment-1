class BoardingPass:
    """A class to represent a boarding pass for  flight."""

    def set_terminal(self, terminal):
        """Sets the terminal for the boarding pass."""
        self._terminal = terminal

    def __init__(self, passenger_name, from_location, to_location, departure_time, arrival_time, terminal,
                 electronic_ticket):
        """Initializes a BoardingPass with all necessary details."""
        self._passenger_name = passenger_name
        self._from_location = from_location
        self._to_location = to_location
        self._departure_time = departure_time
        self._arrival_time = arrival_time
        self._terminal = terminal
        self._electronic_ticket = electronic_ticket

    # Setters and getters are used to encapsulate the data
    # and to provide controlled access to the properties of the class.

    def set_passenger_name(self, name):
        """Updates the passenger name on the boarding pass."""
        self._passenger_name = name

    def get_passenger_name(self):
        """Returns the passenger name."""
        return self._passenger_name

    # Additional setters and getters would follow the same pattern.

    def display_boarding_pass(self):
        """Prints the boarding pass details."""
        print("Boarding Pass for:", self._passenger_name)
        print("From:", self._from_location, "To:", self._to_location)
        print("Departure:", self._departure_time, "Arrival:", self._arrival_time)
        print("Terminal:", self._terminal, "Ticket No.:", self._electronic_ticket)


class Passenger:
    """A class to represent an airline passenger."""

    def __init__(self, name):
        """Initializes a Passenger with a name."""
        self._name = name
        self._boarding_pass = None

    def set_boarding_pass(self, boarding_pass):
        """Assigns a boarding pass to the passenger."""
        self._boarding_pass = boarding_pass

    def get_name(self):
        """Returns the passenger's name."""
        return self._name

    def display_boarding_info(self):
        """Displays boarding information if the passenger has a boarding pass."""
        if self._boarding_pass:
            self._boarding_pass.display_boarding_pass()
        else:
            print(f"No boarding pass information for {self._name}.")


# Create an instance of the Passenger class
passenger = Passenger("JAMES SMITH")
boarding_pass = BoardingPass(
    passenger_name="JAMES SMITH",
    from_location="Chicago ORD",
    to_location="New York JFK",
    departure_time="11:40",
    arrival_time="13:30",
    terminal="2",
    electronic_ticket="629"
)

passenger.set_boarding_pass(boarding_pass)

passenger.display_boarding_info()

boarding_pass.set_terminal("3")

passenger.display_boarding_info()
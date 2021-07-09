class Tesla:
    """
    A class to represent Tesla cars

        Parameter:
            model (str): A string
            color (str): A string

    """

    # WRITE YOUR CODE HERE
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):
        self.__autopilot = autopilot
        self.__color = color
        self.__model = model
        self.__battery_charge = 99.9
        self._is_locked = True
        self.__seats_count = 5
        self.__efficiency = efficiency

    def welcome(self) -> str:
        raise NotImplementedError

    @property
    def color(self):
        """Returns the color of the Tesla object"""
        return self.__color

    def autopilot(self, obstacle: str):
        self.__obstacle = obstacle
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {self.__obstacle}"
        return "Autopilot is not available"

    @property
    def seats_count(self):
        """Returns the seat count of the Tesla object"""
        return self.__seats_count

    @seats_count.setter
    def seats_count(self, new_seats_count):
        if new_seats_count < 2:
            return self.__seats_count
        self.__seats_count = new_seats_count

    def lock(self):
        self._is_locked = True

    def unlock(self):
        self._is_locked = False

    def open_doors(self) -> None:
        if self._is_locked == False:
            return "Doors opens sideways"
        return "Car is locked!"

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self):
        self.__battery_charge = 100
        self.check_battery_level()

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge -= battery_discharge_percent
            self.check_battery_level()
        else:
            print("Battery low! Please recharge")
        return self.check_battery_level()


class ModelX(Tesla):
    def __init__(self, color: str, autopilot: bool = False):
        super().__init__("Model3", color, autopilot, 0.125)

    def open_doors(self):
        if self._is_locked == False:
            return "Doors opens towards roof"
        return "Car is locked!"

    def welcome(self) -> str:
        return "Hello from ModelX!"

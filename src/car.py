class Car:
    """
    Add class description here
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation
        # Note that this function is required in your Car implementation.
        # implement your code and erase the "pass"

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        if self.orientation == 0:
            lsta = []
            for n in range(self.length):
                lsta.append((self.location[0] + n, self.location[1]))
            return lsta

        if self.orientation == 1:
            lstb = []
            for n in range(self.length):
                lstb.append((self.location[0], self.location[1] + n))
            return lstb

        # implement your code and erase the "pass"

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        # implement your code and erase the "pass"

        if self.orientation == 0:
            return {'d': "the car goes down", 'u': "the car goes up"}
        if self.orientation == 1:
            return {'r': "the car goes right", 'l': "the car goes left"}

    def movement_requirements(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        if self.orientation == 0:
            if move_key == 'd':
                return [(self.location[0] + self.length, self.location[1])]
            if move_key == 'u':
                return [(self.location[0] - 1, self.location[1])]
        if self.orientation == 1:
            if move_key == 'l':
                return [(self.location[0], self.location[1] - 1)]
            if move_key == 'r':
                return [(self.location[0], self.location[1] + self.length)]

        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"

    def move(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if move_key in self.possible_moves():
            if self.orientation == 0:
                if move_key == 'u':
                    self.location = (self.location[0] - 1, self.location[1])
                    return True
                elif move_key == 'd':
                    self.location = (self.location[0] + 1, self.location[1])

                    return True
            elif self.orientation == 1:
                if move_key == 'l':
                    self.location = (self.location[0], self.location[1] - 1)
                    return True
                if move_key == 'r':
                    self.location = (self.location[0], self.location[1] + 1)
                    return True
            else :
                return False
        else:
            return False

        # implement your code and erase the "pass"

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name


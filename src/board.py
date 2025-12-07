class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # implement your code and erase the "pass"
        self.board = []
        self.size_board = 7
        for i in range(7):
            self.board.append(["_"] * 7 + ["*"])
        self.target = (3, 7)
        self.board[self.target[0]][self.target[1]] = "E"
        self.cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        # implement your code and erase the "pass"
        disp = []
        c_list = self.cell_list()
        for car in self.cars:
            for row, col in car.car_coordinates():
                self.board[row][col] = car.get_name()
                c_list.remove((row, col))

        for row, col in c_list:
            if (row, col) != self.target_location():
                self.board[row][col] = '_'
        for r in self.board:
            disp.append(" ".join(r))
        return '\n'.join(disp)

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        # implement your code and erase the "pass"
        tup_list = []
        for row in range(self.size_board):
            for col in range(self.size_board):
                tup_list.append((row, col))
        tup_list.append((3, 7))
        return tup_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        # implement your code and erase the "pass"

        list_possible_moves = []
        for car in self.cars:

            for possible_direction in car.possible_moves().keys():

                if car.movement_requirements(possible_direction)[0] in self.cell_list() \
                        and self.cell_content(car.movement_requirements(possible_direction)[0]) is None:
                    list_possible_moves.append(
                        (car.get_name(), possible_direction, car.possible_moves()[possible_direction]))
        return list_possible_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        # implement your code and erase the "pass"
        return self.target

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        r, c = coordinate
        for car in self.cars:
            for cell in car.car_coordinates():
                if cell[0] == r and cell[1] == c:
                    return car.name
        return

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"

        for coord in car.car_coordinates():
            if coord not in self.cell_list():
                return False
        for c in self.cars:
            for coord in c.car_coordinates():
                if coord in car.car_coordinates():
                    return False
            if c.get_name() == car.get_name():
                return False
        self.cars.append(car)
        return True

    def move_car(self, car_name, move_key):
        """
        Moves the specified car by a single step in the specified direction.

        Returns:
            True if the move was successful, False otherwise.
        """
        car_to_move = next((car for car in self.cars if car.get_name() == car_name), None)
        if not car_to_move:
            return False

        if move_key not in car_to_move.possible_moves():
            return False

        move = next((move for move in self.possible_moves() if move[0] == car_name and move[1] == move_key), None)
        if not move:
            return False

        car_to_move.move(move_key)

        c_list = self.cell_list()
        for car in self.cars:
            for row, col in car.car_coordinates():
                self.board[row][col] = car.get_name()
                c_list.remove((row, col))

        for row, col in c_list:
            if (row, col) != self.target_location():
                self.board[row][col] = '_'

        return True

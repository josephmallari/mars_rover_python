class Rover:
  # init
  def __init__(
    self, 
    plateau, 
    first_rover_position, 
    first_rover_instructions, 
    second_rover_position, 
    second_rover_instructions
    ): 

    self.plateau = plateau.split()
    self.first_rover_position = first_rover_position.split()
    self.first_rover_instructions = first_rover_instructions
    self.second_rover_position = second_rover_position.split()
    self.second_rover_instructions = second_rover_instructions

    # first rover move 
    self.move(self.first_rover_instructions, self.first_rover_position)
    # second rover move
    self.move(self.second_rover_instructions, self.second_rover_position)

  def move_forward(self, position):
    # assign array values from split into its own variables 
    direction = position[2]
    xCoordinate = position[0]
    yCoordinate = position[1]

    if (direction == "N"):
      position[1] = int(yCoordinate) + 1
    elif (direction == "W"):
      position[0] = int(xCoordinate) - 1
    elif (direction == "S"):
      position[1] = int(yCoordinate) - 1
    elif (direction == "E"):
      position[0] = int(xCoordinate) + 1
  
  def rotate_right(self, position):
    direction = position[2]

    if (direction == "N"):
      position[2] = "E"
    elif (direction == "E"):
      position[2] = "S"
    elif (direction == "S"):
      position[2] = "W"
    elif (direction == "W"):
      position[2] = "N"

  def rotate_left(self, position):
    direction = position[2]

    if (direction == "N"):
      position[2] = "W"
    elif (direction == "W"):
      position[2] = "S"
    elif (direction == "S"):
      position[2] = "E"
    elif (direction == "E"):
      position[2] = "N"

  def move(self, input, position):
    # loop through input
    for instruction in input:
      if (instruction == "M"):
        self.move_forward(position)
      elif (instruction == "R"):
        self.rotate_right(position)
      elif (instruction == "L"):
        self.rotate_left(position)
      else:
        print(instruction + ' is a wrong input')
  
    print(str(position[0]) + ' ' + str(position[1]) + ' ' + position[2])

rover = Rover(input('Enter Plateau: '),
input('Enter first rover position: '),
input('Enter first rover instructions: '),
input('Enter second rover position: '),
input('Enter second rover instructions: '))

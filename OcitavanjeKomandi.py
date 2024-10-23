import serial
import time

# Define threshold values
LEFT_THRESHOLD = 400
RIGHT_THRESHOLD = 800
UP_THRESHOLD = 400
DOWN_THRESHOLD = 800

# Define command constants
COMMAND_NO = 0x00
COMMAND_LEFT = 0x01
COMMAND_RIGHT = 0x02
COMMAND_UP = 0x04
COMMAND_DOWN = 0x08

# Serial port configuration
ser = serial.Serial('COM5', 9600)  

# Simulate button class
class ezButton:
    def __init__(self, pin):
        self.pin = pin
        self.state = False
        self.last_state = False

    def getState(self):
        return self.state

    def loop(self):
        # Simulate button press
        self.state = not self.state
        time.sleep(0.1)

    def isPressed(self):
        return self.state

    def isReleased(self):
        return not self.state

# Setup
def setup():
    print("Setup complete")

# Function to read and validate serial input
def read_serial_value():
    try:
        line = ser.readline().strip()
        # Ensure the line is in string format before decoding
        line = line.decode('utf-8')
        if line.isdigit():
            return int(line)
        else:
            print(f"{line}")
            return None
    except Exception as e:
        print(f"Error reading serial data: {e}")
        return None

# Loop
def loop():
    # read analog X and Y analog values
    xValue = read_serial_value()
    yValue = read_serial_value()
    
    if xValue is None or yValue is None:
        return  # Skip processing if the values are invalid
    
    bValue = button.getState()

    # converts the analog value to commands
    # reset commands
    command = COMMAND_NO

    # check left/right commands
    if xValue < LEFT_THRESHOLD:
        command |= COMMAND_LEFT
    elif xValue > RIGHT_THRESHOLD:
        command |= COMMAND_RIGHT

    # check up/down commands
    if yValue < UP_THRESHOLD:
        command |= COMMAND_UP
    elif yValue > DOWN_THRESHOLD:
        command |= COMMAND_DOWN

    # NOTE: AT A TIME, THERE MAY BE NO COMMAND, ONE COMMAND OR TWO COMMANDS

    # print command to serial and process command
    if command & COMMAND_LEFT:
        print("COMMAND LEFT")
        # TODO: add your task here

    if command & COMMAND_RIGHT:
        print("COMMAND RIGHT")
        # TODO: add your task here

    if command & COMMAND_UP:
        print("COMMAND UP")
        # TODO: add your task here

    if command & COMMAND_DOWN:
        print("COMMAND DOWN")
        # TODO: add your task here

    if button.isPressed():
        print("The button is pressed")
        # TODO do something here

    if button.isReleased():
        print("The button is released")
        # TODO do something here

# Create button instance
button = ezButton(2)  # Assuming button pin is 2

# Call setup function
setup()

# Main loop
while True:
    loop()

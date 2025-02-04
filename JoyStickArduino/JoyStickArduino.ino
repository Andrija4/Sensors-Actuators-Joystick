#include <ezButton.h>

#define VRX_PIN  A0 // Arduino pin connected to VRX pin
#define VRY_PIN  A1 // Arduino pin connected to VRY pin
#define SW_PIN   2

#define LEFT_THRESHOLD  400
#define RIGHT_THRESHOLD 800
#define UP_THRESHOLD    400
#define DOWN_THRESHOLD  800

#define COMMAND_NO     0x00
#define COMMAND_LEFT   0x01
#define COMMAND_RIGHT  0x02
#define COMMAND_UP     0x04
#define COMMAND_DOWN   0x08

ezButton button(SW_PIN);

int xValue = 0 ; // To store value of the X axis
int yValue = 0 ; // To store value of the Y axis
int bValue = 0; // To store value of the button
int command = COMMAND_NO;

void setup() {
  Serial.begin(9600) ;
}

void loop() {
  // read analog X and Y analog values
  button.loop(); // MUST call the loop() function first
  xValue = analogRead(VRX_PIN);
  yValue = analogRead(VRY_PIN);
  bValue = button.getState();

  // converts the analog value to commands
  // reset commands
  command = COMMAND_NO;

  // check left/right commands
  if (xValue < LEFT_THRESHOLD)
    command = command | COMMAND_LEFT;
  else if (xValue > RIGHT_THRESHOLD)
    command = command | COMMAND_RIGHT;

  // check up/down commands
  if (yValue < UP_THRESHOLD)
    command = command | COMMAND_UP;
  else if (yValue > DOWN_THRESHOLD)
    command = command | COMMAND_DOWN;

  // NOTE: AT A TIME, THERE MAY BE NO COMMAND, ONE COMMAND OR TWO COMMANDS

  // print command to serial and process command
  if (command & COMMAND_LEFT) {
    Serial.print("x: ");
    Serial.println(xValue);
    delay(5);
    // TODO: add your task here
  }

  if (command & COMMAND_RIGHT) {
    Serial.print("x: ");
    Serial.println(xValue);
    delay(5);
    // TODO: add your task here
  }

  if (command & COMMAND_UP) {
    Serial.print("y: ");
    Serial.println(yValue);
    delay(5);
    // TODO: add your task here
  }

  if (command & COMMAND_DOWN) {
    Serial.print("y: ");
    Serial.println(yValue);
    delay(5);
    // TODO: add your task here
  }

  if (button.isPressed()) {
    Serial.println("The button is pressed");
    // TODO do something here
  }

  if (button.isReleased()) {
    Serial.println("The button is released");
    // TODO do something here
  }

  

 // Adjust the delay value as per your requirement
}

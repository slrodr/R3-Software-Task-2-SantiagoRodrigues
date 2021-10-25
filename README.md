# R3 Software Task 2
## Objective
Writing a two programs to control a 4 wheels rover. To do this, a client program receives an input from the keyboard and sends it to the server program, which represents the rover

## Client Program
The client is a simple program that collects keyboard inputs and sends them to the server. To accomplish this I used a computer keyboard alongside msvcrt, as it has the most straighforward way of getting a pressed key.
The program also receives the input back for checking.

## Server Program
The server receives the key input from the client and controls the motor using it. First, it checks to see if the received key is a number between 0-5. If so, the server sets the speed to be equal to (n/5)*255. This is necessary because the speed input is a digital one and not an analog one. <br />
After that, it checks if the input key is either "W", "A", "S" or "D" as these are the motor steering keys. Finally, it prints out the motor settings in the form [direction, speed].

## Issues
I mostly had to rush through this and was focused on getting it completed and working. If given more time, I would probably create a function so that once it is known the input key is one of "WASD" the fuction would print out the correct motor settings. If the key input was not a number between 0 and 5 nor an "WASD" key, it would print out "Incorrect input". I would also like to have added a way to break the function. Since it is running using "while True" it will run forever unless there is a "break" somewhere. I neglected to include it, but I would have liked to include something like "Press ESC to exit" and have included ESC as the break.

### Google Drive Link
[Demo](https://drive.google.com/file/d/1M30m0_GCuzqmRd64RQTa4mriSB1dLkuW/view?usp=sharing)
Note: The file is set to be viewed by RU only
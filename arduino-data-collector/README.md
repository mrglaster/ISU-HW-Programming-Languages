## Arduino Data Collector 

### Description 

Write a program to receive data via ZMQ (port 5555). The program should receive data about the state of the photoresistor, button and reed switch and record these events for future use. The time of each event must be recorded.
The program receives data from ![server](https://github.com/Krushiler/arduino_sensor_reader) and should be run via systemd

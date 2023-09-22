# ObserveDis

### An application for I2C 16x2 LCD Hitachi Displays that show alerts.

The display application is built and tested on a Raspberry Pi 2 Zero, but it is possible
to adapt it to different platforms.

## NOTE

### This is a ongoing project.

Ideally the display API should get decoupled of the main application, even having it auto
selecting the proper library on a configuration routine.

## Packaging libraries

## Old Notes & Ideas

Here are older notes found on this repo that are likely to be changed or removed

### StartUp Routine

    1. Check if the display is available
    2. Check Own IP
    3. Check Server Availbility (Using ICMP)

### To-Do on 'StartUp Routine'

    . Add Logging
    . Fail if display is not found (I2C)
    . MQTT Check routine
    . Add development roadmap on the readme

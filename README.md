# automation_status_display

An application for I2C 16x2 LCD Displays that show Jenkins Automation Status

## StartUp Routine

    1. Check if the display is available
    2. Check Own IP
    3. Check Server Availbility (Using ICMP)
    4. Check Jenkins Availbility (Using GET Request on Login Form)

### To-Do on 'StartUp Routine'

    . Add Logging
    . Fail if display is not found (I2C)
    . MQTT Check routine
    . Add development roadmap on the readme

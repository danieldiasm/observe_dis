# automation_status_display

An application for I2C 16x2 LCD Displays that show Jenkins Automation Status

## StartUp Routine

    - Check if Displays is Available
    - Check Own IP
    - Check Server Availbility (Using ICMP)
    - Check Jenkins Availbility (Using GET Request on Login Form)

    ### To-Do
        - Add Logging
        - Fail if display is not found (I2C)

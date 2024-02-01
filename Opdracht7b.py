#Importeren van de bibiotheken vd Gpio-pinnen en de Rpi-motor voor de stappenmotor
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

#De pinnen waarop de stappenmotor en de button zijn aangesloten op de Raspberry Pi
BUTTON_PIN19 = 19
BUTTON_PIN6 = 6
gpioPins = [22, 10, 9, 11]

#Gpio-modus naar de bcm configureren en de gpio-pin als uitgangpunt zetten voor het aansturen van de button
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN19, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN6, GPIO.IN, GPIO.PUD_DOWN)

#Initialiseren van de Stappenmotor
motor = RpiMotorLib.BYJMotor("MIJNMOTOR", "28BYJ")

try:
    # Loop
    while True:
        # Het lezen van de status van de button
        buttonState19 = GPIO.input(BUTTON_PIN19)

        # Als de button is ingedrukt
        if buttonState19 == GPIO.HIGH:
            print("de button is ingedrukt")
            # De motor wordt in 12sec worden gedraaid en dat gebeurt rechtsom
            motor.motor_run(gpioPins, 0.00234, 100, False, False, "half", 0)

finally:
    GPIO.cleanup()

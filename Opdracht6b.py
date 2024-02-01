#Importeren van de bibiotheken vd Gpio-pinnen
import RPi.GPIO as GPIO
from time import sleep, time

#De pinnen waarop de servo en de button zijn aangesloten op de Raspberry Pi
BUTTON_PIN6 = 6
SERVO_PIN18 = 18

#Gpio-modus naar de bcm configureren en de gpio-pin als uitgangpunt zetten voor het aansturen van de servo en de button
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN6, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(SERVO_PIN18, GPIO.OUT)

#Het aansturen van de pulse width modulation vd servo
pwm = GPIO.PWM(SERVO_PIN18, 50)
pwm.start(0)

#Functie voor de millis
def millis():
    return time() * 1000

#Variablen voor het bijhouden van de servo en tijd
servotijd = millis()
servoangle = 0
laatstetijd = 0

#Functie voor het berekenen van de hoek van de servo
def SetAngle(angle, duration):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN18, True)
    pwm.ChangeDutyCycle(duty)
    sleep(duration)
    pwm.ChangeDutyCycle(0)

#Het zetten van de beginpositie van 0 graden
SetAngle(0, 1)

#Loop
while True:
    laatstetijd = millis()
    buttonstate = GPIO.input(BUTTON_PIN6)
    #Als de button ingedrukt is voer het volgende uit
    if buttonstate == GPIO.HIGH:
        print("Controle button ingedrukt")
        # Laat de servo van 0 graden naar 120 graden gaan in 0.5 sec
        if servoangle == 0:
            servotijd = millis()
            SetAngle(120, 0.5)
            servoangle = 120
        # Laat de servo van 120 graden naar 0 graden gaan in 0.5 sec
        elif servoangle == 120:
            servotijd = millis()
            SetAngle(0, 0.5)
            servoangle = 0

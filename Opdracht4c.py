#Importeren van de bibiotheken vd Gpio-pinnen
import RPi.GPIO as GPIO
import time

#De pinnen waarop de de ledjes en de button zijn aangesloten op de Raspberry Pi
LED_PIN16 = 16
LED_PIN13 = 13
BUTTON_PIN = 19

#Gpio-modus naar de bcm configureren en de gpio-pin als uitgangpunt zetten voor het aansturen van het ledje en de button
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN13, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)

while True:
    # Het lezen van de huidige status vd button
    buttonState = GPIO.input(BUTTON_PIN)
    # Op het moment dat de button ingedrukt is voer het volgende uit
    if buttonState == GPIO.HIGH:
        #Het tweede ledje is uit
        GPIO.output(LED_PIN13, GPIO.LOW)
        # Het eerste ledje knipperd voor 1.3 sec aan en 0.7 sec
        GPIO.output(LED_PIN16, GPIO.HIGH)
        time.sleep(1.3)
        GPIO.output(LED_PIN16, GPIO.LOW)
        time.sleep(0.7)

    else:
        # Het tweede ledje is aan
        GPIO.output(LED_PIN13, GPIO.HIGH)


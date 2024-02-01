#Importeren van de bibiotheken vd Gpio-pinnen en de tijd
import RPi.GPIO as GPIO
import time

#functie millis
def millis():
    return time.time()* 1000

#Pin waarop het ledje is aangesloten op de raspberry pi
LED_PIN16 = 16
LED_PIN13 = 13

KnipperLed = 16

huidigeTijd = millis()
laatsteTijd = millis()

#Gpio-modus naar de bcm configureren en de gpio-pin als uitgangpunt zetten voor het aansturen van het ledje
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN13, GPIO.OUT)

try:
    #Loop
    while True:
        #Huidige tijd wordt gelijk gezet aan de millis
        huidigeTijd = millis()
        #Als knipperled de variable 13 heeft voer het volgende uit
        if KnipperLed == 13:
            #Led13 wordt aangezet
            GPIO.output(LED_PIN13, GPIO.HIGH)
            #Led16 wordt uitgezet
            GPIO.output(LED_PIN16, GPIO.LOW)
            #Knipperled krigt nu de waarde 16
            KnipperLed= 16
            #Is het niet het geval
        else:
            #Led13 wordt uitgezet
            GPIO.output(LED_PIN13, GPIO.LOW)
            #Led16 wordt aangezet
            GPIO.output(LED_PIN16, GPIO.HIGH)
            #Knipperled krijgt nu de waarde 13
            KnipperLed= 13
        #De laatstetijd wordt gelijk aan de millis
        laatsteTijd = millis()
#De GPIO-pinnen worden schoongemaakt
finally:
    GPIO.cleanup()

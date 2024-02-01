#Importeren van de bibiotheken vd Gpio-pinnen en de tijd
import RPi.GPIO as GPIO
import time

#Functie millis
def millis():
    return time.time()* 1000

# Pin waarop het ledje is aangesloten op de raspberry pi
LED_PIN16 = 16
LED_PIN13 = 13

#Variblen
KnipperLed = 16
Button = 0

huidigeTijd = millis()
laatsteTijd = millis()

#Gpio-,odus naar de bcm configureren en de gpio-pin als uitgangpunt zetten voor het aansturen van het ledje
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN13, GPIO.OUT)
GPIO.setup(Button, GPIO.IN, GPIO.PUD_DOWN)

#Loop
try:
    while True:
        #Het lezen vd huidige status vd button en de huidige tijd is in millis
        buttonstate = GPIO.input(Button)
        huidigeTijd = millis()
        #Als de knop is ingedrukt
        if buttonstate == 1:
            #Controlle welke led er knippert en wissel van knipper led naar niet knipperen en andersom
            if KnipperLed == 13:
                #led16 aan
                    GPIO.output(LED_PIN13, GPIO.HIGH)
                # led16 uit
                    GPIO.output(LED_PIN16, GPIO.LOW)
                # knipperled krijgt de waarde 16
                    KnipperLed= 16
            else:
                #led13 uit
                GPIO.output(LED_PIN13, GPIO.LOW)
                # led13 aan
                GPIO.output(LED_PIN16, GPIO.HIGH)
                # knipperled krijgt de waarde 13
                KnipperLed= 13
            #De laatstetijd wordt geupdate naar millis
            laatsteTijd = millis()
            
#het schoonmaken van de GPIO-pinnen 
finally:
    GPIO.cleanup()

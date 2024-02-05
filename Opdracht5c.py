#Importeren van de bibiotheken vd Gpio-pinnen
import RPi.GPIO as GPIO
import time

#De pinnen waarop de de ledjes en de buttons zijn aangesloten op de Raspberry Pi
LED_PIN16 = 16
LED_PIN13 = 13
BUTTON_PIN19 = 19
BUTTON_PIN6 = 6

#Gpio-modus naar de bcm configureren en de gpio-pin als uitgangpunt zetten voor het aansturen van het ledje en de button
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN16, GPIO.OUT)
GPIO.setup(LED_PIN13, GPIO.OUT)
GPIO.setup(BUTTON_PIN19, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN6, GPIO.IN, GPIO.PUD_DOWN)

#Variable voor de laatste tijd bij te houden
laatstetijd = 0

#Functie voor de millis
def millis():
    return time.time() * 1000

while True:
    # Het lezen van de status van de buttons
    buttonState6 = GPIO.input(BUTTON_PIN6)

    # Als de button6 is ingedrukt is voor het volgende uit
    if buttonState6 == GPIO.HIGH:
        # De huidige tijd wordt gelijk gezet aan millis
        huidigetijd = millis()
        # Als de tijd minstent 700 millisec verder is volg het volgende uit
        if huidigetijd - laatstetijd >= 1300:
            # Zet het ledje aan
            GPIO.output(LED_PIN13, not GPIO.input(LED_PIN13))
            GPIO.output(LED_PIN16, not GPIO.input(LED_PIN16))
            # De laatstetijd staat gelijk aan de huidige tijd
            laatstetijd = huidigetijd
        elif millis() - laatstetijd >= 700:
            GPIO.output(LED_PIN13, GPIO.LOW)
            GPIO.output(LED_PIN16, GPIO.HIGH)

    #Als de knop niet is ingedrukt
    if buttonState6 != GPIO.HIGH:
        #Zet de huidige tijd gelijk aan de millis
        huidigetijd = millis()
        # als de huidige tijd min de laatste tijd groter of gelijk is aan 1 sec wissel dan de ledjes van status
        if huidigetijd - laatstetijd >= 1000:
            GPIO.output(LED_PIN13, not GPIO.input(LED_PIN13))
            GPIO.output(LED_PIN16, not GPIO.input(LED_PIN16))
            # De laatstetijd staat gelijk aan de huidige tijd
            laatstetijd = huidigetijd
        elif millis() - laatstetijd >= 2000:
            #Zet anders het ledje uit
            GPIO.output(LED_PIN13, GPIO.LOW)
            # en het andere ledje aan
            GPIO.output(LED_PIN16, GPIO.HIGH)



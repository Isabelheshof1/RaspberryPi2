#Importeren van de bibiotheken vd Gpio-pinnen en de tijd
import RPi.GPIO as GPIO
import time


#Pin waarop het ledje is aangesloten op de raspberry pi en de button
ledPin9 = 9
ledPin10 = 10
buttonPin2 = 2


#Variablen van de status vd ledjes en de tijd
ledStatus1 = False
ledStatus2 = False
laatsteMillis1 = 0
laatsteMillis2 = 0
interval1 = 1
interval2 = 2

#Gpio-modus naar de bcm configureren en de gpio-pin als uitgangpunt zetten voor het aansturen van het ledje
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin9, GPIO.OUT)
GPIO.setup(ledPin10, GPIO.OUT)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    #Loop
    while True:
        #de huidige tijd in millis
        huidigeMillis = time.time()
        #Het lezen van de status van de button
        buttonStatus = GPIO.input(buttonPin2)
        #als de button is ingedrukt wissel elke interval1 sec de status van de ledstatus van de eerste
        if buttonStatus == GPIO.LOW:
            if huidigeMillis - laatsteMillis1 >= interval1:
                laatsteMillis1 = huidigeMillis
                ledStatus1 = not ledStatus1
                GPIO.output(ledPin9, ledStatus1)
        #Zo niet, wissel dan de status van de tweede lesstatus elke interval2 sec
        else:
            if huidigeMillis - laatsteMillis2 >= interval2:
                laatsteMillis2 = huidigeMillis
                ledStatus2 = not ledStatus2
                GPIO.output(ledPin10, ledStatus2)
        #als de status ledstatus1 aan is, verander dan elke interval1 seconde de status
        if ledStatus1:
            if huidigeMillis - laatsteMillis1 >= interval1:
                laatsteMillis1 = huidigeMillis
                GPIO.output(ledPin9, not ledStatus1)
        # als de status ledstatus2 aan is, verander dan elke interval2 seconde de status
        elif ledStatus2:
            if huidigeMillis - laatsteMillis2 >= interval2:
                laatsteMillis2 = huidigeMillis
                GPIO.output(ledPin10, not ledStatus2)
                
#De GPIO-pinnen worden schoongemaakt
finally:
    GPIO.cleanup()

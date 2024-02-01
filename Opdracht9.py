#Importeren van de bibiotheken vd Gpio-pinnen en de tijd
import RPi.GPIO as GPIO
import time

#Defineren vd pinnen van de leds op de Pi en de arduino
LedPinRas = [26, 19, 13, 6]
LedPinArd = [11, 9, 10, 22]

#De variablen van het knipperen vd ledjes, het bijhouden vd laatste tijd, de huidige status
Knippertijd = [100, 400, 600, 800]
Laatstetijd = [0, 0, 0, 0]

Laatsteledinput = -1
LedPinStatus = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]

Knipper = [0, 0, 0, 0]
Laatsteled = [0, 0, 0, 0]

#Gpio-modus naar de bcm configureren en de gpio-pin als uitgangpunt zetten voor het aansturen van het ledje
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#initialeren vd pinnen voor de ledjes en invoer vd arduino
for pin in LedPinRas:
    GPIO.setup(pin, GPIO.OUT)
for pin in LedPinArd:
    GPIO.setup(pin, GPIO.OUT)

#Functie vd millis
def millis():
    return time.time()*1000

#Functie controle welke led aan het knipperen is
def knipperLed(led):
    huidigetijd = millis()
    if huidigetijd - Laatstetijd[led] >= Knipper[led] and Laatsteled[led] >= 1:
        Laatstetijd[led] = huidigetijd
        if LedPinStatus[led] == GPIO.LOW:
            LedPinStatus[led] = GPIO.HIGH
        else:
            LedPinStatus[led] = GPIO.LOW
        GPIO.output(LedPinRas[led], LedPinStatus[led])
        
#Functie de juiste led in te schakelen, betrokkenheid arduino
def ledinvoer(i):
    global Laatsteledinput
    statuspin = GPIO.input(LedPinArd[i])
    if statuspin == GPIO.HIGH:
        if Laatsteledinput > -1:
            controleLed(Laatsteledinput, i)
            Laatsteledinput = -1
        else:
            Laatsteledinput = i
            
#Functie om een led in te schakelen
def controleLed(led, tijd):
    if Laatsteled[led]==0:
        l = 0
        for i in range(len(Laatsteled)):
            if Laatsteled[i] == 2:
                LedPinStatus[i] = 0
                GPIO.output(LedPinRas[i], GPIO.LOW)
    if Laatsteled[led] == 1:
        Laatsteled[led] = 2
    LedPinStatus[led] = GPIO.HIGH
    Laatsteled[led] = 1
    GPIO.output(LedPinRas[led], GPIO.HIGH)

    Knipper[led] = Knippertijd[tijd]
    knipperLed(led)

#Het aanzetten van de led en de bijbehorende tijd
controleLed(0,0)
controleLed(1,0)

#De uitvoerende loop
while True:
    for i in range(4):
        #Het verwerken vd led en de invoer vd arduino
        knipperLed(i)
        ledinvoer(i)
        #moment van pauze om beslasting te verminderen
    time.sleep(0.1)

//hexwaarde 0xF30CFF00, 0xE718FF00, 0xA15EFF00, 0xF708FF00
#include <IRremote.h> 

//Defineren van de pinnen op de arduino en de hex codes
const int PinIr = 8;
const int RasPin[] = {2,3,4,7};

unsigned long hex[] = {0xF30CFF00, 0xE718FF00, 0xA15EFF00, 0xF708FF00};

unsigned long newhex = 0;

//Variable 
unsigned long laatsteMillis[] = {0,0};

int count = 0;
int laatsteLed;

// Initialseren van de ir-ontvangen
IRrecv irrecv(PinIr);
decode_results results;

//Inschakelen vd ir
void setup(){
  irrecv.enableIRIn();
  for (int i = 0; i < sizeof(RasPin)/ sizeof(RasPin[0]);
i++){
    pinMode(RasPin[i], OUTPUT);
  }
}


void loop(){
  juisteButton();
  //Als er een puls is gedetecteerd reset de teller, dit duurt wel 2 sec
  if (count == 1 && millis() - laatsteMillis[0] >= 2000){
    count = 0;
  } 
}

//Functie om de ledjes uit te schakelen
void uitschakelenLed(){
  for (int i = 0; i < sizeof(RasPin) / sizeof(RasPin[0]);
    i++){
      digitalWrite(RasPin[i], LOW);
    }
}

//Functie om de controle uit te voeren of de ir-code overeenkomt met de hex-waarde
void juisteButton(){
  if (irrecv.decode()){
    newhex = irrecv.decodedIRData.decodedRawData;
    Serial.println(newhex);

    for (int i = 0; i < sizeof( hex) / sizeof(hex[0]); i++){
      if (newhex == hex[i]){
        laatsteMillis[0] = millis();
        uitschakelenLed();
        digitalWrite(RasPin[i], HIGH);
        laatsteLed = i;
      }
    }
    //Hervatten vd ir-signalen
    irrecv.resume();
  }
}


 

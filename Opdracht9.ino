//hexwaarde 0xF30CFF00, 0xE718FF00, 0xA15EFF00, 0xF708FF00
#include <IRremote.h> 

//Defineren van de pinnen op de arduino en de hex codes
const int PinIr = 8;
const int RasPin[] = {2,3,4,7};
const unsigned long hex[] = {0xF30CFF00, 0xE718FF00, 0xA15EFF00, 0xF708FF00};
const int PinNum = sizeof(RasPin) / sizeof(RasPin[0]);

// Initialseren van de ir-ontvangen
IRrecv irrecv(PinIr);
decode_results results;

//Variable laatstemillis
unsigned long laatsteMillis = 0;

//Inschakelen vd ir
void setup(){
  irrecv.enableIRIn();
  for (int i = 0; i < PinNum; i++){
    pinMode(RasPin[i], OUTPUT);
  }
}

//loop
//Als er een infraroodsignaal wordt ontvangen worden de hexdecimale opgevraagd
//Als deze overeenkomen met de vooraf gedfineerde waarden wordt het tijdstip vd knop bijgehouden
//De leds worden uitgeschakeld door de functie
//de led die overeenkomt met de ontvangen worden wordt ingeschakeld
void loop(){
  if (irrecv.decode(&results)){
    unsigned long newhex = results.value;
    for (int i = 0; i < PinNum; i++){
      if (newhex == hex[i]) {
        laatsteMillis = millis();
        uitzettenPinnen();
        digitalWrite(RasPin[i], HIGH);
        break;
      }
    }
    irrecv.resume();
  }

  if (millis() - laatsteMillis >= 2000 && laatsteMillis != 0){
    uitzettenPinnen();
    laatsteMillis=0;
  }
}

void uitzettenPinnen(){
  for (int i = 0; i < PinNum; i ++){
    digitalWrite(RasPin[i], LOW);
}
}

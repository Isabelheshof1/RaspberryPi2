//Aansluiten vd pinnen 
const int ledPin9 = 9;
const int ledPin10 = 10;
const int buttonPin2 = 2;

//Variablen voor de status van de ledjes en de button
bool status1 = false;
bool status2 = false;
bool statusButton = false;

unsigned long laatsteMillis1 = 0;
unsigned long laatsteMillis2 = 0;

const long interval1 = 500;
const long interval2 = 1000;

void setup(){
pinMode(ledPin9, OUTPUT);
pinMode(ledPin10, OUTPUT);
pinMode(buttonPin2, INPUT_PULLUP);
}

void loop(){
  //Status vd button lezen
bool buttonState = digitalRead(buttonPin2);

  //Als de knop is ingedrukt voor het volgende uit
if (buttonState == LOW){
  unsigned long huidigeMillis = millis();
  //als de huidige tijd min de laatste tijd gelijk is aan 500 
  if (huidigeMillis - laatsteMillis1 >= interval1){
    laatsteMillis1 = huidigeMillis;
    //de status vd de led wordt gewisseld
    status1 = !status1;
    //zet de led aan
    digitalWrite(ledPin9, status1);
    }
  } else {
  //als de knop niet is ingedrukt
    unsigned long huidigeMillis = millis();
  //Werkt hetzelfde maar dan voor de andere led
  if (huidigeMillis - laatsteMillis2 >= interval2){
    laatsteMillis2 = huidigeMillis;
    status2 = !status2;
    digitalWrite(ledPin10, status2);
    }
  }
}

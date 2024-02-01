const int ledPin9 = 9;
const int ledPin10 = 10;
const int buttonPin2 = 2;

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
bool buttonState = digitalRead(buttonPin2);

if (buttonState == LOW){
  unsigned long huidigeMillis = millis();
  if (huidigeMillis - laatsteMillis1 >= interval1){
    laatsteMillis1 = huidigeMillis;
    status1 = !status1;
    digitalWrite(ledPin9, status1);
    }
  } else {
    unsigned long huidigeMillis = millis();
  if (huidigeMillis - laatsteMillis2 >= interval2){
    laatsteMillis2 = huidigeMillis;
    status2 = !status2;
    digitalWrite(ledPin10, status2);
    }
  }
}

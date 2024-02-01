//Aansluiten vd pinnen 
const int ledPin9 = 9;
const int ledPin10 = 10;
const int buttonPin2 = 2;

unsigned long huidigeTijd = 0;
unsigned long laatsteTijd = 0;
const long interval = 1000;

void setup(){
  pinMode(ledPin9, OUTPUT);
  pinMode(ledPin10, OUTPUT);
  pinMode(buttonPin2, INPUT_PULLUP);
}

void loop(){
  huidigeTijd = millis();

  if (digitalRead(buttonPin2) == HIGH){
    if (huidigeTijd - laatsteTijd >= interval) {
      digitalWrite(ledPin9, HIGH);
      digitalWrite(ledPin10, HIGH);
      delay(1000);
      digitalWrite(ledPin9, LOW);
      delay(1000);
      laatsteTijd = huidigeTijd;
    }
  } else{
    if (huidigeTijd - laatsteTijd >= interval) {
      digitalWrite(ledPin9, HIGH);
      digitalWrite(ledPin10, HIGH);
      delay(1000);
      digitalWrite(ledPin10, LOW);
      delay(1000);
      laatsteTijd = huidigeTijd;
    }
  }
}

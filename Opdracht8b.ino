//Pin waarop de ledjes zijn aangesloten
int ledPin9 = 9;
int ledPin10 = 10;

void setup(){
  pinMode(ledPin9, OUTPUT);
  PinMode(ledPin10, OUTPUT);
}

//Loop
void loop(){
//Led9 laten knipperen 
digitalWrite(ledPin9, HIGH);
digitalWrite(ledPin10, LOW);
delay(3000)
digitalWrite(ledPin9, LOW);

//Led10 laten knipperen
digitalWrite(ledPin10, HIGH);
delay(1000)
digitalWrite(ledPin10, LOW);
}

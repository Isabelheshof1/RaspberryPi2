//Aansluiten vd pinnen 
int ledPin9 = 9;
int ledPin10 = 10;

void setup(){
  pinMode(ledPin9, OUTPUT);
  pinMode(ledPin10, OUTPUT);
}

//loop
void loop(){
  //led 9 aanzetten, laten branden
  digitalWrite(ledPin9, HIGH);
  //led 10 uitzetten
  digitalWrite(ledPin10, LOW);
  //wacht 1 sec
  delay(1000);

 //led 9 uitzetten
  digitalWrite(ledPin9, LOW);
  //led 10 aanzetten, laten branden
  digitalWrite(ledPin10, HIGH);
  //wacht 1 sec
  delay(1000);

}

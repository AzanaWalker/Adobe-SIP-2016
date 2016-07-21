int LEDPIN = 4;
int LEDPIN2 = 6
void setup() {
  // put your setup code here, to run once:
    pinMode(LEDPIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    digitalWrite(LEDPIN, HIGH);
    delay(500);
    digitalWrite(LEDPIN, LOW);
    delay(1500);

    
}

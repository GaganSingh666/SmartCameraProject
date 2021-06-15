
int led = D1;

void setup() {
    pinMode(led, OUTPUT);
    Particle.subscribe("face_detect",blink);
}

void loop() {



}

void blink(const char *event, const char *data){

    digitalWrite(led, HIGH);
    delay(10000);
    digitalWrite(led, LOW);


}
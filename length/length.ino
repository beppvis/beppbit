const int trig = 7;
const int echo = 6;

int duration = 0;
int distance = 0;

void setup(){
    Serial.begin(9600);
    pinMode(trig,OUTPUT);
    pinMode(echo,INPUT);
}

void loop(){
    digitalWrite(trig,HIGH);
    delayMicroseconds(1000);
    digitalWrite(trig,LOW);

    duration = pulseIn(echo,HIGH);
    distance = (duration/2)/2.85;
    String need = Serial.readString();
    if (need == 9){
          if (distance < 300){
            Serial.println("1");
          }
          else{
            Serial.println("0");  
          }
      }
 }

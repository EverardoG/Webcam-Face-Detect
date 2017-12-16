int counter=1;


void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
}




void loop() {
  // put your main code here, to run repeatedly:

if (counter==1)
   {
    Serial.println("Arduino Started!");
    delay(1000);
    counter++;
   }
delay(1000);
while (Serial.available())
{
  //delay(300);
  while (counter==2)
     {
      String robot_mood = Serial.readStringUntil('\n');
      Serial.println(robot_mood);
      //delay(1000);
      
     
     }
}
}

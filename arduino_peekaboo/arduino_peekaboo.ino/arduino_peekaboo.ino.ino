int counter=1;


void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
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
      if (robot_mood.length() ==9) //This means that the robot is happy. Any code for whatever it will do when it is happy should
      //be down below in the place of the code that turns the LED on and off
          {digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
          delay(100);                       // wait for a second
          digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
          delay(100);                       // wait for a second
          digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
          delay(100);                       // wait for a second
          digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
          delay(100); }   
      else //this means that the robot is nuetral. Down below should be code that just tells the robot not to do anything. 
      //Or to do whatever it might do if no one is around.
          {digitalWrite(LED_BUILTIN, LOW);} //this turns off the LED
          
      //delay(1000);
      
     
     }
}
}

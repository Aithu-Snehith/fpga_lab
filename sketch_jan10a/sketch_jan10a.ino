float a[] = { 1.0,         -2.5194645,   2.56083711, -1.20623537,  0.22012927};
float b[] = {0.00345416,  0.01381663,  0.02072494,  0.01381663,  0.00345416};

float x[5];
float y[5];

void setup() {
  
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  for(int i = 0; i < 5; i++)
  {
      x[i] = 0.0;
      y[i] = 0.0;
  }
}


int count= 0;

void loop() {
  
  // put your main code here, to run repeatedly:
  float x_sum = 0.0;
  float y_sum = 0.0;
  
  
  
  if(Serial.available())
  {
    for(int i = 0; i < 4; i++)
    {
      x[i] = x[i+1];
      y[i] = y[i+1];
    }
//    count++;
    x[4] = Serial.parseFloat();
    //y[4] = 0.0;//simply written can even write outside if
//    Serial.print("x = ");
//    Serial.println(x[4]);
    for(int i = 0; i < 5; i++)
    {
      x_sum = x_sum + b[i]*x[4-i];
    }
    
    for(int i = 1; i < 5; i++)
    {
      y_sum = y_sum + a[i]*y[4-i];
    }
    y[4] = (x_sum-y_sum)/a[0];
//    Serial.print("out = ");
    Serial.println(y[4],8);
  }
  

}

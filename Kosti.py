import random; 
print ("Please select number 1 - 6");
numbers = int(input(" "));

while  numbers < 1:
    print ("Please select enother number + ");
    numbers = int(input(" "));
    break;
   
while numbers > 6:
    print ("Please select enother number - ");
    numbers = int(input(" "));    
    break;

pool = random.randint(1, 6);
print (pool);

if pool == numbers:
    print ("YOU WIN!!!");
else:
    print ("Try again");

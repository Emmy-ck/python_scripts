#Create greetings for your program
#Ask user for the city they grew up in
#Ask user for name of a pet
#Combine the name of their city and pet and show them their band name
#Input cursor should show up on a new line

print("This is a band name generator");

city = input("What city did you grow up in? \n");
pet = input("What is the name of your pet? \n");

print("Your bandname is " + city + pet);

#Done
#Another way of doing it:

city = input("What city did you grow up in? ");
print(city);
pet = input("What is the name of your pet? ");
print(pet);
print("Your bandname could be " + city + "" + pet);

#Don't change the coe below
#-----------------------------------------------------------#
a = input("a: ");
b = input("b: ");
#-----------------------------------------------------------#
#Task: Change the values of a and b when printed out

c = a;
a = b;

print("a = " + b);
print("b = " + c);

#Done!
#Another way of doing it:

a = input("a: ");
b = input("b: ");

c = a;
a = b;
b = c;

print("a = " + a)
print("b = " + b);
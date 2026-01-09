
string = input ("please enter your word: ")

character=input("Please enter your own character: ")

i=0
count=0

#Loop will find the occurent of characters
while ( i < len(string)):
    if(string[i]==character):
     
     count = count +1
    i= i+1

     #display the result
print("The total number of times", character, "has occured =", count )
# Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
class IOString(): 
   def __init__(self):
      self.str1=''
      
   def get_String(self):
      self.str1=input('ENTER SOME LETTERS')
   def upp_string(self):
      print('THE STRING GIVEN BY THE USER IS:',self.str1.upper())


obj1=IOString()
obj1.get_String()
obj1.upp_string() 
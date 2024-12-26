#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!

class employee:
    def __init__(self):
        print('EMPLOYEE CREATED')

    def __del__(self):                                                   
        print('DESTRUCTOR MADE')
    
def creating():
    print('OBJECT COMPLETE')
    obj1 = employee
    print('FUNCTION END ')
    return obj1
print('calling creating function')
obj1=creating()

class Car: # creating a Car object
    # showing what __init__ can do
    # __init__ is a constructor 
    # gives what this class can do 
    def __init__(self,window,door,seat):
        ''' '''
        self.windows=window
        self.doors=door
        self.seats=seat
    
    def detail_of_seats(self,seats):
        return "This is having {} number of .format(self.seats)"
    
        
car1=Car(5,4,5) 
# give the inputs



car1.windows = 5
car1.doors = 4
car1.seats = 5

print(car1.windows)
print(car1.detail_of_seats(10))
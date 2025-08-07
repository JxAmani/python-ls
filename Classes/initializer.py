
#initializer:constructor

#Speical method in a class
#initializer: method is called whenver the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to hhave thhe self: keyworkd

class Human():

    def __init__(self):
        print("The initializer wass called")
        
    def learn_self(self,object,gender,name):
        object.gender=gender
        object.name=name
        if object.gender=="Male":
            object.ribs=24
            object.curse="Suffer"
        else :
          object.ribs=23
          object.curse="Pain"
    
# adam=Human(name="adam",gender="Male") #object from a class
adam=Human()
adam.learn_self(name="adam",gender="Male",object=adam)
print("name",adam.name)
print("gender",adam.gender)
print("ribs",adam.ribs)
print("curse",adam.curse)
print("")
# eve=Human(name="eve",gender="Female")
# print("name",eve.name)
# print("gender",eve.gender)
# print("ribs",eve.ribs)
# print("curse",eve.curse)
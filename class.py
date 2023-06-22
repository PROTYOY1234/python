class Animal:
    Fur_color="orange"
    def __init__(self,Fur_color):
        self.Fur_color=Fur_color
    def speak(self):
       print("Rawwrrr") 
    def eat(self):
        pass
    def chase(self,Animal="Tiger"):
        print(Animal,"Run Behind")
    def Get_Fur_color(self):
        print("Getting Fur Colour:" ,self.Fur_color)

class Housecat(Animal):
       def __init__(self, Fur_color):
           super().__init__(Fur_color)
           print("Fur color was Saved To the class object")
       def speak(self):
        print("Meoow")
       def chase(self , Animal="Mouse"):
         super().chase("Tiger")
         print("catch the",Animal)
       
cat=Housecat(Fur_color="Orange") 

print(cat.Fur_color)
cat.speak() 
cat.Get_Fur_color()
cat.chase()  
    
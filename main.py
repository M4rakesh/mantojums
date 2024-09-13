'''class Person:
    def can_walk(self):
        print("Es prot stāigat")
    def can_talk(self):
        print("Es protu runat")
class Docto:
    def can_cure(self):
        print("Es protu ārstēt")
    
class Arhitect:
    def can_build(self):
        print("Es protu celt mājas")
    
d=Docto()
a=Arhitect()
print(issubclass(Docto,Person))
print(issubclass(Person,Docto))'''


print("sdfs")
class Trans:
    def __init__(self,marka,model,maxspeed):
        self.marka = marka
        self.model = model
        self.maxspeed = maxspeed
    def info(self):
        print(f"Auto marka:{self.marka},Model:{self.model},maxspeed: {self.maxspeed}")
class Auto(Trans):
    def __init__(self,marka,model,maxspeed,deg_tips):
        super().__init__(marka,model,maxspeed)
        self.deg_tips = deg_tips
    def info(self):
        super().info()
        print(f"Degvielas tips:{self.deg_tips}")
v=Trans("toyta","corola",170)
v.info()
a=Auto("Mercedes-Benz","e320",240,"Benzīns")
a.info()

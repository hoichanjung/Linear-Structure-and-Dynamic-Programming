# inheritance
class Father():
    strHometown = "Jeju"
    
    def __init__(self, paramHome):
        self.strHometown = paramHome
        print("Father is created")
        
    def doFatherThing(self):
        print("Father's action")
    
    def doRunning(self):
        print("Slow")
        
class Mother():
    strHometown = "Seoul"
    def __init__(self):
        print("Mother is created")
        
    def doMotherThing(self):
        print("Mother's action")
        
        
class Child(Father, Mother):
    strName = "Moon"
    def __init__(self, paramName, paramHome):
        super(Child, self).__init__(paramHome)
        self.strName = paramName
        print("Child is created")
        
    def doRunning(self):
        print("Fast")
        
me = Child("Sun", "Universe")
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHometown)
print(me.strName)
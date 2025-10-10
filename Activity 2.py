class vehicle:

    def __init__(self, max_speed, miledge):
        self.max_speed= max_speed
        self.miledge= miledge

modelX= vehicle(240, 18)
print("Mode X Speed:", modelX.max_speed)
print("Model X Miledge:", modelX.miledge)
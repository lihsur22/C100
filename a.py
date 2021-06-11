class Car:  
    def __init__(self, model, color, company, speedLim):
        self.color = color
        self.company = company
        self.model = model
        self.speedLim = speedLim
        self.gear = 0
        self.started = 0
    def start(self):
        self.started = 1
        print("Car Started")
    def stop(self):
        self.started = 0
        print("Car Stopped")
    def accelerate(self):
        if(self.started == 1):
            if(self.gear == 0):
                print("Change gear first")
            if(self.gear == 1):
                print("Car Accelerated")
            if(self.gear == 6):
                print("Car Gone Back")
            if(self.gear == 2):
                print("Car Accelerated 2x More")
        else:
            print("Start the car first")
    def changeGear(self, gear):
        if(self.started == 1):
            print("Car Changed Gears")
            self.gear = gear
        else:
            print("Start the car first")
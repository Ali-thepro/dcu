class Lamp:

    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        if self.on == False:
            self.on = True
    
    def turn_off(self):
        if self.on == True:
            self.on = False

    def toggle(self):
        if self.on == True:
            self.on = False
        else:
            self.on = True
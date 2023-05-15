# Franchesca Marie U. Donadillo
# BSCPE 1-5

# assign class
class TV():

    # constructor
    #instance variables
    def __init__(self, channel , volume_level, on):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

    # define start
    def start(self):
        start_tv = input("WELCOME! Press any key to start. ")
        return start_tv

    # behaviour 
    def get_channel(self):
        return self.channel
    
    def set_channel(self, channel):
        if channel >= 1 and channel <=120:
            self.channel = channel
            print(f"volume level is {self.channel}")

    def get_volume(self):
        return self.volume_level
        
    def set_volume(self, volume_level):
        if volume_level >= 1 and volume_level <= 7:
            self.volume_level = volume_level
            print(f"volume level is {self.volume_level}")

    def turn_on(self):
        if self.on == "on":
            return True

    def turn_off(self):
        if self.on == "off":
            return False
    

    
    

        

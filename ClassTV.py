# Franchesca Marie U. Donadillo
# BSCPE 1-5

# assign class
class TV:

    # constructor
    #instance variables with user input
    def __init__(self, channel_tv,volume_level_tv, on_tv):
        
        channel_tv = channel_tv
        volume_level_tv = volume_level_tv
        on_tv = "on"

        self.channel = channel_tv
        self.volume_level = volume_level_tv
        self.on = on_tv        
        
      # behaviour 
    def turn_on_off(self):
        if self.on == "on":
            return True

    def turn_off(self):
        if self.on == "off":
            return False
        
    def get_channel(self):
        channel_get = self.channel
        return channel_get
        
    def set_channel(self, channel_get):
        if channel_get >= 1 and channel_get <=120:
            print(f"tv_1's channel is {self.channel}", end = " ")

    def get_volume(self):
        volume_level_get = self.volume_level
        return volume_level_get
        
    def set_volume(self, volume_level_get):
        if volume_level_get >= 1 and volume_level_get <= 7:
            print(f"and the volume level is {self.volume_level}")


    

    
    

        

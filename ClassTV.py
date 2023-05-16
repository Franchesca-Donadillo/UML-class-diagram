# Franchesca Marie U. Donadillo
# BSCPE 1-5

# assign class
class TV:

    # constructor
    #instance variables with user input
    def __init__(self):
        
        channel_tv = int(input("Enter your desired channel number (1-120). "))
        volume_level_tv = int(input("Enter your desired volume level. (1-7) "))
        on_tv = False

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
        return self.channel
        
    def set_channel(self, channel_tv):
        if channel_tv >= 1 and channel_tv <=120:
            channel_tv = self.channel
            return channel_tv

    def get_volume(self):
        return self.volume_level
        
    def set_volume(self, volume_level_tv):
        if volume_level_tv >= 1 and volume_level_tv <= 7:
            volume_level_tv = self.volume_level
            return volume_level_tv

   
    

    
    

        

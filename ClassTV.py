# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import termcolor for colors
from termcolor import colored, cprint

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
    def turn_on(self):
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
            cprint(colored(f"channel is {self.channel}"), "green", end = " ")

    def get_volume(self):
        volume_level_get = self.volume_level
        return volume_level_get
        
    def set_volume(self, volume_level_get):
        if volume_level_get >= 1 and volume_level_get <= 7:
            print("and the ", end= " ") 
            cprint(colored(f"volume level is {self.volume_level}\n"), "cyan")
            
    def channel_up(self):
        self.channel += 1
        cprint(colored("\n" + "*"*80), "grey")
        cprint(colored(f"The current television channel is {self.channel}"),"yellow", end = " ")
    
    def channel_down(self):
        cprint(colored("\n" + "*"*80), "grey")
        self.channel -= 1
        cprint(colored(f"The current television channel is {self.channel}"), "magenta" , end = " ")

    def volume_up(self):
        self.volume_level += 1
        cprint(colored(f"and the volume level is increased to {self.volume_level}\n"), "yellow")
        
    def volume_down(self):
        self.volume_level -= 1
        cprint(colored(f"and the volume level is decreased to {self.volume_level}\n"), "magenta")
        
    
    


    

    
    

        

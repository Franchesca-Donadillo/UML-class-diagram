# assign class
class TV():
    # define start
    def Start(self):
        start_tv = input("WELCOME! Press any key to start. ")
        return start_tv
    
    # define ask user
    def AskUser():
        channel = int(input("Enter your desired channel: "))
        volume_level = int(input("Enter your desired level of volume: "))
        on = bool(input("Is the TV on? "))

        return channel, volume_level, on
